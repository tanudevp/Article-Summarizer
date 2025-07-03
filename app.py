from flask import flask,render_template,request
from text_summary import summarizer
app=flask(_name_)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze',methods=['GET','POST'])
def analyze():
    if request.method=='POST':
        rawtext=request.form['rawtext']
        summary,original_txt,len_orig_txt,len_summary=summarizer(rawdocs)
    return render_template('summary.html',summary=summary,original_txt=original_txt,len_orig_txt=len_orig_txt,len_summary=len_summary)
if _name=="main_":
    app.run(debug=True)
