"""Basic program."""

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello_name():
    """Function1."""
    return render_template('Lbasic.html')

if __name__ == '__main__':
    app.run(host='192.168.1.12', port=2009)
