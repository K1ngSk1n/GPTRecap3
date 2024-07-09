from flask import Blueprint, request, render_template, redirect, flash
from .utils import extract_chat_file_from_zip, find_and_remove_previous_recaps, clean_chat_log, chunk_chat_log, generate_recap_for_chunk, get_time_of_day
import openai
from datetime import datetime

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        OPENAI_API_KEY = request.form.get('apikey')
        if not OPENAI_API_KEY:
            flash('API Key is required')
            return redirect(request.url)
        
        openai.api_key = OPENAI_API_KEY

        if 'file' not in request.files or request.files['file'].filename == '':
            flash('No selected file')
            return redirect(request.url)
        
        file = request.files['file']
        custom_prompt = request.form.get('prompt')
        
        if file and file.filename.endswith('.zip'):
            chat_content = extract_chat_file_from_zip(file)
            cleaned_chat = find_and_remove_previous_recaps(chat_content)
            cleaned_chat = clean_chat_log(cleaned_chat)
            chat_chunks = chunk_chat_log(cleaned_chat)
            recaps = [generate_recap_for_chunk(chunk, custom_prompt) for chunk in chat_chunks]
            day_date = datetime.now().strftime("%A %d %B")
            time_of_day = get_time_of_day()
            recap_header = f"🤖🤖 GPT Recap Generated {day_date} {time_of_day} 🤖🤖\n"
            full_recap = recap_header + "\n".join(recaps)
            return render_template('recap.html', recap=full_recap)

        else:
            flash('Invalid file format. Please attach a ZIP file from WhatsApp.')
            return redirect(request.url)
    
    return render_template('index.html')
