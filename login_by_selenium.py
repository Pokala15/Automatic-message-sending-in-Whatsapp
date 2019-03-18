from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By as b
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://web.whatsapp.com/")
print("scan the QR code")
time.sleep(20)
sear = driver.find_element(b.CLASS_NAME,"_2MSJr")
sear.send_keys("ENTER CHAT NAME")
sear.send_keys(u'\ue007')
# C IS NUMBER OF TIMES THE MSG TO BE SENT BY YOU
c=5
while c>0:
    text = driver.find_element(b.CLASS_NAME,"_2S1VP")
    text.send_keys("ENTER MSG TO SEND")
    text.send_keys(u'\ue007')
    c-=1
ext = driver.find_element(b.XPATH,"//*[@id='side']/header/div[2]/div/span/div[3]/div/span")
ext.click()
time.sleep(5)
ext1 = driver.find_element(b.XPATH,"//*[@id='side']/header/div[2]/div/span/div[3]/span/div/ul/li[6]/div")
ext1.click()
