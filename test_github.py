"""
Test 4: GitHub Repository Test
This script navigates GitHub
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_github():
    print("[TEST 4] Starting GitHub navigation test...")
    
    options = webdriver.ChromeOptions()
    driver = webdriver.Remote(
        command_executor='http://localhost:4444',
        options=options
    )
    
    try:
        # Open GitHub
        driver.get("https://www.github.com")
        print("[TEST 4] ✓ GitHub main page loaded")
        
        # Wait for page content
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "main"))
        )
        print("[TEST 4] ✓ Page loaded successfully")
        
        time.sleep(3)
        print("[TEST 4] ✓ Test completed successfully")
        
    finally:
        driver.quit()

if __name__ == "__main__":
    test_github()
