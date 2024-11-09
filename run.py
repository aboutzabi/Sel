import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime
import time
import random

def human_like_delay(min_delay=1, max_delay=3):
    """Random delay to simulate human interaction."""
    time.sleep(random.uniform(min_delay, max_delay))

def move_mouse_to_element(driver, element):
    """Simulate smooth mouse movement to the element."""
    action = ActionChains(driver)
    action.move_to_element(element).perform()

def set_user_agent():
    """Return a random user agent from the predefined list."""
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
        "Mozilla/5.0 (Linux; Android 11; Pixel 4 XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.110 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 12; Pixel 5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Mobile Safari/537.36",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (iPad; CPU OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/605.1.15",
        "Mozilla/5.0 (iPad; CPU OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/605.1.15",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:60.0) Gecko/20100101 Firefox/60.0",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:92.0) Gecko/20100101 Firefox/92.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0",
        "Mozilla/5.0 (Linux; Android 11; Samsung Galaxy S20; rv:92.0) Gecko/92.0 Firefox/92.0",
        "Mozilla/5.0 (Linux; Android 11; OnePlus 8T; rv:94.0) Gecko/94.0 Firefox/94.0",
        "Mozilla/5.0 (Linux; Android 12; Google Pixel 6; rv:95.0) Gecko/95.0 Firefox/95.0"
    ]
    return random.choice(user_agents)

def create_driver():
    """Create a Chrome driver with a random user agent and disable automation flags."""
    user_agent = set_user_agent()
    
    options = uc.ChromeOptions()
    options.add_argument(f'user-agent={user_agent}')
    #options.add_argument('--headless')  # Use new headless mode if available
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument('--window-size=1920x1080')
    options.add_argument('--disable-infobars')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-software-rasterizer')
    options.add_argument('--disable-extensions')
    options.add_argument('--disable-popup-blocking')

    try:
        driver = uc.Chrome(options=options, timeout=30)
    # your selenium interactions here
    except Exception as e:
        print(f"Error occurred: {e}")
    
    # Disable the automation flag
    driver.execute_cdp_cmd(
    "Page.addScriptToEvaluateOnNewDocument",
    {
        "source": """
        Object.defineProperty(navigator, 'webdriver', {get: () => undefined});
        window.navigator.chrome = { runtime: {}, };  // Mimic the 'chrome' object
        Object.defineProperty(navigator, 'languages', {get: () => ['en-US', 'en']});
        Object.defineProperty(navigator, 'plugins', {get: () => [1, 2, 3, 4, 5]});  // Add fake plugins
        """
    }
)
    
    return driver

# Move Mylinks outside of the create_driver function
Mylinks = [
    "https://futuerdevhub.blogspot.com/",
    "https://futuerdevhub.blogspot.com/2024/11/12-apps-that-pay-you-to-do-nothingeven.html",
    "https://futuerdevhub.blogspot.com/2024/11/18-apps-that-pay-you-to-do-nothingeven.html",
    "https://futuerdevhub.blogspot.com/2024/08/my-7-income-sources-with-one-ai-tool.html",
    "https://futuerdevhub.blogspot.com/2024/11/3-new-online-earning-platforms-to-make.html",
    "https://futuerdevhub.blogspot.com/2024/11/get-paid-10000-monthly-with-amazon.html",
    "https://futuerdevhub.blogspot.com/2024/11/top-10-innovative-ai-fueled-sidehustles.html"
]

# Run 1000 sessions
for session in range(1, 1001):
    driver= None
    try:
        # Create a new driver with a random user agent and headers
        driver = create_driver()
        driver.execute_script('window.localStorage.setItem("ads_blocked", "false")')
        random_link = random.choice(Mylinks)

        # Open the webpage
        driver.get(random_link)
        human_like_delay(3, 5)  # Wait for a bit before interacting

        # Wait until the #bmd-inp-wrapper div is present in the DOM
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.ID, "bmd-inp-wrapper"))
        )

        # Find all elements with class 'bmd-inp-item' inside the #bmd-inp-wrapper div
        items = driver.find_elements(By.CSS_SELECTOR, "#bmd-inp-wrapper .bmd-inp-item")

        # Loop through each element, click it, and handle the redirection
        for item in items:
            # Scroll to the item before clicking
            driver.execute_script("arguments[0].scrollIntoView();", item)
            human_like_delay(1, 2)  # Pause to simulate reading time

            # Move the mouse to the element before clicking
            move_mouse_to_element(driver, item)
            human_like_delay(0.5, 1.5)  # Slight pause before the click

            # Click the item to open the link in a new tab
            item.click()

            # Wait for the new tab to open
            human_like_delay(2, 4)  # Adjust time if necessary based on loading speed

            # Switch to the new tab
            driver.switch_to.window(driver.window_handles[-1])

            # Print the URL of the new tab
            current_url = driver.current_url
            print("Initial URL ok")

            # Wait a bit for any potential redirects to occur
            human_like_delay(3, 5)  # Adjust time if necessary

            # Print the redirected URL after the redirection
            redirected_url = driver.current_url
            print("Redirected URL:", redirected_url)

            # Close the new tab and switch back to the main tab
            driver.close()
            driver.switch_to.window(driver.window_handles[0])

        # Log session completion time
        completion_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(f"Session {session} completed at {completion_time}")

    except Exception as e:
        # Log any errors
        print(f"Session {session} failed with error: {e}")

    finally:
        # Ensure the browser is closed after each session
       
        driver.quit()
    
    # Optional: Add delay between sessions to simulate time gaps
    human_like_delay(5, 10)
