
from flask import Flask, render_template, redirect, request, session
import random, math


app = Flask(__name__)
app.secret_key = 'cookiegold'


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_money', methods=['post'])
def process_money():
    
    if 'gold' not in session:
        session['gold'] = 0
        session['activity'] = ''


    if request.form['building'] == 'farm':
        generate = random.randint(9,20)
        session['gold'] += generate
        session['activity'] += f"you found {session['gold']} gold "


    elif request.form['building'] == 'cave':
        generate = random.randint(5,10)
        session['gold'] += generate
        session['activity'] += f"you found {session['gold']} gold "

    elif request.form['building'] == 'house':
        generate = random.randint(2,5)
        session['gold'] += generate
        session['activity'] += f"you found {session['gold']} gold "

    elif request.form['building'] == 'casino':
        coinflip = random.randint(0,1)
        generate = random.randint(0,50)
        if (coinflip > 0):
            session['gold'] += generate
            session['activity'] += f"you found {session['gold']} gold "
        else:
            session['gold'] -= generate

            session['activity'] += f"you lost {math.trunc(math.fabs(session['gold']))} gold "

    return redirect('/')


@app.route('/reset')
def reset():
    session.clear()

    return redirect('/')







if __name__ == "__main__":
    app.run(debug=True)