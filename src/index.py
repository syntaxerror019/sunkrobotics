from flask import Flask, render_template

app = Flask(__name__)

@app.after_request
def add_cache_headers(response):
    # type of files to cache;
    cache_types = ["image/", "video/", "audio/"]

    if any(response.content_type.startswith(t) for t in cache_types):
        #store them in cache for no more than 30 days.
        response.headers["Cache-Control"] = "public, max-age=2592000"
    else:
        response.headers["Cache-Control"] = "no-store"

    return response

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

@app.route('/jona')
def jona():
    return render_template('jona.html')

@app.route('/jena')
def jena():
    return render_template('jena.html')

@app.route('/steve')
def steve():
    return render_template('steve.html')

if __name__ == '__main__':
    app.run(debug=True)
