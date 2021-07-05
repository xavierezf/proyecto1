from flask import Flask, render_template, url_for, jsonify, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    title='Xavier Web App'
    return render_template('test.html', title=title)

@app.route('/data')
def data():
    headers = request.headers
    body = request.data
    print(headers)
    print(body)
    my_data = {
        'profile': 'Xavier Zuniga',
        'badges': ['uno', 'dos', 'tres']
    }
    return jsonify(my_data)

# random number beetween 1 and 100


if __name__ == '__main__':
    app.run(debug=True)