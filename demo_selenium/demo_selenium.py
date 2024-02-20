from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import location

chrome_options = Options()
driver = webdriver.Chrome(options=chrome_options)

driver.maximize_window()

# url = 'https://the-internet.herokuapp.com/'


#   check box list
def check_boxes():
    driver.get('https://the-internet.herokuapp.com/checkboxes')

    # Select checkboxes if not already selected
    for index in range(1, 3):  # Adjust range to match the number of checkboxes on the page
        checkbox_xpath = location.checkboxes_list.format(checkbox_index=index)
        box = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, checkbox_xpath)))
        if box.is_selected():
            box.click()

    checkbox_indices = input('Choose checkbox (1,2): ')

    # Select checkboxes based on user input
    for index in checkbox_indices.split(','):
        checkbox_xpath = location.checkboxes_list.format(checkbox_index=index.strip())
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, checkbox_xpath))).click()
        print('Checkbox {} selected!'.format(index.strip()))

    time.sleep(5)
    driver.quit()

#   dropdown list
def dropdown():
    driver.get('https://the-internet.herokuapp.com/dropdown')
    index = input('Choose dropdown (1,2): ')
    dropdown_xpath = location.dropdown_list.format(dropdown_index=index)
    dropdown = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, dropdown_xpath)))
    dropdown.click()
    print('You selected {}'.format(dropdown.text))

    time.sleep(5)
    driver.quit()

#   login page
def login():
    driver.get('https://the-internet.herokuapp.com/login')
    username = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, location.username))).text
    password = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, location.password))).text
    input_username = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, location.input_username)))
    input_password = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, location.input_password)))
    input_username.send_keys(username)
    input_password.send_keys(password)
    input_password.submit()

    after_login = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, location.after_login))).text
    print('Monitor show : {}'.format(after_login))

    time.sleep(5)
    driver.quit()

#   window part
def window():
    driver.get('https://the-internet.herokuapp.com/windows')
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, location.click_here))).click()
    driver.switch_to.window(driver.window_handles[1])
    print('New window title: {}'.format(driver.title))
    seconds = 3
    while seconds > 0:
        print(f"Back to previous window in: {seconds} seconds")
        time.sleep(1)
        seconds -= 1
    
    driver.switch_to.window(driver.window_handles[0])
    print('Current window title: {}'.format(driver.title))
    time.sleep(5)
    driver.quit()

#   get text part
def get_text():
    driver.get('https://the-internet.herokuapp.com/notification_message_rendered')

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, location.click_here))).click()
    notify = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'flash'))).text
    notify = notify.split('×')
    print('Notification text : {}'.format(notify[0]))

    time.sleep(10)
    driver.quit()

#   call function


# check_boxes()
# dropdown()
# login()
# window()
# get_text()
    

