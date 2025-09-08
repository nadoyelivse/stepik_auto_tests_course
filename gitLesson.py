from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # считаю значение x
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    
    result = calc(x)

    # Вводим ответ в текстовое поле
    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(result)

    # проскролить страницу вниз
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    # Отмечаем checkbox "I'm the robot"
    robot_checkbox = browser.find_element(By.ID, "robotCheckbox")
    robot_checkbox.click()
    
    # Выбираем radiobutton "Robots rule!"
    robots_rule_radio = browser.find_element(By.ID, "robotsRule")
    robots_rule_radio.click()

    # Нажимаем на кнопку Submit
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()
    
    # Даем время увидеть результат
    time.sleep(10)
    
finally:
    browser.quit()

    