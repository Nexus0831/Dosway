import json
import json_convert
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


if __name__ == '__main__':
    # app.run()
    print(json_convert.convert.json_convert())
