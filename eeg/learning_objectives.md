# Learning Objectives

This chapter covers electroencephalography (EEG), a technique for non-invasively measuring electrical activity from electrodes placed on the scalp.

By the end of this chapter, you should be able to:
- Explain the neural origins of EEG data
- Explain, in basic terms, how EEG is recorded
- Explain the difference between time- and frequency-domain treatments of EEG data
- Explain the rationale for fundamental EEG data preprocessing operations, including:
    - filtering
    - event code processing
    - segmentation (epoching)
    - artifact removal
    - averaging
- Describe the purpose of the MNE-Python software package
- Use MNE-Python to perform the above EEG preprocessing steps
- Use MNE-Python to visualize EEG data in the time and frequency domains, including
    - waveform plots of one or more electrodes
    - scalp topography plots
    - frequency spectra
    - time-frequency plots
- Convert processed EEG data from MNE-Python to a pandas DataFrame
- Plot averaged EEG data using Seaborn
