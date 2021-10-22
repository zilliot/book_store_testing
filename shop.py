# import time
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("http://practice.automationtesting.in/")
# time.sleep(1)
# driver.find_element_by_xpath('//*[@id="menu-item-50"]/a').click()
# driver.find_element_by_id("username").send_keys("Vasya1994@mail.ru")
# driver.find_element_by_id("password").send_keys("!Vfiftkfcfkj+86!")
# driver.find_element_by_xpath('//*[@id="customer_login"]/div[1]/form/p[3]/input[3]').click()
# time.sleep(1)
# driver.find_element_by_id("menu-item-40").click()
# driver.find_element_by_xpath('//*[@id="content"]/ul/li[3]/a[1]/h3').click()
# title = driver.find_element_by_xpath('//*[@id="product-181"]/div[2]/h1')
# title_get_text = title.text
# assert title_get_text == "HTML5 Forms"
# print("Верно, заголовок книги называется HTML5 Forms")
# driver.quit()

############## Кол-во товаров ###########
# import time
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("http://practice.automationtesting.in/")
# time.sleep(1)
# driver.find_element_by_xpath('//*[@id="menu-item-50"]/a').click()
# driver.find_element_by_id("username").send_keys("Vasya1994@mail.ru")
# driver.find_element_by_id("password").send_keys("!Vfiftkfcfkj+86!")
# driver.find_element_by_xpath('//*[@id="customer_login"]/div[1]/form/p[3]/input[3]').click()
# time.sleep(1)
# driver.find_element_by_id("menu-item-40").click()
# driver.find_element_by_xpath('//*[@id="woocommerce_product_categories-2"]/ul/li[2]/a').click()
# items_count = driver.find_elements_by_class_name("woocommerce-LoopProduct-link")
# if len(items_count) == 3:
#     print("В корзине " + str(len(items_count)) + " товара")
# else:
#     print("В корзине " + str(len(items_count)) + " товара")
# driver.quit()

############## Сортировка товаров ###########
# import time
# from selenium import webdriver
# from selenium.webdriver.support.select import Select
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("http://practice.automationtesting.in/")
# time.sleep(1)
# driver.find_element_by_xpath('//*[@id="menu-item-50"]/a').click()
# driver.find_element_by_id("username").send_keys("Vasya1994@mail.ru")
# driver.find_element_by_id("password").send_keys("!Vfiftkfcfkj+86!")
# driver.find_element_by_xpath('//*[@id="customer_login"]/div[1]/form/p[3]/input[3]').click()
# time.sleep(1)
# driver.find_element_by_id("menu-item-40").click()
# sorting = driver.find_element_by_class_name("orderby").get_attribute("value")
# if sorting == "menu_order":
#     print("Выбрана сортировка по: Default")
# else:
#     print("Выбрана сортировка по: " + str(sorting))
#
# sorting_rating = driver.find_element_by_class_name("orderby")
# sorting_rating_changed = Select(sorting_rating).select_by_value("price-desc")
# time.sleep(1)
# sorting = driver.find_element_by_class_name("orderby").get_attribute("value")
# if sorting == "price-desc":
#     print("Выбрана сортировка Sort by price: high to low")
# elif sorting == "price":
#     print("Выбрана сортировка Sort by price: low to high")
# elif sorting == "popularity":
#     print("Выбрана сортировка Sort by popularity")
# elif sorting == "rating":
#     print("Выбрана сортировка Sort by average rating")
# elif sorting == "menu_order":
#     print("Выбрана сортировка по: Default sorting")
# else:
#     print("Выбрана сортировка по: Sort by newness")
# driver.quit()

