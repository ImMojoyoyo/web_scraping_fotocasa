#!python v3.9.12
#scraping.py -  scraping web to idealista website.

# SELENIUM
from selenium import webdriver 
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


# WEBDRIVER_MANGER
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType




class ScrapingWeb:
    
    def __int__(self):
        self.url = "https://www.google.es"
   
    
    def start_scraping(self):
       #TODO : TRY/EXCEPT/FINALLY
       print('Start the scraping process to: ')
       
       # TODO: PONER COMO INCOGNITO EL NAVEGADOR
       #chrome_options = webdriver.ChromeOptions().add_argument("--incognito")
       
       options = webdriver.ChromeOptions()
       options.add_argument("start-maximized")
       options.add_argument("--no-sandbox")
       options.add_argument("--disable-gpu")
       options.add_argument("--disable-extensions")
       #chrome to stay open
       options.add_experimental_option("detach", True)
       
       
       driver = webdriver.Chrome((ChromeDriverManager().install()),options=options)
       driver.get('https://www.fotocasa.com')
       
       # Accept cookies.
       WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="App"]/div[2]/div/div/div/footer/div/button[2]'))).click() ## This is method that wait until appears the tag that we want in the browser.
       
       # Input button.
       input_element = driver.find_element(by=By.XPATH, value='//*[@id="App"]/div[1]/main/section/div[2]/div/div/div/div/div[2]/div[2]/form/div/div/div/div/div/input')
       input_element.send_keys("Onil")
       
       # Search Button.
       driver.find_element(by=By.XPATH, value='//*[@id="App"]/div[1]/main/section/div[2]/div/div/div/div/div[2]/div[2]/form/button').click()
       
       # Wait until 'section' tag appear in the browser.
       WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="App"]/div[1]/div[2]/main/div/div[2]/section')))
       
       
       # TODO: Que haga esto por todas las paginas que haya.
       # Scroll screen down
       htmlElemnt = driver.find_element(by=By.TAG_NAME, value='html')   
       htmlElemnt.send_keys(Keys.END)
       
       time.sleep(5) #  
       
       # Articles of flats.
       parent_article = driver.find_elements(by=By.XPATH, value='//section/article') 
       print(len(parent_article))
       
       time.sleep(2)

       
       # For each article.
       all_flats = []
       
       for i in range(len(parent_article)):
            time.sleep(3)
            driver.find_element(by=By.XPATH, value=f"//section/article{[i+1]}").click() # Click for each article.
            
            time.sleep(2)
            
            
            flat_att = {
                    'title' : f"{driver.find_element(by=By.CLASS_NAME, value='re-DetailHeader-propertyTitle').text}",
                    'price' : f"{driver.find_element(by=By.CLASS_NAME, value='re-DetailHeader-price').text}",
                    #'type' : f"{driver.find_element(by=By.CLASS_NAME, value='re-DetailFeaturesList-featureValue').text}",
                    #'location' : f"{driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[1]/main/div[4]/div[1]/div/section[3]/div/div/div[1]/h2').text}",
                    #'bethroom' : f"{driver.find_element(by=By.XPATH, value='//section[1]/div/div[1]/div[3]/ul/li[1]/span[2]/span').text}",
                    #'bathroom' : f"{driver.find_element(by=By.XPATH, value='//section[1]/div/div[1]/div[3]/ul/li[2]/span[2]/span').text}",
                    #'real_meters' : f"{driver.find_element(by=By.XPATH, value='//section[1]/div/div[1]/div[3]/ul/li[3]/span[2]/span').text}",
                }
            #print(flat_att)
            
            # Append flats in a list.
            all_flats.append(flat_att)
            time.sleep(3)
            # Back button page.
            driver.find_element(by=By.XPATH, value='//*[@id="App"]/div[1]/main/div[1]/div[1]/a').click()
            time.sleep(2)
            
            
       print(all_flats)
       # QUIT BROWSER
       driver.quit()