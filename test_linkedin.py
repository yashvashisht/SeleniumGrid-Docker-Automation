"""
Test 5: LinkedIn Page Test
This script navigates LinkedIn
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_linkedin():
    print("[TEST 5] Starting LinkedIn navigation test...")
    
    options = webdriver.ChromeOptions()
    driver = webdriver.Remote(
        command_executor='http://localhost:4444',
        options=options
    )
    
    try:
        # Open LinkedIn
        driver.get("https://www.linkedin.com")
        print("[TEST 5] ✓ LinkedIn page loaded")
        
        # Wait for page elements
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "main"))
        )
        print("[TEST 5] ✓ Page content loaded")
        
        time.sleep(3)
        print("[TEST 5] ✓ Test completed successfully")
        
    finally:
        driver.quit()

if __name__ == "__main__":
    test_linkedin()
