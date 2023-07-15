import pandas as pd
import numpy as np

global df , df1
df = pd.read_csv('metacritic_2021.csv')
PC_games = df[df['platform'].str.contains('PC', na=False)]
PC_games["user_review"] = pd.to_numeric(PC_games["user_review"], errors='coerce')
PC_games['name'] = PC_games.name.astype(str)
PC_games['year'] = pd.DatetimeIndex(PC_games['release_date']).year
PC_games['meta_score'] = PC_games['meta_score'].div(10).round(1)

PS_games = df[df['platform'].str.contains('PlayStation', na=False)]
PS_games = PS_games.drop(df[df['platform'] == ' PlayStation Vita'].index)
PS_games["user_review"] = pd.to_numeric(PS_games["user_review"], errors='coerce')
PS_games['name'] = PS_games.name.astype(str)
PS_games['year'] = pd.DatetimeIndex(PS_games['release_date']).year
PS_games.user_review = PS_games.user_review*10

XB_games = df[df['platform'].str.contains('Xbox', na=False)]
XB_games["user_review"] = pd.to_numeric(XB_games["user_review"], errors='coerce')
XB_games['name'] = XB_games.name.astype(str)
XB_games['year'] = pd.DatetimeIndex(XB_games['release_date']).year
XB_games.user_review = XB_games.user_review*10

PSvXB = df[df['platform'].isin([  'PlayStation 3' , ' PlayStation 4' , ' PlayStation 5' , 'Xbox 360' , ' Xbox One' , ' Xbox Series X'])]
PSvXB["user_review"] = pd.to_numeric(PSvXB["user_review"], errors='coerce')
PSvXB['name'] = PSvXB.name.astype(str)
PSvXB['year'] = pd.DatetimeIndex(PSvXB['release_date']).year
PSvXB.user_review = PSvXB.user_review*10

GOTY = df.drop_duplicates(subset=['name'])
GOTY['year'] = pd.DatetimeIndex(GOTY['release_date']).year
GOTY = GOTY.drop(columns = ['user_review' , 'release_date' , 'platform'])

def game_of_the_year(df):
    max_scores_idx = df.groupby('year')['meta_score'].idxmax()
    game_of_the_year_df = df.loc[max_scores_idx, ['name', 'year']]
    return game_of_the_year_df

def year_of_GOTY(df):
    max_scores_idx = df.groupby('year')['meta_score'].idxmax()
    game_of_the_year_df = df.loc[max_scores_idx, ['name', 'year']]
    new_df = game_of_the_year_df.copy()
    GOTyear=new_df['year'].tolist()
    return GOTyear

def get_game_name_by_year(year, df):
    game_name = df.loc[df['year'] == year, 'name'].iloc[0]
    return game_name

def no_repeat(df):
    df['name'].duplicated().sum()
    norepeat = df.drop_duplicates(subset=['name'])
    return norepeat

def preprocess2(df):
    df.drop(columns = ['summary'] , inplace=True)
    df["user_review"] = pd.to_numeric(df["user_review"], errors='coerce')  #coerce will ignore the error and convert the value to NaN
    df['platform'] = df.platform.astype('category')
    df['name'] = df.name.astype(str)
    df['year'] = pd.DatetimeIndex(df['release_date']).year
    df['meta_score'] = df['meta_score'].div(10).round(1)
    df1=df.dropna(subset=['user_review'])
    return df

def get_PC(df1):
    PC_games = df1[df1['platform'].str.contains('PC', na=False)]
    return PC_games

def get_PC_summary(df1):
    PC_games = df1[df1['platform'].str.contains('PC', na=False)]
    PC_data = {'min' : [np.min(PC_games['meta_score']), np.min(PC_games['user_review'])],
            'max' : [np.max(PC_games['meta_score']), np.max(PC_games['user_review'])],
            'mean' : [np.mean(PC_games['meta_score']), np.mean(PC_games['user_review'])],
            'median' : [np.median(PC_games['meta_score']), np.median(PC_games['user_review'])],
            'std' : [np.std(PC_games['meta_score']), np.std(PC_games['user_review'])],}
    PC_game_summary = pd.DataFrame(PC_data, index=['Meta Score', 'User Review'])
    return PC_game_summary

def PC_meta_score(df1):
    PC_games_by_year = PC_games.groupby('year')
    PC_critic_by_year = PC_games_by_year['meta_score']
    PC_critic_mean_year = PC_critic_by_year.mean().round(decimals = 2)
    return PC_critic_mean_year

def PC_user_review(df1):
    PC_games_by_year = PC_games.groupby('year')
    PC_user_by_year = PC_games_by_year['user_review']
    PC_user_mean_year = PC_user_by_year.mean().round(decimals = 2)
    return PC_user_mean_year

