###############################################################################
#   Author : Ali Snedden
#   Date   : 3/9/19
#
#   Purpose: 
#       I would like a better understanding of p-values and how they work.
#       So I will run a series of experiments testing the validity the 
#       reproducibility of p-values by drawing from two gaussian random
#       deviates that are statistically significantly apart.
#
#       Reproduce the following work : 
#       http://www.nature.com/nmeth/journal/v12/n3/full/nmeth.3288.html#f4
#
#   Notes : 
#       1. Run with Python 3.6 : 
#          source ~/.local/virtualenvs/python3.6/bin/activate
#       2. https://math.stackexchange.com/questions/80848/calculate-p-value
#          a) I think that this is only relevant to case where we have a 'known'
#             value for the mean, like assuming a fair coin has a mean =0.5.
#             NOT for comparing two normally distributed sample distributions.
#       3. Following : https://en.wikipedia.org/wiki/P-value
#          a) assume X is a random variable and H is the hypothesis under 
#             consideration. P(X|H) is the likelihood of a certain observation 
#             event X if the H is assumed to be correct
#          b) We can reject the Null hypothesis, but that doesn't tell us 
#             which alternative hypothesis is valid. 
#          c) Rejecting the NULL hypothesis means : 
#              (i) the mean is not zero
#             (ii) the variance is not unity
#            (iii) the distribution is not normal,
#       4. To compute a p-value, need:
#          a) a null hypothesis
#          b) a test statistic (e.g. Student's t-test for Gaussian)
#          c) data!
#       5. Student t-distribution
#          a) Used when population size is small and normally distributed
#          b) Used when s.d. is unknown.
#          c) Makes sense that it is difference between expected distribution - experimental
#             distribution divided by stdev_of_mean
#             Basically, interpret as 
#               "how far is the experimental distribution away from the
#                expected distribution of means"
#             t = (sampMean - \mu) / (\sigma / sqrt(N))
#
#       6. Choose significance p-value _before_ experiment
#       7. Intuition on dealing with p-value when comparing two normal distributions
#       8. 1. Standard deviation of the mean : \sigma / sqrt(N)
#          Per : https://en.wikipedia.org/wiki/Standard_error#Standard_error_of_the_mean
#          "the standard error of the mean is a measure of the dispersion of sample
#          means around the population mean"
#       9. Use two sided t-test per 
#          https://stats.idre.ucla.edu/other/mult-pkg/faq/general/faq-what-are-the-differences-between-one-tailed-and-two-tailed-tests/
#
#
#
###############################################################################
import time
import numpy as np
import random as rnd
import sys
from error import exit_with_error
import matplotlib
import random
from functions import convert_tscore_to_pvalue
from functions import student_t_test
from functions import welchs_t_test
from plotting import plot_histogram

def print_help(ExitCode):
    """
    ARGS:
    RETURN:
    DESCRIPTION:
    DEBUG:
    FUTURE:
    """
    sys.stderr.write("./src/main.py mu1 s1 mu2 s2\n"
                     "    mu1 : float, mean(population 1), assumed gaussian\n"
                     "    s1  : float, stdev(population 1)\n"
                     "    mu2 : float, mean(population 2), assumed gaussian\n"
                     "    s2  : float, stdev(population 2)\n"
                     "\nTo run locally, with all correctly installed packages run\n"
                     "     source ~/.local/virtualenvs/python3.6/bin/activate\n")
    sys.exit(ExitCode)



