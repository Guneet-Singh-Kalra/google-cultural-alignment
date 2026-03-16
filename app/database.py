import firebase_admin
from firebase_admin import credentials, firestore
import os
from dotenv import load_dotenv

load_dotenv()

# Initialize Firebase
cred_path = os.getenv("FIREBASE_SERVICE_ACCOUNT_PATH")

if not firebase_admin._apps:
    cred = credentials.Certificate(cred_path)
    firebase_admin.initialize_app(cred)

# Export the db variable
db = firestore.client()