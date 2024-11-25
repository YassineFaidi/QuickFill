from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pickle, time, re

# Setup Chrome options
chrome_options = Options()
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("start-maximized")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")

# Set up ChromeDriver using WebDriver Manager with the above options
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Open WhatsApp Web
driver.get("https://web.whatsapp.com/")
print("[117] Please scan the QR code in WhatsApp Web")

# Wait for the user to scan the QR code and load WhatsApp Web
time.sleep(30)

# Function to check if the message contains the form link
def check_for_link_in_messages():
    try:
        # Find the last message in the chat (newest message)
        last_message = driver.find_elements(By.CSS_SELECTOR, "div.message-in:last-child")
        
        if last_message:
            message_text = last_message[-1].text.strip()
            print("[117]" + message_text[:5] + "...")
            # Check if the message contains a Google Forms link
            match = re.search(r'https://docs\.google\.com/forms/[^\s]+', message_text)
            if match:
                form_url = match.group()
                print(f"[117] New Google Form link received: {form_url}")
                execute_script(form_url, "google_form_cookies.pkl", "Your name", "youremail@gmail.com")
                return True
                
    except Exception as e:
        print(f"[117] Error: {e}")
        return False

# Function to execute your custom script when the link is detected
def execute_script(form_url, cookies_path, name, email):
    # Open the Google Form URL
    driver.get(form_url)

    # Wait for the form to load
    wait = WebDriverWait(driver, 5)

    # Load the cookies from the pickle file
    try:
        cookies = pickle.load(open(cookies_path, "rb"))
        for cookie in cookies:
            try:
                driver.add_cookie(cookie)
                print("[117] Cookie added successfully")
            except Exception as e:
                print(f"[117] Failed to add cookie: {e}")
        # Refresh the page to apply the cookies
        driver.refresh()
        print("[117] Cookies applied, refreshing...")
        time.sleep(1)  # Wait for refresh to complete
    except FileNotFoundError:
        print("[117] Cookie file not found, proceeding without cookies.")

    # Find all input elements
    input_elements = driver.find_elements(By.TAG_NAME, 'input')

    print("[117] Filling the form...")

    # Loop through each input field and fill it dynamically
    for input_element in input_elements:
        input_type = input_element.get_attribute("type")

        if input_type == "text":
            input_element.clear()  # Clear the field before typing
            input_element.send_keys(name)
        elif input_type == "email":
            input_element.clear()  # Clear the field before typing
            input_element.send_keys(email)

    # Handle radio button selection (with a custom XPath)
    try:
        radio_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[translate(@aria-label, "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz")="iccn"]')))
        radio_button.click()
        print("[117] Radio button clicked...")
    except Exception as e:
        print(f"[117] Failed to click radio button: {e}")

    # Submit the form
    try:
        submit_button = driver.find_element(By.XPATH, '//span[text()="Submit" or text()="Envoyer" or text()="Soumettre"]')
        submit_button.click()
        print("[117] Form submitted successfully")
    except Exception as e:
        print(f"[117] Failed to submit the form: {e}")

    time.sleep(5)

# Monitor the chat for new messages (you may want to loop indefinitely or for a specific amount of time)
count = 0
while True:
    print("[" + str(count) +"] Monitoring for new messages...")
    time.sleep(1)
    count += 1
    
    # Check for a link in the messages
    if check_for_link_in_messages():
        print("[117] Script executed successfully.")
        break  # Stop monitoring once the link has been found and the script has run

# Close the browser after the script has been executed
driver.quit()