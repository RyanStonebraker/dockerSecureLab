from flask import Flask, request
from io import StringIO
import sys

app = Flask(__name__)

@app.route("/execute")
def execute():
    command = "=".join(request.args).replace("\\n", "\n").replace("\\t", "\t")
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    output = sys.stdout
    exec(command)
    sys.stdout = old_stdout
    return output.getvalue()


@app.route("/")
def main():
    return "Welcome to my super secure site."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8090", debug=True)

