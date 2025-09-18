from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/sponsors')
def sponsors():
    return render_template('sponsors.html')

@app.route('/robots/jona')
def jona():
    return render_template('jona.html')

if __name__ == '__main__':
    app.run(debug=True)