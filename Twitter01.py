# -*- coding: utf-8 -*-
import os
import tweepy as tw
import pandas as pd

consumer_key='kESXlhKWmwrcpxXGsAJFQZvj7'
consumer_secret='QJGOdskElgzJI0p3HJZCErsmJ3lLBlOUjfTE9v3W85Mt1FRF1y'
access_token_key='1412739736792408064-iQpo9JZXoDnX0CbEMJpdFVOQytATmu'
access_token_secret='F3jVOr8kMiJrUODoCBeAYUujbm9WVQARL3CfuRT68IcJH')


auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)
