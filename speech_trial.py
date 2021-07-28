import tweepy as tw
import pandas as pd 

consumer_key = "[INSERT CONSUMER KEY]"
consumer_secret = "[INSERT CONSUMER SECRET]"
access_token = "[INSERT ACCESS TOKEN]"
access_token_secret = "[INSERT ACCESS TOKEN SECRET]"

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth) 

tweets = tw.Cursor(api.search, q="#freespeech", lang="en", date="2021-7-5", tweet_mode="extended").items(5)

text = []
likes = []
time = []

for tweet in tweets:
    text.append(tweet.full_text)
    likes.append(tweet.favorite_count)
    time.append(tweet.created_at)

df = pd.DataFrame({"tweets": text, "likes": likes, "time": time}) 

df.to_excel("speech_test.xlsx")
print("success")

#I am making a comment!