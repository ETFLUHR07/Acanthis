from matplotlib import rcParams
import pandas as pd
#from pandas_profiling import ProfileReport
import matplotlib.pyplot as plt
import csv
import math


#csv = 'C:\\Users\\ethan\\OneDrive\\Documents\\SD File Reader\\'

altitude = []

""" altVariable = 

rP = 
#relative Pressure

rT = 
#relative Temperature

rH = 
#relative height """

#data = pd.read_csv(
'output-onlinerandomtools.csv'
#)

with open('output-onlinerandomtools.csv') as f:
    reader = csv.reader(f)

    for row in reader:
        altitude.append((44331.5 - 4946.62) * row ** (0.190263))
        print(row)

    
print(altitude)
    