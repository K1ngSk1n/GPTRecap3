# GPT Recap

Welcome to **GPT Recap**, a Flask web application that generates recaps from WhatsApp group chat exports. This project is © Edd White but is free for public, non-commercial use. For commercial use, please contact me at [eddwhite@me.com](mailto:eddwhite@me.com).

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)
- [Contact](#contact)

## Introduction

GPT Recap is a web application and iOS shortcut built with Flask and powered by OpenAI's GPT-4O model. It allows users to upload WhatsApp chat exports and generate concise recaps of the conversations. You can use one of the default prompts, or create a custom prompt in both the iOS Shortcut and the web app.

## Features
- Upload WhatsApp chat exports in ZIP format
- Clean and preprocess chat logs
- Generate recaps using OpenAI's GPT-4 model
- Customize the recap prompt for different contexts (friends, work, custom)
- Copy generated recaps to clipboard

## Requirements
- Python 3.9+
- Flask
- Gunicorn
- OpenAI Python client

## Installation

### Clone the Repository
"
    ```bash
    git clone https://github.com/eddwhite/gpt-recap.git
    cd gpt-recap?

### Set Up a Virtual Environment
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

### Install dependencies
    pip install -r requirements.txt

## Usage
### Running the application
Run the flask app with Gunicorn
    gunicorn --bind 0.0.0.0:8008 run:app

### Access the Application
Open your web browser and navigate to http://localhost:8008.

### API Key
To use the application, you will need an OpenAI API key. You can obtain one from OpenAI.

### iOS Shortcut
Install the iOS Shortcut on to you device. Edit the shortcut and insert your API key and edit the prompts if you need.

### Usage
In WhatsApp, go to Settings -> Chats -> Export and select the chat you wish to be recapped. Export the chat without media. From the share screen in iOS, select the recap shortcut. If using the web app, download the chat. Upload the zip file to the web app and insert secret key. Choose which style of recap you would like. The recap will generate and display on screen. You can then use the copt to clipboard option

## License
© Edd White. Free for public, non-commercial use. For commercial use, please contact eddwhite@me.com.

## Contact
Twitter: @eddwhite
Instagram: @eddiethegeeza
Email: eddwhite@me.com
