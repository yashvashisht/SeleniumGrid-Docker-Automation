"""
Test 3: Wikipedia Page Test
This script navigates through Wikipedia
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_wikipedia():
    print("[TEST 3] Starting Wikipedia navigation test...")
    
    options = webdriver.ChromeOptions()
    driver = webdriver.Remote(
        command_executor='http://localhost:4444',
        options=options
    )
    
    try:
        # Open Wikipedia
        driver.get("https://www.wikipedia.org")
        print("[TEST 3] ✓ Wikipedia main page loaded")
        
        # Wait for search box
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "searchInput"))
        )
        print("[TEST 3] ✓ Search box found")
        
        # Search for something
        search_box.send_keys("Python Programming")
        print("[TEST 3] ✓ Search entered")
        
        time.sleep(3)
        print("[TEST 3] ✓ Test completed successfully")
        
    finally:
        driver.quit()

if __name__ == "__main__":
    test_wikipedia()
