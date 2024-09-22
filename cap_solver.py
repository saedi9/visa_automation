import base64
import requests

class CapSolver:
  def __init__(self, 
              api_key = 'CAP-F1BE3B6B01CEF0E54510784B4B4DDCF5', 
              capsolver_url='https://api.capsolver.com/createTask'):
    self.api_key = api_key
    self.capsolver_url = capsolver_url

  def _load_image(self, image_path):
    """
    Loads an image from the given file path and encodes it to base64.
    """
    try:
      with open(image_path, "rb") as image_file:
          base64_image = base64.b64encode(image_file.read()).decode('utf-8')
      return base64_image
    except FileNotFoundError:
      print(f"Error: File {image_path} not found.")
      return None

  def solve_captcha(self):
    """
    Sends the image to the CapSolver API to solve the CAPTCHA.
    """
    base64_image = self._load_image("ci.png")
    if base64_image is None:
      return None

    data = {
      "clientKey": self.api_key,
      "task": {
        "type": "ImageToTextTask",
        "body": base64_image
      }
    }

    try:
      # Send the POST request to CapSolver
      response = requests.post(self.capsolver_url, json=data, timeout=10)
      result = response.json()

      # Check for successful response
      if result.get("errorId") == 0:
        return result.get("solution", {}).get("text", '0000')
      else:
        print(f"Error: {result.get('errorDescription', 'Unknown error')}")
        return None
    except requests.exceptions.RequestException as e:
      print(f"Request failed: {e}")
      return None
