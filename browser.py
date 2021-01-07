from selenium import webdriver

# from webdriver_manager.chrome import ChromeDriverManager
# driver = webdriver.Chrome(ChromeDriverManager().install())
# browser = webdriver.Chrome(executable_path=r"C:\Users\RCenk\Desktop\Insta\chromedriver_win32_4\chromedriver.exe")
# driver.get('http://google.com/')

import time
import userInfo as ui

class Browser:
    def __init__(self, link):               
        self.link = link                    
        self.browser = webdriver.Chrome()   
        Browser.goInstagram(self)           

    def goInstagram(self):                  
        self.browser.get(self.link)         
        time.sleep(2)                      
        Browser.login(self)                 
        Browser.getFollowers(self)          

    def getFollowers(self):
        self.browser.find_element_by_xpath("//*[@id=\"react-root\"]/section/main/div/header/section/ul/li[2]/a").click()
        time.sleep(4)

        followers = self.browser.find_elements_by_css_selector(".FPmhX.notranslate._0imsa")
        counter = 0
        print("\n", "******************* FOLLOWERS *******************", "\n")
        for follower in followers:
            counter += 1
            print(str(counter) + " - " + follower.text)

    def login(self):
        username = self.browser.find_element_by_name("username") 
        password = self.browser.find_element_by_name("password")  

        username.send_keys(ui.username)                           
        password.send_keys(ui.password)                           

        loginBtn = self.browser.find_element_by_css_selector("#loginForm > div > div:nth-child(3) > button > div")
        loginBtn.click()
        time.sleep(5)

        self.browser.get(self.link + "/" + ui.username)
        time.sleep(3)