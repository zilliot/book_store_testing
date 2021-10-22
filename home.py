import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
time.sleep(1)
driver.execute_script("window.scrollBy(0, 600);")
driver.find_element_by_xpath('//*[@id="text-22-sub_row_1-0-2-0-0"]/div/ul/li/a[1]/h3').click()
driver.find_element_by_xpath('//*[@id="product-160"]/div[3]/ul/li[2]/a').click()
driver.find_element_by_class_name("star-5").click()
my_comment = driver.find_element_by_id("comment")
time.sleep(1)
my_comment.send_keys("Nice book!")
name = driver.find_element_by_id("author").send_keys("Vasyliy")
email = driver.find_element_by_id("email").send_keys("Vasya1986@mail.ru")
driver.find_element_by_id("submit").click()
driver.quit()



