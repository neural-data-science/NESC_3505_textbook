"""
Helper script to convert MTloc_design.txt to BIDS-compliant events file
"""

import numpy as np
import pandas as pd

def design_to_events(design_file, tr=2.0, output_file=None):
    """
    Convert a block design vector to BIDS events format.
    
    Parameters:
    -----------
    design_file : str
        Path to design.txt file (one value per TR, 0=rest, 1=stimulus)
    tr : float
        Repetition time in seconds
    output_file : str
        Output path for events.tsv (if None, returns DataFrame)
    
    Returns:
    --------
    events_df : pd.DataFrame
        BIDS-formatted events with onset, duration, trial_type
    """
    # Read design vector
    design = np.loadtxt(design_file)
    
    # Find block onsets and durations
    events = []
    in_block = False
    onset_tr = 0
    
    for i, val in enumerate(design):
        if val == 1 and not in_block:
            # Start of stimulus block
            onset_tr = i
            in_block = True
        elif val == 0 and in_block:
            # End of stimulus block
            duration_trs = i - onset_tr
            events.append({
                'onset': onset_tr * tr,
                'duration': duration_trs * tr,
                'trial_type': 'motion'
            })
            in_block = False
    
    # Handle case where last block extends to end
    if in_block:
        duration_trs = len(design) - onset_tr
        events.append({
            'onset': onset_tr * tr,
            'duration': duration_trs * tr,
            'trial_type': 'motion'
        })
    
    # Create DataFrame
    events_df = pd.DataFrame(events)
    
    # Add rest periods if desired (optional, can be implicit)
    # For now, we just have the motion stimulus events
    
    if output_file:
        events_df.to_csv(output_file, sep='\t', index=False)
        print(f"Created {output_file}")
    
    return events_df


if __name__ == '__main__':
    # Example usage
    import sys
    
    design_file = 'data/BIDS/sub-001/ses-01/func/MTloc_design.txt'
    output_file = 'data/BIDS/sub-001/ses-01/func/sub-001_ses-01_task-MotionLoc_events.tsv'
    
    events = design_to_events(design_file, tr=2.0, output_file=output_file)
    print(f"\nGenerated {len(events)} events:")
    print(events)
