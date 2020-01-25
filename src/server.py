from flask import Flask, request
from io import StringIO
import sys
import os

app = Flask(__name__)

@app.route("/execute")
def execute():
    command = "=".join(request.args).replace("\\n", "\n").replace("\\t", "\t")
    save_out = sys.stdout
    sys.stdout = StringIO()
    output = sys.stdout
    exec(command)
    sys.stdout = save_out
    return output.getvalue()


@app.route("/")
def main():
    return os.environ.get("SECRET_MESSAGE", "Welcome to my super secure site.")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8090", debug=True)

