<!--
Compile : 
    pandoc - -biblio=notes/p-value_refs.bib -f markdown notes/practical_meta_analysis.md -t latex -o output.pdf

Notes:
    1. http://lierdakil.github.io/pandoc-crossref/ 
    2. https://pandoc.org/MANUAL.html#bullet-lists
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
        #. empirical research studies
    #) Doesn't apply to :
        #. summarize theoretical papers
        #. conventional research reviews
        #. policy proposals

    #) Used to study statistics that summarize research findings
        #. If full data available, better to analyze directly

#. Pre-requisites
    a) Conceptually comparable 
        #. same constructs and relationships
        #. E.g. Don't compare a study with \emph{Treat vs. Control} to a study with \emph{Level of Depression vs. Level of Service Received}.
    #) Comparing same variables
        #. E.g. Don't compare studies where Study 1 = \emph{Treat vs. Control} to Study 2 = \emph{Treat vs. Group 1 vs. Group 2}

#. Meta-analysis represents each study by finding the `effect-size statistics'
    a) Would use different metric for studies using bivariate correlation vs. mean value of dependant variables.

#. Appropriateness of comparing studies is often in the ``eye of the beholder''
    a) Must have rational for inclusion and exclusion
    #) Must have rational for domain of interest


#. Key Concept of Effect Size
    a) Often studies will use different metrics to measure say depression
        #. E.g. Beck's depression inventory vs. Hamilton's rating scale vs. therapists' ratings of depression.
        #. Impossible to compare directly these different metrics because they are constructed differently.
        #. Need method to compare these different metrics.
        #. Effect size to the rescue
    #) Effect size based on using `standardization' to compare different metrics
        #. Standardization method : the difference between means of treatment vs. control in terms of how many $\sigma$ ( standard deviations) the means are separated
            * This is the 'Effect Size', (I think this is Cohen's 'd'?)
        #. Works only if we can assume studies (using different metrics) are drawing from same population.
        #. Effect size can be used to compare studies using different metrics b/c we stardardized to something we can compare.
            * It is basically like using an operator to translate the variables into a new space
    #) Other, less effective / rudimentary, Effect Size statisitcs
        #. statistical significance
        #. p-value
    #) Good effect size statistics measure :
        #. \emph{magnitude} and \emph{direction}
        #. Constructed to avoid other confounding effects
            * E.g. sample size
      
#. Strengths of Meta-Analysis : 
    a) Imposes useful discipline on summarizing results
        #. Each step is documented and open to scrutiny
            * Specify criteria defining population of interest
            * Organized strategy for identifying / retrieving eligible studies
            * Formal coding of study characteristics.
        #. Making transparent permits one to assess author's assumptions, procedures, evidence and conclusions.

    #) Provides quantitative, differentiable and sensitive method of study comparison
        #. Traditionaly, study comparison used qualitative summaries, i.e. `vote-counting', statistical significance
            * Statistical significance reflects both \emph{magnitude of effect} and \emph{sampling error}
                - \emph{sampling error} is almost completely sample size dependant.
            * Small studies suffer from low statistical power.
                - Can find false positives (Type I error)
        #. Effect size is continuous variable, not just 'yes' or 'no'

    #) Capable of finding effects that are obscurred by other approaches to summarizing research
        #. Gives further level of discrimination when compared to qualitative comparisons (i.e. statistical significance)
        #. Meaningful effects, relationships and differences (related to experimental differences between studies) more likely to be discovered in meta-analysis than othere, qualitative comparisons.    
    
    #) Provides organized way of handling information from large numbers of studies.


#. Weaknesses of Meta-Analysis :  
    a) Takes a lot of effort and expertise.
        #. Requires specialized knowledge about research
        #. Requires knowledge of which effect size metrics to use and how to analyze them.

    #) The 'mechanical' nature of the process 
        #. Might miss :
            * social context
            * theoretical influences (and implications)
            * methodological quality
            * subtle / complex aspects data, analysis and results of the studies

    #) Most persistent criticism : the mix of studies involved (i.e. apples vs. oranges) 
        #. Smith and Glass (1977) did meta-anlysis on a wide range of psychotherapies
            * Treatment types :
                - behavioral therapy
                - psychodynamic therapy
                - gestalt therapy
            * Outcome measurables : 
                - fear and anxiety
                - self-esteem
                - global adjustment
                - emotional-somatic problems
                - school functioning
            * Many felt that these treatments and outcomes were way too different to compare.
    
    #) Mixing study findings of different methodological qualities
        #. Shouldn't include poorly designed and under powered studies in meta-analysis.

        #. No agreement about 'good' methodological studies
            * Even 'good' methodological studies are contrived 
                - E.g. univeristy clinics, demonstration projects
                - Don't represent health care delivered in the generic community

        #. If meta-analysts standards are too loose, will be criticized as 'garbage in / garbage out'



