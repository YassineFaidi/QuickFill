# Auto Form Filler Script

## Description
The **Auto Form Filler Script** is an automation tool designed to help you be among the first to fill out Google Forms shared via WhatsApp. The script listens for a Google Form link in your WhatsApp conversations, opens it instantly, fills out the required fields, and submits the form automatically.

---

## Features
- Detects Google Form links in WhatsApp conversations.
- Automatically opens and fills out the form fields (e.g., text, email).
- Handles radio button selections based on label text.
- Submits the form in either English (`Submit`) or French (`Envoyer`).
- Uses saved cookies to bypass login prompts for Google Forms.

---

## Requirements
- Python 3.8+
- Google Chrome browser installed
- WhatsApp Web access enabled
- Required Python libraries (see `requirements.txt`)

---

## Installation Steps

### Step 1: Clone or Download the Repository
Clone the repository to your local machine:
```bash
git clone https://github.com/YourUsername/auto_form_filler.git
cd auto_form_filler
```

### Step 2: Set Up a Virtual Environment
Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
```

### Step 3: Install Dependencies
Install the required dependencies listed in `requirements.txt`:
```bash
pip install -r requirements.txt
```

---

## Usage Steps

### Step 1: Save Google Form Cookies
1. Run the `cookieSaver.py` script:
   ```bash
   python cookieSaver.py
   ```
2. When the browser opens, manually log in to any Google Form. This ensures your session cookies are saved for later use.
3. The cookies will be saved in a file named `google_form_cookies.pkl`.

### Step 2: Run the Auto Form Filler Script
1. Run the `script.py` file:
   ```bash
   python script.py
   ```
2. When prompted, scan the QR code using WhatsApp on your mobile device to log into WhatsApp Web.

### Step 3: Set Up WhatsApp Monitoring
1. Open the WhatsApp conversation where you expect to receive the Google Form link.
2. The script will monitor the conversation for any incoming messages containing a Google Form link.

### Step 4: Automatic Form Filling
- When a Google Form link is detected:
  1. The script opens the form instantly.
  2. Autofills fields like your name and email.
  3. Selects radio buttons or checkboxes based on labels.
  4. Submits the form and displays a success message.

---

## Using the Script
1. Ensure you have run `cookieSaver.py` at least once to save your Google Form cookies.
2. Start the script with:
   ```bash
   python script.py
   ```
3. Ensure your WhatsApp Web session is active by scanning the QR code if necessary.
4. Open the specific WhatsApp conversation where the Google Form link will be shared.
5. Leave the script running — it will automatically detect and process any received Google Form links.

---

## Notes
- The script requires an active internet connection and WhatsApp Web login.
- Ensure the Google Forms shared are accessible without restrictions (e.g., CAPTCHA).
- Ensure your name, email, and other input data are configured in the script.

---

## Troubleshooting
- If the form doesn't load or cookies aren't applied, re-run `cookieSaver.py` to refresh your session cookies.
- If WhatsApp Web fails to sync, check your internet connection or re-scan the QR code.

---

## Author
- **Yassine Faidi**  
  Contact: `yassinefaidi.contact@gmail.com`
```

This `README.md` is a fully structured file, explaining everything step by step, including installation, usage, troubleshooting, and setup. You can save this as `README.md` in the root directory of your project.