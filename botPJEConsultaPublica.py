from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import json 
import time
from selenium.webdriver.support import expected_conditions as EC

chromedriver_autoinstaller.install()

driver = webdriver.Chrome()
driver.get("https://pje.tjpb.jus.br/pje/ConsultaPublica/listView.seam")
driver.maximize_window()
time.sleep(5)


driver.find_element_by_css_selector('#fPP\:numProcesso-inputNumeroProcessoDecoration\:numProcesso-inputNumeroProcesso').send_keys("0818552-51.2021.8.15.0001")
time.sleep(5)
driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[2]/form/div[1]/div/div/div/div/div[8]/div/input').click()
time.sleep(5)
driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[2]/form/div[2]/div/table/tbody/tr/td[1]/a').click()
#time.sleep(3)

time.sleep(3)
print(driver.title)
time.sleep(5)
#script='let retorno  = (function(){return document.querySelector(`a[title="Ver Detalhes"]`)})();return retorno.attributes.onclick.value.split(",'")[1].split("')")[0];'
#processo = driver.execute_script(script)
#processo = driver.find_element_by_css_selector('#j_id141\\:processoTrfViewView\\:j_id147 > div > div.value.col-sm-12 > div')
processos = driver.find_elements_by_xpath ('//*[@id="j_id141:processoTrfViewView:j_id144_body"]/table/tbody/tr[1]/td[1]/text()')
time.sleep(5)
driver.find_element_by_css_selector('#fPP\:numProcesso-inputNumeroProcessoDecoration\:numProcesso-inputNumeroProcesso').send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
time.sleep(5)
driver.find_element_by_css_selector('#fPP\:numProcesso-inputNumeroProcessoDecoration\:numProcesso-inputNumeroProcesso').send_keys("0082292-23.2013.8.19.0021")
time.sleep(5)
driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[2]/form/div[1]/div/div/div/div/div[8]/div/input').click()
time.sleep(5)
driver.find_element_by_css_selector('#fPP\:numProcesso-inputNumeroProcessoDecoration\:numProcesso-inputNumeroProcesso').send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
time.sleep(5)
driver.find_element_by_css_selector('#fPP\:numProcesso-inputNumeroProcessoDecoration\:numProcesso-inputNumeroProcesso').send_keys("0821890-47.2021.8.15.2001")
time.sleep(5)
driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[2]/form/div[1]/div/div/div/div/div[8]/div/input').click()
time.sleep(5)
driver.find_element_by_css_selector('#fPP\:numProcesso-inputNumeroProcessoDecoration\:numProcesso-inputNumeroProcesso').send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
time.sleep(5)
driver.find_element_by_css_selector('#fPP\:numProcesso-inputNumeroProcessoDecoration\:numProcesso-inputNumeroProcesso').send_keys("0831715-98.2021.8.15.0001")
time.sleep(5)
driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[2]/form/div[1]/div/div/div/div/div[8]/div/input').click()
time.sleep(5)
driver.find_element_by_css_selector('#fPP\:numProcesso-inputNumeroProcessoDecoration\:numProcesso-inputNumeroProcesso').send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
time.sleep(5)
driver.find_element_by_css_selector('#fPP\:numProcesso-inputNumeroProcessoDecoration\:numProcesso-inputNumeroProcesso').send_keys("0825435-14.2021.8.15.0001")
time.sleep(5)
driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[2]/form/div[1]/div/div/div/div/div[8]/div/input').click()
time.sleep(5)
driver.find_element_by_css_selector('#fPP\:numProcesso-inputNumeroProcessoDecoration\:numProcesso-inputNumeroProcesso').send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
time.sleep(5)
driver.find_element_by_css_selector('#fPP\:numProcesso-inputNumeroProcessoDecoration\:numProcesso-inputNumeroProcesso').send_keys("1001086-83.2016.8.26.0048")
time.sleep(5)
driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[2]/form/div[1]/div/div/div/div/div[8]/div/input').click()
time.sleep(5)
driver.find_element_by_css_selector('#fPP\:numProcesso-inputNumeroProcessoDecoration\:numProcesso-inputNumeroProcesso').send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
time.sleep(5)
driver.find_element_by_css_selector('#fPP\:numProcesso-inputNumeroProcessoDecoration\:numProcesso-inputNumeroProcesso').send_keys("1007333-98.2018.8.26.0278")
time.sleep(5)
driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[2]/form/div[1]/div/div/div/div/div[8]/div/input').click()
time.sleep(5)
driver.find_element_by_css_selector('#fPP\:numProcesso-inputNumeroProcessoDecoration\:numProcesso-inputNumeroProcesso').send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
time.sleep(5)
driver.find_element_by_css_selector('#fPP\:numProcesso-inputNumeroProcessoDecoration\:numProcesso-inputNumeroProcesso').send_keys("0800538-70.2021.8.15.0081")
time.sleep(5)
driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[2]/form/div[1]/div/div/div/div/div[8]/div/input').click()
time.sleep(5)
driver.find_element_by_css_selector('#fPP\:numProcesso-inputNumeroProcessoDecoration\:numProcesso-inputNumeroProcesso').send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
time.sleep(5)
driver.find_element_by_css_selector('#fPP\:numProcesso-inputNumeroProcessoDecoration\:numProcesso-inputNumeroProcesso').send_keys("0002579-83.2021.8.17.8230")
time.sleep(5)
driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[2]/form/div[1]/div/div/div/div/div[8]/div/input').click()






time.sleep(10)
driver.close()