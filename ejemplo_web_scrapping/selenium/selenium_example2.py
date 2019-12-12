from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://a.testaddressbook.com")

driver.find_element_by_id("sign-in").click()

email = driver.find_element_by_id("session_email")
email.send_keys("watir_example@example.com")

pwd = driver.find_element_by_id("session_password")
pwd.send_keys("password")

signin = driver.find_element_by_id("sign-in")
signin.click()

#element = driver.find_element_by_id("email")
#element.send_keys(user_name)
#element = driver.find_element_by_id("pass")
#element.send_keys(password)
#element.send_keys(Keys.RETURN)oi