# Article-Summarizer
Text Summarizer Web App
A simple web application built with Flask that automatically generates a concise summary of any input text. It leverages basic Python logic (or can integrate NLP models) to produce a shortened version of the original content.

**Features**
  Submit large blocks of raw text
  Get a summarized version instantly
  View word count comparison between original and summary
  Styled using Bootstrap and custom CSS
  Simple, responsive UI
**Tech Stack**
  Backend	Python, Flask
  Frontend	HTML5, CSS3, Bootstrap 4
  Text Processing	Custom summarizer logic (replaceable with NLP models like BART or T5)

**Installation & Setup**
  1. Clone the repository
    git clone https://github.com/yourusername/text-summarizer-flask.git
    cd text-summarizer-flask
  2. Create a virtual environment
    python -m venv venv
    source venv/bin/activate   # On Windows: venv\Scripts\activate
  3. Install dependencies
    pip install -r requirements.txt
  4. Run the app
      python app.py
  5. Open your browser and go to:
      http://127.0.0.1:5000/

**Project Structure**
text_summarizer/
│
├── app.py                  # Main Flask application
├── text_summary.py         # Text summarization logic
├── static/
│   └── style.css           # Custom CSS styling
├── templates/
│   ├── index.html          # Form for user input
│   └── summary.html        # Display summarized results
├── requirements.txt
└── README.md
