# The Grammar of Graphics

This section is based on Leland Wilkinson's seminal book, *The Grammar of Graphics* {cite:ts}`GOG`, originally published in 1999 and a second edition in 2005, and summarized in a shorter form in the [*Handbook of Computational Statistics*](https://doi.org/10.1007/978-3-642-21551-3_13).

In a natural human language, grammar is *generative* — it allows hierarchical, recursive embedding of words in phrases and sentences that allow for virtually infinite forms of expression. Without grammar, we would need one word to explain every individual concept we wished to express. The grammar is the underlying structure that allows us to derive shared meanings from combinations of words.

The grammar of graphics (GOG) is similar. It specifies the underlying structure of graphs (representations/abstractions of data), independent of the data, or the form/type of the graphic visualization. That is to say, it's not about defining categories of graphs such as pie charts and bar charts, but instead about the underlying principles of representing data that generate such visualizations. The grammar of graphics are in part *mathematical* and in part *aesthetic*. Whereas math provides tools for presenting abstractions (e.g., an average of a set of data points), aesthetics provides principles to relate sensory attributes to abstractions (e.g., data points from condition A are in red, and from condition B in blue). The grammar of graphics thus describes processes for transforming **graphs** (sets of data points; mathematical abstractions) into **graphics** (visual representations) using **aesthetics** (physical attributes such as size and colour).

 Wilkinson defines three stages of graphic creation: specification, assembly, and display.

 **Specification** involves translating a human's intentions into a formal set of instructions.

**Assembly** is the creation of a graphic from its specification. This is less about the grammar of graphics itself, as how the grammar is interpreted and used, e.g., by a piece of software, to convert a specification into a visualization.

**Display** is the actual act of rendering the assembled specification. To understand how this is different from assembly, consider that the same graphic can be rendered as a graphics file (e.g., PNG), as an interactive display in a web site, printed on paper, 3D printed in plastic, rendered in VR, etc..

The grammar of graphics is focused primarily on specification. Many software packages (such as [*Altair*](https://altair-viz.github.io/) and [*plotnine*](https://plotnine.readthedocs.io/) in Python; [*ggplot2*](https://ggplot2.tidyverse.org/) in R; [*Vega*](https://vega.github.io/vega/) in JavaScript; and [*plotly*](https://github.com/plotly) which can be used across several languages) use the grammar of graphics to define a set of specifications, and use these to assemble and display graphics. Other plotting packages, such as Python's  *matplotlib* package, are not based around the GOG. That is to say, while the GOG is argued to be a principle that underlies all graphics, software packages need not be designed with a syntax that follows the GOG. On the other hand, once one understands the principles of GOG, software packages whose syntax *does* follow the GOG may be intuitive, elegant, and powerful to use.

## Architecture

According to Wilkinson, the grammar of graphics comprises seven components:
1. Variables
2. Algebra
3. Scales
4. Statistics
5. Geometry
6. Coordinates
7. Aesthetics

The GOG further defines an architecture, the **dataflow**, which defines a logical sequence in which these components should be defined and applied, as the outputs of component are generally needed as the inputs to the next. This flow is shown in the figure below:

![](images/dataflow_GOG.png)
Dataflow of the grammar of graphics. Redrawn from Wilkinson {cite:ts}`GOG`.

### Variables
Data are organized into *variables*. That is, values with labels. For example, in a reaction time study, the values could be RTs in milliseconds, and the labels would indicate things like the experimental condition for a particular reaction time, which subject it was recorded from, etc.. Data are typically organized into tables, as we see when working in pandas, where each row is a data point with (typically) a number of columns and values that provide labels.

A critical categorization of variables is that they can be either **continuous** — varying along a continuum in some range — or **categorical** — having a limited set of discrete values. Reaction times are an example of a continuous variable, as are many neuroscientific measures like voltage in an electrophysiological recording or BOLD signal in an fMRI study. Examples of categorical variables include experimental conditions (e.g., congruent or incongruent flankers; drug vs. placebo). Sometimes, a dimension that is inherently continuous is represented as a categorical variable. For example, time is continuous, however in an experiment we might have discrete time points. Imagine an intervention study where each participant takes a drug every day for 8 weeks. Each participant might come to the lab three times: once prior to the intervention (baseline measurement) once at the end of the 8-week intervention (to see if the measure of interest have changed since the baseline visit), and then a follow-up visit 3 months later (to see if any effects lasted beyond the treatment period). In this case we would typically just treat "time" as a discrete variable with three levels: baseline, post-intervention, and follow-up, rather than treating time as a continuous variable, in terms of the number of days or weeks between each study visit.

In GOG, variables are converted to *varsets*. The varset is, essentially, the organization of data as needed to generate the graph or provide the information that we hope to derive from the graphic. The varset includes the data of interest, its labels, its ranges, and an index. For continuous variables, range could be the minimum to maximum recorded values or, if the values are on a fixed scale such as 0-100, this could define the range even if our data set didn't include any actual 0s or 100s; for categorical variables, this includes the category levels present in the data as well as potentially addition ones, such as for missing data). The index is used to organize the data according to where it came from; in psychology and neuroscience studies, often the index is the ID of the participant.

### Algebra

### Scales

### Statistics

### Geometry

### Coordinates

### Aesthetics
