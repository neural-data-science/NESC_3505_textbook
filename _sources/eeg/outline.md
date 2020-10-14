# EEG Chapter outline
___
## Learning Objectives
- to do
___
## Introducing EEG
- overview

### What are we measuring?
- Neural origins
- time vs frequency
- ERP Components
    - scalp
    - latent

### The Nature of EEG Data
    - Time-varying, analog/continuous
    - Multiple channels

### How is it measured?
- Electrodes and recording basics
- note about MEG

### Preprocessing
*Conceptual* - cover MNE steps below.
- filtering
- event code processing
- segmentation (epoching)
    - baselines
- artifact removal
    - ICA
- averaging
---
## MNE-Python Package

### Overview
- background
- website
- classes

### Data import
- fif files
- other formats

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

### Group-Level Analysis
- reading in multiple data files and organizing as dicts or lists
- group grand averages

### Visualization
#### ERPs
- waveforms
- topo maps
- Coversion to pandas DataFrame
- using seaborn for statistical visualization
- mean amplitude t-tests
- mass univariate tests

#### Frequency Domain
- frequency spectrum
- time-frequency analysis (TFA)
