import sys
from time import sleep
from datetime import datetime, date, time, timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

user = sys.argv[1]
senha = sys.argv[2]
moradia = sys.argv[3]
dias = [d.strip() for d in sys.argv[4].split(',') if d.strip()]
refeicoes = [r.strip() for r in sys.argv[5].split(',') if r.strip()]

servico = Service(GeckoDriverManager().install())
navegador = webdriver.Firefox(service=servico)

navegador.get("https://ru.fw.iffarroupilha.edu.br/")

navegador.find_element(By.XPATH, '//*[@id="username"]').send_keys(user)
navegador.find_element(By.XPATH, '//*[@id="password"]').send_keys(senha)
navegador.find_element(By.XPATH, '//*[@id="kc-login"]').click()

home = True
while home:
    try:
        navegador.find_element(By.XPATH, '//*[@id="frmHeader"]/div[1]')
        home = False
    except NoSuchElementException:
        sleep(.1)

navegador.find_element(By.XPATH, '//*[@id="frmHeader"]/div[1]').click()
navegador.find_element(By.XPATH, '//*[@id="j_idt30:j_idt31_j_idt32"]/ul/li[1]/a').click()
sleep(.2)

for data in dias:
    dia, mes, ano = map(int, data.split('/'))
    dia_semana = date(ano, mes, dia).weekday()
    agora = datetime.now()
    prev_deadline = datetime.combine(date(ano, mes, dia) - timedelta(days=1), time(17, 0))
    janta_deadline = datetime.combine(date(ano, mes, dia), time(11, 30))

    refeicoes_possiveis = []
    if moradia == "sim":
        if agora <= prev_deadline and "cafe" in refeicoes:
            refeicoes_possiveis.append(1)
        if agora <= prev_deadline and "almoco" in refeicoes:
            refeicoes_possiveis.append(2)
        if agora <= janta_deadline and dia_semana != 4 and "janta" in refeicoes:
            refeicoes_possiveis.append(3)
    else:
        if agora <= prev_deadline:
            refeicoes_possiveis.append(2)

    for idx in refeicoes_possiveis:
        navegador.find_element(By.PARTIAL_LINK_TEXT, str(dia)).click()
        sleep(.2)
        navegador.find_element(By.XPATH, '//*[@id="frmMain:tipoRefeicao_label"]').click()
        sleep(.2)
        navegador.find_element(By.XPATH, f'//*[@id="frmMain:tipoRefeicao_{idx}"]').click()
        sleep(.2)
        navegador.find_element(By.XPATH, '//*[@id="frmMain:addButton"]/span[2]').click()
        confirm = True
        while confirm:
            try:
                navegador.find_element(By.XPATH, '//*[@id="frmMain:j_idt79"]/span')
                confirm = False
            except NoSuchElementException:
                sleep(.1)
        navegador.find_element(By.XPATH, '//*[@id="frmMain:j_idt79"]/span').click()
        sleep(.2)

sleep(1)
print("Agendamentos finalizados.")