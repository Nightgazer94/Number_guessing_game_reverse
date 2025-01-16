from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def guess_number():
    if request.method == 'POST':
        min_value = int(request.form['min'])
        max_value = int(request.form['max'])
        guess = int((max_value - min_value) / 2) + min_value
        response = request.form.get('response', '')

        if response == 'too low':
            min_value = guess
        elif response == 'too high':
            max_value = guess
        elif response == 'you guessed':
            return render_template('result.html', message='I won!')
        else:
            return render_template('index.html', guess=guess, min_value=min_value, max_value=max_value,
                                   message='Don\'t cheat!')

        guess = int((max_value - min_value) / 2) + min_value
        return render_template('index.html', guess=guess, min_value=min_value, max_value=max_value)

    return render_template('index.html', guess=None, min_value=0, max_value=1000)


if __name__ == '__main__':
    app.run(debug=False)
