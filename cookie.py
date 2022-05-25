from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

COOKIE_URL = "http://orteil.dashnet.org/experiments/cookie/"

chrome_driver_path = Service("C:\Development\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_driver_path)

driver.get(COOKIE_URL)
# ----------------------TIME INTERVALS-------------------#
time_out = time.time() + 5
game_time_over = time.time() + (60 * 5)

# -----------------------COOKIE---------------------------#
cookie = driver.find_element(By.ID, "cookie")

# -------------------------MONEY-----------------------#
money_tag = driver.find_element(By.CSS_SELECTOR, "#money").text
your_money = int(money_tag)

#------------------------UPGRADES/ REWARDS - AMOUNT& NAME----------------#
upgrades = driver.find_elements(By.CSS_SELECTOR, "div#store > div")

# -----------------------REWARDS LOCATOR




upgrady=[]
for upgrade in upgrades:
    upgrady.append(upgrade.text)
upgrady.remove("")
print(upgrady)
upgrade_types = []
for upgrade in upgrady:
    upgrade_types.append(upgrade.split("-")[0].replace(" ",""))


upgrade_amount = []
for upgrade in upgrady:
    upgrade_amount.append(int(upgrade.split("\n")[0].split(" - ")[1].replace(",", "")))


# print(upgrade_amount)
# print(upgrade_types)


rewards = {upgrade_types[i]: upgrade_amount[i] for i in range(len(upgrade_amount))}
# print(rewards)
# {15: 'Cursor', 100: 'Grandma', 500: 'Factory', 2000: 'Mine',
# 7000: 'Shipment', 50000: 'Alchemylab', 1000000: 'Portal', 123456789: 'Timemachine'}

while True:
    cookie.click()
    # time.sleep(0.01)
    # print(time_out)


    if your_money > rewards["Mine"] or time.time() > time_out + 3:
        mine_click = driver.find_element(By.ID, "buyMine")
        mine_click.click()
    if your_money > rewards['Factory'] or time.time() > time_out + 5:
        factory_click = driver.find_element(By.ID, "buyFactory")
        factory_click.click()
    if your_money > rewards["Cursor"] or time.time() > time_out + 15:
        cursor_click =driver.find_element(By.ID, "buyCursor")
        cursor_click.click()
    if your_money > rewards["Grandma"] or time.time() > time_out + 10:
        grandma_click = driver.find_element(By.ID,"buyGrandma")
        grandma_click.click()




    if time.time() > game_time_over:
        final_score = money_tag
        print(f"You have baked {money_tag}!!!!")
        cookie_sec = driver.find_element(By.ID, "cps").text
        print(f"Your Speed is {cookie_sec}")
        break

    #



# store end time


# total time taken
