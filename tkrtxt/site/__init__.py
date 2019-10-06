from flask import Blueprint


bp = Blueprint('site', __name__,)

from tkrtxt.site import routes
