# Telegram Bot with OpenAI and Firebase Integration

## Description
This project is a **Telegram Bot** built using **OpenAI's GPT** for generating responses and **Firebase** for storing conversation histories.
The bot is designed to handle user interactions, including:
- Responding to user queries using OpenAI's GPT.
- Storing past conversation data in Firebase for a more personalized experience.
- Clearing conversation history upon user request.

---

## Features
- **Memory Storage**: Firebase Realtime Database is used to store conversation history for continued interactions.
- **Command Handling**:
  - `/start`: Starts the bot and provides a welcome message.
  - `/clear`: Clears the stored conversation history for the user.

---

## Installation and Setup

### Prerequisites
- Python 3.7 or higher
- Telegram Bot Token 
- OpenAI API Key
- Firebase Service Account JSON file

### Steps
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/telegram-bot-with-openai.git
   cd telegram-bot-with-openai
2. **Create a Virtual Environment**
   
3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt'
4. **Set Environment Variables:**
   ```bash
   set TELEGRAM_BOT_TOKEN=your-telegram-bot-token
   set OPENAI_API_KEY=your-openai-api-key
   set TELEGRAM_BOT_FIREBASE=path/to/firebase-key.json
   set FIREBASE_URL=https://your-firebase-database-url
5. **Run the bot**
   ```bash
   python main.py

# To-do list
- Deploy the bot on a cloud platform like AWS, Google Cloud, or Heroku for 24/7 availability.
- Add support for voice-to-text transcription for a more interactive user experience.
- Integrate Google Calendar for scheduling and reminders based on user input.
- Enable multilingual support for a wider audience.
