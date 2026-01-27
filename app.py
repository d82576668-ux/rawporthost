from flask import Flask, request, Response, redirect
import os

app = Flask(__name__)

TEXT_FILE = "ports.txt"

@app.route("/raw")
def raw():
    if os.path.exists(TEXT_FILE):
        with open(TEXT_FILE, "r", encoding="utf-8") as f:
            return Response(f.read(), mimetype="text/plain")
    return Response("", mimetype="text/plain")

@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        with open(TEXT_FILE, "w", encoding="utf-8") as f:
            f.write(request.form["text"])
        return redirect("/edit")

    text = ""
    if os.path.exists(TEXT_FILE):
        with open(TEXT_FILE, "r", encoding="utf-8") as f:
            text = f.read()

    return f"""
    <html>
    <body>
        <form method="POST">
            <textarea name="text" style="width:100%;height:300px;">{text}</textarea><br>
            <button>Save</button>
        </form>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
