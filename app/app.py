''' CLook Web application using Flask '''

from flask import Flask, render_template

app = Flask(__name__)

#To render homepage
@app.route('/')
def index():
    return render_template('index.html')

#To render Trial page
@app.route('/trial/')
def trial():
	return render_template('trial.html')


if __name__ == '__main__':
	app.run(debug=True,threaded=True)