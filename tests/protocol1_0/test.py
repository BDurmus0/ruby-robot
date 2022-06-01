import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd
import read_write as motor_cntrl 
import time 

DELAY_BETWEEN_FRAMES = 0.3
# Mapping procces between 0-1023
def multiplied(dfm): 
    result_of_mapping = dfm/0.297
    result_of_rounded_number = round(result_of_mapping)
    return result_of_rounded_number

# Read csv file
df = pd.read_csv('/home/rubi/Desktop/Testdir/python/data/yorunge.csv')

# Convert data frame to matrix 
dfm = np.array(df)

# Initial Position of the motors
present = [0, 590, 495, 440, 445, 540, 600, 430, 433, 525, 491, 540, 435]

#Algorithm of the walking
for frame in range(0,51,1): # Each frame are in loop (we can change of the range value that we can need it)
    for motor_id in range(1,13): # This is respect to motor id declaration 
        motor_cntrl.SDK(motor_id, present[motor_id], multiplied(dfm[frame][motor_id+1])+present[motor_id])
    
    time.sleep(DELAY_BETWEEN_FRAMES) # Delay for frames