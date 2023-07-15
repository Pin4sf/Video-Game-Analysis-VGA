import pandas as pd
import numpy as np

global df , df1
df = pd.read_csv('metacritic_2021.csv')

def preprocess(df):
    df.drop(columns = ['summary'] , inplace=True)
    df["user_review"] = pd.to_numeric(df["user_review"], errors='coerce')  #coerce will ignore the error and convert the value to NaN
    df['platform'] = df.platform.astype('category')
    df['name'] = df.name.astype(str)
    df['year'] = pd.DatetimeIndex(df['release_date']).year
    df['meta_score'] = df['meta_score'].div(10).round(1)
    df1=df.dropna(subset=['user_review'])
    return df

def get_platforms(df1):
    count_platform = df1["platform"].value_counts().reset_index()
    count_platform.columns = ["Platform", "Count",]
    return count_platform

def top_games_meta(df1):
    top_meta_score = df1.sort_values(by='meta_score', ascending=False).drop_duplicates('name').head(25)
    top_meta_score
    return top_meta_score

def top_games_user(df1):
    top_user_score = df1.sort_values(by='user_review', ascending=False).drop_duplicates('name').head(25)
    top_user_score
    return top_user_score

def grouped_critic(df1):
    grouped = df1.groupby('platform')
    critic_grouped = grouped['meta_score']
    critic_mean = critic_grouped.mean().round(decimals = 2).sort_values(ascending = False)
    return critic_mean

def grouped_user(df1):
    grouped = df1.groupby('platform')
    user_grouped = grouped['user_review']
    user_mean = user_grouped.mean().round(decimals = 2).sort_values(ascending = False)
    return user_mean

def grouped_year_critic(df1):
    grouped_year = df1.groupby('year')
    critic_groupedYear = grouped_year['meta_score']
    critic_meanYear = critic_groupedYear.mean().round(decimals = 2)
    return critic_meanYear

def grouped_year_user(df1):
    grouped_year = df1.groupby('year')
    user_groupedYear = grouped_year['user_review']
    user_meanYear = user_groupedYear.mean().round(decimals = 2)
    return user_meanYear

def GName(df):
    norepeat = df.drop_duplicates(subset=['name'])
    get_summary = norepeat.drop(columns = [ 'user_review' , 'release_date' , 'platform'])
    get_summary = get_summary.sort_values(by='meta_score', ascending=False).head(200)
    get_summary = get_summary.reset_index(drop=True)
    name = get_summary['name'].tolist()
    name.insert(0, 'Select')
    return name


def get_game_summary(game_name, df):
    norepeat = df.drop_duplicates(subset=['name'])
    get_summary = norepeat.drop(columns = [ 'user_review' , 'release_date' , 'platform'])
    get_summary = get_summary.sort_values(by='meta_score', ascending=False).head(200)
    game_row = get_summary[get_summary['name'] == game_name]
    if not game_row.empty:
        return game_row['summary'].iloc[0]
    else:
        return "Select A game to get summary."
