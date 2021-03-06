#!/usr/bin/env python2
# -*- coding: utf-8 -*- #

from twitterbot import TwitterBot

class EchoBot(TwitterBot):
    def bot_init(self):
        """
        Iniciar y configurar nuestra herramienta!

        Use esta configuracion y opcion para iniciar y personalizar el estado de nuestra herramienta
        """

        ############################
        # REQUERIDOS: LOGIN DETALLES! #
        ############################
        self.config['api_key'] = ''
        self.config['api_secret'] = ''
        self.config['access_key'] = ''
        self.config['access_secret'] = ''


        ######################################
        # SEMI-OPCIONAL: OTRAS CONFIFURACIONES! #
        ######################################

        # how often to tweet, in seconds
        self.config['tweet_interval'] = 30 * 60     # default: 30 minutes

        # use this to define a (min, max) random range of how often to tweet
        # e.g., self.config['tweet_interval_range'] = (5*60, 10*60) # tweets every 5-10 minutes
        self.config['tweet_interval_range'] = None

        # only reply to tweets that specifically mention the bot
        self.config['reply_direct_mention_only'] = False

        # only include bot followers (and original tweeter) in @-replies
        self.config['reply_followers_only'] = True

        # fav any tweets that mention this bot?
        self.config['autofav_mentions'] = False

        # fav any tweets containing these keywords?
        self.config['autofav_keywords'] = []

        # follow back all followers?
        self.config['autofollow'] = False


        ###########################################
        #CUSTOMIZARLO#
        ###########################################
        
        # If you'd like to save variables with the bot's state, use the
        # self.state dictionary. These will only be initialized if the bot is
        # not loading a previous saved state.

        # self.state['butt_counter'] = 0

        # You can also add custom functions that run at regular intervals
        # using self.register_custom_handler(function, interval).
        #
        # For instance, if your normal timeline tweet interval is every 30
        # minutes, but you'd also like to post something different every 24
        # hours, you would implement self.my_function and add the following
        # line here:
        
        # self.register_custom_handler(self.my_function, 60 * 60 * 24)


    def on_scheduled_tweet(self):
        """
        Make a public tweet to the bot's own timeline.

        It's up to you to ensure that it's less than 140 characters.

        Set tweet frequency in seconds with TWEET_INTERVAL in config.py.
        """
        pass
        

    def on_mention(self, tweet, prefix):
        """
        Defines actions to take when a mention is received.

        tweet - a tweepy.Status object. You can access the text with
        tweet.text

        prefix - the @-mentions for this reply. No need to include this in the
        reply string; it's provided so you can use it to make sure the value
        you return is within the 140 character limit with this.

        It's up to you to ensure that the prefix and tweet are less than 140
        characters.

        When calling post_tweet, you MUST include reply_to=tweet, or
        Twitter won't count it as a reply.
        """
        text = '(' + ' '.join(w for w in tweet.text.split() if '@' not in w) + '...)'
        prefixed_text = prefix + ' ' + text
        self.post_tweet(prefix + ' ' + text, reply_to=tweet)


    def on_timeline(self, tweet, prefix):
        """
        Defines actions to take on a timeline tweet.

        tweet - a tweepy.Status object. You can access the text with
        tweet.text

        prefix - the @-mentions for this reply. No need to include this in the
        reply string; it's provided so you can use it to make sure the value
        you return is within the 140 character limit with this.

        It's up to you to ensure that the prefix and tweet are less than 140
        characters.

        When calling post_tweet, you MUST include reply_to=tweet, or
        Twitter won't count it as a reply.
        """
        if 'wanna hear u echo' in tweet.text.lower():
            self.post_tweet(prefix + ' ECHO (ECHO) ECHO (ECHO)', reply_to=tweet)


if __name__ == '__main__':
    bot = EchoBot()
    bot.run()
