from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

import time


def load_url_selenium_tiki(url):
    options = Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--headless")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    print("Loading url=", url)
    driver.get(url)
    driver.execute_script("window.scrollTo(0,1500)")
    driver.execute_script("window.scrollTo(0,2500)")
    driver.execute_script("window.scrollTo(0,3500)")
    time.sleep(1)
    list_review = []
    # just craw 10 page
    x = 0
    while x < 20:
        product_reviews = driver.find_elements(By.CLASS_NAME, "review-comment__content")
        # Get product review
        for product in product_reviews:
            review = product.text
            if review != "" or review.strip():
                print(review, "\n")
                list_review.append(review)
        # Check for button next-pagination-item have disable attribute then jump from loop else click on the next button
        try:
            # driver.find_element_by_xpath("//li[@class='btn next']/a").click()
            button_next = driver.find_elements(By.CSS_SELECTOR, "a[class='btn next']")[
                0
            ]
            driver.execute_script("arguments[0].click();", button_next)
            time.sleep(1)
            x += 1
        except (TimeoutException, WebDriverException, IndexError) as e:
            break
    driver.close()
    return list_review


def crawl_text_tiki(url):
    result = "\n".join(load_url_selenium_tiki(url))
    return result
