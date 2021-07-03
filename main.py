import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.proxy import Proxy, ProxyType
from proxy import get_proxies,cycle

#Proxy Getting
proxies = get_proxies()
proxy_pool = cycle(proxies)

for i in range(10):
    start_time = time.time()
    proxy = next(proxy_pool)

    try:
        prox = Proxy({
            'proxyType': ProxyType.MANUAL,
            'httpProxy': proxy,
            'httpsProxy': proxy,
            'ftpProxy': proxy,
            'sslProxy': proxy,
            'noProxy': ''
        })
        driver = webdriver.Firefox(proxy=prox)
        print(prox.httpProxy)
        driver.get("https://mamenadoznat.ru/?page_id=18")
        elem = driver.find_element_by_name("text")
        elem.send_keys("калинов родник")
        elem.send_keys(Keys.ENTER)
        time.sleep(2)
        elem = driver.find_element_by_name("text").clear()
        for handle in driver.window_handles:
            driver.switch_to.window(handle)
            driver.close()
        print("--- %s seconds ---" % (time.time() - start_time))
    except:
        print("Skipping. Connection error")


# # profile = webdriver.FirefoxProfile()
# # profile.set_preference("general.useragent.override", "New user agent")
#
# driver = webdriver.Firefox(firefox_profile=profile)
