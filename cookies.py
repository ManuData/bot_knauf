from selenium import webdriver


drive = webdriver.Chrome(executable_path='./web_driver_chrome/chromedriver')

drive.get('https://www.knauf.de')

