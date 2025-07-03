from flask import Flask, render_template, request
from text_summary import summarizer

app = Flask(__name__)  # Corrected instantiation

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['GET', 'POST'])
def analyze():
    if request.method == 'POST':
        rawtext = request.form['rawtext']
        summary, original_txt, len_orig_txt, len_summary = summarizer(rawtext)  # Corrected variable name
        return render_template('summary.html', summary=summary, original_txt=original_txt, len_orig_txt=len_orig_txt, len_summary=len_summary)
    return render_template('index.html')  # Optional: redirect to form if not POST

if __name__ == '__main__':  # Corrected check for main
    app.run(debug=True)
