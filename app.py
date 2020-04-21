from flask import Flask, render_template

app = Flask(__name__)
app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True

# Home Page
@app.route('/')
def index():
    return render_template('index.html')

# Resume Page
@app.route('/resume')
def resume():
    return render_template('resume.html')
