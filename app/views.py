import time, random

from flask import render_template, url_for
from app import app

@app.route('/')
@app.route('/index')
@app.route('/home')
def index():

    number=0
    if time.time()%10>9:
        number=random.randint(1,3)

    return render_template('home.html',number=number)

@app.route('/robots.txt')
#@app.route('/sitemap.xml')
def static_from_root():
        return send_from_directory(app.static_folder, request.path[1:])

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    errors=[str(e)]
    return render_template('500.html',errors=errors), 500
