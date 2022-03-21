import os

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='J:\Downloads\chromedriver.exe')
plantumlURL = 'http://www.plantuml.com/plantuml/uml/LP1B3iCW30NtFWNAghr3LUKcaGj4GG8Z6MVHsxS81yBRpVW3ybe4MSuK0Jz56AqOpSMZO2EMOimoYmMGA0jAoAIJdS46jj6RdiRmU9efJM_bo2pRdZc1lZKwAeCBc3AvRfNXzPxtgRylz2H1lgEbyL-VwJvP6GA9vntjzV7Ei7fozLW_'

driver.get(plantumlURL)

plantuml_code_box = driver.find_element(By.ID, 'inflated')
plantuml_submit_button = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/button[1]')
plantuml_code_box.clear()
plantuml_code_box.send_keys('@startuml\n\n')

f = open("sourceCode.txt", "r")
# for lines in f:
plantuml_code_box.send_keys(f.readlines())
plantuml_submit_button.click()

plantuml_diagram_image = driver.find_element(By.XPATH, '//*[@id="diagram"]/img')

with open('diagram.png', 'wb') as file:
    file.write(plantuml_diagram_image.screenshot_as_png)

driver.close()

f.close()

os.remove("sourceCode.txt")
