from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    price = WebDriverWait(browser, 20).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )

    button=browser.find_element_by_css_selector(".btn.btn-primary").click()

    x_element=browser.find_element_by_id('input_value')
    x=x_element.text
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    answer=calc(x)
    input=browser.find_element_by_id('answer')
    input.send_keys(answer)

    solve_but=browser.find_element_by_id('solve').click()


    time.sleep(100)

finally:
    time.sleep(4)
    browser.quit()