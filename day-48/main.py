from selenium import webdriver

drive_path = "C:\chromedriver.exe"
driver = webdriver.Chrome(executable_path=drive_path)

driver.get("https://en.wikipedia.org/wiki/Main_Page")
article_count = driver.find_element("css selector", "#articlecount a")
print(article_count.text)

driver.close()
