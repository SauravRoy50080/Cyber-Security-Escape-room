from flask import Flask, render_template, request, session, redirect, url_for
import os

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Change this in production!

# Ensure session directory exists
os.makedirs('sessions', exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/puzzle1', methods=['GET', 'POST'])
def puzzle1():
    if request.method == 'POST':
        answer = request.form.get('answer').lower().strip()
        if answer == 'biometric research database':
            session['puzzle1_solved'] = True
            return redirect(url_for('puzzle2'))
        else:
            return render_template('puzzle1.html', error="Incorrect answer. Try again!")
    return render_template('puzzle1.html')

@app.route('/puzzle2', methods=['GET', 'POST'])
def puzzle2():
    if not session.get('puzzle1_solved'):
        return redirect(url_for('puzzle1'))
    
    if request.method == 'POST':
        answer = request.form.get('answer').strip()
        if answer == '192.168.1.100':
            session['puzzle2_solved'] = True
            return redirect(url_for('puzzle3'))
        else:
            return render_template('puzzle2.html', error="Incorrect IP address. Try again!")
    return render_template('puzzle2.html')

@app.route('/puzzle3', methods=['GET', 'POST'])
def puzzle3():
    if not session.get('puzzle2_solved'):
        return redirect(url_for('puzzle2'))
    
    if request.method == 'POST':
        answer = request.form.get('answer').lower().strip()
        if answer == 'creating backdoor and exfiltrating data':
            session['puzzle3_solved'] = True
            return redirect(url_for('puzzle4'))
        else:
            return render_template('puzzle3.html', error="Incorrect analysis. Try again!")
    return render_template('puzzle3.html')

@app.route('/puzzle4', methods=['GET', 'POST'])
def puzzle4():
    if not session.get('puzzle3_solved'):
        return redirect(url_for('puzzle3'))
    
    if request.method == 'POST':
        answer = request.form.get('answer').strip()
        if answer == 'powershell':
            session['puzzle4_solved'] = True
            return redirect(url_for('puzzle5'))
        else:
            return render_template('puzzle4.html', error="Incorrect language. Try again!")
    return render_template('puzzle4.html')

@app.route('/puzzle5', methods=['GET', 'POST'])
def puzzle5():
    if not session.get('puzzle4_solved'):
        return redirect(url_for('puzzle4'))
    
    if request.method == 'POST':
        answer = request.form.get('answer').strip()
        if answer == 'taylor smith':
            session['puzzle5_solved'] = True
            return redirect(url_for('success'))
        else:
            return render_template('puzzle5.html', error="Incorrect suspect. Try again!")
    return render_template('puzzle5.html')

@app.route('/success')
def success():
    if not session.get('puzzle5_solved'):
        return redirect(url_for('puzzle5'))
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
