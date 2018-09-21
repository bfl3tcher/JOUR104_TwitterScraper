## Twython -J140 Tweet Downloader

'''
RECORD OF PULLS made (START, hard-stop END date)
    09/01 - 09/03
    09/04 - 09/07
    09/08 - 09/11
    09/11 - 09/12
    09/12 - 09/13
    09/13 - 09/15
    09/15 - 09/18
    09/18 - 09/19
'''

# start date
pull_start = '2018-09-18'
# end date
pull_end = '2018-09-19'

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
Main code below
'''

import Twitter_Credentials
from twython import Twython
import json as js
import pandas as pd



tweets = Twython(
Twitter_Credentials.CONSUMER_KEY,
Twitter_Credentials.CONSUMER_SECRET)

# Search tweets
dict_ = {
    'user': [],
    'date': [],
    'text': [],
    'favorite_count': [],
    'hashtags': []
}


for status in tweets.search(**query)['statuses']:
    dict_['user'].append(status['user']['screen_name'])
    dict_['date'].append(status['created_at'])
    dict_['text'].append(status['full_text'])
    dict_['hashtags'].append(status['entities']['hashtags']
    )



# Structure data in a pandas DataFrame for easier manipulation
df_day = pd.DataFrame(
    data=dict_,
    columns=['user', 'date', 'text', 'hashtags'])

df_day['date'] = pd.to_datetime(df_day.date)


df_day.to_csv(export_fn, index=False)