############## Отображение, скидка ###########

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
#
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("http://practice.automationtesting.in/")
# time.sleep(1)
# driver.find_element_by_xpath('//*[@id="menu-item-50"]/a').click()
# driver.find_element_by_id("username").send_keys("Vasya1994@mail.ru")
# driver.find_element_by_id("password").send_keys("!Vfiftkfcfkj+86!")
# driver.find_element_by_xpath('//*[@id="customer_login"]/div[1]/form/p[3]/input[3]').click()
# time.sleep(1)
# driver.find_element_by_id("menu-item-40").click()
# driver.find_element_by_xpath('//*[@id="content"]/ul/li[1]/a[1]/h3').click()
# old_price = driver.find_element_by_xpath('//*[@id="product-169"]/div[2]/div[1]/p/del/span')
# # rupee = u'\u20B9'
# old_price_get_text = old_price.text
# assert old_price_get_text == "₹600.00"
# print("Старая цена книги " + old_price_get_text)
# new_price = driver.find_element_by_xpath('//*[@id="product-169"]/div[2]/div[1]/p/ins/span')
# new_price_get_text = new_price.text
# assert new_price_get_text == "₹450.00"
# print("Цена книги со скидкой составляет " + new_price_get_text)
# time.sleep(1)
# # url_paint = driver.find_element_by_xpath('//*[@id="product-169"]/div[1]/a/img')
# # url_paint_get_text = url_paint.get_attribute("src")
# # print(url_paint_get_text)
# #
# # wait = WebDriverWait(driver, 10)
# # open_window = wait.until(
# #     EC.url_to_be("url_paint")
# # )
#
# # open_paint = driver.find_element_by_id("fullResImage")
# # wait = WebDriverWait(driver, 5)
# # driver.find_element_by_class_name("images").click()
#
# open_paint_minisize = WebDriverWait(driver, 5).until(
#     EC.element_to_be_clickable((By.CLASS_NAME, "images"))
# )
# open_paint_minisize.click()
#
# close_paint_minisize = WebDriverWait(driver, 7).until(
#     EC.element_to_be_clickable((By.CLASS_NAME, "pp_close"))
# )
# close_paint_minisize.click()
# driver.quit()


###################### ПРОВЕРКА ЦЕНЫ В КОРЗИНЕ ####################
# import time
# from selenium import webdriver
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("http://practice.automationtesting.in/")
# time.sleep(1)
# driver.find_element_by_xpath('//*[@id="menu-item-40"]/a').click()
# driver.find_element_by_xpath('//*[@id="content"]/ul/li[4]/a[2]').click()
# time.sleep(1)
# item_basket = driver.find_element_by_xpath('//*[@id="wpmenucartli"]/a/span[1]')
# item_basket_get_text = item_basket.text
# assert "1 Item" in item_basket_get_text
# print("В корзине " + item_basket_get_text)
#
# item_price = driver.find_element_by_xpath('//*[@id="wpmenucartli"]/a/span[2]')
# item_price_get_text = item_price.text
# assert "₹180.00" in item_price_get_text
# print("Цена товара составляет " + item_price_get_text)
#
# driver.find_element_by_class_name("wpmenucart-contents").click()
# subtotal_price = WebDriverWait(driver, 5).until(
#     EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#page-34 > div > div.woocommerce > div > div > table > tbody > tr.cart-subtotal > td > span"), "₹180.00")
# )
#
# total_price = WebDriverWait(driver, 5).until(
#     EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#page-34 > div > div.woocommerce > div > div > table > tbody > tr.order-total > td > strong > span"), "")
# )
#
# # driver.find_element_by_class_name("wpmenucart-contents").click()
# # subtotal_price = WebDriverWait(driver, 5).until(
# #     EC.text_to_be_present_in_element_value((By.XPATH, '//*[@id="page-34"]/div/div[1]/div/div/table/tbody/tr[1]/td/span'), "₹180.00")
# # )
#
# driver.quit()

