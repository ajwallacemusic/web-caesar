from flask import Flask, request
from caesar import rotate_string
import html

app = Flask(__name__)
app.config['DEBUG']=True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form method="POST">
            <label>Rotate by:</label>
            <input type="text" name="rot" value="0">
            <textarea name="text">{0}</textarea>
            <input type="submit">
        </form>
        <!-- create your form here -->
    </body>
</html>
"""

@app.route("/")
def index():
    enc_text = ""
    return form.format(enc_text)

@app.route("/", methods=["POST"])
def encrypt():
    rot = request.form['rot']
    rot = int(rot)
    text = request.form['text']

    enc_text = html.escape(rotate_string(text, rot))

    return form.format(enc_text)


app.run()