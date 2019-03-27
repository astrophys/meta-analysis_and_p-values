from math import pi
from math import sqrt
from math import exp
from math import erf
import numpy as np



def convert_tscore_to_pvalue(T=None):
    """
    ARGS:
    RETURN:
    DESCRIPTION:
    DEBUG:
        1. convert_tscore_to_pvalue() is working correctly.
           t=2.0 -> p = 0.045500263896363025
           t=3.0 -> p = 0.002699796063260762
           t=4.0 -> p = 6.334248366629547e-05
           t=5.0 -> p = 5.733031437360481e-07
           t=6.0 -> p = 1.9731752898266564e-09
           Pretty much exact match
    FUTURE:
    """
    xV,pdfV = gaussian(S=1,Mu=0)
    pvalue = np.sum(pdfV[xV<-T]) + np.sum(pdfV[xV>T])
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



def t_distribution(DF=None):
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
    dx = S/100.0
    for x in np.arange(-10*S+Mu, 10*S+Mu, dx):
        #xL.append(1 / sqrt(2*pi*S**2) * exp(-(x-Mu)**2 / (2*(S**2))  ))
        pdfL.append(gaussian_integral(S=S, Mu=Mu, Xmin=x-dx, Xmax=x))
        xL.append(x)
    xV = np.asarray(xL)
    pdfV = np.asarray(pdfL)
    return(xV,pdfV)






def student_t_test_eq_samp_and_var(Pop1V = None, Pop2V = None, NSamp = None):
    """
    ARGS:
        Pop1V : The total population of the WT
        Pop2V : The total population of the Treatment
        NSamp in both experiments
    RETURN:
        a student t-score
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
    sp    = np.sqrt( (s1**2 + s2**2)/2.0) ### Pooled stdev
    t     = (mu1 - mu2) / (sp * np.sqrt(2.0 / NSamp))
    return(t)



def welchs_t_test(Pop1V = None, Pop2V = None, N1Samp = None, N2Samp = None):
    """
    ARGS:
        Pop1V : The total population of the WT
        Pop2V : The total population of the Treatment
        N1Samp: Number of samples in experiment 1
        N2Samp: Number of samples in experiment 2
    RETURN:
        a student t-score
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
    samp1 = Pop1V[np.random.randint(low=0, high=N1, size=NSamp)]
    samp2 = Pop2V[np.random.randint(low=0, high=N2, size=NSamp)]
    s1    = np.std(samp1)
    s2    = np.std(samp2)
    mu1   = np.mean(samp1)
    mu2   = np.mean(samp2)
    t     = (mu1 - mu2) / np.sqrt(s1**2/N1Samp + s2**2/N2Samp)
    v1    = N1Samp - 1
    v2    = N2Samp - 1
    v     = (s1**2/N1Samp + s2**2/N2Samp)**2 / (s1**4/(N1Samp**2*v1) + s2**4/(N2Samp**2*v2))
    return(t)


def gamma(Z=None):
    """
    ARGS:
        Z can be either integer or float
    RETURN:
    DESCRIPTION:
        This 
    DEBUG:
    FUTURE:
        Do better integration scheme
    """
    sum=0
    tol=10**-7
    frac=1.0
    dx = 10**-4
    x = 10**-9

    while frac > tol:
        prevSum = sum
        # integrate
        xi = x
        xf = x + dx
        try:
            yi = xi**(Z - 1) * np.exp(-xi)
        except ZeroDivisionError:
            exit_with_error("ERROR!!")
            #yi = xi**(Z - 1) * np.exp(-xi)   ### HANDLE xi=0!!!
        yf = xf**(Z - 1) * np.exp(-xf)
        area = dx * yi + dx * (yf - yi) * 0.5   ## Integrate triangle
        sum = sum + area
        x = x + dx
        frac = abs(sum - prevSum) / sum


    return(sum)
