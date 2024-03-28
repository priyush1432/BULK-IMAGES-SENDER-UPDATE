from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from urllib.parse import quote
import time


with open('messege.txt', 'r') as file:
    msg = file.read()

msg =quote(msg)

number = []
with open('number.txt', 'r') as file:
    for num in file.readlines():
        number.append(num.rstrip())


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

link ='https://web.whatsapp.com'
driver.get(link)
time.sleep(15)


for num in number:
    link2 = f'https://web.whatsapp.com/send/?phone=91{num}&text={msg}'
    driver.get(link2)
    time.sleep(10)
    action = ActionChains(driver)
    action.send_keys(Keys.ENTER)
    action.perform()
    time.sleep(5)
    
time.sleep(100)


