import json

tweets_ary = None
with open('trump_tweets.json', encoding="utf8") as f:
  tweets_ary = json.load(f)

print("Number of tweets extracted: {}.\n".format(len(tweets_ary)))

filtered_tweets_ary = []

for tweet in tweets_ary:
    lcase_tweet_txt = tweet['text'].lower()
    if(lcase_tweet_txt.find('china') > -1):
        filtered_tweets_ary.append(tweet)
    elif(lcase_tweet_txt.find('covid') > -1):
        filtered_tweets_ary.append(tweet)
    elif(lcase_tweet_txt.find('corona') > -1):
        filtered_tweets_ary.append(tweet)
    elif(lcase_tweet_txt.find('hospital') > -1):
        filtered_tweets_ary.append(tweet)
    elif(lcase_tweet_txt.find('ventilator') > -1):
        filtered_tweets_ary.append(tweet)
    elif(lcase_tweet_txt.find('vaccine') > -1):
        filtered_tweets_ary.append(tweet)
    elif(lcase_tweet_txt.find('reopen') > -1):
        filtered_tweets_ary.append(tweet)
    elif(lcase_tweet_txt.find('fauci') > -1):
        filtered_tweets_ary.append(tweet)
        
with open("tweets_keyword_filtered.json", "w") as outfile:
    json.dump(filtered_tweets_ary, outfile)
