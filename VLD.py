import requests
import os



class VURL():

    def __init__(self, url):
        self.url = url


    def valid(self):

        content = requests.get(self.url)
        print (self.url,'|', content.status_code)
        if content.status_code != 200:
            slack_webhook_url = 'https://hooks.slack.com/services/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'
            payload = {"text": "URL [{}] --- ERROR [{}]".format(self.url,content.status_code)}
            response = requests.post(slack_webhook_url, json=payload)
        return '-------------------------------------------'
