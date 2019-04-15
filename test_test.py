from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from splinter.driver.webdriver import BaseWebDriver, WebDriverElement
from selenium import webdriver


options = webdriver.ChromeOptions()
#options.add_argument('--start-maximized')
#options.add_argument(r'C:\Users\TAASIBA2\AppData\Local\Google\Chrome\User Data\Profile 2')
options.add_argument(r"--user-data-dir=2")#C:\Users\TAASIBA2\Documents\Pypy\P7\User Data")
options.add_argument('--profile-directory=Profile 1')
#options.add_argument("--incognito")

driver = webdriver.Chrome(chrome_options=options)
#browser = driver
#browser = BaseWebDriver()
#browser.driver = Chrome(chrome_options=options)
driver.get('https://yahoo.com')

#url='http://127.0.0.1:5000'
#browser.visit(url)
#browser.fill('q', 'splinter - python acceptance testing for web applications')
val = "12" #browser.find_by_tag('h1')
print(val)