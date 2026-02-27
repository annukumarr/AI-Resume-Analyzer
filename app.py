from flask import Flask, render_template, request
from resume_parser import extract_text
from skill_matcher import detect_skills, suggest_missing, calculate_score, detect_role

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    detected = []
    missing = []
    score = None
    role = None

    if request.method == 'POST':
        file = request.files['resume']
        text = extract_text(file)
        detected = detect_skills(text)
        missing = suggest_missing(detected)
        score = calculate_score(detected)
        role = detect_role(detected)

    return render_template('index.html',
                           detected=detected,
                           missing=missing,
                           score=score,
                           role=role)

if __name__ == "__main__":
    app.run(debug=True)