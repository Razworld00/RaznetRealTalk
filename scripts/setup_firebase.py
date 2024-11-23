# Firebase setup script
import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate("path/to/serviceAccountKey.json")
firebase_admin.initialize_app(cred, {"databaseURL": "https://your-database.firebaseio.com"})
print("Firebase setup complete.")
