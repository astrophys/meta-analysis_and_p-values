<!--
Compile : 
    pandoc - -biblio=notes/p-value_refs.bib -f markdown notes/practical_meta_analysis.md -t latex -o output.pdf

Notes:
    1. http://lierdakil.github.io/pandoc-crossref/ 
--> 


<!--
    YAML section
--> 
---
title: Notes on ``Practical Met-Analysis" by Lipsey and Wilson.
author: Ali Snedden
date: 2019-04-05
abstract: In this document, I record my notes and thoughts as I read ``Practical Met-Analysis'' by Lipsey and Wilson [@lipsey01]
...

\maketitle
\tableofcontents
\pagebreak

Chapter 1 : Introduction
========================
<!-- 
Situations whee meta-analysis is applicable
--------------------------------------------
-->

1. Situations where meta-analysis is applicable
    a) Applies to 
        * empirical research studies
    #) Doesn't apply to :
        * summarize theoretical papers
        * conventional research reviews
        * policy proposals

    #) Used to study statistics that summarize research findings
        * If full data available, better to analyze directly

#. Pre-requisites
    a) Conceptually comparable 
        * same constructs and relationships
        * E.g. Don't compare a study with \emph{Treat vs. Control} to a study with \emph{Level of Depression vs. Level of Service Received}.
    #) Comparing same variables
        * E.g. Don't compare studies where Study 1 = \emph{Treat vs. Control} to Study 2 = \emph{Treat vs. Group 1 vs. Group 2}

#. Meta-analysis represents each study by finding the `effect-size statistics'
    a) Would use different metric for studies using bivariate correlation vs. mean value of dependant variables.

#. Appropriateness of comparing studies is often in the ``eye of the beholder''
    a) Must have rational for inclusion and exclusion
    #) Must have rational for domain of interest


#. Key Concept of Effect Size
    a) Often studies will use different metrics to measure say depression
        * E.g. Beck's depression inventory vs. Hamilton's rating scale vs. therapists' ratings of depression.
        * Impossible to compare directly these different metrics because they are constructed differently.
        * Need method to compare these different metrics.
        * Effect size to the rescue
    #) Effect size based on using `standardization' to compare different metrics
        * Standardization method : the difference between means of treatment vs. control in terms of how many $\sigma$ ( standard deviations) the means are separated
            - This is the 'Effect Size', (I think this is Cohen's 'd'?)
        * Works only if we can assume studies (using different metrics) are drawing from same population.
        * Effect size can be used to compare studies using different metrics b/c we stardardized to something we can compare.
            - It is basically like using an operator to translate the variables into a new space
    #) Other, less effective / rudimentary, Effect Size statisitcs
        * statistical significance
        * p-value
    #) Good effect size statistics measure :
        * \emph{magnitude} and \emph{direction}
        * Constructed to avoid other confounding effects
            - E.g. sample size
      
#. Strengths of Meta-Analysis : 
    a) Imposes useful discipline on summarizing results
        * Each step is documented and open to scrutiny
            - Specify criteria defining population of interest
            - Organized strategy for identifying / retrieving eligible studies
            - Formal coding of study characteristics.
        * Making transparent permits one to assess author's assumptions, procedures, evidence and conclusions.

    #) Provides quantitative, differentiable and sensitive method of study comparison
        * Traditionaly, study comparison used qualitative summaries, i.e. `vote-counting', statistical significance
            - Statistical significance reflects both \emph{magnitude of effect} and \emph{sampling error}
                + \emph{sampling error} is almost completely sample size dependant.
            - Small studies suffer from low statistical power.
                + Can find false positives (Type I error)
        * Effect size is continuous variable, not just 'yes' or 'no'

    #) Capable of finding effects that are obscurred by other approaches to summarizing research
        * Gives further level of discrimination when compared to qualitative comparisons (i.e. statistical significance)
        * Meaningful effects, relationships and differences (related to experimental differences between studies) more likely to be discovered in meta-analysis than othere, qualitative comparisons.    
    
    #) Provides organized way of handling information from large numbers of studies.


#. Weaknesses of Meta-Analysis :  
    a) Takes a lot of effort and expertise.
        * Requires specialized knowledge about research
        * Requires knowledge of which effect size metrics to use and how to analyze them.

    #) The 'mechanical' nature of the process 
        * Might miss :
            - social context
            - theoretical influences (and implications)
            - methodological quality
            - subtle / complex aspects data, analysis and results of the studies

    #) Most persistent criticism : the mix of studies involved (i.e. apples vs. oranges) 
        * Smith and Glass (1977) did meta-anlysis on a wide range of psychotherapies
            - Treatment types :
                + behavioral therapy
                + psychodynamic therapy
                + gestalt therapy
            - Outcome measurables : 
                + fear and anxiety
                + self-esteem
                + global adjustment
                + emotional-somatic problems
                + school functioning
            - Many felt that these treatments and outcomes were way too different to compare.
    
    #) Mixing study findings of different methodological qualities
        a) Shouldn't include poorly designed and under powered studies in meta-analysis.

        #) No agreement about 'good' methodological studies
            - Even 'good' methodological studies are contrived 
                + E.g. univeristy clinics, demonstration projects
                + Don't represent health care delivered in the generic community

        #) If meta-analysts standards are too loose, will be criticized as 'garbage in / garbage out'



#. Criticism mitigation
    a) Can test for statisitcal homogeneity to see if grouping effect sizes from different studies has more variation than would be expected from sampling error alone.
        * Provides 'plausibility' argument to validity of grouping
        * Use variance in effect size of distributions instead of only comparing the means of the effect sizes.
            - I think this is why [@smith15] puts confidence intervals
    #) Two approaches to mitigate mixing study with different methodological quality:
        * Keep methodological criteria strict.  Accept consequences.
        * Treat methodological variation among studies as an empirical matter to be investigated with meta-analysis

#. Recommendations for further reading
    a) [@cooper93] 
    
    #) [@wang98] 



Chapter 2 : Problem Specification and Study Retrieval 
========================
1. Problem / Hypothesis considered in this chapter
    a) How effective are challenge programs in reducing the subsequent antisocial behavior of juveniles with behavioral problems?
    #) What are the characteristics of the most and least effective programs?
    #) Do these programs have favorable effects on other outcomes such as relations with peers, locus-of-control and self-esteem?

#. Identifying the Form of the Reseach to be Analyzed
    a) Research into Hypothesis may take different forms:
        * Differences between group means
        * Correlations between variables
        * Proportion of kk
    #) Must find effect size statistic that can effectively encode all the studies' results.
    #) Possible effect-size statistics:
        * standardized mean difference
        * correlation coefficient
        * odds-ratio
        * some custom ad-hoc thing that you make up
    #) Forms of research findings that can be represented with 'off-the-shelf' effect size statistics


Bibibliography
--------------







