import tkinter as tk
import time
import os

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# url inicio (login)
#https://login.natura.net/acesso-seguro

# Função para iniciar a automação do login
def iniciar_automacao_pedido():
    load_dotenv()
    print("Boas vindas a automação de pedidos para consultoras")
    print("Abaixo insira suas credenciais para acesso")
    
    login_url = 'https://login.natura.net/acesso-seguro'


    username = os.getenv("USERNAME_ACESSO")
    senha = os.getenv("SENHA_ACESSO")
    
    service = Service(ChromeDriverManager().install())
    
    navegador = webdriver.Chrome(service=service)
    navegador.get(login_url)
    
    navegador.find_element(By.CLASS_NAME, "goBackButton").click() #volta pra página de login
    username_input = navegador.find_element(By.ID, "username")
    username_input.send_keys(username) #insere o usuário
    senha_input = navegador.find_element(By.ID, "password")
    senha_input.send_keys(senha) #insere a senha
    time.sleep(10)
    navegador.find_element(By.CLASS_NAME, "sc-jSprwV").click() #submit no login
    
    while True:
        time.sleep(2)
    
    print(username, password)
    codigo_consultora = str

iniciar_automacao_pedido()
#     # Configurar o driver do navegador
#     driver_path = 'caminho/para/seu/chromedriver'  # Atualize com o caminho do seu ChromeDriver
#     driver = webdriver.Chrome(executable_path=driver_path)

#     # URL do site
#     url = 'https://example.com/login'  # Atualize com a URL do site
#     driver.get(url)

#     # Localizar e preencher os campos de login
#     username_field = driver.find_element(By.ID, 'username_field_id')  # Atualize com o ID correto
#     password_field = driver.find_element(By.ID, 'password_field_id')  # Atualize com o ID correto
#     login_button = driver.find_element(By.ID, 'login_button_id')  # Atualize com o ID correto

#     username_field.send_keys(username)
#     password_field.send_keys(password)
#     login_button.click()

#     # Esperar até que a página de destino após o login esteja carregada
#     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'elemento_da_pagina_pos_login')))  # Atualize com o ID correto

#     # Continuar a automação conforme necessário
#     # Exemplo: Navegar para outra página e inserir dados
#     driver.get('https://example.com/form')  # Atualize com a URL da página do formulário
#     time.sleep(5)  # Espera a página carregar

#     # Lista de códigos que você quer inserir
#     codigos = ['codigo1', 'codigo2', 'codigo3']

#     # Localizar o campo de input pelo ID, nome, classe, etc.
#     input_field = driver.find_element(By.ID, 'input_field_id')  # Atualize com o ID correto

#     # Inserir códigos um por um
#     for codigo in codigos:
#         input_field.clear()
#         input_field.send_keys(codigo)
#         input_field.send_keys(Keys.ENTER)  # ou outro comando para submeter o código, se necessário

#         # Esperar um pouco antes de inserir o próximo código (ajuste conforme necessário)
#         time.sleep(2)

#     # Não fechar o navegador imediatamente para que o usuário possa ver o resultado final
#     # driver.quit()

# # Configurar a janela principal do tkinter
# root = tk.Tk()