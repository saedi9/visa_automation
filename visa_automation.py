import time
from cap_solver import CapSolver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from whatsapp import WhatsappCall


class VisaAutomation:
  def __init__(self):
    self.browser = None
    self.cap_solver = CapSolver()

  def start_browser(self):
    """Initialize the WebDriver and navigate to the URL."""
    print('Starting browser...')
    self.browser = webdriver.Firefox()
    self.browser.get('https://evisatraveller.mfa.ir/en/request/applyrequest/')

  def start_process(self):
    """Complete the full process of solving the CAPTCHA and submitting the form."""
    self.start_browser()
    time.sleep(30)

    # Loop until the form is successfully submitted and next page is reached
    cc = self.browser.find_elements(By.ID, 'id_father_name')

    while len(cc) <= 0:
      ci = self.browser.find_element(By.CLASS_NAME, 'ecaptcha')
      ci.screenshot('ci.png')
      print("Solving CAPTCHA...")
      captcha = self.cap_solver.solve_captcha()
      print(captcha)
      self.browser.find_element(By.NAME, 'captcha_1').clear()
      self.browser.find_element(By.NAME, 'captcha_1').send_keys(captcha)
      WebDriverWait(self.browser, 10).until(EC.invisibility_of_element_located((By.ID, "select2-drop-mask")))
      self.browser.find_element(By.ID, 'first_step_submit_btn').click()
      time.sleep(10)
      cc = self.browser.find_elements(By.ID, 'id_father_name')
      if len(cc) <= 0:
        print("Failed to solve CAPTCHA, retrying...")

    print("Form successfully submitted and navigated to the next step!")

      # making call to mobile

    call = WhatsappCall()
    while True:
      call.call()
      time.sleep(90)

  def close_browser(self):
    """Close the browser instance."""
    if self.browser:
      self.browser.quit()
    print("Browser closed.")
