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
#       6. Choose significance p-value _before_ experiment
#       7. Intuition on dealing with p-value when comparing two normal distributions
#       8. 1. Standard deviation of the mean : \sigma / sqrt(N)
#          Per : https://en.wikipedia.org/wiki/Standard_error#Standard_error_of_the_mean
#          "the standard error of the mean is a measure of the dispersion of sample
#          means around the population mean"
#
#
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

def print_help(ExitCode):
    """
    ARGS:
    RETURN:
    DESCRIPTION:
    DEBUG:
    FUTURE:
    """
    sys.stderr.write("./src/main.py [analyze|collect|test]\n"
                     "   [analyze]: Analyze previously collected data\n"
                     "   [collect]: Collect fresh data and then analyze\n"
                     "   [test]   : Run some unit tests and a test data set, "
                     "              check output\n"
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
    elif(len(sys.argv) != 1):
        print_help(ExitCode=1)
    random.seed(42)

    ### Create the population distributions, draw our experimental samples from these ###
    # Population / Dist 1
    mu1 = 0     ### average
    sd1 = 1     ### standard dev
    N1  = 1000  ### Number of samples 
    pop1V = np.zeros([N1])
    for i in range(N1):
        pop1V[i] = random.gauss(mu1, sd1)
    # Population / Dist 2
    mu2 = 1
    sd2 = 1
    N2  = 1000   ### Number of samples 
    pop2V = np.zeros([N2])
    for i in range(N2):
        pop2V[i] = random.gauss(mu2, sd2)

    ### 
    #  Explore Standard deviation of the mean : \sigma / sqrt(N)
    #    Per : https://en.wikipedia.org/wiki/Standard_error#Standard_error_of_the_mean
    #    "the standard error of the mean is a measure of the dispersion of sample
    #    means around the population mean"
    ###
    # Draw 20 experiments, see if the means cluster with std. dev. of mean. Use dist. 2
    nSamp       = 50          # Number of samples in each experiment
    nExpL       = [20, 200, 2000, 20000, 50000, 100000]     # Number of experiments
    print("Population mean = {:<.4f}, {} samples per experiment\n".format(
          np.mean(pop2V),nSamp))
    print("---------------------------------------------------------")
    print("{:<10}{:<15}{:<15}{:<17}{:<15}".format("nExp", "mean_of_means", "std_of_means",
          "stdL[0]/sqrt(N)", "mean(stdL/sqrt(N))"))
    for nExp in nExpL:
        experL = []               # Experiment list
        experMeanL = []
        experStdL = []
        for i in range(nExp):
            idxL    = np.random.randint(low=0, high=N2, size=nSamp)
            sampL   = pop2V[idxL]     # Samples drawn from dist 2.
            mean    = np.mean(sampL)
            std     = np.std(sampL)
            experMeanL.append(mean)
            experStdL.append(std)
            experL.append([mean,std])
        ### Let's plot the distribution ###
        print("{:<10}{:<15.4f}{:<15.4f}{:<17.4f}{:<15.4f}".format(nExp,np.mean(experMeanL),
              np.std(experMeanL), experStdL[0] / np.sqrt(nSamp),
              np.mean(experStdL) / np.sqrt(nSamp-1)))
    print("Notice that 'std_of_means' converges to 'mean(stdL/sqrt(N))', we'd \n"
          "     expect this if the standard deviation of the mean really is standard \n"
          "     dev of the distribution of means")
    


    ### Calculate distributions ###
    ### Take distribution 1 as the Wild Type or standard or null hypothesis ###   
    ### We want to reject the Null Hypothesis, which is mu1 ###
    t = (np.mean(pop2V) - mu1) / (sd2 / np.sqrt(N2))

    print("t = {:<.3f}\nmean2 = {:<.3f}\nstd_dev2 = {:<.3f}\n".format(t,
           np.mean(pop2V), np.std(pop2V)))
    
    


if __name__ == "__main__":
    main()

