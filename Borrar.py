
import pandas as pd
import matplotlib.pyplot as plt
import datetime
import numpy as np
 
# create dataframe
 
dataframe = pd.DataFrame({'date_of_week': np.array([datetime.datetime(2021, 11, i+1)
                                                    for i in range(7)]),
                          'classes': [5, 6, 8, 2, 3, 7, 4]})
 
# Plotting the time series of given dataframe
plt.plot(dataframe.date_of_week, dataframe.classes)
 
# Giving title to the chart using plt.title
plt.title('Classes by Date')
 

 
# Providing x and y label to the chart
plt.xlabel('Date')
plt.ylabel('Classes')
