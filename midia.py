import requests
import json
from conexão import *
class Mid:
    def __init__(self, id, contato):
        self.id = id
        self.contato = contato
      #metodo ultilizado para fazer o disparo da imagem com mensagem.
    def dispara(self,numer,link,mensagem):   
          url = "http://ipAPI:8000/chat/send-file?"+"id="+ self.id
          payload=json.dumps({
                "id": self.id,
                "receiver": numer,
                "link": link,
                "message": mensagem
                })
          headers = {
                    'Content-Type': 'application/json'
          }
          response = requests.request("POST", url, headers=headers, data=payload)
      #Metodo ultilizado para fazer o diparo do pdf    
    def disparapdf(self,numer,link,mensagem,nome):
          url = "http://ipAPI:8000/chat/send-pdf?"+"id="+ self.id
          payload=json.dumps({
                "id": self.id,
                "receiver": numer,
                "link": link,
                "message": mensagem,
                "nome": nome
                })
          headers = {
                    'Content-Type': 'application/json'
          }
          response = requests.request("POST", url, headers=headers, data=payload)