#. Criticism mitigation
    a) Can test for statisitcal homogeneity to see if grouping effect sizes from different studies has more variation than would be expected from sampling error alone.
        #. Provides 'plausibility' argument to validity of grouping
        #. Use variance in effect size of distributions instead of only comparing the means of the effect sizes.
            * I think this is why [@smith15] puts confidence intervals
    #) Two approaches to mitigate mixing study with different methodological quality:
        #. Keep methodological criteria strict.  Accept consequences.
        #. Treat methodological variation among studies as an empirical matter to be investigated with meta-analysis

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
        #. Differences between group means
        #. Correlations between variables
        #. Proportion of kk
    #) Must find effect size statistic that can effectively encode all the studies' results.
    #) Possible effect-size statistics:
        #. standardized mean difference
        #. correlation coefficient
        #. odds-ratio
        #. some custom ad-hoc thing that you make up
    #) Forms of research findings that can be represented with 'off-the-shelf' effect size statistics
        #. Central Tendency Description
            * E.g. mean, median, mode or proportion on single sample of respondents
            * E.g. proportion of women who have migraines
            * Can be done if various studies provide number of samples * meta-analysis can be used.
            * Can only be done if 'operationalization' of variable of interest is same for all findings.
                - E.g. every study uses same measure, like mean
        #. Pre-Post Contrasts
            * E.g. how much better reading scores are at end of school year vs. beginning.
            * Types of statistics used are mean difference gain
            * [@becker88] used standardized difference between means for meta-analysis.
        #. Group Contrasts
            * Type of research involves one or more variables between two or more groups
            * Central tendency values (i.e. mean or proportion) are measured and compared
            * Two primary forms of this research:
                - Experimental or clinical trials research
                    + Treatment vs. Control
                - Group differnces research
                    + Groups are compared based on identified differences.
                    + E.g. income of men vs. women
                    + E.g. reading ability of ID students and low-achieving but non-ID students
            * Frequent application to research of this type, esp treatment vs. control
                - No generalized method for comparison between 3 or more groups, but still can compare two groups.
        #. Association between Variables
            * covariation between two variables.
                - E.g. correlation between socioeconomic status and student's math grades
                - Reported as : e.g. chi-square coefficient, odds-ratio, lambda
            * Two distinct types of studies here:
                - Measurement research
                    + Associations using measurement instruments
                    + E.g. SAT scores vs. later college scores, measuring prediction ability of future college performance.
                - Individual differences research
                    + Measures correlation between selected characteristics
                    + E.g. relation between IQ and number of siblings
                    + E.g. alcohol use vs. domestic violence
    #) Each preceding forms can usually be meta-analyzed straight forwardly
    #) Research not following above formats can be challanging to meta-analyze
        #. E.g. multiple regression results cannot be generally represented by effect size statistic.
            * But the correlation matrix which it is based can be used in bivariate correlations
        #. Other challenging research types to meta-analyze:
            * multiple regression
            * discriminant analysis 
            * factor analysis 
            * structural equation modeling
            
#. Study Eligibility Criteria
1. Recommendations for including studies in meta-analysis
    a) Draw up detailed specifications of the criteria a study must meet if its findings are to be includeded in the meta-analysis.
    #) Categories to consider
        #. Distinguishing features of a qualifying study
            * Flesh out what a study must and must not have to be included.
            * E.g. If topic is the effectiveness of interventions, specify type/critical features of the intervention.
        #. Research respondents
            * Constrain study's demographics.  
                - E.g. Only juviniles? Adults? What is a juvinile (18 or 21)? English-speaking?
        #. Key variables
            * Interventions Studies : specific outcome variables needed to address target question
            * Group Comparison Studies : certain essential variables on which groups are contrasted
            * Correlational Studies : may be certain covariates or control variables 
            * Must have enough data to construct effect size statistics.
        #. Research designs
            * Maybe only include a certain set (or combination) of studies like 
                - Random assignment control group
                - quasi-experiments
                - double blind studies
                - placebo controls
        #. Cultural and linguistic range
            * Maybe only include studies in language which researcher are fluent. 
            * Must specify
        #. Time frame
            * Only interested in the most recent studies?
            * Only interested when certain instrument or method became available?
        #. Publication type
            * Journal articles, books, dissertations, technical reports, conference presentations.
            * If unpublished material excluded, then there will be an upward bias.
                - Often used as proxy for research quality.
    #) Methodological Quality Revisited
        #. How inclusive to be when considering studies?
            * More inclusive 
                - More studies
                - Higher noise
                - Will include studies that critics find unacceptable
            * Less inclusive 
                - Less studies
                - Higher signal 
                - Possibility that more rigorous studies are conducted in unrepresentative circumstances and produce findings of limited generalizability
        #. Research findings generally aren't robust to methodological differences between studies.
            * Often method characteristics that make the most difference, aren't the ones that meta-analyst assumes are most influential.
        #. Methodological reporting in social and behavioral science literature is poor
            * Silent or ambiguous on important methodological or procdural matters.
            * As meta-analyst criteria evolves, will find that studies won't provide enough information to apply that criteria.
        #. Methodological quality is in the eye of the beholder
            * Only a few methodological canons are agreed upon
                - valid measures
                - random assignment
            * No general agreement on methods / procedures to use in a given field of study.
        #. Few researchers and meta-analysts have developed schemes for assessing methodological quality.
        #. There should be a reciprocal relationship between restrictiveness of criteria and the extent of coding after studies are selected.
            * If more methodological variation is permitted, more important to encode this.
            * Allows measuring possible methodological effects.
        #. Can use meta-analysis to study relationship of methods to findings (see above)

#. Identifying, Locating, and Retrieving Research Reports
    a) Usually want to select all studies that meet criteria, sampling for population of studies is generally ill-advised.
    #) Most of this section is outdated and irrelevant to me.
        #. Summarized:
            * Do literatures search by walking through references in papers
            * Use computerized data bases.
            * Use boolean logic and regex like syntax.
    #) Possible electronic resources (this is from 1992...)
        #. PsycINFO
        #. ERIC (Educational Resources Information Center
        #. MEDLINE (precursor to pubmed?)
        #. Library of Congress
        #. GOOGLE! (from me)
        #. University libraries.




Bibibliography
--------------







