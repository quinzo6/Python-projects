import pyautogui
import keyboard
from selenium import webdriver
import time

path = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(path)

driver.get('https://twitter.com/login')

twiter_user = driver.find_element_by_css_selector("#react-root > div > div > div.css-1dbjc4n.r-13qz1uu.r-417010 > main > div > div > div.css-1dbjc4n.r-13qz1uu > form > div > div:nth-child(6) > label > div > div.css-1dbjc4n.r-18u37iz.r-16y2uox.r-1wbh5a2.r-1udh08x > div > input")
twiter_pass = driver.find_element_by_css_selector('#react-root > div > div > div.css-1dbjc4n.r-13qz1uu.r-417010 > main > div > div > div.css-1dbjc4n.r-13qz1uu > form > div > div:nth-child(7) > label > div > div.css-1dbjc4n.r-18u37iz.r-16y2uox.r-1wbh5a2.r-1udh08x > div > input')
twiter_username = input('Please provide a Username, email, or phone number. ')
twiter_password = input('Please provide a password for this account. ')
login = driver.find_element_by_css_selector('#react-root > div > div > div.css-1dbjc4n.r-13qz1uu.r-417010 > main > div > div > div.css-1dbjc4n.r-13qz1uu > form > div > div:nth-child(8) > div > div')

if pyautogui.locateOnScreen(r"images\chrome.png", confidence=0.5) != None:
    pyautogui.click(1544, 1057)

time.sleep(1)

twiter_user.send_keys(twiter_username)

time.sleep(1)

twiter_pass.send_keys(twiter_password)

login.click()

if pyautogui.locateOnScreen(r"images\error.png", confidence=0.29) != None:
    print('There was an error logging in!')
    print('Please Re-run the script.')
    exit()
else:
    print('You have logged in!')

time.sleep(2)

tweet_question = input('Would you like to send a tweet? ')

if tweet_question == 'yes':
    print('Alright, please wait a few seconds')
else:
    print('Ok, have a good day!') 
    exit()

time.sleep(2)


start_tweet = driver.find_element_by_css_selector('#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > main > div > div > div > div.css-1dbjc4n.r-yfoy6g.r-18bvks7.r-1ljd8xs.r-13l2t4g.r-1phboty.r-1jgb5lz.r-11wrixw.r-61z16t.r-1ye8kvj.r-13qz1uu.r-184en5c > div > div.css-1dbjc4n.r-yfoy6g.r-184en5c > div > div.css-1dbjc4n.r-yfoy6g.r-atwnbb > div:nth-child(1) > div > div > div > div.css-1dbjc4n.r-1iusvr4.r-16y2uox.r-1777fci.r-glunga.r-1bylmt5.r-13tjlyg.r-7qyjyx.r-1ftll1t > div.css-1dbjc4n.r-184en5c > div > div > div > div > div > div > div > div > div > div.css-901oao.r-jwli3a.r-6koalj.r-16y2uox.r-1qd0xha.r-1b6yd1w.r-16dba41.r-ad9z0x.r-bcqeeo.r-qvutc0 > div > div > div > div.DraftEditor-editorContainer > div > div > div > div')
start_tweet.click()

time.sleep(2)

tweet = input('Please type what you want to tweet: ')

start_tweet.send_keys(tweet)

tweet_send = driver.find_element_by_css_selector('#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > main > div > div > div > div.css-1dbjc4n.r-yfoy6g.r-18bvks7.r-1ljd8xs.r-13l2t4g.r-1phboty.r-1jgb5lz.r-11wrixw.r-61z16t.r-1ye8kvj.r-13qz1uu.r-184en5c > div > div.css-1dbjc4n.r-yfoy6g.r-184en5c > div > div.css-1dbjc4n.r-yfoy6g.r-atwnbb > div:nth-child(1) > div > div > div > div.css-1dbjc4n.r-1iusvr4.r-16y2uox.r-1777fci.r-glunga.r-1bylmt5.r-13tjlyg.r-7qyjyx.r-1ftll1t > div:nth-child(4) > div > div > div:nth-child(2) > div > div > span > span')
tweet_send.click()

print('Success! Your tweet was sent!')