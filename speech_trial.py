import tweepy as tw
import pandas as pd
import openpyxl

consumer_key = [INSERT CONSUMER KEY]
consumer_secret = [INSERT CONSUMER SECRET]
access_token = [INSERT ACCESS TOKEN]
access_token_secret = [INSERT ACCESS TOKEN SECRET]

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth)

search_words = "#freespeech"
date_since = "2021-7-5"

tweets = tw.Cursor(api.search, q=search_words, lang="en", date=date_since, tweet_mode="extended").items(5)

text = []
likes = []
time = []

for tweet in tweets:
    text.append(tweet.full_text)
    likes.append(tweet.favorite_count)
    time.append(tweet.created_at)

df = pd.DataFrame({'tweets': text, 'likes': likes, 'time': time})

file_name = 'speech_test.xlsx'

df.to_excel(file_name)
print("success")