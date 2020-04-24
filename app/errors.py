from flask import render_template
from app import app,db

from helper import escape

#ERROR Handling
@app.errorhandler(404)
def not_found_error(error):
    return render_template('error.html',code=str(error.code),text=escape(error.name)), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('error.html',code=str(error.code), text=escape(error.name)), 500