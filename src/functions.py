from math import pi
from math import sqrt
from math import exp
from math import erf
from math import gamma
from error import exit_with_error
import numpy as np



def convert_tscore_to_pvalue(T=None,DF=None):
    """
    ARGS:
        T : T-score
        DF : Degrees of freedom
    RETURN:
        Converts T-Score to P-value
    DESCRIPTION:
    DEBUG:
        1. Previously (when I assumed that t-distribution -> gaussian):
           convert_tscore_to_pvalue() is working correctly.
           t=2.0 -> p = 0.045500263896363025
           t=3.0 -> p = 0.002699796063260762
           t=4.0 -> p = 6.334248366629547e-05
           t=5.0 -> p = 5.733031437360481e-07
           t=6.0 -> p = 1.9731752898266564e-09
           Pretty much exact match
        2. Now using correct t-distribution...Compare with
           https://www.danielsoper.com/statcalc/calculator.aspx?id=8
           Can also use wolfram, E.g. : 
            1 - Integrate PDF[StudentTDistribution[3], x] dx, -1.25,1.25

           [DF=15, t-score=1.25] = 0.23045059 (Soper) vs 0.23047198 (Ali)  : 0.09% diff
           [DF=3, t-score=1.25] = 0.29992947  (Soper) vs 0.29781848 (Ali)  : 0.70% diff 
           [DF=2, t-score=1.25] = 0.33773382  (Soper) vs 0.32789701 (Ali)  : 2.91% diff
           [DF=6, t-score=3]    = 0.02400820  (Soper) vs 0.02395244 (Ali)  : 0.23% diff

    FUTURE:
    """
    #xV,pdfV = gaussian(S=1,Mu=0)
    xV,pdfV = t_dist(DF=DF)
    pvalue = np.sum(pdfV[xV<-abs(T)]) + np.sum(pdfV[xV>abs(T)])
    return(pvalue)
    
    
    
def gaussian_integral(S=None, Mu=None, Xmin=None, Xmax=None):
    """
    ARGS:
    RETURN:
        Gaussian pdf integral. 

    DESCRIPTION:
        Used wolfram alpha to get the integral.
                E.g. integrate 1/sqrt(2*pi*s**2) exp(-(x-m)**2 / (2*s**2)) dx
    DEBUG:
        1. This must work correctly since convert_tscore_to_pvalue() works
    FUTURE:
    """
    lower = (-erf( (Mu - Xmin) / (sqrt(2.0) * S))  / 2.0)
    upper = (-erf( (Mu - Xmax) / (sqrt(2.0) * S))  / 2.0)
    return(upper - lower)


def gaussian(S=None, Mu=None):
    """
    ARGS:
    RETURN:
        pdf: Gaussian pdf in bins. Each bin has the fraction of the total 
             curve (which sums to 1) within the bin.
        xL : x list of values corresponding with probL
    DESCRIPTION:
        Maybe this is really a gaussian kernel ?
    DEBUG:
        1. Roughly sums to 1.0
        2. This must work correctly since convert_tscore_to_pvalue() works
    FUTURE:
    """
    xL=[]
    pdfL=[]
    dx = S/100.0
    for x in np.arange(-10*S+Mu, 10*S+Mu, dx):
        #xL.append(1 / sqrt(2*pi*S**2) * exp(-(x-Mu)**2 / (2*(S**2))  ))
        pdfL.append(gaussian_integral(S=S, Mu=Mu, Xmin=x-dx, Xmax=x))
        xL.append(x)
    xV = np.asarray(xL)
    pdfV = np.asarray(pdfL)
    return(xV,pdfV)



def t_dist(DF=None):
    """
    ARGS:
        DF = Degrees of Freedom
    RETURN:
        pdf: Gaussian pdf in bins. Each bin has the fraction of the total 
             curve (which sums to 1) within the bin.
        xL : x list of values corresponding with probL
    DESCRIPTION:
        Maybe this is really a gaussian kernel ?
    DEBUG:
        1. Roughly sums to 1.0
        2. This must work correctly since convert_tscore_to_pvalue() works
    FUTURE:
    """
    xL=[]
    pdfL=[]
    v = DF
    dx = 1/100.0
    for x in np.arange(-10, 10, dx):
        pdfL.append(integrate(Function=t_dist_pdf_at_x, DF=v, Xmin=x, Xmax=x+dx))
        xL.append(x)
    xV = np.asarray(xL)
    pdfV = np.asarray(pdfL)
    return(xV,pdfV)


def t_dist_pdf_at_x(DF=None, X=None):
    """
    ARGS:
        DF = Degrees of Freedom
    RETURN:
        The value of a student t-distribution at a particular value of x.
    DESCRIPTION:
    DEBUG:
        1. Compared to PDF[StudentTDistribution[5], 2] in wolfram alpha.
           IDENTICAL for several values:
            [DF=5, X=2]
            [DF=3, X=0.5]
            [DF=1, X=0.5]
    FUTURE:
    """
    v = DF      ### Use notation of Wikipedia, with nu (or v) = Degrees of Freedom
    x = X
    return(gamma((v + 1)/2.0) * (1 + x**2/v)**(-(v+1)/2.0) / (sqrt(v*pi) * gamma(v/2.0)))



