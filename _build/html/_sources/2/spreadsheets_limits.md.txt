# Limitations of Spreadsheets

...OK, so here are some issues with this "manual" process of doing data science:

Firstly, it's tedious. You are doing the same thing — computing the average RT for each participant and condition — 100 times. While maybe you can get into a groove, with some chill music playing and a nice cup of coffee, it's still tedious and probably not the best use of your time. On top of that, it's **error prone**. You might make typos, you might accidentally miss including some rows for some subjects, you might forget to do one subject's data file, you might accidentally swap the congruent and incongruent values for one participant during the copying process, etc.. Wouldn't it be great if there was a machine that could do this automatically, and far more quickly and accurately than you? Then you would have more free time to just enjoy that coffee and music!

Another issue is that the manual process is not readily **scalable**: if you ran another experiment with 100 participants, you would be bringing twice as much boredom, tedium, and risk of human error as in your first experiment.

Finally, and perhaps most importantly, the manual process is not easily **reproducible**. That is to say, if you ran a new experiment, you would have to perform the same tedious process all over again, with the same risks of human error and terminal boredom. And if you wanted someone else to do the analysis for you, you would need to write out instructions and hope that they followed those instructions exactly. Furthermore, as often happens, if you were a student in the lab who graduates and moves on before the study is finished, someone else may be assigned to finish the data analysis, and they would have to figure out what you did, how you organized your files, etc.. In many cases when this happens, people have to start from scratch because the pervious person's process was not clearly documented, and it's very hard to check for errors except by going through a large number of files.

There has to be a better way!
