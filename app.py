from flask import Flask, render_template, request
from googletrans import Translator

app = Flask(__name__)
translator = Translator()

@app.route('/', methods=['GET', 'POST'])
def index():
    translated_text = ""
    if request.method == 'POST':
        text_to_translate = request.form['text']
        target_language = request.form['language']
        try:
            # Translate the input text to the target language
            translation = translator.translate(text_to_translate, dest=target_language)
            translated_text = translation.text
        except Exception as e:
            translated_text = f"Error: {str(e)}"
    return render_template('index.html', translated_text=translated_text)

if __name__ == '__main__':
    app.run(debug=True)
