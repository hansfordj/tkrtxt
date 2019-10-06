from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from tkrtxt.admin import bp


@bp.route('/')
def admin():
     return render_template('admin/admin.html')
