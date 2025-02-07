# AI FAQ Chatbot with Voice Recognition

## Description
An intelligent chatbot built with Rasa framework that handles frequently asked questions (FAQs) with added voice input capability. The chatbot uses Natural Language Processing (NLP) to understand user queries and provide appropriate responses.

## Features
- Natural Language Understanding (NLU) for intent recognition
- Voice input support using Speech-to-Text
- Custom action server for handling complex responses
- Configurable FAQ responses
- Multi-turn conversation capabilities

## Tech Stack
- Rasa Framework
- Python
- SpeechRecognition
- PyAudio
- Google Cloud Speech API

## Project Structure
rasa_chatbot/
│
├── data/
│   ├── nlu.yml
│   ├── stories.yml
│   └── rules.yml
│
├── actions/
│   └── actions.py
    └── voice_input.py    
│
├── models/
      └── requirements.txt
│
├── config.yml           # Model configuration
├── domain.yml          # Bot responses and intents

## Setup
1. Create a virtual environment
```bash
conda create -n rasa_bot python=3.10
conda activate rasa_bot
2. Install dependencies
```bash
pip install -r requirements.txt
3. Train the model
```bash
rasa train
4.Run the bot
```bash
rasa run actions --port 5058   
rasa shell --endpoints endpoints.yml

## Usage
- Start chatting with the bot using text input  
- Use voice commands (if configured)  
- Ask FAQs about products, services, or support  

## Features To Be Added

- Web interface integration  
- More training data  
- Enhanced voice recognition  
- Multi-language support  
- Integration with external APIs  
