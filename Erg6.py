import tweepy
import re
import twitter_credentials

auth = tweepy.OAuthHandler(twitter_credentials.consumer_key, twitter_credentials.consumer_secret)
auth.set_access_token(twitter_credentials.access_token, twitter_credentials.access_token_secret)

api = tweepy.API(auth)
ChosenUser = input("Enter a twitter profile: ")
TheTweets = ""
for status in tweepy.Cursor(api.user_timeline, id=ChosenUser, tweet_mode="extended").items(10):
    try:
        tweet = status.retweeted_status.full_text

    except AttributeError:
        tweet = status.full_text
    #removing urls from the string and characters that make
    #words read as longer even though they aren't
    tweet =re.sub(r'http\S+', '', tweet)
    tweet = tweet.replace(",", "").replace(".", "").replace("?", "").replace(";", "").replace("@", "").replace("!", "")
    tweet = tweet.replace("#", "").replace(">", "").replace("<", "").replace(":", "").replace("(","").replace(")","")
    tweet = tweet.replace("1","").replace("2","").replace("3","").replace("4","").replace("5","").replace("6","")
    tweet = tweet.replace("7","").replace("8","").replace("9","").replace("0","").replace("#","").replace("$","")
    tweet = tweet.replace("%","").replace("^","").replace("&","").replace("*","").replace("-"," ").replace("=","")
    tweet = tweet.replace("+","").replace("_"," ").replace("\\","").replace("|","").replace("[","").replace("]","")
    tweet = tweet.replace("{","").replace("}","").replace("/","").replace("`","").replace("~","")
    tweet = tweet
    tweet = tweet
    tweet = tweet
    TheTweets += tweet + " "
TheTweetList =TheTweets.split()
BiggestWords = []
SmallestWords =[]
TheTweetList2 = TheTweetList #Declaring 2 equal variables incase
#there is a tweet that belongs to the BiggestWords and SmallestWords
for i in range(5):
    CurrentBiggestWord = (max(TheTweetList, key=len))
    BiggestWords.append(CurrentBiggestWord)
    print(CurrentBiggestWord)
    for i in TheTweetList:
        if (i == CurrentBiggestWord):
            TheTweetList.remove(i)
for i in range(5):
    CurrentSmallestWord = (min(TheTweetList2, key=len))
    SmallestWords.append(CurrentSmallestWord)
    print(CurrentSmallestWord)
    for i in TheTweetList2:
        if (i == CurrentSmallestWord):
            TheTweetList2.remove(i)
