from cgitb import text
from unicodedata import name
from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import json 
import time
from selenium.webdriver.support import expected_conditions as EC

chromedriver_autoinstaller.install()

driver = webdriver.Chrome()
driver.get("https://cna.oab.org.br/")
driver.maximize_window()
time.sleep(5)

driver.find_element_by_css_selector('#txtName').send_keys("NELSON WILIANS")
time.sleep(5)
driver.find_element_by_css_selector('#txtInsc').send_keys("PB-26878")
time.sleep(5)
driver.find_element_by_xpath('/html/body/div[2]/div[1]/form/div/div/div[6]/button').click()
time.sleep(10)
element = driver.find_element_by_tag_name('#textResult')
print(element.text)
time.sleep(5)
driver.find_element_by_css_selector('#txtInsc').send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
time.sleep(5)
driver.find_element_by_css_selector('#txtInsc').send_keys("SP-128341")
time.sleep(5)
driver.find_element_by_xpath('/html/body/div[2]/div[1]/form/div/div/div[6]/button').click()
time.sleep(10)
nome = driver.find_element_by_class_name('rowName')
print(nome.text)
tipo = driver.find_element_by_class_name('rowTipoInsc')
print(tipo.text)
insc= driver.find_element_by_class_name('rowInsc')
print(insc.text)
uf = driver.find_element_by_class_name('rowUf')
print(uf.text)
time.sleep(5)
driver.find_element_by_xpath('//*[@id="divResult"]/div[1]').click()
time.sleep(3)
sociedade = driver.find_element_by_class_name('trSoci')
print(sociedade.text)
time.sleep(5)
driver.find_element_by_xpath('/html/body/div[6]/div/button')
time.sleep(10)
driver.close()