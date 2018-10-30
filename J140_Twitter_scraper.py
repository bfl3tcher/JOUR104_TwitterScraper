## Twython -J140 Tweet Downloader

'''
Enter search criteria below
Lowly API account means 100 results max per pull
'''

# path
path = '/Users/bfletcher/Desktop/8-Academia-Projects/BF_TwitterDatabase/Saved_Tweets'

# start date
pull_start = '2018-10-25'
# end date
pull_end = '2018-10-29'

export_fn = 'J104Tweets'+pull_start+'.csv'

# Create our query
query = {
    'q': ['#CSULB104'],
    'count':100,
    'lang': 'en',
    'result_type':'mixed',
    'tweet_mode':'extended',
    'since':pull_start,
    'until':pull_end
}




'''
Extract Tweets
'''


# import libraries
import Twitter_Credentials
from twython import Twython
import json as js
import pandas as pd
import numpy as np


# import Twitter credentials
tweets = Twython(
Twitter_Credentials.CONSUMER_KEY,
Twitter_Credentials.CONSUMER_SECRET)


# Search tweets
dict_ = {
    'user': [],
    'date': [],
    'text': [],
    'favorite_count': [],
    'Hashtags': []
}


#  Tweet query - data structure
for status in tweets.search(**query)['statuses']:
    dict_['user'].append(status['user']['screen_name'])
    dict_['date'].append(status['created_at'])
    dict_['text'].append(status['full_text'])
    dict_['Hashtags'].append(status['entities']['hashtags']
    )


# Structure data in a pandas DataFrame for easier manipulation
df_day = pd.DataFrame(
    data=dict_,
    columns=['user', 'date', 'text', 'Hashtags'])


# converting to date time
df_day['date'] = pd.to_datetime(df_day.date)


# export
df_day.to_csv(export_fn, index=False)



'''
Process Tweets Extracted
'''


# import file
df = pd.read_csv(export_fn)

# isolate tweet strings
regex = "(\[\d+\, \d+)|text|indices|\'|\]|\[|\:|}|text|\,|{"
df['Hashtags'] = df.Hashtags.str.replace(regex, '').str.replace('    ', ', ')
df['date'] = pd.to_datetime(df.date, infer_datetime_format=True)


'''Creating date - columns'''
df['date'] = pd.to_datetime(df.date, infer_datetime_format=True)
df['r_date'] = df.date.dt.date
df['weekday'] = df.date.dt.weekday_name
df['hour'] = df.date.dt.hour


'''Coding week of class'''
# week - date
df.loc[((df['date'] > '2018-8-28') & (df['date'] < '2018-9-4')), 'week'] = 'Week 1'
df.loc[((df['date'] > '2018-9-4') & (df['date'] < '2018-9-11')), 'week'] = 'Week 2'
df.loc[((df['date'] > '2018-9-11') & (df['date'] < '2018-9-18')),'week'] = 'Week 3'
df.loc[((df['date'] > '2018-9-18') & (df['date'] < '2018-9-25')), 'week'] = 'Week 4'
df.loc[((df['date'] > '2018-9-25') & (df['date'] < '2018-10-2')), 'week'] = 'Week 5'
df.loc[((df['date'] > '2018-10-2') & (df['date'] < '2018-10-9')), 'week'] = 'Week 6'
df.loc[((df['date'] > '2018-10-9') & (df['date'] < '2018-10-16')),'week'] = 'Week 7'
df.loc[((df['date'] > '2018-10-16') & (df['date'] < '2018-10-23')), 'week'] = 'Week 8'
df.loc[((df['date'] > '2018-10-23') & (df['date'] < '2018-10-30')), 'week'] = 'Week 9'
df.loc[((df['date'] > '2018-10-30') & (df['date'] < '2018-11-6')), 'week'] = 'Week 10'
df.loc[((df['date'] > '2018-11-6') & (df['date'] < '2018-11-13')), 'week'] = 'Week 11'
df.loc[((df['date'] > '2018-11-13') & (df['date'] < '2018-11-20')), 'week'] = 'Week 12'
df.loc[((df['date'] > '2018-11-20') & (df['date'] < '2018-11-27')), 'week'] = 'Week 13'
df.loc[((df['date'] > '2018-11-27') & (df['date'] < '2018-12-4')), 'week'] = 'Week 14'
df.loc[((df['date'] > '2018-12-4') & (df['date'] < '2018-12-13')), 'week'] = 'Week 15'
df.loc[((df['date'] > '2018-12-13') & (df['date'] < '2018-12-20')), 'week'] = 'Week 16'

# week - subject
subject_val = {'Week 1':'Introduction-SocialMedia+Journalism','Week 2':'Social Media Best Practices/Electronic Communication Theories/Social Media Ethics','Week 3':'SEO/Analytics and Hashtags','Week 4':'Light Side/DarkSide','Week 5':'Fake News/Business Advertising','Week 6':'Prepare Case Studies','Week 7':'GuestLecture/Case Study Homework','Week 8':'Case Study Presentation/Rise of Influencers','Week 9':'Nonprofits/Social Movements','Week 10':'Social Media and Politics','Week 11':'Multimedia Storytelling','Week 12':'Personal Privacy on Social Media','Week 13':'Thanksgiving Break','Week 14':'Careers in Social Media','Week 15':'Social Media Campaign Presentatation','Week 16':'Final Exam'}
df['subject'] = df.week
df.subject.replace(subject_val, inplace=True)


'''Vader Sentiment Analyzer'''
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()

data_OE = df.loc[:, ['user', 'text']]
data_OE.fillna('0', inplace=True)

columns = []
for i in data_OE.columns:
    if i != 'user':
        columns.append(i+'_cmp')
        columns.append('pos_%s'%i)
        columns.append('neg_%s'%i)
        columns.append('neu_%s'%i)

i = 0
df_dict = {}
for i in np.arange(len(columns)):
    for j in columns:
        df_dict[j]=[]

df_empty = pd.DataFrame(df_dict)
df_empty = df_empty[columns]

compound_list = []
positive_list = []
negative_list = []
neutral_list = []


i = 0;
for i in range(0,len(list(data_OE))-1):
    for text in data_OE.iloc[:,i+1]:

        # Run Vader Analysis on each tweet
        compound = analyzer.polarity_scores(text)["compound"]
        pos = analyzer.polarity_scores(text)["pos"]
        neu = analyzer.polarity_scores(text)["neu"]
        neg = analyzer.polarity_scores(text)["neg"]

        # Add each value to the appropriate array
        compound_list.append(compound)
        positive_list.append(pos)
        negative_list.append(neg)
        neutral_list.append(neu)

    # print(compound_list)
    j = (i*4);
    k = (i*4)+1;
    l = (i*4)+2;
    m = (i*4)+3;
    df_empty.iloc[:,j] = compound_list
    df_empty.iloc[:,k] = positive_list
    df_empty.iloc[:,l] = negative_list
    df_empty.iloc[:,m] = neutral_list
    compound_list = []
    positive_list = []
    negative_list = []
    neutral_list = []

# merges sentiment results into dataframe
df = pd.merge(df,df_empty, left_index=True, right_index=True)


# save processed file
df.to_csv(export_fn, index=False)
