import pandas as pd
import numpy as np
import math

new_delhi_data = pd.read_csv("new_delhi_covid_aqi_2.csv")

mean_pm25 = new_delhi_data['pm25'].mean()
mean_pm10 = new_delhi_data['pm10'].mean()
mean_o3 = new_delhi_data['o3'].mean()
mean_no2 = new_delhi_data['no2'].mean()
mean_so2 = new_delhi_data['so2'].mean()
mean_co = new_delhi_data['co'].mean()

mean_corona = new_delhi_data['Daily'].mean()

xix_pm25 = []
xix_pm10 = []
xix_o3 = []
xix_no2 = []
xix_so2 = []
xix_co = []
yiy_corona = []

for i in range(0,len(new_delhi_data)):
    xix_pm25.append(new_delhi_data['pm25'].iloc[i] - mean_pm25)
    xix_pm10.append(new_delhi_data['pm10'].iloc[i] - mean_pm10) 
    xix_o3.append(new_delhi_data['o3'].iloc[i] - mean_o3)
    xix_no2.append(new_delhi_data['no2'].iloc[i] - mean_no2)
    xix_so2.append(new_delhi_data['so2'].iloc[i] - mean_so2)
    xix_co.append(new_delhi_data['co'].iloc[i] - mean_co)
    yiy_corona.append(new_delhi_data['Daily'].iloc[i] - mean_corona)

s_pm25 = 0
s_pm10 = 0
s_o3 = 0
s_no2 = 0
s_so2 = 0
s_co = 0
s_corona = 0

for j in range(0,len(xix_pm25)):
    s_pm25 = s_pm25 +  (xix_pm25[j] * xix_pm25[j])
    s_pm10 = s_pm10 +  (xix_pm10[j] * xix_pm10[j])
    s_o3 = s_o3 +  (xix_o3[j] * xix_o3[j])
    s_no2 = s_no2 +  (xix_no2[j] * xix_no2[j])
    s_so2 = s_so2 +  (xix_so2[j] * xix_so2[j])
    s_co = s_co +  (xix_co[j] * xix_co[j])
    s_corona = s_corona +  (yiy_corona[j] * yiy_corona[j])

s_pm25 = math.sqrt(s_pm25/(len(new_delhi_data) - 1)) 
s_pm10 = math.sqrt(s_pm10/(len(new_delhi_data) - 1)) 
s_o3 = math.sqrt(s_o3/(len(new_delhi_data) - 1)) 
s_no2 = math.sqrt(s_no2/(len(new_delhi_data) - 1)) 
s_so2 = math.sqrt(s_so2/(len(new_delhi_data) - 1)) 
s_co = math.sqrt(s_co/(len(new_delhi_data) - 1)) 
s_corona = math.sqrt(s_corona/(len(new_delhi_data) - 1)) 

r_pm25 = 0
r_pm10 = 0
r_o3 = 0
r_no2 = 0
r_so2 = 0
r_co = 0

for k in range(0,len(xix_pm25)):
    r_pm25 = r_pm25 + ((xix_pm25[k] * yiy_corona[k]) / (s_pm25 * s_corona))
    r_pm10 = r_pm10 + ((xix_pm10[k] * yiy_corona[k]) / (s_pm10 * s_corona))
    r_o3 = r_o3 + ((xix_o3[k] * yiy_corona[k]) / (s_o3 * s_corona))
    r_no2 = r_no2 + ((xix_no2[k] * yiy_corona[k]) / (s_no2 * s_corona))
    r_so2 = r_so2 + ((xix_so2[k] * yiy_corona[k]) / (s_so2 * s_corona))
    r_co = r_co + ((xix_co[k] * yiy_corona[k]) / (s_co * s_corona))

r_pm25 = r_pm25/(len(new_delhi_data) - 1)
r_pm10 = r_pm10/(len(new_delhi_data) - 1)
r_o3 = r_o3/(len(new_delhi_data) - 1)
r_no2 = r_no2/(len(new_delhi_data) - 1)
r_so2 = r_so2/(len(new_delhi_data) - 1)
r_co = r_co/(len(new_delhi_data) - 1)

print('Using Basic Statistics:')
print('Correlation Coefficient (PM2.5 and Daily Corona Cases): ', r_pm25)
print('Correlation Coefficient (PM10 and Daily Corona Cases): ', r_pm10)
print('Correlation Coefficient (O3 and Daily Corona Cases): ', r_o3)
print('Correlation Coefficient (NO2 and Daily Corona Cases): ', r_no2)
print('Correlation Coefficient (SO2 and Daily Corona Cases): ', r_so2)
print('Correlation Coefficient (CO and Daily Corona Cases): ', r_co)

print()
print('Using Pearson Method: ')
print('Correlation Coefficient (PM2.5 and Daily Corona Cases): \n', new_delhi_data[['pm25','Daily']].corr(method='pearson'))
print('Correlation Coefficient (PM10 and Daily Corona Cases): \n', new_delhi_data[['pm10','Daily']].corr(method='pearson'))
print('Correlation Coefficient (O3 and Daily Corona Cases): \n', new_delhi_data[['o3','Daily']].corr(method='pearson'))
print('Correlation Coefficient (NO2 and Daily Corona Cases): \n', new_delhi_data[['no2','Daily']].corr(method='pearson'))
print('Correlation Coefficient (SO2 and Daily Corona Cases): \n', new_delhi_data[['so2','Daily']].corr(method='pearson'))
print('Correlation Coefficient (CO and Daily Corona Cases): \n', new_delhi_data[['co','Daily']].corr(method='pearson'))