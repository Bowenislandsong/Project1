import  tweepy

consumer_key = 'mw5qwkQaBjvw99F2pNF9R3Ht8'
consumer_secret = '9ESeJIDYx3BXS15yYEbxtOqakFVxGJdoEWQ2Xg5h4d2eIcTnqy'
access_token = '1038768523366019074-0jW1slz19e304mGsTTMNSqjx0NM2s7'
access_token_secret='hlmCDhNAeNbx8zv1dUXUnamqhB1XI1Svd4xFGqjy83U0j'

auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth)
tweet='Hello world!'
public_tweets=api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)
#api.update_status('Hello World!')