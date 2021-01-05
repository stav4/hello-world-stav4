from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    username = 'stav'
    return 'helo'


@app.route('/Stav Ben Shoshan CV')
def cv():
    return render_template('Stav Ben Shoshan CV.html')


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
