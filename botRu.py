from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

user = (input("\nUsuário: "))
senha = (input("\nSenha: "))


data = int(input("\nDeseja agendar apartir de que dia dessa semana?: "))
data = str(data)

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

cont = 1
navegador.get(
    "https://ru.fw.iffarroupilha.edu.br/"
    )
#sleep(1)

navegador.find_element('xpath','//*[@id="username"]').send_keys(user)
#sleep(1)
navegador.find_element('xpath','//*[@id="password"]').send_keys(senha)
##sleep(1)
navegador.find_element('xpath','//*[@id="kc-login"]').click()
#sleep(6)
home = True
while home:
    try:
        navegador.find_element('xpath','//*[@id="frmHeader"]/div[1]')
        home = False
    except NoSuchElementException:
        sleep(.1)

navegador.find_element('xpath','//*[@id="frmHeader"]/div[1]').click()
navegador.find_element(By.XPATH,'//*[@id="j_idt30:j_idt31_j_idt32"]/ul/li[1]/a').click()
sleep(.2)

for i in range(5):
    navegador.find_element(By.PARTIAL_LINK_TEXT,data).click()
    sleep(.2)
    navegador.find_element(By.XPATH,'//*[@id="frmMain:tipoRefeicao_label"]').click()
    #sleep(.8)
    navegador.find_element(By.XPATH,'//*[@id="frmMain:tipoRefeicao_1"]').click()
    #sleep(.8)
    navegador.find_element(By.XPATH,'//*[@id="frmMain:addButton"]/span[2]').click()
    #sleep(.8)
    confirm = True
    while confirm:
        try:
            navegador.find_element(By.XPATH,'//*[@id="frmMain:j_idt79"]/span')
            confirm = False
        except NoSuchElementException:
            sleep(.1)
    
    navegador.find_element(By.XPATH,'//*[@id="frmMain:j_idt79"]/span').click()
    data = int(data) + cont
    data = str(data)
sleep(2)
print("\n---------------------------- Tudo pronto Parça------------------------")
print("""
\n
⠀⠉⠉⠉⣿⡿⠿⠛⠋⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⣻⣩⣉⠉⠉
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢀⣀⣀⣀⣀⣀⣀⡀⠄⠄⠉⠉⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣠⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⢤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠄⠄⠄
⡄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠉⠄⠉⠉⠉⣋⠉⠉⠉⠉⠉⠉⠉⠉⠙⠛⢷⡀⠄⠄
⣿⡄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠠⣾⣿⣷⣄⣀⣀⣀⣠⣄⣢⣤⣤⣾⣿⡀⠄
⣿⠃⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣹⣿⣿⡿⠿⣿⣿⣿⣿⣿⣿⣿⣿⢟⢁⣠
⣿⣿⣄⣀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠉⠉⣉⣉⣰⣿⣿⣿⣿⣷⣥⡀⠉⢁⡥⠈
⣿⣿⣿⢹⣇⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠒⠛⠛⠋⠉⠉⠛⢻⣿⣿⣷⢀⡭⣤⠄
⣿⣿⣿⡼⣿⠷⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢀⣀⣠⣿⣟⢷⢾⣊⠄⠄
⠉⠉⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⣈⣉⣭⣽⡿⠟⢉⢴⣿⡇⣺⣿⣷
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠁⠐⢊⣡⣴⣾⣥⣿⣿⣿
""")