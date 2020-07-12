from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pyperclip

options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:\\Users\\akjas\\AppData\\Local\\Google\\Chrome\\User Data\\wtsp")
driver = webdriver.Chrome(options=options)
driver.maximize_window()

driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 300)

with open('groups.txt', 'r', encoding='utf8') as f:
    groups = [group.strip() for group in f.readlines()]

with open('msg.txt', 'r', encoding='utf8') as f:
    msg = f.read()
    print(msg)

for i in groups:
    search_xpath = '//div[@contenteditable="true"][@data-tab="3"]'
    search_box = wait.until(EC.presence_of_element_located((By.XPATH, search_xpath)))
    pyperclip.copy(i)
    search_box.clear()
    search_box.send_keys(Keys.CONTROL + "v")
    time.sleep(2)

    x_arg = "//span[@title='" + i + "']"
    group_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
    group_title.click()

    inp_xpath = '//div[@contenteditable="true"][@data-tab="1"]'
    input_box = wait.until(EC.presence_of_element_located((By.XPATH, inp_xpath)))

    pyperclip.copy(msg)
    input_box.clear()
    input_box.send_keys(Keys.CONTROL + "v")
    input_box.send_keys(Keys.ENTER)
    time.sleep(3)
