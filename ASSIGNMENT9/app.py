from flask import Flask, redirect, url_for, render_template, request, session

app = Flask(__name__)
app.secret_key = '123'
userslist = [{'FirstName': 'Stav', 'LastName': 'Ben Shoshan'},
             {'FirstName': 'Roy', 'LastName': 'Cohen'},
             {'FirstName': 'Carmel', 'LastName': 'Ben Shoshan'}]


@app.route('/')
def hello_world():
    userName = 'stav'
    return 'helo'


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


if __name__ == '__main__':
    app.run(debug=True)


@app.route('/userList')
def userList():
    return render_template('userList.html')
