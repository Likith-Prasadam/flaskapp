from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Store notes temporarily
notes = []

@app.route('/')
def home():
    return render_template('index.html', notes=notes)

@app.route('/add', methods=['POST'])
def add_note():

    note = request.form['note']

    if note:
        notes.append(note)

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)