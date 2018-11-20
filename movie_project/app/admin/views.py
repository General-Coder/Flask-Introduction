from flask import Blueprint, render_template, redirect, url_for

admin = Blueprint('admin',__name__,url_prefix='/admin')

@admin.route('/')
def index():
    return "<h1 style='color:red'>this is admin</h1>"

@admin.route('/login/')
def login():
    return render_template('admin/login.html')

@admin.route('/logout/')
def logout():
    return redirect(url_for('admin.login'))