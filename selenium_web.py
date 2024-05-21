from selenium import webdriver 

class infow():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="C:/Users/srira/Anaconda3/Lib/site-packages/selenium/webdriver/chrome/chromedriver.exe") 
    
    def get_info(self, query):
        self.query = query
        self.driver.get("https://www.wikipedia.org/")
        search = self.driver.find_element_by_xpath('//*[id="searchInput"]')
        search.click()
        search.send_keys(query)
        enter = self.driver.find_element_by_xpath('//*[id="searchInput"]/fieldset/button')
        enter.click()
assist = infow()
assist.get_info("Tunisha Sharma") 
