# Generated by Selenium IDE

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_():
    driver = webdriver.Firefox()
    driver.get("http://web.sanguosha.com/login/index.html")
    driver.set_window_size(1100, 749)
    driver.find_element(By.ID, "dobest_inputUserId_175c206d4b2").click()
    driver.find_element(By.ID, "dobest_inputUserId_175c206d4b2").send_keys("huanlingshao2")
    driver.find_element(By.ID, "dobest_password_175c206d4b2").send_keys("xijinping")
    driver.find_element(By.CSS_SELECTOR, ".dobest_extra").click()
    driver.find_element(By.ID, "dobest_loginBtn_175c206d4b2").click()
    driver.find_element(By.ID, "dobest_protocol_175c206d4b2").click()
    driver.find_element(By.ID, "dobest_loginBtn_175c206d4b2").click()
    driver.find_element(By.CSS_SELECTOR, ".new_ser1:nth-child(2) > img").click()
    driver.find_element(By.ID, "newGoInGame").click()
    driver.switch_to.frame(0)
    driver.find_element(By.ID, "layaCanvas").click()
    driver.find_element(By.ID, "layaCanvas").click()
    driver.find_element(By.ID, "layaCanvas").click()
    driver.find_element(By.ID, "layaCanvas").click()
    driver.find_element(By.ID, "layaCanvas").click()
    driver.find_element(By.ID, "layaCanvas").click()
    driver.find_element(By.ID, "layaCanvas").click()
    driver.find_element(By.ID, "layaCanvas").click()
    driver.find_element(By.ID, "layaCanvas").click()
    driver.find_element(By.ID, "layaCanvas").click()
    driver.find_element(By.ID, "layaCanvas").click()
    # driver.quit()


if __name__ == '__main__':
    test_()
