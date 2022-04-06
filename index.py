import streamlit as st
import pandas as pd
from conexão import *
from mensagem import *
from midia import *
from adicionar import *
from users import*
#Campo aonde o usuario digita seu login.
email = st.text_input("Digite seu login: ")
senha = st.text_input("Digite sua senha: ", type="password")
conexao1= Banco()
a1 = conexao1.login(email,senha)
id = conexao1.consultar_id(email,senha)
try:
    teto = str(id[0])
except:
     st.stop()
contatos = conexao1.consultar_contatos(teto)
id_checks = conexao1.consultar_id_check(teto)
bot = Mensagse(teto,contatos)
mid = Mid(teto,contatos)
if a1  == True:
    #Imagem do menu
    st.sidebar.image("https://cdn.dooca.store/21068/files/cta-whatsapp.png?v=1640009589&webp=0",
                     use_column_width=True)
    dd_selectbox = st.sidebar.selectbox('MENU', ['Inicio', 'Enviar Mensagem', 'Adicionar Contatos','Adicionar Conta'])
    hide_menu_style = """
            <style>
            #MainMenu {visibility: hidden;}
            </style>
            """
    st.markdown(hide_menu_style, unsafe_allow_html=True)
    if dd_selectbox == 'Inicio':
        st.title("Bem Vindo")
        st.caption("Shoot Zap 1.0")
    #Caixa de envio de mensagem:
    if dd_selectbox == 'Enviar Mensagem':
        genrre = st.radio(
            "Selecione uma das opções",
            ('', 'Enviar imagem e mensagem','Enviar PDF', 'Enviar mensagem: ', 'Enviar mensagem para um numero: '))
    #Faz o envio de imagem com mensagem.        
        if genrre == 'Enviar imagem e mensagem':
            mensagems = st.text_area("Digite a mensagem que deseja disparar: ")
            links = st.text_input("Digite o link da imagem: ")
            botaaosa = st.button("Enviar", disabled=False)
            if botaaosa == (True):
                ids = len(id_checks)
                numero1 = int(ids)
                total = len(contatos)
                numero2 = int(total)
                if (numero1) == (numero2): 
                    conexao1.delet_ids_check(teto)                    
                for output in contatos:
                    conta = conexao1.consultar_id_cont(output)
                    if conta == False:
                        a2 = str(output)
                        mid.dispara(a2, links, mensagems)
                        conexao1.add_ids(output)
    #Faz o envio de imagem com mensagem e pdf                    
        if genrre == 'Enviar PDF':
            mensagems = st.text_area("Digite a mensagem que deseja disparar: ")
            link = st.text_input("Digite o link do encarte: ")
            links = st.text_input("Digite o link do pdf: ")
            nome = st.text_input("Digite o nome do pdf: ")
            botaaosa = st.button("Enviar", disabled=False)
            if botaaosa == (True):
                ids = len(id_checks)
                numero1 = int(ids)
                total = len(contatos)
                numero2 = int(total)
                if (numero1) == (numero2): 
                    conexao1.delet_ids_check(teto)                    
                for output in contatos:
                    conta = conexao1.consultar_id_cont(output)
                    if conta == False:
                        a2 = str(output)
                        mid.dispara(a2, link, mensagems)
                        mid.disparapdf(a2, links, mensagems, nome) 
                        conexao1.add_ids(output)  
        #Faz apenas o envio de mensagem simples.                     
        if genrre == 'Enviar mensagem: ':
            mensagems = st.text_input("Digite a mensagem que deseja disparar: ")
            botaaosa = st.button("Enviar", disabled=False)
            if botaaosa == (True):
                ids = len(id_checks)
                numero1 = int(ids)
                total = len(contatos)
                numero2 = int(total)
                if (numero1) == (numero2): 
                    conexao1.delet_ids_check(teto)                    
                for output in contatos:
                    conta = conexao1.consultar_id_cont(output)
                    if conta == False:
                            a2 = str(output)
                            bot.disparo(a2, mensagems)
                            conexao1.add_ids(output)
        #Faz o envio de uma mensagem para apenas um numero.                    
        if genrre == 'Enviar mensagem para um numero: ':
            mensagens = st.text_input("Digite o numero que deseja enviar mensagem:  ")
            mensagems = st.text_input("Digite a mensagem: ")
            botaaosa = st.button("Enviar", disabled=False)
            if botaaosa == (True):
                bot.disparo(mensagens, mensagems)  
    #Caixa para adicionar contatos.                    
    if dd_selectbox == 'Adicionar Contatos':
        st.title("Adicionar Contatos")
        genre = st.radio(
            "Selecione uma das opções",
            ('', 'Adicionar Varios Contato', 'Adicionar Um Contato'))
    #Adiciona diversos contatos (Para adicionar varios contato é necessario que digite da seguinte forma ==> Numero1,Numero2,Numero3)        
        if genre == 'Adicionar Varios Contato':
           joi = st.text_input("Digita: ")
           cavalo = joi.split(',')
           botaodecon = st.button("Adicionar", disabled=False)
           if botaodecon == (True):
               for x in cavalo:
                cont = Add(x,teto)
                cont.adicionar_contato()
    #Adiciona apenas um contato.
        if genre == 'Adicionar Um Contato':
           escreve = st.text_input("Escreva o contato: ")
           adicionarc = st.button("Adicionar", disabled=False)
           if adicionarc == (True):
               cont = Add(escreve,teto)
               cont.adicionar_contato()
    #Caixa de consulta de contatos ao usuario logado(Busca feita no banco de dados.)           
        with st.expander("Consultar Contatos: "):
            Consultap, Consultag = st.columns(2)
            with Consultap:
                contatoss = conexao1.consultar_contatos(teto)
                df = pd.DataFrame(
                    contatoss,
                    columns=('Numeros %d' % i for i in range(1)))
                st.dataframe(df)
            with Consultag:
                total = len(contatoss)
                st.metric(label="Total", value=total)
    if dd_selectbox == 'Adicionar Conta':
        st.title("CADASTRO DE NOVO USUARIO")      
        nome = st.text_input("Nome: ")
        login = st.text_input("Login: ")
        senha = st.text_input("Senha: ", type = "password")
        cadastro = st.button("Cadastro", disabled=False)
        if cadastro == (True):
            novo = Users(nome,login,senha)
            novo.adicionar_users()

        
else:
    st.caption("Verifique novamente o seu login")