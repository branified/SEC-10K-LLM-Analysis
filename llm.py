import os
from dotenv import load_dotenv
from llamaapi import LlamaAPI
from utils import chunk_text

def analyze_text_file(text_file_path, line_ranges, insight=None):
    load_dotenv()

    # Initialize the SDK
    llama = LlamaAPI(os.getenv('LLAMA_API_KEY'))

    with open(text_file_path, "r", encoding="utf-8") as file:
        # Read all lines into a list
        all_lines = file.readlines()

    # Select specific lines based on line_ranges. This is because we only have free LLM API credits and do not want to go over for this demo.
    # This also ensures that we are passing the best data possible for the experiment.
    selected_lines = []
    for start_line, end_line in line_ranges:
        selected_lines.extend(all_lines[start_line:end_line+1])

    # If insight is "revenue", strip each line individually. This is because the revenue insight file has a lot of white spaces.
    if insight == "revenue":
        selected_lines = [line.strip() for line in selected_lines]
    
    # Concatenate the selected lines into text content
    text_content = "".join(selected_lines)

    # Chunk size that will fit token limit 2048 tokens/5 tokens per word
    MAX_CHUNK_SIZE = 400

    text_chunks = chunk_text(text_content, MAX_CHUNK_SIZE)

    # Array to store LLM responses
    insights = []

    for chunk in text_chunks:
        if insight == "risk":
        # Build the API request with the text chunk included
            api_request = {
                "messages": [
                    {"role": "user", "content": f"""You are a SEC-10K filing analyst. Your job is to look through this text and give a valuable insights on the risk factors 
                     that one can put in a dashboard. I want you to return the insights you see in bullet point format. Here is what I want you to analyze. Return only the bullet points. 
                     {chunk}"""},
                ],
            }
        elif insight == "revenue":
            api_request = {
                "messages": [
                    {"role": "user", "content": f"""You are a SEC-10K filing analyst. Your job is to look through this text and give a valuable insights on the revenue trends 
                     that one can put in a dashboard. From your analysis I want you to return only the total revenue after all the calculations. Here is what I want you to analyze. 
                     Return only the revenue after calculating expenses, fees, profit, etc. 
                     {chunk}"""},
                ],
            }
        else:
            api_request = {
                "messages": [
                    {"role": "user", "content": f"""You are a SEC-10K filing analyst. Your job is to look through this text and give a valuable insights on the management analysis 
                     that one can put in a dashboard. I will be passing these insights to a sentiment analysis so I want you to look through this text and return whether or not the text
                     is positive or negative. I want you to return the score between -1 and 1 where -1 is very negative and 1 is very positive and a sentence that exemplifies the score you gave.
                     I want you to return (score): (sentence). Here is what I want you to analyze: {chunk}"""},
                ],
            }
        # Execute the Request
        response = llama.run(api_request)
        insights.append(response.json()['choices'][0]['message']['content'])

    # Combine insights from all chunks
    combined_insights = "\n".join(insights)
    return combined_insights
