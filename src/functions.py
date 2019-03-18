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


