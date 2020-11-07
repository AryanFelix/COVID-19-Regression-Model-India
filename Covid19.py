import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

ds = pd.read_csv('https://api.covid19india.org/csv/latest/case_time_series.csv')
edits = []
x = ds.iloc[:-1, -1].values
for i in range(len(x)+1):
    edits.append(i+1)
ds = ds.assign(Day_No =  edits)
x = ds.iloc[:-1, -1].values
y = ds.iloc[:-1, 2].values
yrec = ds.iloc[:-1, 4].values
ydec = ds.iloc[:-1, 6].values
x = np.reshape(x,(-1,1))

polyreg = PolynomialFeatures(degree=4)
x_poly = polyreg.fit_transform(x)
linreg = LinearRegression()
linreg.fit(x_poly,y)
linreg2 = LinearRegression()
linreg2.fit(x_poly,yrec)
linreg3 = LinearRegression()
linreg3.fit(x_poly,ydec)

plt.plot(x,linreg.predict(x_poly),color='red')
plt.plot(x,linreg2.predict(x_poly),color='green')
plt.plot(x,linreg3.predict(x_poly),color='grey')
plt.title('COVID - 19 Cases in India (Infection-Recovery-Deaths Analysis) - Pre Prediction')
plt.xlabel('Day')
plt.ylabel('Cases')
plt.show()

print("\nCOVID-19 PREDICTOR\n")
print("Yesterday was Day Number : {}".format(ds.iat[-1,-1]))
xvalue = int(input("Enter Day Number for which COVID data is to be predicted : "))
y1 = linreg.predict(polyreg.fit_transform([[xvalue]]))
print("Predicted Infection = {}".format(y1))
y2 = linreg2.predict(polyreg.fit_transform([[xvalue]]))
print("Predicted Recovery = {}".format(y2))
y3 = linreg3.predict(polyreg.fit_transform([[xvalue]]))
print("Predicted Deaths = {}".format(y3))

x2 = np.array([xvalue])
x = np.append(x,x2)
x = np.reshape(x,(-1,1))
x_poly = polyreg.fit_transform(x)
plt.scatter(xvalue,y1,color='red')
plt.plot(x,linreg.predict(x_poly),color='red')
plt.scatter(xvalue,y2,color='green')
plt.plot(x,linreg2.predict(x_poly),color='green')
plt.scatter(xvalue,y3,color='grey')
plt.plot(x,linreg3.predict(x_poly),color='grey')
plt.title('COVID - 19 Cases in India (Infection-Recovery-Deaths Analysis) - Post Prediction')
plt.xlabel('Day')
plt.ylabel('Cases')
plt.show()