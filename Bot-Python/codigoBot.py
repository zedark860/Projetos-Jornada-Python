# PASSO A PASSO DO PROJETO
# Passo 1: Entrar no sistema da empresa
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login
import pyautogui
import time

# pyautogui.click -> clicar com mouse
# pyautogui.write -> escrever texto
# pyautogui.press -> apertar uma tecla
# pyautogui.hotkey -> atalho (combinação de teclas)

pyautogui.PAUSE = 0.5

# abrir o chrome
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

# entrar no link
link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
time.sleep(1)
pyautogui.write(link)
pyautogui.press('enter')

# esperar o site carregar
time.sleep(1.5)

# Passo 2: Fazer login
pyautogui.click(x=-634, y=396)
pyautogui.write('oversouls11@gmail.com')

pyautogui.press('tab')
pyautogui.write('123')

pyautogui.click(x=-705, y=553)
time.sleep(1.5)

# Passo 3: Importar a base de dados de produtos
import pandas as pd
import pandas

tabela = pandas.read_csv('D:\Códigos\Projetos-Jornada-Python\Bot-Python\produtos.csv')

# Passo 4: Cadastrar 1 produto

# Passo 5: Repetir cadastro para todos os produto

for linha in tabela.index:
    pyautogui.click(x=-780, y=277)

    codigo = tabela.loc[linha, 'codigo']
    marca = tabela.loc[linha, 'marca']
    tipo = tabela.loc[linha, 'tipo']
    categoria = tabela.loc[linha, 'categoria']
    preco_unitario = tabela.loc[linha, 'preco_unitario']
    custo = tabela.loc[linha, 'custo']
    obs = tabela.loc[linha, 'obs']

    pyautogui.write(str(codigo))
    pyautogui.press('tab')
    pyautogui.write(str(marca))
    pyautogui.press('tab')
    pyautogui.write(str(tipo))
    pyautogui.press('tab')
    pyautogui.write(str(categoria))
    pyautogui.press('tab')
    pyautogui.write(str(preco_unitario))
    pyautogui.press('tab')
    pyautogui.write(str(custo))
    pyautogui.press('tab')
    if not pd.isna(obs):
        pyautogui.write(str(obs))

    # aperta para enviar
    pyautogui.press('tab')
    pyautogui.press('enter')

    pyautogui.scroll(50000)