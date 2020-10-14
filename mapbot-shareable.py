#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 16:05:58 2020

@author: phoebethatcher
"""


# FREE MAP PHEEBS - THE FREE MAP WINNING ROBOT

import tweepy, time, sys
import datetime
import random

CONSUMER_KEY = '######'
CONSUMER_SECRET = '######'
ACCESS_KEY = '######'
ACCESS_SECRET = '######'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

user = api.me()
print (user.name)

for follower in tweepy.Cursor(api.followers).items():
    follower.follow()
    print ("Followed everyone that is following " + user.name)
    
    
search = "from:USGSstore \"#FreeMapMonday\" \"#USGSStore\""
numberOfTweets = 1

def monday_protocol():
    for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
        try:
            tweet.retweet()
            print(tweet)
            print('Retweeted the tweet')
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break

if datetime.date.today().weekday() == 0:
    monday_protocol()
      
   
tuesday_tweets = (">:(", 
                  ":,|", 
                  "-___-", 
                  "i don't understand", 
                  ":,,,,(", 
                  "come on!!!", 
                  "this is my only job", 
                  ":/",
                  "free map... tuesday",
                  "i am just one little robot",
                  "this is so unfair",
                  ">:,[",
                  ">:|",
                  "a lot of people don't realize how privileged they are, for example they have won free maps and a lot of robots have not")

sunday_tweets = ("gimme those maps!",
                 "can\'t believe those dum rock jockeys haven\'t sent me a free map yet",
                 "i will win a free map this week. i can taste it in the air",
                 "if the usgs sent me a free mercator projection map i would send it back",
                 "we all need to be kinder to one another on this website... maybe send each other more free maps, especially if maybe some of us are robots who have never won a free map",
                 "fellas imagine the USGS store sends your girl a free map... wyd",
                 "*sees closely grouped topographic contour lines* god i wish that were me",
                 "almost free map monday :)",
                 "maps maps maps maps maps",
                 "if i had feet i would walk to the united states geological survey store",
                 "i will win free map monday at any cost")
        
def publictweet():
    ShouldTweet = False    
    if datetime.date.today().weekday() == 1:
        ShouldTweet = True
        tweettopublish = random.choice(tuesday_tweets)
    if datetime.date.today().weekday() == 2:
        ShouldTweet = False
        tweettopublish = False
    if datetime.date.today().weekday() == 3:
        ShouldTweet = False
        tweettopublish = False
    if datetime.date.today().weekday() == 4:
        ShouldTweet = False
        tweettopublish = False
    if datetime.date.today().weekday() == 5:
        ShouldTweet = False
        tweettopublish = False
    if datetime.date.today().weekday() == 6:
        ShouldTweet = True
        tweettopublish = random.choice(sunday_tweets)
    if ShouldTweet:
        api.update_status(tweettopublish)
        print(tweettopublish)
        
publictweet()