import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

start_time = time.time()
driver = webdriver.Firefox()
driver.get("https://mamenadoznat.ru/?page_id=18")

for i in range(0,2000):
    elem = driver.find_element_by_name("text")
    elem.send_keys("калинов родник")
    elem.send_keys(Keys.ENTER)
    time.sleep(1)
    elem = driver.find_element_by_name("text").clear()

assert "No results found." not in driver.page_source
driver.close()
print("--- %s seconds ---" % (time.time() - start_time))
