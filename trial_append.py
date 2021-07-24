import tweepy as tw
import openpyxl as px
import schedule
import time

consumer_key = "[INSERT CONSUMER KEY]"
consumer_secret = "[INSERT CONSUMER SECRET]"
access_token = "[INSERT ACCESS TOKEN]"
access_token_secret = "[INSERT ACCESS TOKEN SECRET]"

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth)
 
def append():
    tweets = tw.Cursor(api.search, q="#freespeech", lang="en", date="2021-7-5", tweet_mode="extended").items(5)

    text = []
    likes = []
    time = []

    for tweet in tweets:
        text.append(tweet.full_text)
        likes.append(tweet.favorite_count)
        time.append(tweet.created_at)

    wb = px.load_workbook("speech_test.xlsx")
    ws = wb.active

    rows = []

    for i in range(5):
        rows.append([" ", text[i], likes[i], time[i]])

    for row in rows:
        ws.append(row)

    wb.save("speech_test.xlsx")
    wb.close()

schedule.every(1).minutes.do(append)

while True:
    schedule.run_pending()
    time.sleep(1)