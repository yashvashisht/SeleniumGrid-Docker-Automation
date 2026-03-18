"""
Test 1: Facebook Login Test
This script tests Facebook login via Selenium Grid
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_facebook():
    print("[TEST 1] Starting Facebook login test...")
    
    # Connect to Selenium Grid Hub
    options = webdriver.ChromeOptions()
    driver = webdriver.Remote(
        command_executor='http://localhost:4444',
        options=options
    )
    
    try:
        # Open Facebook
        driver.get("https://www.facebook.com")
        print("[TEST 1] ✓ Facebook page loaded")
        
        # Wait for login form
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "email"))
        )
        print("[TEST 1] ✓ Login form found")
        
        # Fill form (demo credentials)
        driver.find_element(By.NAME, "email").send_keys("test@example.com")
        driver.find_element(By.NAME, "pass").send_keys("demo_password")
        print("[TEST 1] ✓ Form filled")
        
        time.sleep(3)
        print("[TEST 1] ✓ Test completed successfully")
        
    finally:
        driver.quit()

if __name__ == "__main__":
    test_facebook()
