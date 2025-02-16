from flask import Flask, request, jsonify, render_template
import subprocess
import os

# Set the template folder to the current directory
template_dir = os.path.abspath(".")

app = Flask(__name__, template_folder=template_dir)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/run", methods=["POST"])
def run_code():
    code = request.json.get("code")
    try:
        # Execute Python code
        result = subprocess.run(
            ["python3", "-c", code],
            capture_output=True,
            text=True
        )
        output = result.stdout if result.returncode == 0 else result.stderr
        return jsonify({"output": output})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')