def main():
    """
    ARGS:
    RETURN:
    DESCRIPTION:
    DEBUG:
    FUTURE:
    """
    if(sys.version_info[0] < 3):
        exit_with_error("ERROR!!! Runs with python3, NOT {}\n".format(sys.argv[0]))
    if(len(sys.argv) == 2 and ("--h" in sys.argv[1] or "-h" in sys.argv[1])):
        print_help(ExitCode=0)
    elif(len(sys.argv) != 5):
        print_help(ExitCode=1)
    np.random.seed(42)
    random.seed(42)

    ### Create the population distributions, draw our experimental samples from these ###
    # Population / Dist 1
    pop1_mu = float(sys.argv[1])         ### average
    pop1_sd = float(sys.argv[2])         ### standard dev
    N1  = 100000    ### Number of samples 
    pop1V = np.zeros([N1])
    for i in range(N1):
        pop1V[i] = random.gauss(pop1_mu, pop1_sd)
    # Population / Dist 2
    pop2_mu = float(sys.argv[3])
    pop2_sd = float(sys.argv[4])
    N2  = 100000    ### Number of samples 
    pop2V = np.zeros([N2])
    for i in range(N2):
        pop2V[i] = random.gauss(pop2_mu, pop2_sd)
    print("\n---------------------------------------------------------")
    print("Population 1 : [mu,sd] = [{:<.3f},{:<.3f}]\n"
          "Population 2 : [mu,sd] = [{:<.3f},{:<.3f}]\n".format(pop1_mu,pop1_sd,pop2_mu,pop2_sd))

    ### 
    #  Explore Standard deviation of the mean : \sigma / sqrt(N)
    #    Per : https://en.wikipedia.org/wiki/Standard_error#Standard_error_of_the_mean
    #    "the standard error of the mean is a measure of the dispersion of sample
    #    means around the population mean"
    ###
    # Draw 20 experiments, see if the means cluster with std. dev. of mean. Use dist. 2
    nSamp       = 50          # Number of samples in each experiment
    nExpL       = [20, 200, 2000, 20000, 50000, 100000]     # Number of experiments
    print("\n\n---------------------------------------------------------")
    print("########## SECTION 1 ##########")
    print("# Testing Std. Dev. of Mean for Population 2.\n"
          "# Pop2_mu = {:<.4f}\n# {} samples per experiment\n"
          "# The variance of the sampling distribution should tend to the population variance \n"
          "# divided by number of trials per experiment, i.e.\n"
          "#    std_sampdist -> std_pop / sqrt({}) = {:<.5f}"
          .format(np.mean(pop2V), nSamp, nSamp, np.std(pop2V)/np.sqrt(nSamp)))
    print("---------------------------------------------------------")
    print("{:<10}{:<15}{:<15}{:<17}{:<15}".format("nExp", "mean_sampdist", "std_sampdist",
          "stdL[0]/sqrt(N)", "mean(stdL/sqrt(N-1))"))
    # Loop over number of experiments
    for nExp in nExpL:
        experL = []               # Experiment list
        experMeanL = []
        experStdL = []
        for i in range(nExp):
            idxL    = np.random.randint(low=0, high=N2, size=nSamp)  # random draw of indices 
            sampL   = pop2V[idxL]                                    # Get Samples drawn from dist 2.
            mean    = np.mean(sampL)
            std     = np.std(sampL)
            # Record mean, stdev for this experiment
            experMeanL.append(mean)
            experStdL.append(std)
            experL.append([mean,std])
        ### Let's plot the distribution ###
        print("{:<10}{:<15.4f}{:<15.4f}{:<17.4f}{:<15.4f}".format(nExp,np.mean(experMeanL),
              np.std(experMeanL), experStdL[0] / np.sqrt(nSamp),
              np.mean(experStdL) / np.sqrt(nSamp-1)))
    print("Notice that 'std_sampdist' converges to 'mean(stdL/sqrt(N-1))', we'd \n"
          "     expect this if the standard deviation of the mean really is standard \n"
          "     dev of the distribution of means")
    


    ##############################################
    ### Calculate distributions ###
    ### Take distribution 1 as the Wild Type or standard or null hypothesis ###   
    ### We want to reject the Null Hypothesis, which is mu1 ###
    ### Use the Independent two sample t-test ###
    ###     ASSUMPTIONS : 
    ###         1. samples are equal in size
    ###         2. both groups (underlying populations) have same vairance
    ##############################################
    #t = (np.mean(pop2V) - mu1) / (sd2 / np.sqrt(N2))
    nSamp = N1
    #t=student_t_test_eq_samp_and_var(Pop1V=pop1V, Pop2V=pop2V, NSamp=nSamp)
    samp1 = pop1V[np.random.randint(low=0, high=N1, size=nSamp)]
    samp2 = pop2V[np.random.randint(low=0, high=N2, size=nSamp)]
    s1    = np.std(samp1)
    s2    = np.std(samp2)
    mu1   = np.mean(samp1)
    mu2   = np.mean(samp2)
    sp    = np.sqrt( (s1**2 + s2**2)/2.0) ### Pooled stdev
    t     = (mu1 - mu2) / (sp * np.sqrt(2.0 / nSamp))
    print("\n\n---------------------------------------------------------")
    print("########## SECTION 2 ##########")
    print("---------------------------------------------------------")
    print("t-score using entire distribution N1 {} and N2 {}".format(N1,N2))
    print("t = {:<.3f}\n    Pop1  : [mu,sd] = [{:<.3f},{:<.3f}]\n"
          "    Pop2  : [mu,sd] = [{:<.3f},{:<.3f}]".format(t,
           pop1_mu, pop1_sd,pop2_mu, pop2_sd))
    print("    Samp1 : [mu,sd] = [{:<.3f},{:<.3f}]\n"
          "    Samp2 : [mu,sd] = [{:<.3f},{:<.3f}]\n".format(mu1,s1,mu2,s2))
    



    ### Let's now look at the distribution of t-scores ###
    #print("\n---------------------------------------------------------")
    nExp  = 500
    print("\n---------------------------------------------------------"
          "-----------------------------------")
    print("########## SECTION 3 ##########")
    print("# Running {} Experiments per each sample size. Computing stats "
          "over all {} Experiments".format(nExp, nExp))
    print("---------------------------------------------------------"
          "-----------------------------------")
    print("   Equal sample sizes, equal variance                   |   "
          "   Equal sample sizes, equal variance - Welchs'")
    print("---------------------------------------------------------"
          "-----------------------------------")
    print("{:<7}{:<8}{:<8}{:<7} "
          "{:<8}{:<8}{:<9}| "
          "{:<8}{:<8}{:<7} "
          "{:<8}{:<8}{:<9}".format(
          "nSamp", "mu(t)", "std(t)", "frac>2",
          "mu(p)", "std(p)", "frac<.05",
          "mu(tW)", "std(tW)", "frac>2",
          "mu(pW)", "std(pW)", "frac<.05"))
    #for nSamp in [3,5,10,15,20,30,40,50,75,100]:
    for nSamp in [3,5,10,15,20,30,40]:
        ### Equal sample sizes, equal variance
        tL = np.zeros(nExp)
        pL = np.zeros(nExp)
        vL = np.zeros(nExp)
        ### un-equal sample sizes, un-equal variance
        tWelchL = np.zeros(nExp)
        pWelchL = np.zeros(nExp)
        vWelchL = np.zeros(nExp)
        for i in range(nExp):
            ### Draw Samples ###
            samp1V = pop1V[np.random.randint(low=0, high=N1, size=nSamp)]
            samp2V = pop2V[np.random.randint(low=0, high=N2, size=nSamp)]
            ### Compute t-score, p-values - equal samp size, equal variance ###
            (t,v,p)=student_t_test(Samp1V=samp1V, Samp2V=samp2V)
            tL[i] = t
            pL[i] = p
            ### Compute t-score, p-values - un-equal samp size, un-equal variance ###
            (t,v,p)=welchs_t_test(Samp1V=samp1V, Samp2V=samp2V)
            tWelchL[i] = t
            pWelchL[i] = p
        print("{:<7}{:<8.3f}{:<8.3f}{:<7.3f} "
              "{:<8.3f}{:<8.3f}{:<9.3f}| "
              "{:<8.3f}{:<8.3f}{:<7.3f} "
              "{:<8.3f}{:<8.3f}{:<9.3f}".format(
              nSamp, np.mean(tL), np.std(tL), len(tL[np.abs(tL) > 2])/nExp,
              np.mean(pL), np.std(pL), len(pL[np.abs(pL) < 0.05])/nExp,
              np.mean(tWelchL), np.std(tWelchL), len(tWelchL[np.abs(tWelchL) > 2])/nExp,
              np.mean(pWelchL), np.std(pWelchL), len(pWelchL[np.abs(pWelchL) < 0.05])/nExp))

    ### Let's now emulate the studies in Table 4 of
    ### "Evidence Base Update for Autism Spectrum Disorder" by Smith and Iadarola ###
    # first column is early intervertion, 2nd column is treatment as usual
    studySizeLL=[[13,12], [31,12], [35,24], [12,22], [24,21], [177,117]]
    esL = []        # List of effect sizes from studySizeLL
    varL= []        # List of variances from studySizeLL, computed from pooled stdev, sp
    for studyL in studySizeLL:
        samp1V = pop1V[np.random.randint(low=0, high=N1, size=studyL[0])]
        samp2V = pop2V[np.random.randint(low=0, high=N2, size=studyL[1])]
        mean1  = np.mean(samp1V)
        mean2  = np.mean(samp2V)
        sd1    = np.std(samp1V)
        sd2    = np.std(samp2V)
        # pooled stdev. see eqn 3.20 in Lipsey & Wilson
        var = (((studyL[0] - 1)*sd1**2 + (studyL[1] - 1)*sd2**2) /
               ((studyL[0] - 1) + (studyL[1] - 1) ))
        stdP  = np.sqrt(var)
        # Standardized mean diff - Cohen's d (?)- eq 3.21 Lipsey & Wilson, eq 7 latex notes
        es = (mean1 - mean2) / stdP   # Effect size
        esL.append(es)
        varL.append(var)

    cIL = []        # Confidence interval for each studySizeLL
    meanES = np.mean(esL)
    stdES  = np.sqrt(1/sum(varL))   # Eqn 13 in latex., p114 in Lipsey & Wilson
    z = 1.96        # Critical value for z-distribution, with alpha = 0.05
    lower  = meanES - z*stdES       # Eqn 14 in latex
    upper  = meanES + z*stdES       # Eqn 15 in latex
    print("\n\n---------------------------------------------------------"
          "-----------------------------------")
    print("########## SECTION 4 ##########")
    print("---------------------------------------------------------"
          "-----------------------------------")
    print("{:<10} {:<8} {:<8} {:<12} {:<8}".format("study",
          "N_treat", "N_wt", "Effect_Size", "Var") )
    for idx in range(len(studySizeLL)):
        print("{:<10} {:<8} {:<8} {:<12.6f} {:<8.6f}".format("study_{}".format(idx),
              studySizeLL[idx][0], studySizeLL[idx][1], esL[idx], varL[idx]))
          
    print("Total Effect Size = {:<10.6f}; 95% CI = [{:<10.6f}, {:<10.6f}]\n".format(meanES,
         lower, upper))
        
    
    

    


if __name__ == "__main__":
    main()

