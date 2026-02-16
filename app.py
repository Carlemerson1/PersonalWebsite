from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/portfolio')
def portfolio():
    return render_template('maintenance.html')

@app.route('/tutoring')
def tutoring():
    return render_template('tutoring.html')

if __name__ == '__main__':
    app.run(debug=True)


# **File structure:**
# /your-project
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