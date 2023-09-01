from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://www.avito.ru/nikel/knigi_i_zhurnaly/domain-driven_design_distilled_vaughn_vernon_2639542363")
object_name = driver.find_element(By.CLASS_NAME, 'title-info-title-text').text
element_button = driver.find_element(By.CLASS_NAME, "style-header-add-favorite-M7nA2")
element_button.click()
link_button = driver.find_element(By.CLASS_NAME, 'desktop-1gzlbya')
link_button.click()
text = driver.find_element(By.CLASS_NAME, 'styles-module-root-hwVld').text
if text == object_name:
    print('Test passed')
else:
    print('Test failed')