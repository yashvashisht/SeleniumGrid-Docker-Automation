"""Keep a WebDriver session open for a short time so you can see it in the Grid UI."""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

GRID_URL = "http://localhost:4444"

print("Connecting to Grid and opening a Chrome session...")
options = webdriver.ChromeOptions()

try:
    driver = webdriver.Remote(command_executor=GRID_URL, options=options)
    driver.get("https://www.example.com")
    print("Session created. Open http://localhost:4444/ui now to see the active session.")
    print("Keeping session alive for 60 seconds...")
    time.sleep(60)
finally:
    print("Closing session...")
    driver.quit()
    print("Done.")
