from conexão import *
class Users :
    def __init__(self, nome,email , senha):
        self.nome = nome
        self.senha = senha
        self.email = email
    #metodo para fazer o registro do usuario
    def adicionar_users(self):
        conecta = Banco()
        conecta.conec()
        inserir = "INSERT INTO users (nome,senha,email) VALUES (%s,%s,%s)"
        sqls = self.nome, self.senha,self.email
        conecta.dml(inserir,sqls)