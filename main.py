'''
Author : Shantonu Mandal
Email  : shantonu.2610[at]gmail.com
Date   : Wed 04 Dec 2012 03:00:40 PM IST

Description :
A Google App Engine app to load 200 tweets from the Twitter user specified in the GET request to the app. The GET parameter is 'user'.
'''

#!/usr/bin/env python

import webapp2
import tweepy

class MainHandler(webapp2.RequestHandler):
    def get(self):
        arg = self.request.get('user')
	api = tweepy.API()
	timeline = api.user_timeline(count=200, screen_name = arg,  trim_user=True, include_rts=True)
	ctr=1
	for tweet in timeline: 
		self.response.out.write('<title>Tweet Loader</title>')		
		self.response.out.write(ctr)
		self.response.out.write(". ")
		self.response.out.write(tweet.text)
		self.response.out.write("<br>")
		ctr=ctr+1
	 
app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
