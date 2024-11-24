# Web Automation Agent

**Web Automation Agent** is a versatile web automation tool powered by OpenAI's GPT-4o-mini model and the `browser_use` library. This application allows users to input generic tasks related to web automation, such as logging into websites, fetching data, or performing specific actions. The Gradio-based web interface ensures an intuitive and user-friendly experience, making it accessible even to those with minimal technical expertise.

---

## Prerequisites
- Python 3.7 or higher

---

## Installation
1. **Extract the ZIP File**
   - Download and extract the provided ZIP file to your desired location.

---

## How to Run the Code

### Step 1: Create a Virtual Environment
- **For Windows:**
  ```bash
  python -m venv venv
  venv\Scripts\activate
  ```

- **For macOS/Linux:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### Step 2: Install Dependencies
- Upgrade `pip`:
  ```bash
  pip install --upgrade pip
  ```
- Install required Python packages:
  ```bash
  pip install -r requirements.txt
  ```
  (All required Python packages are listed in `requirements.txt`.)

### Step 3: Configure OpenAI API Key
- Replace the empty string in the code with your actual OpenAI API key:
  ```python
  openai_api_key = "your-openai-api-key-here"
  ```

### Step 4: Run the Application
- Execute the application:
  ```bash
  python app.py
  ```

### Step 5: Access the Interface
- After running the above command, Gradio will provide a local URL in the terminal (e.g., `http://127.0.0.1:7860`).
- Open this URL in your web browser to access the Web Automation Agent interface.

### Step 6: Usage
1. **Enter Task Description:**  
   Describe the web automation task you want to perform. For example:
   ```
   Log in or Sign up to Spotify and fetch the top 50 trending USA songs, displaying their titles, artist names, plays, album names, and durations.
   ```

2. **Run the Task:**  
   Click the appropriate button to execute the described task.

---

## Features
- **AI-Powered Automation:** Automates tasks using the GPT-4o-mini model.
- **User-Friendly Interface:** Simplified web interface powered by Gradio.
- **Custom Task Execution:** Handles tasks like logging in, data fetching, and other specific actions.

---

## Technologies Used
- **Backend:** Python, OpenAI GPT-4o-mini
- **Frontend:** Gradio
- **Automation Library:** browser_use
