import re
from zipfile import ZipFile
from datetime import datetime
import openai

def extract_chat_file_from_zip(zip_path):
    print("Extracting chat from Zip File")
    with ZipFile(zip_path, 'r') as zip_ref:
        file_names = zip_ref.namelist()
        if file_names:
            with zip_ref.open(file_names[0]) as file:
                return file.read().decode('utf-8')
    return ""

def find_and_remove_previous_recaps(chat_content):
    print("Finding and removing previous Recaps")
    recap_start = chat_content.rfind('🤖🤖 GPT Recap')
    if recap_start != -1:
        recap_end = chat_content.find('\n[', recap_start)
        if recap_end != -1:
            return chat_content[recap_end+1:]
    return chat_content

def clean_chat_log(file_content):
    print("Cleaning Chat Log")
    return "\n".join([re.sub(r"\[\d{2}/\d{2}/\d{4}, \d{2}:\d{2}:\d{2}\]|\[\d{2}:\d{2} [APMapm]*\s?-?\s?", "", line).strip()
                      for line in file_content.split('\n') if line.strip()])

def chunk_chat_log(chat_log, chunk_size=128000):
    "Chunking Chat Log"
    chunks, current_chunk = [], []
    for line in chat_log.split('\n'):
        if len('\n'.join(current_chunk) + line) + 1 <= chunk_size:
            current_chunk.append(line)
        else:
            chunks.append('\n'.join(current_chunk))
            current_chunk = [line]
    chunks.append('\n'.join(current_chunk))
    if len(chunks) > 5:
        print("Error!Too many chunks!")
        return "Chunk Error! >5 chunks generated. Are you trying to recap the works of Shakespere?"
        raise ValueError("Error: The operation would generate more than 5 chunks, which is not allowed.")
    print(f"Number of chunks generated: {len(chunks)}")
    return chunks

def generate_recap_for_chunk(chunk, custom_prompt):
    print("Generating Recap for Chunk")
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": custom_prompt},
                {"role": "user", "content": chunk}
            ],
            temperature=0.7,
            max_tokens=4096
        )
        
        if response.choices:
            print("Recap generated!")
            return response.choices[0].message['content']
        else:
            print("Recap not available")
            return "Recap not available."
    except Exception as e:
        print(f"An error occurred: {e}")
        return "Recap not available due to an error."

def get_time_of_day():
    print("Determining Time of Day")
    current_hour = datetime.now().hour
    if current_hour < 12:
        return "Morning"
    elif current_hour < 18:
        return "Afternoon"
    else:
        return "Evening"
