from selenium import webdriver
import time


driver = webdriver.Firefox()

driver.get('https://www.knauf.de')

#print(drive.get_cookies())
time.sleep(3)
test = driver.execute_script('return dataLayer')
print(test)


#test = drive.find_element(By.ID, "accept-recommended-btn-handler")
#test = drive.find_element(By.CLASS_NAME, "button-theme")
#test.click()
