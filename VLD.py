import requests



class VURL():

    def __init__(self, url):
        self.url = url


    def valid(self):

        content = requests.get(self.url) 
        if content.status_code != 200:#caso o status code seja um valor diferente de 200 o canal recebera um alerta
            slack_webhook_url = 'https://hooks.slack.com/services/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'#Endereço do canal
            payload = {"text": "URL [{}] --- ERROR [{}]".format(self.url,content.status_code)}#Text com link quebrado
            response = requests.post(slack_webhook_url, json=payload)#Post da mensagem no canal do Slack
        return '-------------------------------------------'
