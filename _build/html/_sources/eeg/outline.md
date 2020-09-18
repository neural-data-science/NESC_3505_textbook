# EEG Chapter outline
___
## Learning Objectives
___
## Introducing EEG

### What are we measuring?
- Neural origins

### How is it measured?
- Electrodes and recording basics

### The Nature of EEG Data
- Time-varying, analog/continuous
- Multiple channels

### Ways of Looking at EEG Data
- Time domain - ERPs
- Frequency domain

### Preprocessing
*Conceptual* - cover MNE steps below.
- filtering
- event code processing
- segmentation (epoching)
- artifact removal
    - ICA
- averaging
---
## MNE-Python Package

### Overview
- background
- website

### Data import

### MNE Data Structure
- .info
- .__dict__

### Visualizing raw data
- raw.plot()

### Preprocessing
- filtering
- event code processing
- segmentation (epoching)
- artifact removal
    - ICA
- averaging

### Visualization
#### ERPs
- grand averages per subject
- group grand averages
- waveforms
- topo maps
- Coversion to pandas DataFrame
- using seaborn for statistical visualization
- mass univariate tests
- mean amplitude t-tests

#### Frequency Domain
- frequency spectrum
- time-frequency analysis (TFA)
