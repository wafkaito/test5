# Generated by Selenium IDE
import pytest
import time
import json
import allure
from SC import take_screenshot
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import NoSuchElementException

class TestTest4():
  def setup_method(self, method):
    self.driver = webdriver.Remote(command_executor='http://192.168.41.66:4445', desired_capabilities=DesiredCapabilities.CHROME)
    #self.driver = webdriver.Chrome()
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # Enable headless mode
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    #self.driver = webdriver.Remote(command_executor='http://10.99.20.121:4445',options=chrome_options)
    #self.driver = webdriver.Chrome(options=chrome_options)
    self.driver.set_window_size(1920, 1080)
    self.driver.maximize_window()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def wait_for_window(self, timeout = 2):
    time.sleep(round(timeout / 1000))
    wh_now = self.driver.window_handles
    wh_then = self.vars["window_handles"]
    if len(wh_now) > len(wh_then):
      return set(wh_now).difference(set(wh_then)).pop()
  
  def test(self):
    with allure.step("Open URL"):
      self.driver.get("http://10.100.3.65/en/public")#HST
    try:

      time.sleep(1)
      self.driver.execute_script("window.scrollTo(0, 500);")
      time.sleep(1)

      self.vars["window_handles"] = self.driver.window_handles
      try:
        self.driver.find_element(By.CSS_SELECTOR, ".col-lg-4:nth-child(1) .bt-n2").click()
      except NoSuchElementException:
        time.sleep(1.5)
      if (len(self.driver.window_handles) == 2):
        self.vars["win_new"] = self.wait_for_window(2000)
        self.driver.switch_to.window(self.vars["win_new"])
        text = self.driver.find_element(By.CSS_SELECTOR, "center").text
        assert text != "ไม่พบข่าวที่คุณต้องการค้นหา"
        time.sleep(1)
        self.driver.close()
      pass
      self.driver.switch_to.window(self.vars["window_handles"][0])
      time.sleep(1.5)

      self.vars["window_handles"] = self.driver.window_handles
      try:
        self.driver.find_element(By.CSS_SELECTOR, ".col-lg-4:nth-child(2) .bt-n2").click()
      except NoSuchElementException:
        time.sleep(1.5)
      if (len(self.driver.window_handles) == 2):
        self.vars["win_new"] = self.wait_for_window(2000)
        self.driver.switch_to.window(self.vars["win_new"])
        text = self.driver.find_element(By.CSS_SELECTOR, "center").text
        assert text != "ไม่พบข่าวที่คุณต้องการค้นหา"
        time.sleep(1)
        self.driver.close()
      pass
      self.driver.switch_to.window(self.vars["window_handles"][0])
      time.sleep(1.5)

      self.vars["window_handles"] = self.driver.window_handles
      try:
        self.driver.find_element(By.CSS_SELECTOR, ".col-lg-4:nth-child(3) .bt-n2").click()
      except NoSuchElementException:
        time.sleep(1.5)
      if (len(self.driver.window_handles) == 2):
        self.vars["win_new"] = self.wait_for_window(2000)
        self.driver.switch_to.window(self.vars["win_new"])
        text = self.driver.find_element(By.CSS_SELECTOR, "center").text
        assert text != "ไม่พบข่าวที่คุณต้องการค้นหา"
        time.sleep(1)
        self.driver.close()
      pass
      self.driver.switch_to.window(self.vars["window_handles"][0])
      time.sleep(1.5)     

    except Exception as e:
      # If an assertion error occurs, capture a screenshot and attach it to the Allure report
      allure.attach(self.driver.get_screenshot_as_png(), name="Error Screenshot", attachment_type=allure.attachment_type.PNG)
      raise e