def get_ps(df1):
    PS_games = df1[df1['platform'].str.contains('PlayStation', na=False)]
    PS_games = PS_games.drop(df1[df1['platform'] == ' PlayStation Vita'].index)
    return PS_games

def PS_summary(df1):
    PS_games = df1[df1['platform'].str.contains('PlayStation', na=False)]
    PS_games = PS_games.drop(df1[df1['platform'] == ' PlayStation Vita'].index)
    PS_data = {'min' : [np.min(PS_games.meta_score) , np.min(PS_games.user_review)],
        'max' : [np.max(PS_games.meta_score) , np.max(PS_games.user_review)],
        'mean' : [np.mean(PS_games.meta_score) , np.mean(PS_games.user_review)],
        'std' : [np.std(PS_games.meta_score) , np.std(PS_games.user_review)],
        'median' : [np.median(PS_games.meta_score) , np.median(PS_games.user_review)],}
    PS_summary = pd.DataFrame(PS_data , index=['Meta Score' , 'User Review'])
    return PS_summary

def PS_by_year(PS_games):
    PS_by_year = PS_games.groupby('year')[['meta_score','user_review']].mean().reset_index()
    return PS_by_year

def PS_by_gen(PS_games):
    PS_by_Gen = PS_games.groupby('platform')[['meta_score','user_review']].mean().reset_index()
    PS_by_Gen = PS_by_Gen.dropna()
    return PS_by_Gen

def PS_top_meta(PS_games):
    toppsm=PS_games[['name', 'platform', 'meta_score' , 'year']].sort_values('meta_score', ascending = False)[:10]
    return toppsm
def PS_top_user(PS_games):
    toppsu=PS_games[['name', 'platform', 'user_review' , 'year']].sort_values('user_review', ascending = False)[:10]
    return toppsu

def get_XB(df1):
    XB_games = df1[df1['platform'].str.contains('Xbox', na=False)]
    return XB_games

def XB_summary(df1):
    XB_games = df1[df1['platform'].str.contains('Xbox', na=False)]
    XB_data = {'min' : [np.min(XB_games['meta_score']), np.min(XB_games['user_review'])],
            'max' : [np.max(XB_games['meta_score']), np.max(XB_games['user_review'])],
            'mean' : [np.mean(XB_games['meta_score']), np.mean(XB_games['user_review'])],
            'std' : [np.std(XB_games['meta_score']), np.std(XB_games['user_review'])],
            'median' : [np.median(XB_games['meta_score']), np.median(XB_games['user_review'])],}
    XB_summary = pd.DataFrame(XB_data , index=['Meta Score' , 'User Review'])
    return XB_summary

def XB_by_year(XB_games):
    XB_by_year = XB_games.groupby('year')[['meta_score','user_review']].mean().reset_index()
    return XB_by_year

def XB_by_gen(XB_games):
    XB_by_Gen = XB_games.groupby('platform')[['meta_score','user_review']].mean().reset_index()
    XB_by_Gen = XB_by_Gen.dropna()
    return XB_by_Gen

def XB_top_meta(XB_games):
    topxbm=XB_games[['name', 'platform', 'meta_score' , 'year']].sort_values('meta_score', ascending = False)[:10]
    return topxbm
def XB_top_user(XB_games):
    topxbu=XB_games[['name', 'platform', 'user_review' , 'year']].sort_values('user_review', ascending = False)[:10]
    return topxbu


def get_PSvXB(df1):
    PSvXB = df1[df1['platform'].isin([  'PlayStation 3' , ' PlayStation 4' , ' PlayStation 5' , 'Xbox 360' , ' Xbox One' , ' Xbox Series X'])]
    return PSvXB

def PSvXB_count(PSvXB):
    PSvXB_count = PSvXB.groupby('platform').count()
    PSvXB_count.drop(PSvXB_count.index[0:11] , inplace=True)
    PSvXB_count.drop(PSvXB_count.index[2:9] , inplace=True)
    PSvXB_count.drop(['meta_score' , 'user_review' ,'release_date','year',] , axis=1 , inplace=True)
    PSvXB_count.rename(columns={'name':'Count'} , inplace=True)
    return PSvXB_count


def PSvXB_meta(PSvXB):
    PSvXB_meta = PSvXB[['name', 'platform', 'meta_score']].sort_values('meta_score', ascending = False)[:20]
    return PSvXB_meta

def PSvXB_user(PSvXB):
    PSvXB_user = PSvXB[['name', 'platform', 'user_review']].sort_values('user_review', ascending = False)[:20]
    return PSvXB_user

def count(PSvXB):
    PSvXB_count = PSvXB.groupby('platform').count()
    PSvXB_count.drop(['meta_score' , 'user_review' ,'release_date','year',] , axis=1 , inplace=True)
    PSvXB_count.rename(columns={'name':'Count'} , inplace=True)
    return PSvXB_count