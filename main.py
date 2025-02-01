from flask import Flask, jsonify
import gspread
import os
from google.oauth2.service_account import Credentials

app = Flask(__name__)

# Google Sheets setup
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
# Set the default path for the service account file
SERVICE_ACCOUNT_FILE = "/etc/secrets/service_account.json"  # Path where Render stores secret files
SPREADSHEET_ID = "1FCdaPQssDNfu1LrYA-bL-H_XwS6S3v2MUrqdXVE2W68"  # Extract this from the Google Sheet URL

# Authenticate and connect to Google Sheets
creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
client = gspread.authorize(creds)
sheet = client.open_by_key(SPREADSHEET_ID).sheet1

@app.route('/fetch-scripts', methods=['GET'])
def fetch_scripts():
    try:
        # Fetch all rows from the sheet
        data = sheet.get_all_records()
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
@app.route('/', methods=['GET'])
def home():
    return "Welcome to the Custom GPT Fetch Scripts API!", 200

if __name__ == '__main__':
    app.run(port=5000)
