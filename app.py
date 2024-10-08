from flask import Flask, render_template
from utils.auth.auth import init_login_manager
from routes import auth


app = Flask(__name__)
app.config['SECRET_KEY'] = 'srrdfhyjgk,.l/k;l.hgjfctxdyes4ydufjrkg,j'

app.register_blueprint(auth, url_prefix='/auth')



init_login_manager(app)


@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
