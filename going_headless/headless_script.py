import os  
from selenium import webdriver  
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.chrome.options import Options  

chrome_options = Options()  
chrome_options.add_argument("--headless")  
# chrome_options.binary_location = '/Applications/Google\ Chrome\ Canary.app/Contents/MacOS/Google\ Chrome\ Canary' 

options = webdriver.ChromeOptions()
options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
# options.binary_location = '/Applications/Google\ Chrome\ Canary.app/Contents/MacOS/Google\ Chrome\ Canary'
chrome_driver_binary = "/Users/rodrialejandro/git/headlessChrome/going_headless/chromedriver"
driver = webdriver.Chrome(chrome_driver_binary, chrome_options=options)
# driver = webdriver.Chrome(executable_path=os.path.abspath("chromedriver"), chrome_options=chrome_options)
driver.get("http://www.youtube.com")  

# magnifying_glass = driver.find_element_by_id("js-open-icon")  
# if magnifying_glass.is_displayed():  
#   magnifying_glass.click()  
# else:  
#   menu_button = driver.find_element_by_css_selector(".menu-trigger.local")  
#   menu_button.click() 

search_field = driver.find_element_by_id("search")  
# search_field.clear()  
search_field.send_keys("brooklynn 99 Captain holt hot damn")  
search_field.send_keys(Keys.RETURN) 
driver.implicitly_wait(2)
browser = driver.find_element_by_xpath('//a[@title="brooklynn 99 Captain holt hot damn"]') 
browser.click()
assert "brooklyn 99 holt hot damn" in driver.page_source   
# driver.close()  