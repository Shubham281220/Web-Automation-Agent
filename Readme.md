# Web Automation Agent

## Description
Web Automation Agent is a versatile web automation tool powered by OpenAI's GPT-4o-mini model and the `browser_use` library. This application allows users to input generic tasks related to web automation, such as logging into websites, fetching data, or performing specific actions. The Gradio-based web interface ensures an intuitive and user-friendly experience, making it accessible even to those with minimal technical expertise.

## Prerequisites
- **Python 3.7 or higher**

## Installation

1. **Extract the Zip File**
   - Unzip the provided archive to your desired directory.

## How to Run the Code

### 1. Create a Virtual Environment

- **Windows:**
  ```bash
  python -m venv venv
  venv\Scripts\activate
macOS/Linux:
bash
Copy code
python3 -m venv venv
source venv/bin/activate
2. Install Dependencies
bash
Copy code
pip install --upgrade pip
pip install -r requirements.txt
All required Python packages are listed in requirements.txt.

3. Configure OpenAI API Key
Open app.py in a text editor.
Locate the line containing openai_api_key = " ".
Replace the empty string with your actual OpenAI API key:
python
Copy code
openai_api_key = "your-openai-api-key-here"
4. Run the Application
bash
Copy code
python app.py
5. Access the Interface
After running the above command, Gradio will provide a local URL (e.g., http://127.0.0.1:7860) in the terminal. Open this URL in your web browser to access the Web Automation Agent interface.

Usage
Enter Task Description:

Describe the web automation task you want to perform. For example:
css
Copy code
Log in or Sign up to Spotify and fetch the top 50 trending USA songs, displaying their titles, artist names, plays, album names, and durations.
Run the Task:

Click the "Run Task" button to execute the task.
