import os
import re
import json
import whisper
from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
USERS_FILE = "users.json"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

model = whisper.load_model("base")

# Utility to clean passphrase and transcript for comparison
def clean_phrase(phrase):
    phrase = re.sub(r'[^\w\s]', '', phrase)  # remove punctuation
    phrase = phrase.lower().strip()
    phrase = re.sub(r'\s+', ' ', phrase)
    return phrase

# Load all users
def load_users():
    if not os.path.exists(USERS_FILE):
        return {}
    with open(USERS_FILE, "r") as f:
        return json.load(f)

# Save all users
def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=2)

# Home/login page
@app.route('/')
def index():
    return render_template('index.html', access_denied=False)

# Success route with dynamic username
@app.route('/success/<username>')
def success(username):
    return render_template('success.html', username=username)

# Register page (GET + POST)
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get("username", "").strip()
        phrase = request.form.get("phrase", "").strip()

        if not username or not phrase:
            return render_template('register.html', error="Both fields are required.")

        users = load_users()
        if username in users:
            return render_template('register.html', error="User already exists. Try another name.")

        users[username] = phrase
        save_users(users)
        return redirect(url_for('index'))

    return render_template('register.html')

# Handle voice file and match passphrase
@app.route('/transcribe', methods=['POST'])
def transcribe_audio():
    if 'audio_file' not in request.files:
        return render_template('index.html', access_denied=True)

    file = request.files['audio_file']
    if file.filename == "":
        return render_template('index.html', access_denied=True)

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    result = model.transcribe(file_path)
    transcript = result["text"]
    print("Raw transcript:", transcript)

    cleaned_transcript = clean_phrase(transcript)
    print("Cleaned transcript:", cleaned_transcript)

    users = load_users()

    # Match user by comparing passphrases
    for username, stored_phrase in users.items():
        if clean_phrase(stored_phrase) == cleaned_transcript:
            print(f"Match found for user: {username}")
            return redirect(url_for('success', username=username))

    print("No match found.")
    return render_template('index.html', access_denied=True)

if __name__ == '__main__':
    app.run(debug=True)
