from selenium import webdriver 

class info():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="C://Users//srira//Downloads//chromedriver-win32//chromedriver-win32//chromedriver.exe")
    
    def get_info(self, query):
        self.query = query
        self.driver.get("https://www.wikipedia.org/")
        search = self.driver.find_element_by_xpath(By.XPATH,'//*[@id="searchInput"]')
        search.click()
        search.send_keys(query)
        enter = self.driver.find_element_by_xpath(By.XPATH,'//*[@id="search-form"]/fieldset/button')
        enter.click()
