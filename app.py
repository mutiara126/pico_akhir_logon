from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

# Define the flag
FLAG = "TI404{ini_flagnya_logon}"

# Users database
users = {
    "warkun": "osengayam"
}

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username in users and users[username] == password:
            return redirect(url_for('flag'))
        else:
            return "Invalid credentials! Please try again."
    return render_template('login.html')

@app.route('/flag')
def flag():
    return render_template('flag.html', flag=FLAG)

if __name__ == '__main__':
    app.run(debug=True)
