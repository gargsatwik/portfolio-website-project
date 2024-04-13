import smtplib
import flask


app = flask.Flask(__name__)


app.route('/')
def home():
    return flask.render_template()

if __name__ == '__main__':
    app.run(debug=True)
