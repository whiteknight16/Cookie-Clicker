from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def cookie_click():
    buy_time=time.time()+5.0
    while (time.time()<buy_time):
        cookie=driver.find_element(By.CSS_SELECTOR,"#bigCookie")
        cookie.click()

chrome_driver_path="C:/Development/chromedriver.exe"
driver=webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://orteil.dashnet.org/cookieclicker/")

time.sleep(7)
language_click=driver.find_element(By.CSS_SELECTOR,"#langSelect-EN")
language_click.click()

time.sleep(7)
end_time=time.time()+30.0
while (time.time()<end_time):
    cookie_click()
    least_item_price=int(driver.find_element(By.CSS_SELECTOR,"#productPrice0").text)
    current_money=(driver.find_element(By.CSS_SELECTOR,"#cookies").text)
    current_money=(current_money.split(" "))
    current_money=int(current_money[0])
    while(current_money>least_item_price):
        purchase_list=driver.find_elements(By.CSS_SELECTOR,"#products .unlocked")
        for i in range(len(purchase_list)):
            least_item_price=int(driver.find_element(By.CSS_SELECTOR,"#productPrice0").text)
            last_item_price=int(driver.find_element(By.CSS_SELECTOR,f"#productPrice{len(purchase_list)-1}").text)
            if int(current_money)>last_item_price:
                purchase_list[-1].click()
                current_money-=last_item_price

driver.quit()