###################### РАБОТА В КОРЗИНЕ ####################
# import time
# from selenium import webdriver
#
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("http://practice.automationtesting.in/")
# time.sleep(2)
#
# driver.find_element_by_xpath('//*[@id="menu-item-40"]/a').click()
# time.sleep(2)
# driver.execute_script("window.scrollBy(0, 300);")
# driver.find_element_by_xpath('//*[@id="content"]/ul/li[4]/a[2]').click()
# time.sleep(2)
# driver.find_element_by_xpath('//*[@id="content"]/ul/li[5]/a[2]').click()
# time.sleep(2)
# driver.find_element_by_class_name("wpmenucart-contents").click()
# time.sleep(2)
# driver.find_element_by_class_name("remove").click()
# time.sleep(3)
# driver.find_element_by_xpath('//*[@id="page-34"]/div/div[1]/div[1]/a').click()
#
# quantity_text = driver.find_element_by_xpath('//*[@id="page-34"]/div/div[1]/form/table/tbody/tr[1]/td[5]/div/input')
# quantity_text.clear()
# quantity_text.send_keys(3)
#
# # выполняем update корзины
# driver.find_element_by_xpath('//*[@id="page-34"]/div/div[1]/form/table/tbody/tr[3]/td/input[1]').click()
# # выбираем заново ячейку
# time.sleep(3)
# quantity = driver.find_element_by_css_selector("#page-34 > div > div.woocommerce > form > table > tbody > tr:nth-child(1) > td.product-quantity > div > input")
# quantity_get_text = quantity.get_attribute("value")
# print(quantity_get_text)
#
# assert quantity_get_text == "3"
# print("Количество товара равно " + quantity_get_text)
# time.sleep(3)
# driver.find_element_by_css_selector("#page-34 > div > div.woocommerce > form > table > tbody > tr:nth-child(3) > td > div > input.button").click()
# time.sleep(3)
# message_error = driver.find_element_by_css_selector("#page-34 > div > div.woocommerce > ul > li")
# message_error_get_text = message_error.text
#
# # проверяем фразу про купоны
# assert "Please enter a coupon code." in message_error_get_text
# print('Фраза "Please enter a coupon code." присутствует на странице')
#
# driver.quit()

###################### ПОКУПКА ТОВАРА ####################
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
time.sleep(2)

driver.find_element_by_xpath('//*[@id="menu-item-40"]/a').click()
time.sleep(2)
driver.execute_script("window.scrollBy(0, 300);")

driver.find_element_by_xpath('//*[@id="content"]/ul/li[4]/a[2]').click()
time.sleep(2)
driver.find_element_by_class_name("wpmenucart-contents").click()
time.sleep(2)
checkout = WebDriverWait(driver, 7).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "checkout-button"))
)
checkout.click()
# Вводим данные в обязательные поля
first_name = WebDriverWait(driver, 7).until(
    EC.element_to_be_clickable((By.ID, "billing_first_name"))
)
first_name.send_keys("Vasya1986")
last_name = driver.find_element_by_id("billing_last_name")
last_name.send_keys("Auto-man")
driver.find_element_by_id("billing_email").send_keys("Vasya1994@mail.ru")
driver.find_element_by_id("billing_phone").send_keys("7954658877")
driver.find_element_by_xpath('//*[@id="s2id_billing_country"]/a/span[2]/b').click()
time.sleep(5)
country = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "select2-input"))
)
country.click()
country.send_keys("Spain")
driver.find_element_by_class_name("select2-result-label").click()
time.sleep(2)
adress = driver.find_element_by_id("billing_address_1")
adress.send_keys("Nevskiy prospect, 68")
postcode = driver.find_element_by_xpath('//*[@id="billing_postcode"]')
postcode.send_keys("08001")
city = driver.find_element_by_id("billing_city")
city.send_keys("Barcelona")

driver.find_element_by_xpath('//*[@id="s2id_billing_state"]/a/span[2]/b').click()
province = driver.find_element_by_xpath('//*[@id="s2id_autogen360_search"]')
province.send_keys("Palencia")
driver.find_element_by_class_name("select2-match").click()
time.sleep(2)
# Выбор чекбокса
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(2)
driver.find_element_by_id("payment_method_cheque").click()
driver.find_element_by_id("place_order").click()

text = WebDriverWait(driver, 7).until(
    EC.text_to_be_present_in_element((By.CLASS_NAME, "woocommerce-thankyou-order-received"), "Thank you. Your order has been received.")
)
text_payment = WebDriverWait(driver, 7).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#page-35 > div > div.woocommerce > ul > li.method > strong"), "Check Payments")
)

print("Всё работет хорошо")
time.sleep(5)
driver.quit()
#page-35 > div > div.woocommerce > ul > li.method > strong










