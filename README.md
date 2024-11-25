# Auto Form Filler Script

## Description
The **Auto Form Filler Script** is designed to automatically detect and fill Google Forms shared via WhatsApp, ensuring that you can be among the first to submit the form. This script listens for a form link received in a WhatsApp chat, opens it instantly, fills out the required fields dynamically, and submits the form automatically.

---

## Features
- Monitors WhatsApp for incoming Google Form links.
- Automatically opens and fills the form fields (text, email).
- Handles radio button selection based on label text.
- Submits the form in either English (`Submit`) or French (`Envoyer`).
- Supports cookies for persistent sessions to bypass login prompts.

---

## Requirements
- Python 3.8+
- Google Chrome browser installed
- WhatsApp Web access enabled
- Required Python libraries:
  - `selenium`
  - `webdriver-manager`
  - `pickle`

---

## Installation

1. **Clone or Download the Repository:**
   ```bash
   git clone https://github.com/YourUsername/auto_form_filler.git
   cd auto_form_filler
