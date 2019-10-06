from flask import Blueprint

bp = Blueprint('admin', __name__)

from tkrtxt.admin import routes
