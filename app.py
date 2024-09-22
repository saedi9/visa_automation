from visa_automation import VisaAutomation
import time

class VisaAutomationApp:
  def __init__(self):
    self.automation = VisaAutomation()

  def run(self):
    print('\n\n...:: WELCOME TO THE VISA AUTOMATIC AVAILABILITY CHECKER ::...\n')
    while True:
      print('\nChoose an option from below:')
      print('1. Start or Restart\n2. Close\n')
      choice = input('Your option: ')
      if choice == '1':
        self.automation.start_process()
      elif choice == '2':
        self.automation.close_browser()
        print('Exiting...')
        time.sleep(1)
        exit()
      else:
        print("Invalid choice, please try again.")
