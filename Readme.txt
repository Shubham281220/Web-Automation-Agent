Web Automation Agent:
Web Automation Agent is a versatile web automation tool powered by OpenAI's GPT-4o-mini model and the browser_use library. This application allows users to input generic tasks related to web automation, such as logging into websites, fetching data, or performing specific actions. The Gradio-based web interface ensures an intuitive and user-friendly experience, making it accessible even to those with minimal technical expertise.

Prerequisites: Python 3.7 or higher

Installation: Extract the Zip File

How to run the code:
1. Create a Virtual Environment:
Windows:
python -m venv venv
venv\Scripts\activate

macOS/Linux:
python3 -m venv venv
source venv/bin/activate

2. Install dependencies:
pip install --upgrade pip
pip install -r requirements.txt
( All required Python packages are listed in requirements.txt.)

3. Configure OpenAI API Key:
Replace the empty string with your actual OpenAI API key.
openai_api_key = "your-openai-api-key-here"

4. Run the application:
python app.py

5. Access the Interface:
After running the above command, Gradio will provide a local URL (e.g., http://127.0.0.1:7860) in the terminal.
Open this URL in your web browser to access the Web Automation Agent interface.

6. Usage:
Enter Task Description:
describe the web automation task you want to perform. For example:
Log in or Sign up to Spotify and fetch the top 50 trending USA songs, displaying their titles, artist names, plays, album names, and durations.

7. Run the task. 

