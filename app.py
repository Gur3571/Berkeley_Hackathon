from flask import Flask, render_template, request, redirect
from pdf_reader import process

app = Flask(__name__)

conversation = []


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        prompt = request.form['query']
        if len(conversation) == 0:
            conversation.append(
                "Pretend that you are a lawyer, speak from a first person point of view, please provide your professional perspective on the following matter: " + prompt)
        else:
            conversation.append(prompt)

        result = process('-'.join(conversation))

        return render_template('result.html', conversation=" ", result=result)
    else:
        conversation.clear()
        return render_template('index.html')


if __name__ == '__main__':
    app.run()
