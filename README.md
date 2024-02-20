# For interview with Doppio Tech Co., Ltd. (21/02/2024)

### This repository is divided into three main parts of test automation tech stack:

   1. Demo Appium
   2. Demo Locust
   3. Demo Selenium (python)

---

## 1. Demo Appium 
This project utilizes Appium and Selenium to automate interactions with the Android Dialer application. It establishes a connection with a virtual device, inputs a 10-digit phone number, and initiates a call. Additionally, it integrates Line Notify to send notifications about the call status. This demonstration showcases automation capabilities for mobile application testing and interaction.

### Installation

Use [pip](https://pypi.org/project/Appium-Python-Client/) to install Appium-Python-Client selenium requests
```Zsh
pip install Appium-Python-Client selenium requests
```

---

## 2. Demo Locust 
This Demo contains an example of load testing using Locust, a popular open-source load testing tool, against the Reqres API. Reqres provides a simple mock API for testing and prototyping, making it ideal for demonstrating load testing scenarios.

Features:
   Comprehensive API Request Coverage: Demonstrates load testing scenarios for all major types of HTTP requests:
   1. **GET** : Simulate retrieving data from the API using GET requests.
   2. **POST** : Perform data creation operations via POST requests, ensuring proper handling of request payloads.
   3. **PUT** : Update existing data in the API using PUT requests, validating proper modification of resources.
   4. **PATCH** : Partially update resources with PATCH requests, ensuring accurate modification of specific fields.
   5. **DELETE** : Validate deletion operations with DELETE requests, ensuring proper removal of resources.

### Installation

Use [pip](https://pypi.org/project/locust/) to install locust
```Zsh
pip install locust
```

---

## 3. Demo Selenium(python) 
This Python script demonstrates various commonly used functionalities for automate tester using Selenium WebDriver:

  1. **Checkboxes**: It selects checkboxes on a web page based on user input.
  2. **Dropdowns**: It interacts with dropdown menus on a web page based on user input.
  3. **Login Page**: It simulates logging in to a web page using provided credentials.
  4. **Windows**: It interacts with browser windows, opening a new window and then switching back to the original one.
  5. **Notification Text**: It retrieves notification text displayed on a web page.
Each function in the script represents one of these functionalities. By calling the respective function, you can demonstrate each feature individually. The script utilizes Selenium WebDriver to interact with web elements and perform actions such as clicking, inputting text, and retrieving information.

To use this script for demonstration, uncomment the desired function calls at the end of the script and execute it. Each function will showcase a different aspect of web automation using Selenium.

### Installation

Use [pip](https://pypi.org/project/selenium/) to install selenium
```Zsh
pip install selenium
```

---
I want to express my sincere gratitude for the opportunity to interview with Doppio Tech Co., Ltd. and for considering my application. If you need any further information or have any additional questions, please feel free to contact me. Thank you again, and I look forward to the possibility of joining your team.




