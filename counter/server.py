from flask import Flask, render_template, request, redirect, session
import os
app = Flask(__name__)
app.secret_key = os.urandom(16)


@app.route('/')
def index():
    

    if 'counter' not in session:
        session['counter'] = 1
    else:
      session['counter'] += 1

    return render_template("index.html", counter=session['counter'])


@app.route('/enter')
def refresh():
    session['counter'] += 1        

    return redirect('/')


@app.route('/reset')
def reset():
    session['counter'] = 0        

    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
