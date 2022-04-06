import pymysql
class Banco:
    def __init__(self, host='localhost',user='root',passwd='', database = 'dispara'):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.database = database
    #metodo de conexão ao banco de dados
    def conec(self):
        self.con = pymysql.connect(
            host = self.host,
            user = self.user,
            passwd = self.passwd,
            database = self.database
        )
        self.cur = self.con.cursor()
    #metodo ultilizado para fazer o desligamento ao banco de dados
    def desconect(self):
        self.con.close()
    #metodo ultilizado para executar comandos dml    
    def dml(self,sql,dados):
        self.cur.execute(sql,dados)
        self.con.commit()
        self.desconect()
    #metodo para efetuar login na aplicação
    def login(self, email, senha):
        self.conec()
        comando = """SELECT * FROM users WHERE email = %s and senha = %s"""
        self.cur.execute(comando, [email, senha])
        resultado = self.cur.fetchall()
        if resultado:
            return True
        else:
            return False
    #metodo ultilizado para fazer a consulta dos contatos no banco de dados
    def consultar_contatos(self,user):
            self.conec()
            comando = """SELECT contatos.contatos FROM contatos INNER JOIN users ON contatos.id_users=users.id WHERE id_users LIKE %s"""
            self.cur.execute(comando,user)
            resultado = self.cur.fetchall()
            return resultado
    #metodo que faz a consulta do id no banco de dados
    def consultar_id(self, email, senha):
        self.conec()
        comando = """SELECT * FROM users WHERE email = %s and senha = %s"""
        self.cur.execute(comando, [email, senha])
        resultado = self.cur.fetchall()
        for x in resultado:
           return x
    #Metodo que consulta o id do contato no banco de dados.       
    def consultar_ids(self,contato):
            self.conec()
            comando = """SELECT id FROM contatos WHERE contatos = %s"""
            self.cur.execute(comando,contato)
            resultado = self.cur.fetchall()
            for x in resultado:
                v = str(x).strip("()")
                a2 = str(v)
                d = a2.replace(',','')
                return d
    #metodo que consulta o id do usuario na tabela de contatos.            
    def consultar_ids_users(self,contato):
            self.conec()
            comando = """SELECT id_users FROM contatos WHERE contatos = %s"""
            self.cur.execute(comando,contato)
            resultado = self.cur.fetchall()
            for x in resultado:
                v = str(x).strip("()")
                a2 = str(v)
                d = a2.replace(',','')
                return d    
    #metodo que adiciona o registro de envio na tabela check.                        
    def add_ids(self,contato):
            self.conec()
            ids = self.consultar_ids(contato)
            id_users = self.consultar_ids_users(contato)
            comando = """INSERT INTO api.check (id_contato, id_user) VALUES (%s,%s)"""
            dados = ids,id_users
            self.dml(comando,dados)
    #metodo que consulta o id do usuario na tabela check.        
    def consultar_id_check(self,user):
            self.conec()
            comando = """SELECT id_user FROM api.check WHERE id_user LIKE %s"""
            self.cur.execute(comando,user)
            resultado = self.cur.fetchall()
            return resultado
    #metodo que faz a validação do envio da mensagem para o contato        
    def consultar_id_cont(self,contato):
            self.conec()
            contat = self.consultar_ids(contato)
            user = self.consultar_ids_users(contato)
            comando = """SELECT * FROM api.check WHERE id_contato = %s and id_user = %s"""
            dados = contat,user
            self.cur.execute(comando,dados)
            resultado = self.cur.fetchall()
            if resultado:
                 return True
            else:
                 return False   
    #metodo que faz a limpeza do banco quando todas as mensagem são enviada.                                                      
    def delet_ids_check(self,user):
            self.conec()
            comando = """DELETE FROM api.check where id_user=%s"""
            self.dml(comando,user)        