def integrate(Function=None, DF=None, Xmin=None, Xmax=None):
    """
    ARGS:
        Function : any function that takes a value X and returns a value Y
    RETURN:
        a float
    DESCRIPTION:
        Integrates using Simpson's rule 
        See : http://mathworld.wolfram.com/SimpsonsRule.html
    DEBUG:
        1. Using Wolfram alpha vs. integrate()
            --> Wolfram : Integrate PDF[StudentTDistribution[10], x] dx, x=0..0.5 
                [DF=10, Xmin=0, Xmax=0.5] : 0.186053 vs. 0.1860670
                [DF=1, Xmin=0, Xmax=0.5] : 0.147584  vs. 0.14760840
                [DF=1, Xmin=0, Xmax=0.25] : 0.0779791 vs. 0.0779811
    FUTURE:
    """
    h  = (Xmax - Xmin)/2.0
    f0 = Function(DF=DF, X=Xmin)
    f1 = Function(DF=DF, X=Xmin+h)
    f2 = Function(DF=DF, X=Xmin+2*h)
    return(1/3.0 * h * (f0 + 4*f1 + f2))


def student_t_test_eq_samp_and_var(Pop1V = None, Pop2V = None, NSamp = None):
    """
    ARGS:
        Pop1V : The total population of the WT
        Pop2V : The total population of the Treatment
        NSamp in both experiments
    RETURN:
        a student t-score, degrees of freedom and associated p-value
    DESCRIPTION:
        Per https://en.wikipedia.org/wiki/Student%27s_t-test, this test assumes
        Equal sample sizes, equal variance are assumed
    DEBUG:
        1. Matches results expected in high N limit with mu1 ~ mu2
    FUTURE:
    """
    N1 = len(Pop1V)
    N2 = len(Pop2V)
    samp1 = Pop1V[np.random.randint(low=0, high=N1, size=NSamp)]
    samp2 = Pop2V[np.random.randint(low=0, high=N2, size=NSamp)]
    s1    = np.std(samp1)
    s2    = np.std(samp2)
    mu1   = np.mean(samp1)
    mu2   = np.mean(samp2)
    ### Equal variance and sample size ###
    #sp    = np.sqrt( (s1**2 + s2**2)/2.0) ### Pooled stdev
    #t     = (mu1 - mu2) / (sp * np.sqrt(2.0 / NSamp))      

    ### Un-Equal variance and unequal sample size ###
    (t,v) = welchs_t_test(Pop1V = Pop1V, Pop2V = Pop2V, N1Samp = len(samp1), N2Samp = len(samp2))
    p = convert_tscore_to_pvalue(T=t, DF=v)
    return(t,v,p)



def welchs_t_test(Pop1V = None, Pop2V = None, N1Samp = None, N2Samp = None):
    """
    ARGS:
        Pop1V : The total population of the WT
        Pop2V : The total population of the Treatment
        N1Samp: Number of samples in experiment 1
        N2Samp: Number of samples in experiment 2
    RETURN:
        a student t-score and degrees of freedom
    DESCRIPTION:
        Per https://en.wikipedia.org/wiki/Welch%27s_t-test
        Test assumes:
            1. unequal variances
            2. Normal distributions
            3. Unequal sample sizes
    DEBUG:
    FUTURE:
    """
    N1 = len(Pop1V)
    N2 = len(Pop2V)
    samp1 = Pop1V[np.random.randint(low=0, high=N1, size=N1)]
    samp2 = Pop2V[np.random.randint(low=0, high=N2, size=N2)]
    s1    = np.std(samp1)
    s2    = np.std(samp2)
    mu1   = np.mean(samp1)
    mu2   = np.mean(samp2)
    t     = (mu1 - mu2) / np.sqrt(s1**2/N1Samp + s2**2/N2Samp)
    v1    = N1Samp - 1
    v2    = N2Samp - 1
    v     = (s1**2/N1Samp + s2**2/N2Samp)**2 / (s1**4/(N1Samp**2*v1) + s2**4/(N2Samp**2*v2))
    return(t,v)


#def gamma(Z=None):
#    """
#    ARGS:
#        Z can be either integer or float
#    RETURN:
#    DESCRIPTION:
#        Use simpson's rule to compute the value of the Gamma function
#        http://mathworld.wolfram.com/SimpsonsRule.html
#    DEBUG:
#    FUTURE:
#        Do better integration scheme
#    """
#    sum=0
#    tol=10**-7
#    frac=1.0
#    dx = 10**-4
#    x = 10**-9
#
#    if(Z < 1.0):
#        exit_with_error("ERROR!!! Our gamma() misbehaves when Z<1.0 b/c the "
#                        " integral beings at 0 and 0**(Z-1) = 1/0 which is undefined\n"
#                        " We must be more clever than that\n")
#    while frac > tol:
#        prevSum = sum
#        # integrate
#        h = dx / 2.0
#        x0 = x
#        x1 = x + h
#        x2 = x + 2.0*h
#        try:
#            y0 = x0**(Z - 1) * np.exp(-x0)
#            y1 = x1**(Z - 1) * np.exp(-x1)
#            y2 = x2**(Z - 1) * np.exp(-x2)
#        except ZeroDivisionError:
#            exit_with_error("ERROR!!")
#            #yi = xi**(Z - 1) * np.exp(-xi)   ### HANDLE xi=0!!!
#        #area = dx * yi + dx * (yf - yi) * 0.5   ## Integrate triangle
#        area = 1/3.0 * h * (y0 + 4*y1 + y2)
#        sum = sum + area
#        x = x + dx
#        frac = abs(sum - prevSum) / sum
#    return(sum)
