from flask import render_template
from app import db
from helper import escape
from app.errors import bp

#ERROR Handling
@bp.app_errorhandler(404)
def not_found_error(error):
    return render_template('errors/error.html',code=str(error.code),text=escape(error.name)), 404

@bp.app_errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('errors/error.html',code=str(error.code), text=escape(error.name)), 500