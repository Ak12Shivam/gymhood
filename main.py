from flask import Flask, render_template

app = Flask(__name__)

# Route 1 – loads index1.html
@app.route('/')
@app.route('/index1.html')
def load_index1():
    return render_template('index1.html')

# Route 2 – loads index2.html
@app.route('/index2.html')
def load_page2():
    return render_template('index2.html')

if __name__ == "__main__":
    app.run(debug=True)
