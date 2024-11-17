import pandas
import matplotlib.pyplot as plt

data=pandas.read_csv('empdata.csv')

plt.plot(data.id, data.firstname)

plt.show() 