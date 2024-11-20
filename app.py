import gradio as gr
import asyncio
import re
from langchain_openai import ChatOpenAI
from browser_use import Agent

# Your OpenAI API key 
openai_api_key = "Enter your API key"

def remove_unwanted_characters(text):
    text = text.replace('**', '')
    
    # Remove markdown links [text](url) -> text
    text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text)
    
    return text

# Asynchronous function to run the agent
async def run_agent(task):
    try:
        # Initialize the ChatOpenAI model with "gpt-4o-mini"
        llm = ChatOpenAI(model="gpt-4o-mini", api_key=openai_api_key)
        
        # Create the Agent with the task and LLM
        agent = Agent(task=task, llm=llm)
        
        # Run the agent
        result = await agent.run()
        
        # Extract the main text from the result
        main_text = ""
        if isinstance(result, tuple) and len(result) > 0:
            first_item = result[0]
            if hasattr(first_item, 'text'):
                main_text = first_item.text
            elif isinstance(first_item, dict) and 'text' in first_item:
                main_text = first_item['text']
            else:
                main_text = str(first_item)
        elif isinstance(result, (list, tuple)):
            # If result is a list or tuple, concatenate all text elements
            texts = []
            for item in result:
                if hasattr(item, 'text'):
                    texts.append(item.text)
                elif isinstance(item, dict) and 'text' in item:
                    texts.append(item['text'])
                else:
                    texts.append(str(item))
            main_text = "\n".join(texts)
        elif hasattr(result, 'text'):
            main_text = result.text
        else:
            main_text = str(result)
        
        # Clean the extracted text
        cleaned_text = remove_unwanted_characters(main_text)
        
        return cleaned_text
    
    except Exception as e:
        # Return any errors encountered
        return f"An error occurred: {str(e)}"

# Define the Gradio interface
def build_interface():
    with gr.Blocks() as app:
        gr.Markdown("# Web Automation Agent")
        gr.Markdown("Enter any task you'd like to automate on a website.")
        
        # Task Input Box
        task_input = gr.Textbox(
            label="Enter Task Description",
            placeholder="e.g., Log in to Spotify and fetch top 50 trending Bollywood songs."
        )
        
        # Output Display
        output = gr.Textbox(label="Task Result")
        
        # Button to Trigger the Agent
        run_button = gr.Button("Run Task")
        run_button.click(fn=run_agent, inputs=task_input, outputs=output)
    
    return app

# Launch the Gradio app
if __name__ == "__main__":
    app = build_interface()
    app.launch()  
