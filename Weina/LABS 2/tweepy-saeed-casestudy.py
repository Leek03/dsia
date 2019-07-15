#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 13:17:27 2019

@author: weinazhu1
"""

{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Streaming Tweets from Twitter to Database\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Streaming tweets from the Twitter API v1.1\n",
    "\n",
    "First let's cover streaming tweets from Twitter. You're going to need a Twitter dev account. Sometimes Twitter uses dev.twitter.com to advertise various things they expect devs to be interested in. The problem is they sometimes make it hard to get to where you want to be. Just in case they've done this and the video's method isn't available, here's the link: Twitter Apps\n",
    "https://apps.twitter.com/\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Next, make a new application, filling in your name, description, website, agree to their terms, do the captcha, and create the application."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Once submitted successfully, you should be presented with a page where you can see your consumer key and consumer secret. Now you need an access token, so scroll down and click on \"create my access token.\"\n",
    "\n",
    "After a few moments, refresh, and you should be able to see the access key and access token. Once you have that, you're going to need to get Tweepy, which is a Python module for streaming Twitter tweets.\n",
    "\n",
    "It is probably easiest to download and install Tweepy via pip if you're using a current version of Python.\n",
    "\n",
    "pip install tweepy"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "You can also install using the setup.py method that I used in the video.\n",
    "\n",
    "Once you have Tweepy, let's show a very basic example of its use:"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "First, We should import the package for streaming tweets from Twitter."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "from tweepy import Stream\n",
    "from tweepy import OAuthHandler\n",
    "from tweepy.streaming import StreamListener"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Then, We need to insert access info.\n",
    "#consumer key, consumer secret, access token, access secret."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "ckey=\"NXjcTeC2lNWx3VzKGiVqpBWA9\"\n",
    "csecret=\"RVBGUGiNZLdIIQKEUyDCyE3HgmqHmJMJPCoXLllqyL694XNs6B\"\n",
    "atoken=\"3047153088-1bFN3Nn6kquZyIw3f65QeEqc5xbHqYmjaKanltx\"\n",
    "asecret=\"k9q41NrKODusuupKAOOGM8Y0JUvoXu1kngnmh4GePIxZv\"\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We need to define a class to listen to the tweets in Twitter"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "class listener(StreamListener):\n",
    "\n",
    "    def on_data(self, data):\n",
    "        print(data)\n",
    "        # read the data by json\n",
    "        all_data = json.loads(data)\n",
    "        tweet = all_data[\"text\"]\n",
    "        username = all_data[\"user\"][\"screen_name\"]\n",
    "\n",
    "\n",
    "        \n",
    "        return(True)\n",
    "\n",
    "    def on_error(self, status):\n",
    "        \n",
    "        print (status)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now, we can call the authenticator API for validating the access to Twitter."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "auth = OAuthHandler(ckey, csecret)\n",
    "auth.set_access_token(atoken, asecret)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Finally, We can Listen to tweets :)\n",
    "\n",
    "We just want to listen the tweets about the F1 racing.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{\"created_at\":\"Wed Jul 10 10:45:12 +0000 2019\",\"id\":1148906009609609216,\"id_str\":\"1148906009609609216\",\"text\":\"RT @SoyMotor: Ocho ni\\u00f1os, seleccionados para estar en la parrilla del #BritishGP junto a sus \\u00eddolos - https:\\/\\/t.co\\/vlRTtpjjji #F1 https:\\/\\/t\\u2026\",\"source\":\"\\u003ca href=\\\"http:\\/\\/twitter.com\\/download\\/android\\\" rel=\\\"nofollow\\\"\\u003eTwitter for Android\\u003c\\/a\\u003e\",\"truncated\":false,\"in_reply_to_status_id\":null,\"in_reply_to_status_id_str\":null,\"in_reply_to_user_id\":null,\"in_reply_to_user_id_str\":null,\"in_reply_to_screen_name\":null,\"user\":{\"id\":780480121463529473,\"id_str\":\"780480121463529473\",\"name\":\"Alegria Lucas\",\"screen_name\":\"alelufi68\",\"location\":\"Ciudadana del mundo\",\"url\":null,\"description\":null,\"translator_type\":\"none\",\"protected\":false,\"verified\":false,\"followers_count\":7,\"friends_count\":15,\"listed_count\":0,\"favourites_count\":6900,\"statuses_count\":282,\"created_at\":\"Mon Sep 26 18:52:16 +0000 2016\",\"utc_offset\":null,\"time_zone\":null,\"geo_enabled\":false,\"lang\":null,\"contributors_enabled\":false,\"is_translator\":false,\"profile_background_color\":\"F5F8FA\",\"profile_background_image_url\":\"\",\"profile_background_image_url_https\":\"\",\"profile_background_tile\":false,\"profile_link_color\":\"1DA1F2\",\"profile_sidebar_border_color\":\"C0DEED\",\"profile_sidebar_fill_color\":\"DDEEF6\",\"profile_text_color\":\"333333\",\"profile_use_background_image\":true,\"profile_image_url\":\"http:\\/\\/pbs.twimg.com\\/profile_images\\/783779297903386624\\/QdweJ9Ca_normal.jpg\",\"profile_image_url_https\":\"https:\\/\\/pbs.twimg.com\\/profile_images\\/783779297903386624\\/QdweJ9Ca_normal.jpg\",\"profile_banner_url\":\"https:\\/\\/pbs.twimg.com\\/profile_banners\\/780480121463529473\\/1475702578\",\"default_profile\":true,\"default_profile_image\":false,\"following\":null,\"follow_request_sent\":null,\"notifications\":null},\"geo\":null,\"coordinates\":null,\"place\":null,\"contributors\":null,\"retweeted_status\":{\"created_at\":\"Tue Jul 09 09:30:04 +0000 2019\",\"id\":1148524713758646274,\"id_str\":\"1148524713758646274\",\"text\":\"Ocho ni\\u00f1os, seleccionados para estar en la parrilla del #BritishGP junto a sus \\u00eddolos - https:\\/\\/t.co\\/vlRTtpjjji #F1 https:\\/\\/t.co\\/WOXKXy4a5W\",\"display_text_range\":[0,115],\"source\":\"\\u003ca href=\\\"http:\\/\\/twitter.com\\\" rel=\\\"nofollow\\\"\\u003eTwitter Web Client\\u003c\\/a\\u003e\",\"truncated\":false,\"in_reply_to_status_id\":null,\"in_reply_to_status_id_str\":null,\"in_reply_to_user_id\":null,\"in_reply_to_user_id_str\":null,\"in_reply_to_screen_name\":null,\"user\":{\"id\":994741592,\"id_str\":\"994741592\",\"name\":\"SoyMotor.com\",\"screen_name\":\"SoyMotor\",\"location\":null,\"url\":\"http:\\/\\/www.SoyMotor.com\",\"description\":\"F\\u00f3rmula 1 y Coches, de la mano de @alobatof1 y @crosaleny. \\u00a1Tambi\\u00e9n en @SoyMotorCoches!\",\"translator_type\":\"none\",\"protected\":false,\"verified\":true,\"followers_count\":59455,\"friends_count\":277,\"listed_count\":986,\"favourites_count\":3486,\"statuses_count\":73138,\"created_at\":\"Fri Dec 07 10:06:50 +0000 2012\",\"utc_offset\":null,\"time_zone\":null,\"geo_enabled\":true,\"lang\":null,\"contributors_enabled\":false,\"is_translator\":false,\"profile_background_color\":\"000000\",\"profile_background_image_url\":\"http:\\/\\/abs.twimg.com\\/images\\/themes\\/theme14\\/bg.gif\",\"profile_background_image_url_https\":\"https:\\/\\/abs.twimg.com\\/images\\/themes\\/theme14\\/bg.gif\",\"profile_background_tile\":false,\"profile_link_color\":\"F80056\",\"profile_sidebar_border_color\":\"FFFFFF\",\"profile_sidebar_fill_color\":\"DDEEF6\",\"profile_text_color\":\"333333\",\"profile_use_background_image\":true,\"profile_image_url\":\"http:\\/\\/pbs.twimg.com\\/profile_images\\/877806258543357952\\/UmYBJTnf_normal.jpg\",\"profile_image_url_https\":\"https:\\/\\/pbs.twimg.com\\/profile_images\\/877806258543357952\\/UmYBJTnf_normal.jpg\",\"profile_banner_url\":\"https:\\/\\/pbs.twimg.com\\/profile_banners\\/994741592\\/1562337832\",\"default_profile\":false,\"default_profile_image\":false,\"following\":null,\"follow_request_sent\":null,\"notifications\":null},\"geo\":null,\"coordinates\":null,\"place\":null,\"contributors\":null,\"is_quote_status\":false,\"quote_count\":0,\"reply_count\":2,\"retweet_count\":7,\"favorite_count\":11,\"entities\":{\"hashtags\":[{\"text\":\"BritishGP\",\"indices\":[56,66]},{\"text\":\"F1\",\"indices\":[112,115]}],\"urls\":[{\"url\":\"https:\\/\\/t.co\\/vlRTtpjjji\",\"expanded_url\":\"https:\\/\\/bit.ly\\/2XzRIAJ\",\"display_url\":\"bit.ly\\/2XzRIAJ\",\"indices\":[88,111]}],\"user_mentions\":[],\"symbols\":[],\"media\":[{\"id\":1148524641465589760,\"id_str\":\"1148524641465589760\",\"indices\":[116,139],\"media_url\":\"http:\\/\\/pbs.twimg.com\\/media\\/D_BhE4ZW4AATSZm.jpg\",\"media_url_https\":\"https:\\/\\/pbs.twimg.com\\/media\\/D_BhE4ZW4AATSZm.jpg\",\"url\":\"https:\\/\\/t.co\\/WOXKXy4a5W\",\"display_url\":\&q...