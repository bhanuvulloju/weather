import matplotlib.pyplot as plt
import numpy as np
from bs4 import BeautifulSoup
import requests


city_code = input("Enter city id : ")
url =f'https://weather.com/en-IN/weather/today/l/{city_code}'
airquality_url = 'https://weather.com/en-IN/forecast/air-quality/l/' + city_code
source = requests.get(url).text

soup = BeautifulSoup(source, 'lxml')

# Get Temperature Value
tem = soup.find('span', class_='CurrentConditions--tempValue--MHmYY')
print("Temperature  ->  ",tem.text)


# Get Air Quality Index
source2 = requests.get(airquality_url).text
soup2 = BeautifulSoup(source2, 'lxml')
tem2 = soup2.find('text', class_='DonutChart--innerValue--3_iFF')
print( "AQI  ->  " + tem2.text)


# Get information about primary pollutant
prim_polt = soup2.find('span', class_="AirQualityText--severity--1smy9 AirQuality--pollutantName--3SjhF")
prim = soup2.find('span' ,class_='AirQualityText--measurement--3LY0r AirQuality--pollutantMeasurement--2s1IZ')
print("Primary pollutant   " + prim_polt.text + "   " + prim.text)

polts = soup2.find('div', class_='AirQualityText--AirQuality--2uuF7')
print(polts.div.span.text)


# Get information about composition of Air
pol = soup2.find('div', class_='AirQuality--allPollutantDials--2h_JC')
pol2 = pol.find('span', 'AirQualityText--severity--1smy9 AirQuality--pollutantName--3SjhF')
num = pol.find('div', 'AirQuality--col--3I-4C')

list_pol2 = []
list_num = []
for pol2 in pol:
    list_pol2.append(pol2.span.text)

for num in pol:
    list_num.append(num.svg.text)

print("--"*30)
print("Composition of Air ")
print("--"*30)

for a, b in zip(list_pol2, list_num):
    print(a + "  :  " + b)

nums =[]
for i in range(0, len(list_num)):
    nums.append(int(list_num[i]))

vals = nums

# plot a pie chart on composition :
plt.pie(vals, labels= list_pol2)
plt.show()

# ------------------------------------------------------------------------------------------------------------------ #
# The weather channel website
#eg:https://weather.com/en-IN/weather/today/l/3521f274b0b6ed47a6b8c40f90a3f3699fa4cadc3669d9950e303310c7c2314a
# The above link is dehradun's information
