<!--
Compile : 
    pandoc - -biblio=notes/p-value_refs.bib -f markdown notes/practical_meta_analysis.md -t latex -o output.pdf
    pandoc - -biblio=p-value_refs.bib -f markdown practical_meta_analysis.md - -filter pandoc-crossref -t latex -o output.pdf

Notes:
    1. http://lierdakil.github.io/pandoc-crossref/ 
    2. https://pandoc.org/MANUAL.html#bullet-lists
--> 
\newcommand{\overbar}[1]{\mkern 1.5mu\overline{\mkern-1.5mu#1\mkern-1.5mu}\mkern 1.5mu}


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


Chapter 3 : Selecting, Computing and Coding the Effect Size Statistic
========================
1. Effect Size Statisitcs and their Variances
    a) Only consider statistics that encode magnitude and direction
        #. Excludes 
            * Simple direction of effects (dichotomous coding of whether treatment is better than control)
            * p-values 
                - confound effect magnitude with sample size
                - lack information on the overall magnitude and consistency of the effect
    #) Single research finding
        #. Statistical representation of one empirical relationship involving variables of interest on a single subject (study?) sample. This is the 'result'
        #. E.g.
            * correlation coefficient amongst data
            * correlation matrix
            * difference in means between treatment and control in research study
        #. Each research finding must be encoded as a value on the same effect size statistic
            * Statistic must be appropriate for nature of relationship measured in the studies
            * Compute value from quantitative values in study
            * If not enough information (distressingly common) to compute effect size, sometimes it can be estimated.
                - This is a necessary task for the meta-analyst
    #) Computing Effect size
        #. Studies with different sample sizes complicates computing effect size
            * Studies with more samples lead to a better estimation of underlying population.
            * Every effect size doesn't carry the same weight
            * Handled by 
                - Weighting effect size by a value that represents its precision. Can use:
                    + Sample size
                    + Standard error
                - Weights are inverse of squared standard error value, aka 'inverse variance weight'
                    + Question : How is this any better than the sample size being embedded within the p-value?
            * Sometimes getting standard error is challenging, so use already well formulated effect size statistics.
                - standardized mean difference
                - correlation coefficient
                - odds-ratio
    #) Notes on Notation 
        #. $ES$ = effect size 
        #. $SE$ = standard error of the effect size
        #. $w$  = inverse variance weight of the effect size
        #. Subscripts used to indicate type of effect size. 
            * E.g.
                - $sm$ for standardized mean difference 
                - $p$ for proportion effect size.
#. Types of Research Findings and Applicable Effect Size Statisticso
    a) One-Variable Relationsips (Central Tendency Description)
        #. Pattern of observation across categories (i.e. treatment vs. control)
           * E.g.
                - Central Tendancy Statistics : mean, median, mode
                - Distribution of Values statistics : frequency, proportions, sums, variance standard deviation and range.
        #. These types of one-variable relations aren't often meta-analyzed.
        #. Effect size issues are straight forward if the following two things are met:
            * First, variable must be operationalized the same way across studies to be meaningfully compared.
                - Ex. that works:   
                    + Each study reports the average value of people reporting as male or female
                - Ex. that fails: 
                    + Each study uses a different mathematics achievement test. Would need a method to standardize in order to compare
            * Second, must be possible to define an effect size statistic that represents the information of interest and to determine the standard error associated with that statistic.
        #. Proportions
            * Research involving proportions, can use the proportion effect size statistic.
                - E.g.
                    + Fraction of homeless who abuse alcohol
            * Each study must draw from the same population
                - E.g. 
                    + homeless, persons hospitalized, substance abusers.
            * Two types of methods for generating effect size statistics
                - Base it on proportions. 
                    $$ES_{p} = p = \frac{k}{n}$$ {#eq:es_p}
                    $$SE_{p} = \sqrt{\frac{p(1-p)}{n}}$$ {#eq:se_p}
                    $$w_{p} = \frac{1}{SE_{p}^{2}} = \frac{n}{p(1-p)}$$ {#eq:w_p}
                    + $k$ = number of subjects in category of interest
                    + $n$ = total number of subjects
                    + Numeric simulations indicate that when $p \leq 0.2$ or $p \geq 0.8$ size of confidence interval is underestimated b/c of compression of standard error as $p$ approaches either 0 or 1
                    + Direct proportion works only when 
                    +  Mean is of interest
                    +  $0.2 \leq p \leq 0.8$
                - Base it on proportions converted to logits
#.  \bf{HERE I Stopped to focus on Cohen's d which is the whole reason I started reading this book}

<!--
        #. Arithmetic Means
    #) Two-Variable Relationsips 
        #. Pre-Post Contrasts
        #. Unstandardized Mean Gain
            * Estimation Procedures
            * Example
        #. Standardized Mean Gain
            * Estimation Procedures
            * Example
        #. Group Contrasts
        #. Unstandardized Mean Difference
            * Estimation Procedures
            * Example
        #. Standardized Mean Difference
            * Estimation Procedures
            * Example
        #. Proportion Difference
            * Estimation Procedures
            * Example
        #. Odds-Ratio
            * Estimation Procedures
            * Cell Frequencies Equal to Zero
            * Example
        #. Mixing Group Differences measured on continuous and dichotomous scales
    #) Association between variables
        #. Two Dichotomous Variables (Odds-Ratio and Phi Coefficient)
            * Example
        #. A Dichotomous and Continuous Variables (The Point-Biserial Coefficent and Standardized Mean Difference)
        #. Two continuous variables (the Product-Moment Correlation)
            * Estimation Procedures
            * Example
        #. Mixed Pairings of Dichotomous and Continuous Variables
    #) Multivariate Relationships
        #. Reports of Nonsignificance and Missing Data Problems in Coding Effect Sizes
-->


Chapter 8 : Interpreting and Using Meta-Analysis Results
========================
1. Interpreting Effect Size Values
    a) Problems : 
        #. Effect size statistics are non-intuitive
    #) Rules of Thumb for Effect Size Magnitude [@cohen77; @cohen88] . Standardized mean difference : 

    |  small        |medium       | large |
    |------:        |------:      |:------|
    | $ES \leq 0.20$| $ES = 0.50$ | $ES \leq 0.80$|

    #) Rules of Thumb for correlation effect size : 

    |  small       |medium      | large |
    |------:       |------:     |:------|
    | $r \leq 0.10$| $r = 0.25$ | $r \geq 0.40$|

        #. Supported by distribution in Figure 8.1 from [@lipsey93]
    #) Translation of Effect Sizes to other metrics
        #. Original Metric
            * Often in field of research there is a dominant metric that is used, E.g. 
                - achievement test
                - length of stay at an institution
            * To do this : 
                - Determine mean and standard deviation.
                - Ensure control groups in each study represent sample population
                - Pool results from multiple studies into overall mean
                - Put both the intervention and control groups on the same scale
                    + Control group mean plus product of effect size and standard deviation 
                    + I'm conceptually confused here
            * E.g.
                - Suppose mean effect size is +0.30 on client satisfaction survey for medical treatment.
                - In control group - nurses tell patients 'treatment as ususal'
                - In treatment group - nurses give patients an orientation session
                - Most common metric is the Likert scale (ranging from very unsatisfied to very satisfied)
                - Meta-analyst pulls out all studies using the Likert scale.
                    + Determine control group mean and standard deviation, call pair of values $k$
                    + Find grand mean and standard deviation from all $k$ pairs from selected studies
                    + Because each study will likely have a different sample size, need to use weighted mean with degrees of freedom as weights.
                    $$Pooled Mean = \bar{X}_{control} = \frac{\sum(n_{i} - 1)\bar{X}_{i}}{\sum(n_{i} - 1)}$$ {#eq:mean_pooled}
                    $$Pooled sd = \sigma_{control} = \sqrt{\frac{\sum(n_{i} - 1)\sigma_{i}}{\sum(n_{i} - 1)}}$$ {#eq:sd_pooled}
                    $$\bar{X}_{i} = \text{mean of the control group}$$ {#eq:mean}
                    $$n_{i} = \text{sample size of control group}$$ {#eq:samp}
                    $$s_{i} = \text{standard deviation of control group}$$ {#eq:sd}
                    + Calculations yield mean = 3.5 and standard deviation = 1.5. This would yield an average value of treatment as : 
                    $$\bar{X}_{treat} = \bar{X}_{control} + ES \times \sigma_{control}$$ {#eq:sd}
                    $$\bar{X}_{treat} = 3.5 + 0.3 \times 1.5 = 3.95 $$ {#eq:sd}

#. Caveats in Interpreting Meta-Analysis Results
    a) Methodological Adequacy of the Research Base
        #. Meta-analysis is only as good as the constituent studies.
            * When better quality studies differ from lower quality studies, discard lower quality (really? This contradicts what was said in Ch 1. and 2.)
        #. Often not possible to simply classify studies as good or bad
            * Use multivariate analysis from Ch. 6. to handle.
    #) Confounding of Substantitve and Methodological Features
        #. Can use meta-analysis to break out different treatment vairants and compare effect sizes.
        #. E.g., Shadish 1992, p131 mentions meta-analysis of psychotherapy
            * Break out shows behavioral therapy has larger effect vs. nonbehavioral therapy
            * Behavioral therapy, e.g. use desensitization therapy for phobias and monitor effects by measuring tolerance for feared situation.
                - Called 'reactive' measures.
                - More sensitve then pencil and paper standardized anxiety scale.
                    + This is the reason why behavioral therapy has a larger effect.
        #. Point of above example is that you need to be careful about not confusing results (effect sizes) with confounding variables.
            * Break out effect sizes and compare with confounding variables.
                - E.g. compare rigorous vs. not rigorous studies and the resultant effect sizes.
    #) Importance of Variance
        #. Can't look strictly at means. Need to consider variance also
        #. Look at distribution of effect sizes (see homogeneity test in Ch. 6)
            * If distribution of effect sizes is hetergeneous (i.e. widely distributed), it would be bad practice to just 'average' over all of them.
                - "averaging over contrary results is not likely to converge on truth, just muddle it" : what a great quote.
            * Want homogenous distribution of effect sizes.
        #. Use random effects model to account for nonsampling error variance in effect size
            * Use when there is a plausible suspicion that there will be an additional random component contributing to effect size.
    #) Research Gaps and Generalizability
        #. If certain treatments, settings, client populations, etc. are not well represented then generalization of results is questionable.
        #. Sometimes the hypothesis being researched is not what we would want (or do) see in clinical settings.
        #. The research setting usually is not the clinical setting
            * This is my point with the ABA therapy promulgated by ?
                + The advise and consent group (control) likely gets treatment in the community from people with high school degrees vs. the treatment group which gets therapy from University of Washington therapists with BS or MS.
    #) Sampling Bias
        #. Literature is suspected of being highly biased towards statisitcally significantly studies.
        #. Is sampling bias large enough to effect conclusion of meta-analysis?
        #. Use unpublished studies to bracket publication bias.
            * Thought : there may be a reason a study was unpublished, i.e. poor experimental design
            * Thought : getting reliable unpublished work is likely very challenging.
        #. Can use [@rosenthal79] \emph{fail-safe N} adapted by [@orwin83]
            * Number of additional studies with null result to lower the $z \leq 1.65$  ($p \geq 0.05$)
        $$k_{0} = k \left(\frac{\overbar{ES}_{k}}{\overbar{ES}_{c}} - 1\right)$$ {#eq:fsN}
        $$k_{0} = \text{N studies w/ ES = 0 needed to reduce mean ES to } \overbar{ES}_{c}$$
        $$k = \text{number of studies in mean effect size}$$
        $$\overbar{ES}_{k} = \text{weighted mean effect size}$$
        $$\overbar{ES}_{c} = \text{criterion effect size level}$$
        #. E.g. 
            * let $k$ = 42, $\overbar{ES}_{k}$ = 0.74, $\overbar{ES}_{c}$ = 0.50.  Solving [@eq:fsN] yields 
            $$k_{0} = 42\left(\frac{.74}{.50} - 1\right) = 20$$ {#eq:fsN_ex}
            * Thus it takes 20 null studies to drop the $ES$ to 0.50


#. Implications of Meta-Analysis for Practice and Policy
    a) Purpose of book is to help researcheres without meta-analytic experience to properly undertake one.
    #) Properly formed meta-analysis studies can be used to inform policy.
    #) Good meta-analysis is conducted in 'fish bowl'
        #. All criteria, data and procedures are explicit
                    
    
Questions
--------------
1. Question : How is this any better using $\frac{1}{\sigma_{mean}}$ in effect sizes than the sample size being embedded within the p-value?
#.

To Do
--------------
1. Read Chapter 6 on homengeity test
#. Read Chapter 3 on unstandardized mean gain
#. Read p117(?) on confidence intervals.




Bibibliography
--------------







