import os
import matplotlib.pyplot as plt
import pandas as pd
# Set the desired directory path
directory_path = r'C:\Users\maglab\Documents\Python Scripts\data\BPBO\B031\test'
file = 'IV_sweep_2K_0Oe_500.00uA_0deg_list_0.txt'
# Change the current working directory
os.chdir(directory_path)
data=pd.read_csv(file,sep='\t', header=0)

x = data['Current']
y = data['Voltage']
# Plot the data
plt.scatter(x, y)
plt.show()
