"""
Simple Selenium test to run against Docker Selenium Grid.

This script:
1. Connects to the Grid at http://localhost:4444
2. Requests a Chrome browser session
3. Opens Google.com
4. Searches for "Selenium WebDriver"
5. Verifies the page title contains "Selenium"
6. Closes the browser

Prerequisites:
- Grid running: docker compose -f docker-compose-v3.yml up
- Python 3.8+
- selenium library: pip install selenium
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

# Grid URL
GRID_URL = "http://localhost:4444"

def test_google_search():
    """Test: Search on Google via Selenium Grid"""
    
    # Step 1: Define browser capabilities
    # "capabilities" tells the Grid: "I want a Chrome browser"
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")
    
    print("[1] Creating WebDriver connection to Grid...")
    try:
        # Connect to Grid at http://localhost:4444
        # Grid will assign a Chrome node to handle this request
        driver = webdriver.Remote(
            command_executor=GRID_URL,
            options=options
        )
        print("✓ Connected to Grid successfully")
    except Exception as e:
        print(f"✗ Failed to connect to Grid: {e}")
        print("  Make sure Grid is running: docker compose -f docker-compose-v3.yml up")
        return False
    
    try:
        # Step 2: Navigate to Google
        print("\n[2] Opening https://www.google.com...")
        driver.get("https://www.google.com")
        print("✓ Page loaded")
        
        # Step 3: Find the search box and enter a query
        print("\n[3] Searching for 'Selenium WebDriver'...")
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "q"))
        )
        search_box.send_keys("Selenium WebDriver")
        search_box.send_keys(Keys.RETURN)
        print("✓ Search query submitted")
        
        # Step 4: Wait for results and check page title
        print("\n[4] Waiting for search results...")
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a[data-sokoban-feature]"))
        )
        
        # Get page title
        page_title = driver.title
        print(f"✓ Page title: {page_title}")
        
        # Step 5: Verify results
        print("\n[5] Verifying search results...")
        if "Selenium" in page_title:
            print("✓ TEST PASSED: Title contains 'Selenium'")
            return True
        else:
            print("✗ TEST FAILED: Title does not contain 'Selenium'")
            return False
            
    except Exception as e:
        print(f"✗ Test failed with error: {e}")
        return False
        
    finally:
        # Step 6: Close the browser
        print("\n[6] Closing browser...")
        driver.quit()
        print("✓ Browser closed, session ended")

def test_simple_chrome():
    """Test 2: Simple Chrome test (faster)"""
    
    print("\n" + "="*60)
    print("TEST 2: Simple Chrome Page Load Test")
    print("="*60)
    
    options = webdriver.ChromeOptions()
    
    try:
        print("[1] Creating Chrome session via Grid...")
        driver = webdriver.Remote(
            command_executor=GRID_URL,
            options=options
        )
        print("✓ Chrome session created")
        
        # Navigate to a simple page
        print("[2] Loading https://www.python.org...")
        driver.get("https://www.python.org")
        
        title = driver.title
        print(f"✓ Page title: {title}")
        
        if "Python" in title:
            print("✓ TEST PASSED: Python.org loaded successfully")
            return True
        else:
            print("✗ TEST FAILED: Unexpected page title")
            return False
            
    except Exception as e:
        print(f"✗ Test failed: {e}")
        return False
        
    finally:
        driver.quit()
        print("[3] Browser closed\n")

def test_firefox():
    """Test 3: Firefox test"""
    
    print("\n" + "="*60)
    print("TEST 3: Firefox Browser Test")
    print("="*60)
    
    options = webdriver.FirefoxOptions()
    
    try:
        print("[1] Creating Firefox session via Grid...")
        driver = webdriver.Remote(
            command_executor=GRID_URL,
            options=options
        )
        print("✓ Firefox session created")
        
        print("[2] Loading https://www.wikipedia.org...")
        driver.get("https://www.wikipedia.org")
        
        title = driver.title
        print(f"✓ Page title: {title}")
        print("✓ TEST PASSED: Firefox session successful")
        return True
        
    except Exception as e:
        print(f"✗ Test failed: {e}")
        return False
        
    finally:
        driver.quit()
        print("[3] Firefox browser closed\n")

if __name__ == "__main__":
    print("="*60)
    print("SELENIUM GRID TEST SUITE")
    print("="*60)
    print(f"\nConnecting to Grid at: {GRID_URL}")
    print("Make sure Grid is running before starting tests!\n")
    
    # Run all tests
    results = []
    
    # Test 1: Google search (more complex)
    print("\n" + "="*60)
    print("TEST 1: Google Search Test")
    print("="*60)
    result1 = test_google_search()
    results.append(("Google Search", result1))
    
    # Test 2: Simple Chrome test
    result2 = test_simple_chrome()
    results.append(("Simple Chrome", result2))
    
    # Test 3: Firefox test
    result3 = test_firefox()
    results.append(("Firefox", result3))
    
    # Summary
    print("\n" + "="*60)
    print("TEST SUMMARY")
    print("="*60)
    for test_name, passed in results:
        status = "✓ PASSED" if passed else "✗ FAILED"
        print(f"{test_name}: {status}")
    
    total_passed = sum(1 for _, passed in results if passed)
    print(f"\nTotal: {total_passed}/{len(results)} tests passed")
