"""
Test 2: Google Search Test
This script tests Google search functionality
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_google():
    print("[TEST 2] Starting Google search test...")
    
    options = webdriver.ChromeOptions()
    driver = webdriver.Remote(
        command_executor='http://localhost:4444',
        options=options
    )
    
    try:
        # Open Google
        driver.get("https://www.google.com")
        print("[TEST 2] ✓ Google page loaded")
        
        # Wait for search box
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "q"))
        )
        print("[TEST 2] ✓ Search box found")
        
        # Perform search
        search_box.send_keys("Selenium Grid Docker")
        print("[TEST 2] ✓ Search query entered")
        
        time.sleep(3)
        print("[TEST 2] ✓ Test completed successfully")
        
    finally:
        driver.quit()

if __name__ == "__main__":
    test_google()
