from flask import Flask, request, render_template
import argostranslate.translate

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():

    translated_text = ""

    if request.method == "POST":

        text = request.form["text"]

        translated_text = argostranslate.translate.translate(text, "en", "hi")

    return render_template("index.html", translated=translated_text)


if __name__ == "__main__":
    app.run(debug=True)