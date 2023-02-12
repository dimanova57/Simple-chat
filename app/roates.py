import sqlite3
from random import shuffle

from app import app
from flask import render_template, request, redirect

gr_list = []


def get_data():
    connection = sqlite3.connect("app/app.db")
    cursor = connection.cursor()
    cursor.execute("select name from groceries")
    all_data = cursor.fetchall()
    all_data = [i[0] for i in all_data]
    return all_data, gr_list


@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template("index.html", all_data=get_data()[0], gr_list=get_data()[1])


@app.route('/add', methods=['POST'])
def add():
    global gr_list
    selected = request.form['selected']
    gr_list.append(selected)
    return redirect('/')


@app.route('/delete', methods=['POST'])
def delete():
    main_list = request.form.getlist('selected')
    global gr_list
    for i in main_list:
        if i in gr_list:
            gr_list.remove(i)
    return redirect('/')
