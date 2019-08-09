# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load in 

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns

# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory
""" from subprocess import check_output
print(check_output(["ls", "../input"]).decode("utf8")) """

"""
import os
 for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))
 """
# Any results you write to the current directory are saved as output.
"""
I have choosen to analyze Suicide rates for years between 1985-2016 since it is an interesting topic.
Every step i have taken along the way is possible thanks to the https://www.kaggle.com/kanncaa1. 
I would like to thank him in advance for sharing his wisdom with us.
And i would like to thank https://www.kaggle.com/russellyates88 for sharing his beautiful dataset.
"""
data = pd.read_csv('master.csv')

def file_info():
        return data.info()
# HDI(Human Development Index) is calculated with these three factors: 
# 1- Life Expectancy 
# 2- Education 
# 3- Income per capita

# We can see correlation of columns with this code.
# But a map can be more useful, so;

f,ax = plt.subplots(figsize=(15,15))
sns.heatmap(data.corr(), annot=True, linewidths= .6, fmt ='.1f', ax=ax)
plt.show()

data.head(8)
data.columns

# Scatter Plot 
# x = Age, y =suicides/100k pop
data.plot(kind='scatter', x='suicides/100k pop', y='year',alpha = 0.2,color = 'red', grid= True)
plt.xlabel('suicides/100k pop')   # label = name of label
plt.ylabel('year')
plt.title('Suicides/100k population -Year Scatter Plot') # title = title of plot

#I want to see how many suicides happened in Turkey so i will filter out the rows i am not interested in.

turkey_suicides = data[data['country']=="Turkey"]
print(turkey_suicides) # 84 rows × 12 columns

# Now we only see suicides happened in Turkey.
# İ wish to see total suicides happened every year.

total_suicides = turkey_suicides.eval('Total= suicides_no', inplace=False)\
        .groupby('year')['Total'].sum().reset_index()

print(total_suicides)

# Scatter Plot 
# x = Age, y =suicides/100k pop
total_suicides.plot(kind='line', x='year', y='Total',color = 'red', grid= True)
plt.xlabel('Total Suicides')              # label = name of label
plt.ylabel('Year')
plt.title('Total Suicides -Year Scatter Plot')            # title = title of plot



# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\///////////////////////////////////
# From our line plot it can be seen that 2013 goes for the prize.

turkey_suicides_2013 = turkey_suicides[turkey_suicides['year'] == 2013]
print(turkey_suicides_2013)


turkey_sex = turkey_suicides.eval('Total= suicides_no', inplace=False)\
        .groupby('sex')['Total'].sum().reset_index()

print(turkey_sex)

"""
Suicide Rates Overview 1985 to 2016  
Suicide Rates Overview 1985 to 2016
Compares socio-economic info with suicide rates by year and country
Last Updated: 8 months ago (Version 1)
About this Dataset

Content
This compiled dataset pulled from four other datasets linked by time and place, 
and was built to find signals correlated to increased suicide rates among different cohorts globally, 
across the socio-economic spectrum.

References
United Nations Development Program. (2018). 
Human development index (HDI). 
Retrieved from http://hdr.undp.org/en/indicators/137506

World Bank. (2018). 
World development indicators: GDP (current US$) by country:1985 to 2016. 
Retrieved from http://databank.worldbank.org/data/source/world-development-indicators#

[Szamil]. (2017). 
Suicide in the Twenty-First Century [dataset]. 
Retrieved from https://www.kaggle.com/szamil/suicide-in-the-twenty-first-century/notebook

World Health Organization. (2018). 
Suicide prevention. 
Retrieved from http://www.who.int/mental_health/suicide-prevention/en/

Inspiration
Suicide Prevention.
"""



