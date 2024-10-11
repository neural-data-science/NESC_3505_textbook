## Summary

Preprocessing EEG data and deriving ERPs is a multi-step process. It's important to understand what each step does, why it's applied, and how to choose the correct parameters. 

There are a few additional steps that could be included in a preprocessing pipeline, that we have omitted here. For example, sometimes there there are *bad channels* — electrodes that had a poor connection throughout the recording, or were broken. There are ways to manually or automatically identify these and have them ignored throughout the preprocessing stream, and then *interpolate* data for these electrodes after artifact correction. 

After each individual participant's data has been preprocessed through a pipeline line this, the next step in analyzing an ERP experiment would be a group-level analysis. In a group-level analysis, the data from all participants would typically be averaged, and visualized using waveform plots and scalp topographic maps similar to the ones we've created here for one participant. 

As well, statistics can be applied. An important question in applying statistics to EEG data is how to handle time - do we perform statistical comparisons between conditions at every time point, or average over periods of time when ERP components occur, or include time as an additional variable in an analysis? 

One of the most common ways for ERP studies to run statistics is to average the data at each channel over a time period appropriate for the component of interest. For example, in this study a mean amplitude could be computed over the 600–800 ms time window, and then a *t*-test could be performed to compare the mean amplitude values between conditions. 