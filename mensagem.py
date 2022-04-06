import requests
import json
from conexão import *
class Mensagse:
    def __init__(self, id,contato):
        self.id = id
        self.contato = contato
    #Metodo ultilizado para fazer o disparo de mensagem simples.    
    def disparo(self,cont,mensa):
        conecta = Banco()
        conecta.conec()
        url = "http://ipAPI:8000/chat/send?"+"id="+ self.id
        payload = json.dumps({
                "id": self.id,
                "receiver": cont,
                "message": mensa
        })
        headers = {
                'Content-Type': 'application/json'
        }
        response = requests.request("POST", url, headers=headers, data=payload)