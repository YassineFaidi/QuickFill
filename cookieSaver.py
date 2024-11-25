from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import pickle

# Setup Chrome options
chrome_options = Options()
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("start-maximized")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")

# Set up ChromeDriver using WebDriver Manager with the above options
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Open Google login page
driver.get("https://docs.google.com/forms/any/form/link")

# Wait for the login page to load and manually log in
input("Log in manually and press Enter once you are logged in...")

# Save cookies after login
pickle.dump(driver.get_cookies(), open("google_form_cookies.pkl", "wb"))

# Close the browser after saving cookies
driver.quit()