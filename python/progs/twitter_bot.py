import tweepy
import schedule
import time


#source ./venv/bin/activate
# # # Authenticate to Twitter
CONSUMER_KEY = 'SrKGZCYIbaeqRt7sUpVU3ubkt'
CONSUMER_SECRET = 'IU5SZlcTwyPLIeVyct13Y0AiQpdKShLnzlyj88NzG1XSIh4M73'
ACCESS_TOKEN = '1656320334247731201-0XtqFvDlJWxSKwPxiCZVwqUkN80jmM'
ACCESS_SECRET = '5hMsFK7c7LcxkoWoEIXMte2Xf7SbPsyB0mhKH1HZEjjfp'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

# # Create API object
client = tweepy.Client(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET, access_token=ACCESS_TOKEN, access_token_secret=ACCESS_SECRET)

# # Create a tweet
client.create_tweet(text='this is fine')

# # At exact time
# tweet = client.create_tweet(text='this is fin')

# def run_bot():
#     tweet
#     return

# schedule.every().day.at("18:50").do(run_bot)

# while True:
#     schedule.run_pending()
#     time.sleep(60) # wait one minute







# Create API object
# api = tweepy.API(auth)

# Create a tweet
# api.update_status("Hello Tweepy")




#TEST Authenecation

# api = tweepy.API(auth)

# try:
#     api.verify_credentials()
#     print("Authentication OK")
# except:
#     print("Error during authentication")



# mkdir tweepy-bots
# $ cd tweepy-bots
# $ python3 -m venv venv
# The commands above create the virtual environment inside the project directory.

# Then you can install the Tweepy package. First, you need to activate the newly created virtual environment and then use pip to do the installation:

# $ source ./venv/bin/activate


