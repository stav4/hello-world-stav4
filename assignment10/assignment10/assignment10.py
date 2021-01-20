from flask import Flask, render_template, redirect, url_for, request, Blueprint
import mysql.connector
import pkgutil
import sys

assignment10 = Flask(__name__)
assignment10.secret_key = '124'
assignment10 = Blueprint('assignment10',
                         __name__,
                         static_folder='static',
                         static_url_path='/assignment10.html',
                         template_folder='templates')


def interact_db(query, query_type: str):
    return_value = False
    connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                         passwd='stav141S',
                                         database='myflask')

    cursor = connection.cursor(named_tuple=True)
    cursor.execute(query)
    if query_type == 'commit':
        connection.commit()
        return_value = True
    if query_type == 'fetch':
        query_result = cursor.fetchall()
        return_value = query_result
    connection.close()
    cursor.close()
    return return_value


@assignment10.route('/insert_user', methods=['GET', 'POST'])
def insert_user():
    if request.method == 'POST':
        firstName = request.form['firstName']
        lastName = request.form['lastName']
        email = request.form['email']
        query = "INSERT INTO Users(firstName,lastName, email) VALUES ('%s','%s','%s')" % (firstName, lastName, email)
        interact_db(query=query, query_type='commit')
        return redirect('/assignment10')

@assignment10.route('/update_row', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        firstName = request.form['firstName']
        lastName = request.form['lastName']
        email = request.form['email']
        query = "UPDATE Users SET lastName= '%s', email= '%s'  WHERE firstName = '%s';" % (lastName, email, firstName)
        interact_db(query=query, query_type='commit')
        return redirect('/assignment10')
    return 'update user details'


@assignment10.route('/assignment10', methods=['GET', 'POST'])
def Users():
    query = "select * from Users"
    query_result = interact_db(query=query, query_type='fetch')
    return render_template('assignment10.html', Users=query_result)


@assignment10.route('/delete_user', methods=['GET', 'POST'])
def delete_user():
    if request.method == 'GET':
        firstName = request.args.get('firstName')
        query = "DELETE FROM Users WHERE firstName ='%s';" % firstName
        interact_db(query=query, query_type='commit')
        return redirect('/assignment10')
