from errbot import BotPlugin, botcmd

import requests
import random
import logging

log = logging.getLogger(name='errbot.plugins.StackOverflow')

class StackOverflow(BotPlugin):

    def get_configuration_template(self):
        """ configuration entries """
        config = {
            'api_key': '',
        }
        return config

    def _check_config(self, option):

        # if no config, return nothing
        if self.config is None:
            return None
        else:
            # now, let's validate the key
            if option in self.config:
                return self.config[option]
            else:
                return None

    def _get_api_key(self):
        return self._check_config('api_key') or 'API_KEY_HERE'

    @botcmd
    def stackoverflow(self, msg, args):
        """ Return top 5 voted results from stackoverflow
            Example:
            !stackoverflow python debugger
            !stackoverflow javascript cors
        """

        API_ENDPOINT = 'https://api.stackexchange.com/2.2/search'
        RESULT_LIMIT = 5

        #api_key = self._get_api_key()
  
        request_url = '%s?pagesize=%d&order=desc&sort=votes&intitle=%s&site=stackoverflow' % (API_ENDPOINT, RESULT_LIMIT, args[0])
        print request_url
        r = requests.get(request_url)
        results = r.json()
        
        #self.send(msg.frm,
        #          response,
        #          message_type=msg.type,
        #          in_reply_to=msg,
        #          groupchat_nick_reply=True)
        return results
