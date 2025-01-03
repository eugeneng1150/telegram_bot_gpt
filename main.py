import os
from dotenv import load_dotenv
import requests
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from firebase_helper import save_conversation_to_firebase, get_conversation_from_firebase, clear_conversation_in_firebase

load_dotenv()
# Define your API keys
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
BOT_TOKEN = os.getenv("BOT_TOKEN")

def chat_with_gpt(prompt: str, user_id: int) -> str:
    """Send a prompt to OpenAI GPT with conversation history."""
    # Retrieve conversation history
    conversation = get_conversation_from_firebase(user_id)
    conversation.append({"role": "user", "content": prompt})

    data = {
        "model": "gpt-3.5-turbo",
        "messages": conversation,
        "max_tokens": 150,
        "temperature": 0.7,
    }

    try:
        response = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers={"Authorization": f"Bearer {OPENAI_API_KEY}", "Content-Type": "application/json"},
            json=data,
        )
        if response.status_code == 200:
            assistant_response = response.json().get("choices")[0].get("message", {}).get("content", "").strip()
            # Save GPT's response to Firebase
            save_conversation_to_firebase(user_id, "assistant", assistant_response)
            return assistant_response
        else:
            return f"API Error: {response.status_code} - {response.text}"
    except Exception as e:
        return f"Error: {str(e)}"

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle text messages and respond using GPT."""
    user_id = update.message.from_user.id
    user_message = update.message.text

    # Save the user's message
    save_conversation_to_firebase(user_id, "user", user_message)

    # Process with OpenAI GPT
    gpt_response = chat_with_gpt(user_message, user_id)

    # Send GPT response to the user
    await update.message.reply_text(gpt_response)

async def clear(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Clear conversation history."""
    user_id = update.message.from_user.id
    clear_conversation_in_firebase(user_id)
    await update.message.reply_text("Conversation history cleared.")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle the /start command."""
    await update.message.reply_text("Welcome! Send me a message, and I'll respond. Use /clear to reset your conversation history.")

def main() -> None:
    """Start the bot."""
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("clear", clear))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))

    app.run_polling()

if __name__ == "__main__":
    main()
