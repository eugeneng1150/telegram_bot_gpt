import firebase_admin
from firebase_admin import credentials, db
import os
from dotenv import load_dotenv
load_dotenv()
TELEGRAM_BOT_FIREBASE = os.getenv("TELEGRAM_BOT_FIREBASE")
FIREBASE_URL = os.getenv("FIREBASE_URL")
# Firebase Initialization
def initialize_firebase():
    """Initialize Firebase app if not already initialized."""
    try:
        # Check if Firebase app is already initialized
        firebase_admin.get_app()
    except ValueError:
        # Initialize Firebase
        cred = credentials.Certificate(TELEGRAM_BOT_FIREBASE)
        firebase_admin.initialize_app(cred, {
            "databaseURL": FIREBASE_URL
        })

# Call Firebase initialization
initialize_firebase()

def save_conversation_to_firebase(user_id: int, role: str, content: str):
    """Save a message to Firebase."""
    ref = db.reference(f"conversations/{user_id}")
    conversation = ref.get() or []
    conversation.append({"role": role, "content": content})
    ref.set(conversation)

def get_conversation_from_firebase(user_id: int):
    """Retrieve conversation history from Firebase."""
    ref = db.reference(f"conversations/{user_id}")
    return ref.get() or []

def clear_conversation_in_firebase(user_id: int):
    """Clear conversation history from Firebase."""
    ref = db.reference(f"conversations/{user_id}")
    ref.delete()
