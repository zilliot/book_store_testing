import time
from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
driver = webdriver.Chrome()
driver.maximize_window()
# driver.implicitly_wait(3)
driver.get("http://practice.automationtesting.in/")
time.sleep(1)
driver.find_element_by_xpath('//*[@id="menu-item-50"]/a').click()
registration = driver.find_element_by_id("reg_email")
registration.send_keys("Vasya1994@mail.ru")
time.sleep(2)
password = driver.find_element_by_id("reg_password")
password.send_keys("!Vfiftkfcfkj+86!")
# registration_button = WebDriverWait(driver, 5).until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, "#customer_login > div.u-column2.col-2 > form > p:nth-child(2) > div"))
# )
# registration_button.click()
driver.find_element_by_xpath('//*[@id="customer_login"]/div[2]/form/p[3]/input[3]').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="page-36"]/div/div[1]/nav/ul/li[6]/a').click()
driver.quit()

import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
time.sleep(1)
driver.find_element_by_xpath('//*[@id="menu-item-50"]/a').click()
driver.find_element_by_id("username").send_keys("Vasya1994@mail.ru")
driver.find_element_by_id("password").send_keys("!Vfiftkfcfkj+86!")
driver.find_element_by_xpath('//*[@id="customer_login"]/div[1]/form/p[3]/input[3]').click()
time.sleep(1)
logout = driver.find_element_by_xpath('//*[@id="page-36"]/div/div[1]/nav/ul/li[6]/a')
logout_get_text = logout.text
assert logout_get_text == "Logout"
print("Элемент 'Logout' присутствует на странице")
driver.quit()