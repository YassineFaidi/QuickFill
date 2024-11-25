# Auto Form Filler Script

## Overview

The **Auto Form Filler Script** is an automation tool designed to quickly fill out Google Forms shared via WhatsApp. This script listens for incoming Google Form links in WhatsApp conversations, automatically fills in the required fields, and submits the form. It is ideal for ensuring you're one of the first to fill out forms that may have time-sensitive submissions.

---

## Features

- **Link Detection**: Automatically detects and opens Google Form links shared in WhatsApp conversations.
- **Auto Fill**: Fills form fields such as name and email automatically.
- **Radio Button Handling**: Supports selecting radio buttons based on their labels.
- **Language Support**: Detects form submission buttons in English (`Submit`) and French (`Envoyer`) and submits the form accordingly.
- **Cookie Management**: Uses saved cookies to bypass login prompts for Google Forms.

---

## Requirements

- Python 3.8+
- Google Chrome installed on your system
- WhatsApp Web enabled and logged in
- The required Python libraries (listed in `requirements.txt`)

---

## Installation Instructions

Follow the steps below to install and set up the script:

### 1. Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/YassineFaidi/Auto-Form-Filler.git
cd Auto-Form-Filler
```

### 2. Install Dependencies

Next, install the required Python libraries using `pip`:

```bash
pip install -r requirements.txt
```

---

## Usage Instructions

### Step 1: Save Google Form Cookies

Before running the form filling script, you need to save your Google Form cookies to bypass login prompts.

1. Run the `cookieSaver.py` script:

    ```bash
    python cookieSaver.py
    ```

2. The script will open Google Chrome, and you must manually log in to any Google Form to generate the necessary cookies.
3. The cookies will be saved in a file named `google_form_cookies.pkl`, which will be used later to bypass login on subsequent form submissions.

### Step 2: Run the Auto Form Filler Script

Now that your cookies are saved, you're ready to run the main script:

1. Run the `script.py` file:

    ```bash
    python script.py
    ```

2. When prompted, scan the QR code with WhatsApp on your mobile device to log into WhatsApp Web.

### Step 3: Set Up WhatsApp Monitoring

1. Open the WhatsApp conversation where you expect to receive the Google Form link.
2. The script will monitor this conversation for any incoming messages containing a Google Form link.

### Step 4: Automatic Form Filling

Once the script detects a Google Form link:

- It will open the form in the browser.
- The script will automatically fill in the predefined fields (e.g., name, email).
- If there are radio buttons or checkboxes, the script will select them based on their labels.
- Finally, the script will submit the form and print a success message in the terminal.

---

## Additional Notes

- Ensure that WhatsApp Web is logged in before running the script.
- Make sure the Google Form shared with you is accessible without restrictions, such as CAPTCHA challenges.
- You can configure your name, email, and other form fields directly in the script.

---

## Troubleshooting

- **Form not loading or cookies not applied**: Ensure you've run `cookieSaver.py` and generated fresh cookies.
- **WhatsApp Web not syncing**: If WhatsApp Web doesn't sync, check your internet connection or re-scan the QR code.
- **Form submission issues**: If the form is not submitted, verify that the form’s submission button text is detected correctly (either "Submit" or "Envoyer").

---

## Author

- **Yassine Faidi**  
  Contact: [yassinefaidi.contact@gmail.com](mailto:yassinefaidi.contact@gmail.com)

---

## License

This project is open source and available under the [MIT License](LICENSE).