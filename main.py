from flask import Flask, jsonify
import gspread
from google.oauth2.service_account import Credentials

app = Flask(__name__)

# Google Sheets setup
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
SERVICE_ACCOUNT_FILE = "/Users/akashaggarwal/Desktop/CustomGPT_backend/service_account.json"  # Path to your JSON file
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

if __name__ == '__main__':
    app.run(port=5000)
