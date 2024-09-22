import pyautogui
import time


class WhatsappCall:
  def __init__(self, contact_image = 'contact.png', call_image = 'call.png'):
    self.contact_image = contact_image
    self.call_image = call_image

  def open_whatsapp(self):
    """Open Whatsapp application."""
    pyautogui.hotkey('winleft')  # Open Start Menu (adjust as needed)
    time.sleep(1)  # Wait for the Start Menu to open
    pyautogui.write('Whatsapp')  # Search for whatsapp
    time.sleep(1)  # Wait for search results
    pyautogui.press('enter')

  def locate_and_click(self, image_path):
    """Locate an image on the screen and click it."""
    location = pyautogui.locateOnScreen(image_path)
    if location:
      button_center = pyautogui.center(location)
      pyautogui.click(button_center)
      pyautogui.click(button_center)
      return True
    else:
      return False

  def make_call(self):
    """Make a call to the contact."""
    time.sleep(5)  # Wait for the app to be loaded

    if self.locate_and_click(self.contact_image):
      time.sleep(2)  # Wait for the next screen to load
      if self.locate_and_click(self.call_image):
        print('Calling...')
      else:
        print('Could not find call button')
    else:
      print('Contact not found')

  def call(self):
    """Run the complete process."""
    self.open_whatsapp()
    self.make_call()
