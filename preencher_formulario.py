from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import pyautogui

# Perguntar ao utilizador o mês inicial e final para o qual os recibos serão gerados
mes_inicial = int(input('Mês inicial: '))
mes_final = int(input('Mês final: '))

# Caminho para o driver do Chrome
chrome_driver_path = '/usr/local/bin/chromedriver'

# Iniciar o serviço do ChromeDriver
chrome_service = Service(chrome_driver_path)

# Iniciar o navegador
driver = webdriver.Chrome(service=chrome_service)

# URL do formulário
form_url = 'https://imoveis.portaldasfinancas.gov.pt/arrendamento/criarRecibo/437278'

# Abrir o formulário no navegador
driver.get(form_url)

# Esperar até que a página seja carregada
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.TAG_NAME, 'html')))

# Encontrar a tab 'NIF' pelo XPath e clicar nela
tab_nif = driver.find_element(By.XPATH, '//label[@for="tab2"]')
tab_nif.click()

# Encontrar e preencher o campo de username
campo_data_inicio = driver.find_element(By.ID, 'username')
campo_data_inicio.send_keys('username') # Preencher com username

# Encontrar e preencher o campo de password
campo_data_inicio = driver.find_element(By.ID, 'password-nif')
campo_data_inicio.send_keys('password') # Preencher com password

# Encontrar o botão 'Autenticar' pelo ID e clicar nele
botao_autenticar = driver.find_element(By.ID, 'sbmtLogin')
botao_autenticar.click()

from datetime import datetime

# Ano para o qual os recibos serão gerados
ano = datetime.now().year

# Importar o módulo calendar
import calendar

# Loop sobre os meses do ano
for mes in range(mes_inicial, mes_final + 1):

	# Obter o último dia do mês
	ultimo_dia = calendar.monthrange(ano, mes)[1]

	# Primeira data (primeiro dia do mês)
	data_inicio = f"{ano}-{mes:02d}-01"

	# Segunda data (último dia do mês)
	data_fim = f"{ano}-{mes:02d}-{ultimo_dia}"

	# Terceira data (data do pagamento, que é a mesma que a segunda data)
	data_pagamento = data_fim

	# Se data de pagamento for depois da data actual, então a data de pagamento é a dara actual
	if data_pagamento > datetime.now().strftime('%Y-%m-%d'):
		data_pagamento = datetime.now().strftime('%Y-%m-%d')

	# Encontrar e preencher o campo de data de início
	campo_data_inicio = driver.find_element(By.NAME, 'dataInicio')
	campo_data_inicio.send_keys(data_inicio)

	# Encontrar e preencher o campo de data de fim
	campo_data_fim = driver.find_element(By.NAME, 'dataFim')
	campo_data_fim.send_keys(data_fim)

	# Encontrar e preencher o campo de data de pagamento
	campo_data_pagamento = driver.find_element(By.NAME, 'dataRecebimento')
	campo_data_pagamento.send_keys(data_pagamento)

	# Encontrar o elemento de input do tipo rádio
	radio_button = driver.find_element(By.CSS_SELECTOR, 'input[type="radio"][ng-model="recibo.tipoImportancia"]')
	# Clicar no elemento de input do tipo rádio
	radio_button.click()

	time.sleep(2)

	# Localizar o botão Emitir pela classe do botão
	botao_emitir = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-sm.btn-success")))

	# Clicar no botão Emitir
	botao_emitir.click()

	# Localizar o botão Emitir pela classe do botão
	botao_emitir2 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-success")))

	# Clicar no botão Emitir
	botao_emitir2.click()

	# Localizar o botão Imprimir pela classe do botão
	botao_imprimir = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-sm.btn-default-hover-primary")))

	# Clicar no botão Imprimir
	botao_imprimir.click()

	# Esperar até que uma nova aba seja aberta
	WebDriverWait(driver, 20).until(EC.number_of_windows_to_be(2))

	# Mudar o foco para a nova aba
	driver.switch_to.window(driver.window_handles[-1])

	# Esperar que o utilizador feche a aba actual
	while len(driver.window_handles) > 1:
		time.sleep(1)

	# Mudar o foco para a aba anterior
	driver.switch_to.window(driver.window_handles[-1])

	# Abrir o formulário no navegador
	driver.get(form_url)

	# Esperar até que a página seja carregada
	WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.TAG_NAME, 'html')))
