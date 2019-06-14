# Meta-analysis and p-values
## Purpose
I recently became interested in meta-analysis after reading the [Smith and Iadarola 2015](https://www.tandfonline.com/doi/abs/10.1080/15374416.2015.1077448).
In their paper they compare a variety of papers and used Cohen's 'd' as the metric for their analsysis.  
They utilize 95% confidence intervals, but fail to describe how they compute either Cohen's 'd' or the confidence intervals.
They state "When possible, we present results in terms of effect size (Cohen’s d) and 95% confidence intervals, as reported by the investigators or derived from Wilson’s (n.d.) effect size calculator, which uses formulas presented by [Lipsey and Wilson (2001)](https://psycnet.apa.org/record/2000-16602-000)"
This is a very unsatisfying description of their work and they should provide the formula from which they work.  
So, I decided to look into this myself.

## Description
I have no formal statistics training, so I took this as an opportunity to learn about p-values and meta-analysis.
Within this repo you'll find :

1. My notes on Chapters 1,2,3,6 and 8 from [Practical Meta-Analysis by Lipsey and Wilson](https://psycnet.apa.org/record/2000-16602-000).
See `notes/practical_meta_analysis.md`.
2. A code that runs a series of 'experiments' to help develop intuition on :
    - Standard deviation / standard error of the mean 
    - t-scores (incl. Student and Welchs' distribution)
    - p-values
    - meta-analysis


## Installation / Running
#### Dependencies
All this was built on OSX 10.13.6 using Homebrew 2.1.0:
1. Python 3 (tested with v3.6.5)
2. numpy    (tested with v1.14.2)
3. matplotlib (tested with v2.2.2)
4. pandoc   (tested with v2.7.2)
5. pandoc-citeproc (tested with v0.16.1.3)
6. pandoc-crossref (tested with v0.3.4.0)

#### Running
To run the simulation / numerical experiments :

```
./src/main.py mu1 s1 mu2 s2

    mu1 : float, mean(population 1), assumed gaussian
    s1  : float, stdev(population 1)
    mu2 : float, mean(population 2), assumed gaussian
    s2  : float, stdev(population 2)
```

E.g.

```
python src/main.py 0 1 0 1
```

To compile the notes on [Practical Meta-Analysis by Lipsey and Wilson](https://psycnet.apa.org/record/2000-16602-000) : 

```
pandoc --biblio=notes/meta-analysis_refs.bib -f markdown notes/practical_meta_analysis.md --filter pandoc-crossref -t latex -o notes/output.pdf
```


## Discussion
The python code generates two large populations (100,000 samples each) that follow Gaussian distributions with means and standard deviations specified at the command line (see previous section).
This code does a series of experiments by drawing samples from these two underlying populations and computing p-values, standard deviations of the mean and other quantities. 
The point is to generate some statistical intuition.
Let's now discuss the various sections of the code.

### Section 1 : Standard error of the mean 
Here we sample population 2 50 times per experiment.
Each experiment is conducted `nExp = [20, 200, 2000, 20000, 50000, 100000]` times.
We call each series of experiments a 'set'.
So for the first set, there are 20 experiments where each experiment samples population 2 50 times.

We compute 4 columns : 
1. `mean_sampdist` column : mean of the set using each experiment's mean 
2. `std_sampdist` column  : standard deviation of the set using each experiment's mean 
3. `stdL[0]/sqrt(N)` column : standard deviation of first experiment in the set divided by the sqrt(50) samples in the experiment. `N` = 50 samples per experiment.
4. `mean(stdL/sqrt(N-1))` column : mean of all the sets standard deviations divided by the number of samples. `N` = 50 samples per experiment. This isn't particularly useful for intuition. It isn't surprising that this tends to `std_sampdist` b/c ultimately it is using the same underlying data.

Each set of experiments has its own variance and mean, this is called a "sampling distribution."
Per Wikipedia's entry on ["Standard Error of the Mean"](https://en.wikipedia.org/wiki/Standard_error#Standard_error_of_the_mean), we can show mathematically that the variance of the sampling distribution is equal to the _population's_ variance divided by sample size of each experiment.

```
std_sampdist^2 = std_pop^2 / N  
std_sampdist = std_pop / sqrt(N)
# In our example, when nExp = 200 (with 50 samples per experiment) and Population 2's std = 1.0, std_sampdist = 0.1396 
0.1396 ~ 1.0 / sqrt(50)
0.1396 ~ 0.1414
```

So the important take away from the standard error of the mean provides us a method of estimating the population standard deviation / variance.  
This is rather neat.

### Section 2 : t-score using entire sample
In this section we use the [Independent two-sample t-test](https://en.wikipedia.org/wiki/Student%27s_t-test).
In order for this to work, the population distributions must have the same number of samples and standard deviation.
Therefor for this section to run, these conditions must be met.




### Section 3 : Computing t-scores using Student's t-test and Welch's t-test


### Section 4 : Computing Cohen's 'd' and a meta-analysis example.



When running identical distributions (i.e. `python src/main.py 0 1 0 1`):

<!---[Smith and Iadarola 2015][https://www.tandfonline.com/doi/abs/10.1080/15374416.2015.1077448]'s confidence intervals aren't necessarily symetric, which is confusing because on p114 of [Lipsey and Wilson (2001)][https://psycnet.apa.org/record/2000-16602-000] they describe computing the confidence interval utilizing the critical value of the z-distribution and simply doing `mean effect size +/- z_crit_value`.
Using [Lipsey and Wilson (2001)][https://psycnet.apa.org/record/2000-16602-000] formulation of the confidence interval, it should be symmetric about the mean.
It is not obvious from their -->

