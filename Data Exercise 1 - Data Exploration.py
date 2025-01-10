#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Import pandas library
import pandas as pd


# In[2]:


#I am reading csv for a dataset I downloaded from Kaggle
#I am going to filter down this data to a specific league for a specific year to demonstrate how to use booleans to filter data in Pandas.
#.head() simply restricts the shown results to the first five rows
pd.read_csv("season_stats_teams_clean.csv").head()


# In[3]:


#I am assigning a name to this dataframe to make it easier to use
season_team_stat_df = pd.read_csv("season_stats_teams_clean.csv")


# In[4]:


season_team_stat_df.head()


# In[5]:


#I can see there are 58 columns, but I want to know how many rows there are. I'll use .shape to see.
season_team_stat_df.shape


# In[6]:


#I want to see what column labels we have so that I can eliminate columns that don't interest me.
season_team_stat_df.columns.tolist()


# In[7]:


#I'll use .value_counts() just to get some more general information about my dataset.
season_team_stat_df.league_name.value_counts()


# In[8]:


season_team_stat_df.league_season.value_counts()


# In[9]:


#I personally enjoy watching La Liga more than other leagues, so I want to filter the data to only show rows matching that league name.
la_liga_df = season_team_stat_df[ season_team_stat_df["league_name"] == "La Liga"]
print(la_liga_df.shape)
la_liga_df.head()


# In[10]:


#I've decided to pull La Liga team statistics from last year in particular, so I am going to add another condition to my filter.
filter_criteria = (season_team_stat_df["league_name"] == "La Liga") & (season_team_stat_df["league_season"] == 2024)
liga_2024_df = season_team_stat_df[ filter_criteria ]
print(liga_2024_df.shape)
liga_2024_df.head()


# In[11]:


#The team stat that interests me most is points scored and points allowed, so I am going to print only those columns.
print(liga_2024_df[['team_name', 'goals_for_total', 'goals_against_total']])


# In[12]:


#I am going to reassign these three columns as their own table so that it is easier to sort.
final_df = liga_2024_df[['team_name', 'goals_for_total', 'goals_against_total']]
print(final_df)


# In[13]:


#I am sorting values here based on which team scored the most goals with the output in descending order.
final_df.sort_values('goals_for_total', ascending=False)


# In[14]:


#Lastly for this exploration, I want to sort by goals allowed in ascending order since the best defense will allow the fewest points.
final_df.sort_values('goals_against_total')


# In[ ]:




