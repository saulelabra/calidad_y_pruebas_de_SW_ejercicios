#Saúl Enrique Labra Cruz A01020725

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 

browser = webdriver.Firefox(executable_path=r'./geckodriver')
browser.get("https://a.testaddressbook.com")

#Login
elem = browser.find_element_by_id("sign-in")
elem.click()
elem = browser.find_element_by_id("session_email")
elem.send_keys("watir_example@example.com")
elem = browser.find_element_by_id("session_password")
elem.send_keys("password")
btn = browser.find_element_by_name('commit').click()

#Form
elem = browser.find_element_by_link_text("Addresses")
elem.click()
browser.get('https://a.testaddressbook.com/addresses/new')
browser.find_element_by_id('address_first_name').send_keys("Saúl")
browser.find_element_by_id('address_last_name').send_keys("Labra")
browser.find_element_by_id('address_street_address').send_keys("Carlos Lazo")
browser.find_element_by_id('address_secondary_address').send_keys("Av. de las Palmas")
browser.find_element_by_id('address_city').send_keys("CDMX")
browser.find_element_by_xpath("//select[@name='address[state]']/option[text()='New York']").click()
browser.find_element_by_id('address_zip_code').send_keys("12345")
elem = browser.find_element_by_id('address_country_us')
elem.send_keys("us")
elem.click()
elem = browser.find_element_by_id("address_birthday")
elem.clear()
elem.send_keys('2019-11-15')
browser.execute_script("document.getElementById('address_color').value = '#f6ff33';")
browser.find_element_by_id('address_age').send_keys(21)
browser.find_element_by_id('address_website').send_keys("https://github.com/saulelabra")
browser.find_element_by_css_selector('input[type=file]').send_keys('/home/saul/Desktop/image.jpeg')
browser.find_element_by_id('address_phone').send_keys("55123456")
elem = browser.find_element_by_id('address_interest_dance')
elem.click()
browser.find_element_by_id('address_note').send_keys("I made it")
browser.find_element_by_css_selector('input[type=submit]').click()
time.sleep(7)
browser.close()
