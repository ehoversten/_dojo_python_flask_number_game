# ------------------------------------------------------------------------------/
#   Assignment: Great Number Game
#       Objectives:
#         Practice using session to store data about a client's history with the web app
#          Practice clearing a session
#          Practice having the server use data submitted by a client with a form
#
# ------------------------------------------------------------------------------/


from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'bobby'

@app.route('/')
def index():
    randNum = random.randrange(0, 101)
    print('Randomly generated number is: ' + str(randNum))

    if 'randNum' not in session:
        session['randNum'] = randNum

    print('Session var: ' + str(session['randNum']))
    return render_template("index.html", randNum = session['randNum'])

@app.route('/guess', methods=['POST'])
def guess():

    print('Form Dict: ' + str(request.form))
    print('User Guess: ' + str(request.form['guess']))
    guess = request.form['guess']
    print('Random Number: ' + str(session['randNum']))
    # create session['keys']
    if 'win' not in session:
        session['win'] = ''
        session['color'] = ''

    # test logic - compare 'guess' to 'session['randNum']'
    if int(guess) == int(session['randNum']):
        session['win'] = 'correct'
        session['color'] = 'green'
        return render_template("index.html", guess=guess, win=session['win'], color=session['color'])
    elif int(guess) > int(session['randNum']):
        session['win'] = 'high'
        session['color'] = 'red'
        return render_template("index.html", guess=guess, win=session['win'], color=session['color'])
    elif int(guess) < int(session['randNum']):
        session['win'] = 'low'
        session['color'] = 'red'
        return render_template("index.html", guess=guess, win=session['win'], color=session['color'])

    print('Win State is: ' + str(win))
    return render_template("index.html", guess=guess, win=session['win'], color=session['color'])

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__=="__main__":

    app.run(debug=True)
