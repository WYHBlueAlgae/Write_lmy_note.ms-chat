from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

chrome_options=Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

def invade():
    print("开始攻击")
    global t
    browser1 = webdriver.Chrome(chrome_options=chrome_options)
    browser1.get("https://note.ms/chatbf")
    textarea1 = browser1.find_element_by_tag_name("textarea")
    text = textarea1.text
    browser1.close()
    browser2 = webdriver.Chrome(chrome_options=chrome_options)
    browser2.get("https://note.ms/chat")
    textarea = browser2.find_element_by_tag_name("textarea")
    textarea.click()
    time.sleep(0.5)
    textarea.clear()
    textarea.send_keys(text)
    time.sleep(0.5)
    browser2.refresh()
    browser2.close()
    print("攻击完毕,已夺回聊天室")


while True:
    browser =webdriver.Chrome(chrome_options=chrome_options)
    browser.get("https://note.ms/chat")
    textarea = browser.find_element_by_tag_name("textarea")
    text = textarea.text
    browser.close()
    if "lmy" not in text:
        invade()
    time.sleep(300)