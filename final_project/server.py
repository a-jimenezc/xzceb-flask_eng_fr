from machinetranslation.translator import englishToFrench, frenchToEnglish
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishTo_French():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    translation = englishToFrench(textToTranslate)
    return translation

@app.route("/frenchToEnglish")
def frenchTo_English():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    translation = frenchToEnglish(textToTranslate)
    return translation

@app.route("/")
def renderIndexPage():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
