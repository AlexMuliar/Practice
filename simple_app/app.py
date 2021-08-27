from flask import Flask, make_response

app = Flask('app')

@app.route('/')
def f():
    return make_response('Hello world', 200)


if __name__ == '__main__':
    app.run('0.0.0.0', 5000)
