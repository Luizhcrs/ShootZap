from conexão import *
class Add :
    def __init__(self,contato,id):
        self.contato = contato
        self.id = id
    #metodo para adicionar contato
    def adicionar_contato(self):
        conecta = Banco()
        conecta.conec()
        inserir = "INSERT INTO contatos (contatos, id_users) VALUES (%s,%s)"
        sqls = self.contato,self.id
        conecta.dml(inserir,sqls) 