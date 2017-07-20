import nltkplay
import time
import tweepy
import face
import vision
import pyspeedtest

auth = tweepy.OAuthHandler('fqZF3eiteUiPH3egDQBjYQ8YU','Dyhgk1vUDrKmSrwjNyGVnBN8ivFkKV16Y0o6wjHig7koUwaPYJ')
auth.set_access_token('878469632088199168-IYVkHjUUzdIMGX8xyap12hGhDEqtm7J','dd3qRDquAfWWzUjUNAYiVXSdNB868QgoaqkFNKHIJzQWP')
api = tweepy.API(auth)
latest_mention_id = "886561780473909250"
while True:
    mentions = api.mentions_timeline(count=1, include_entities=True)
    tweet = mentions[0]
    if tweet.id == latest_mention_id:
        pass
    elif ('media' in tweet.entities):
        for image in tweet.entities['media']:
            try: 
                age = face.getAge(image['media_url'])
                api.update_status('@' + str(tweet.user.screen_name) + ' This person looks like ' + str(age) + 'years old.')
                face.connectionclose()
                latest_mention_id = tweet.id
            except:
                contents = vision.getContents(image['media_url'])
                api.update_status('@' + str(tweet.user.screen_name) + ' ' + contents) 
                vision.connectionclose()
                latest_mention_id = tweet.id
    elif ("speed" in mentions[0].text):
        st = pyspeedtest.SpeedTest()
        api.update_status('@' + str(mentions[0].user.screen_name) + ' My Internet download speed is ' + str(st.download()) + ' bps')
        latest_mention_id = tweet.id 
    else:
        reply = nltkplay.respondtweet(str(tweet.text)[10:]) 
        api.update_status('@' + str(mentions[0].user.screen_name) + ' ' + reply)
        latest_mention_id = tweet.id 
    time.sleep(5)
