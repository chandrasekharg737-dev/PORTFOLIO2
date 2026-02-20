from flask import Flask, render_template, send_from_directory, request, jsonify
import os
from groq import Groq

app = Flask(__name__)

# Configuration
app.config['RESUME_FILENAME'] = 'G ROSHNI PROFFESIONAL RESUME.pdf'
app.config['RESUME_PATH'] = os.path.abspath(app.config['RESUME_FILENAME'])
app.config['GROQ_API_KEY'] = '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'

# Initialize Groq Client
client = Groq(api_key=app.config['GROQ_API_KEY'])

# Load Resume Content
RESUME_CONTENT = ""
try:
    with open("resume_text.txt", "r", encoding="utf-8") as f:
        RESUME_CONTENT = f.read()
except Exception as e:
    print(f"Error loading resume text: {e}")
    RESUME_CONTENT = "Resume content not available."

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/download_resume')
def download_resume():
    directory = os.path.dirname(app.config['RESUME_PATH'])
    filename = os.path.basename(app.config['RESUME_PATH'])
    return send_from_directory(directory, filename, as_attachment=True)

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    if not user_message:
        return jsonify({'error': 'No message provided'}), 400

    system_prompt = f"""You are a helpful AI assistant for G Roshni's portfolio website. 
    Your goal is to answer questions about Roshni based ONLY on her resume content provided below.
    Be professional, concise, and friendly. If the answer is not in the resume, say you don't know but can forward the inquiry.
    
    RESUME CONTENT:
    {RESUME_CONTENT}
    """

    try:
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message}
            ],
            temperature=0.7,
            max_tokens=200,
            top_p=1,
            stream=False,
            stop=None,
        )
        ai_response = completion.choices[0].message.content
        return jsonify({'response': ai_response})
    except Exception as e:
        print(f"Groq API Error: {e}")
        return jsonify({'error': 'Failed to get response from AI'}), 500

if __name__ == '__main__':
    app.run(debug=True)
