from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@app.route('/tutoring')
def tutoring():
    return render_template('tutoring.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)


# **File structure:**
# /PersonalWebsite
#   /static
#     /css
#       main.css
#       nav.css
#     /images
#       (your images)
#     /js
#       nav.js
#   /templates
#     base.html
#     home.html
#     portfolio.html
#     tutoring.html
#   app.py`