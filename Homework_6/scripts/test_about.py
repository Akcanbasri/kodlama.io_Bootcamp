# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestAbout():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_about(self):
    self.driver.get("https://www.saucedemo.com/")
    self.driver.set_window_size(1552, 840)
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.ID, "user-name")))
    self.driver.find_element(By.ID, "user-name").click()
    self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.ID, "password")))
    self.driver.find_element(By.ID, "password").click()
    self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
    WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.ID, "login-button")))
    self.driver.find_element(By.ID, "login-button").click()
    self.driver.find_element(By.ID, "react-burger-menu-btn").click()
    self.driver.find_element(By.ID, "about_sidebar_link").click()
    self.driver.close()
  
