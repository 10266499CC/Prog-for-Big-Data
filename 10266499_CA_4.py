# -*- coding: utf-8 -*-
"""
Created on Fri May 15 14:17:16 2020

@author: User1
"""
# This is a data exploration project based on Craft Beer Data from Kaggle.
# Two CSV files were downloaded from https://www.kaggle.com/nickhould/craft-cans/data?select=breweries.csv

# This data set is a sample of canned beer brewed in the US. 

# Exploratory Data Analysis:  explore the structure of your dataset, the variables and their relationships.

# Step 1: import the relevant libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load and merge the two csv files

beers= pd.read_csv("C:/Users/User1/Desktop/beers.csv", index_col=0, parse_dates=True)

breweries= pd.read_csv("C:/Users/User1/Desktop/breweries.csv", index_col=0, parse_dates=True)

beers_and_breweries = pd.DataFrame.merge(beers, 
                               breweries, 
                               how='inner', 
                               left_on="id", 
                               right_on="brewery_id", 
                               sort=True,
                               suffixes=('_beer', '_brewery'))


# Conduct exploratory data analysis
    # Build a function to identify the category of each column in a dataframe

def get_var_category(series):
    unique_count = series.nunique(dropna=False)
    total_count = len(series)
    if pd.api.types.is_numeric_dtype(series):
        return 'Numerical'
    elif pd.api.types.is_datetime64_dtype(series):
        return 'Date'
    elif unique_count==total_count:
        return 'Text (Unique)'
    else:
        return 'Categorical'

def print_categories(df):
    for column_name in df.columns:
        print(column_name, ": ", get_var_category(df[column_name]))

# print_categories(beers)

print_categories(breweries)

# Basic information on the dataset 

print(beers_and_breweries.info())
print(beers_and_breweries.shape)
print(beers_and_breweries.count())
print(beers_and_breweries.head(5))
print(beers_and_breweries.tail(5))
print(beers_and_breweries.describe())


# Q.1 Which State has the most breweries? 

print(beers_and_breweries.state.value_counts())
print(beers_and_breweries.state.value_counts().mean())
plot1 = beers_and_breweries.state.value_counts().plot(kind='bar', title="Number of Breweries in Each State", \
                             figsize=(8,6), colormap='summer')
plot1.set_xlabel('State')
plot1.set_ylabel('Number of Breweries')
mean_line = plot1.axhline(beers_and_breweries.state.value_counts().mean(), color='r',\
                         label='Average Number of Breweries')
plot1.legend()

# Interpret the result: 
        # Colorado the most breweries in the US.

# Q.2  If you were interested in brewery tours, which is the best city to visit?

print(beers_and_breweries.groupby('city')['name_brewery'].count())
plot2 = beers_and_breweries.groupby('city')['name_brewery'].count().nlargest(15).plot(kind='bar', \
               title='Cities with the Most Breweries', \
               colormap='summer',  )
plot2.set_ylabel('Number of Breweries')
mean_line = plot2.axhline(beers_and_breweries.city.value_counts().mean(), color='r',\
                         label='Average Number of Breweries')
plot2.legend()

# Interpret the result: 
        # Portland (OR) and Boulder (CO) are the best cities to visit if you are interested in visitng craft breweries.

# Q. 3 What is the most brewed beer style in U.S. craft breweries?

print(beers_and_breweries.groupby('style')['name_beer'].count())

plot3 = beers_and_breweries.groupby('style')['name_beer'].count().nlargest(15).plot(kind='bar', \
               title='Most Brewed Beer Styles', \
               colormap='summer')
plot.set_ylabel('Number of Beers')

# Interpret the result: 
        # American IPAs are the most commonly brewed beer at Craft Breweries.

# Q. 4 What is the average Alcohol Per Volume (ABV) metric for the beer in this dataset?

print('Total number of individual beers in the dataset:', beers.shape[0])
print(beers.isnull().sum())
print('Average ABV of all beers:', beers['abv'].mean())
print('The highest ABV beer:', (beers['abv'].max() * 100), '%')
print('The lowest ABV beer:', (beers['abv'].min() * 100), '%')

# Interpret the result: 
        # There are a total of 376 induvidal beers in the dataset. 22 beers had no ABV value.
        # The ABV level of the beer ranges from 0.1% to 12.8%.
        # The average ABV reading is 5.97%. 

# Q. 5 Do breweries tend to produce more light, medium or strong beers?

breweries_by_abv = beers_and_breweries.groupby('abv', as_index=False)[['name_brewery']].count()
breweries_by_abv.columns =['abv', 'count']
print(breweries_by_abv[pd.isnull(breweries_by_abv).any(axis=1)])
breweries_by_abv['categories'] = pd.cut(breweries_by_abv.abv,3, labels=['low_abv(0.00083-0.0433)', 'medium_abv(0.0433-0.0857)','high_abv(0.0857-0.128)'])
abv_category_count = breweries_by_abv.groupby('categories')[['count']].count()
print(abv_category_count.sum())
abv_category_count.plot.barh(title='breweries count producing beer by abv content category', color=(0.2, 0.4, 0.6))
plt.show()

# Interpret the result: 
        # Most breweries brew medium strength beer. 

# Q. 6 Which State brews the strongest beer?

avg_abv_by_state = beers_and_breweries.groupby('state')[['abv']].mean().sort_values(by='abv', ascending=False)
plt.figure(figsize=(8,11))
sns.barplot(y=avg_abv_by_state.index, x=avg_abv_by_state['abv'], orient='horizontal')
plt.title('States Ranked by Average ABV')
plt.ylabel('State')
plt.xlabel('ABV')

# Interpret the result: 
        # Tennessee has the highest average ABV in their beers, while Hawaii has the lowest.




