from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import os
import requests
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

os.system('clear')

token = 'KA51ZOgutUa2ypKfiabwd67McgA4rPXWNqPcdIwVFPZ'
link = 'https://notify-api.line.me/api/notify'
headers = {'Authorization': f'Bearer {token}'}

cap: Dict[str, Any] = {
  "platformName": "Android",
  "appium:automationName": "UiAutomator2",
  "appium:deviceName": "emulator-5554",
  "appium:platformVersion": "14",
  "appium:appPackage": "com.google.android.dialer",
  "appium:appActivity": ".extensions.GoogleDialtactsActivity"
}

url = 'http://localhost:4723'
driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))

delay = 1  # script delay

print('Sync emulator!')

# Function to send Line Notify message
def send_line_notify(message):
    payload = {'message': message}
    response = requests.post(link, headers=headers, data=payload)

# Application logic
driver.find_element(by=AppiumBy.XPATH, value= '//android.widget.ImageButton[@content-desc="key pad"]').click()  #click on bottom right menu

while True:
    phone = input('Phone number : ')
    if len(phone) == 10 and phone.isdigit():
        try:
            for digit in phone:
                element_xpath = f'//android.widget.FrameLayout[contains(@content-desc, "{digit}")]'
                digit_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, element_xpath)))
                digit_element.click()

            dial_button_xpath = '//android.widget.Button[@content-desc="dial"]'
            dial_button_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, dial_button_xpath)))
            dial_button_element.click()

            print(f'Calling {phone}...')
            message = 'Calling {} . . .'.format(phone)
            send_line_notify(message)

            break  # Break out of the loop if the phone number is valid
        except TimeoutException:
            print('Timeout: Element not found. Please check the app state.')
    else:
        print('Wrong phone number. Please enter a 10-digit numeric phone number.')

# Close the driver session
driver.quit()