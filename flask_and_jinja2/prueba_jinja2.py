#!/usr/bin/python3

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    table = []
    for x in range(0, 10):
        y = 2 * x
        table.append((x, y))
    return render_template('index.html', data=table)


if __name__ == '__main__':
    app.run(debug=True)