from flask import Flask, redirect, url_for, render_template, request, session, Blueprint, jsonify
import mysql.connector

import pkgutil
import sys

app = Flask(__name__)
app.secret_key = '123'
userslist = [{'FirstName': 'Stav', 'LastName': 'Ben Shoshan'},
             {'FirstName': 'Roy', 'LastName': 'Cohen'},
             {'FirstName': 'Carmel', 'LastName': 'Ben Shoshan'}]

from assignment10.assignment10 import assignment10

app.register_blueprint(assignment10)


@app.route('/')
def hello_world():
    userName = 'stav'
    return 'helo'


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


@app.route('/Stav Ben Shoshan CV')
def cv():
    return render_template('Stav Ben Shoshan CV.html')


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    session.pop('username', '')
    return redirect(url_for("ass9"))


@app.route('/assignment9', methods=['GET', 'POST'])
def ass9():
    username = ''
    usersearch = None
    userInList = False
    isEmpty = False
    userDet = ''
    if request.method == 'POST':
        username = request.form['username']
        session['username'] = username
    if request.method == 'GET':
        usersearch = request.args.get('usersearch')
        userInList, userDet = findUser(usersearch, userslist)
    if usersearch == '':
        isEmpty = True
    return render_template('assignment9.html', username=username, usersearch=usersearch,
                           userInList=userInList, isEmpty=isEmpty, userslist=userslist, userDet=userDet)


def findUser(usersearch, userslist):
    userDet = ''
    userInList = False
    for user in userslist:
        for value in user.values():
            if usersearch == value:
                userInList = True
                userDet = user
    return userInList, userDet


@app.route('/assignment8')
def ass8():
    username = {'firstName': 'Stav', 'LastName': 'Ben Shoshan', 'gender': 'male'}
    hobbies = ['travel', 'play the guitar', 'watch netflix']
    music = ['Aviv Gefen', 'Berry sakharof', 'Billie eilish']
    return render_template('assignment8.html', user=username, hobbies=hobbies, music=music)


@app.route('/assignment82')
def ass82():
    username = {'firstName': 'Stav', 'LastName': 'Ben Shoshan', 'gender': 'male'}
    hobbies = ['travel', 'play the guitar', 'watch netflix']
    music = ['Aviv Gefen', 'Berry sakharof', 'Billie eilish']
    return render_template('assignment82.html', user=username, hobbies=hobbies, music=music)


@app.route('/userList')
def userList():
    return render_template('userList.html')


# -----------------------------------------------------

@app.route('/Users')
def Users():
    query = "select * from users"
    query_result = interact_db(query=query, query_type='fetch')
    return render_template('userList.html', users=query_result)


@app.route('/insert_user', methods=['GET', 'POST'])
def insert_user():
    if request.method == 'POST':
        ID = request.form['ID']
        firstName = request.form['firstName']
        lastName = request.form['lastName']
        email = request.form['email']
        query = "INSERT INTO users(ID, first_name,last_name, email) VALUES ('%s','%s','%s','%s')" % (
            ID, firstName, lastName, email)
        interact_db(query=query, query_type='commit')
        return redirect('/users')
    return render_template('insert_user.html', req_method=request.method)


@app.route('/delete_user', methods=['GET', 'POST'])
def delete_user():
    if request.method == 'GET':
        ID = request.args.get('ID')
        query = "DELETE FROM users WHERE ID ='%s';" % ID
        interact_db(query=query, query_type='commit')
        return redirect('/users')

    return 'deleted user'


@app.route('/assignment11/users')
def get_users():
    if request.method == 'GET':
        query = "select * from users"
        query_result = interact_db(query=query, query_type='fetch')
    if (len(query_result) == 0):
        return jsonify({
            'Success': 'False',
            'Error': 'There is no users data'
        })
    else:
        return jsonify({
            'success': 'True',
            'data': query_result
        })


@app.route('/assignment11/users/selected/', defaults={'ID': 00})
@app.route('/assignment11/users/selected/<int:ID>')
def get_user_by_id(ID):
    if request.method == "GET":
        query = "SELECT * FROM users where ID ='%s'" % ID
        query_result = interact_db(query=query, query_type='fetch')
    if (len(query_result) == 0):
        return jsonify({
            'success': 'False',
            'Error': 'User does not exist'
        })
    else:
        return jsonify({
            'success': 'True',
            'data': query_result[0]
        })

if __name__ == '__main__':
    app.run(debug=True)
