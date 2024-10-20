# funcionalidade.py

from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, WebDriverException

def agendar_almoço(user, senha, dias):
    # Verificação das entradas
    if not user or not senha:
        raise ValueError("Usuário e senha são obrigatórios!")

    if not dias:
        raise ValueError("Selecione pelo menos um dia para agendar.")

    # Realiza o agendamento usando Selenium
    try:
        servico = Service(ChromeDriverManager().install())
        navegador = webdriver.Chrome(service=servico)
    except WebDriverException as e:
        raise RuntimeError(f"Erro ao iniciar o navegador: {e}")

    try:
        navegador.get("https://ru.fw.iffarroupilha.edu.br/")
        navegador.find_element('xpath', '//*[@id="username"]').send_keys(user)
        navegador.find_element('xpath', '//*[@id="password"]').send_keys(senha)
        navegador.find_element('xpath', '//*[@id="kc-login"]').click()

        # Aguarda a página inicial
        home = True
        while home:
            try:
                navegador.find_element('xpath', '//*[@id="frmHeader"]/div[1]')
                home = False
            except NoSuchElementException:
                sleep(.1)

        # Acessa o menu de agendamento
        navegador.find_element('xpath', '//*[@id="frmHeader"]/div[1]').click()
        navegador.find_element(By.XPATH, '//*[@id="j_idt30:j_idt31_j_idt32"]/ul/li[1]/a').click()
        sleep(.2)

        # Faz o agendamento para os dias selecionados
        for dia in dias:
            try:
                # Acessa o dia usando o valor inteiro
                navegador.find_element(By.PARTIAL_LINK_TEXT, str(dia)).click()
                sleep(.2)
                navegador.find_element(By.XPATH, '//*[@id="frmMain:tipoRefeicao_label"]').click()
                navegador.find_element(By.XPATH, '//*[@id="frmMain:tipoRefeicao_1"]').click()
                navegador.find_element(By.XPATH, '//*[@id="frmMain:addButton"]/span[2]').click()

                # Confirmação do agendamento
                confirm = True
                while confirm:
                    try:
                        navegador.find_element(By.XPATH, '//*[@id="frmMain:j_idt79"]/span')
                        confirm = False
                    except NoSuchElementException:
                        sleep(.1)

                navegador.find_element(By.XPATH, '//*[@id="frmMain:j_idt79"]/span').click()

            except NoSuchElementException:
                print(f"Erro: Elemento não encontrado ao tentar agendar para o dia {dia}.")
                continue
            except Exception as e:
                print(f"Erro desconhecido ao tentar agendar para o dia {dia}: {e}")
                continue

    except WebDriverException as e:
        raise RuntimeError(f"Erro ao acessar o site: {e}")
    finally:
        navegador.quit()
