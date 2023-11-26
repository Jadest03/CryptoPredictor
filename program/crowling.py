# crowling.py
import os
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from io import StringIO
from PyQt5.QtWidgets import QApplication, QInputDialog
from PyQt5.QtWidgets import QInputDialog, QLineEdit

def get_coin_name():
    app = QApplication([])
    coin_name, okPressed = QInputDialog.getText(None, "Coin Name", "Enter the coin name:", QLineEdit.Normal, "")
    if okPressed and coin_name.strip():
        return coin_name.strip()
    else:
        return None

def data_crowling():
    input_value = get_coin_name()

    if input_value is None:
        print("Coin name not provided. Exiting.")
        return

    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    browser = webdriver.Chrome(options=chrome_options)

    url = "https://upbit.com/exchange?code=CRIX.UPBIT."
    browser.get(url)

    if input_value != '비트코인':
        search_area = browser.find_element(By.XPATH, '//*[@id="UpbitLayout"]/div[3]/div/section[2]/article/span[1]/div[1]/input').send_keys(input_value)
        table = browser.find_element(By.XPATH, '//*[@id="UpbitLayout"]/div[3]/div/section[2]/article/span[2]/div/div/div[1]/table')
        item_select = table.find_elements(By.TAG_NAME, 'strong')

        for item in item_select:
            if item.text == input_value:
                parent = item.find_element(By.XPATH, "..")
                grand_parent = parent.find_element(By.XPATH, "..")
                coin = grand_parent.find_element(By.TAG_NAME, "em")
                name, country = coin.text.split("/")
                break

        browser.get(url + str(country) + '-' + str(name))

    time.sleep(3)

    df = pd.read_html(StringIO(browser.page_source))[4]
    df.dropna(axis='columns', how='all', inplace=True)

    file_name = 'coin.csv'
    if os.path.exists(file_name):  # 파일이 있다면 헤더 제외
        df[3].to_csv(file_name, encoding='utf-8-sig', index=False, mode='w', header=['Percentage'])
    else:  # 파일이 없다면 헤더 포함
        df[3].to_csv(file_name, encoding='utf-8-sig', index=False, header=['Percentage'])

    print("크롤링 시작")
    with open(file_name, 'a') as f:
        while True:
            price_rate = browser.find_element(By.XPATH, '//*[@id="UpbitLayout"]/div[3]/div/section[1]/article[1]/div/span[1]/div[1]/span[2]/strong[1]').text
            f.write(price_rate+"\n")
            f.flush()   
            time.sleep(1)
