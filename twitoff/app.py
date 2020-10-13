
from flask import Flask, render_template, request
from .db_model import DB, User, Tweet
from .twitter import add_user_tweepy
#from.predict import predict_user


def create_app():
    '''Create and configure an instance of our Flask application'''
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\Users\\sboov\\Documents\\DSPT7-Twitoff\\twitoff.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    DB.init_app(app) # connect Flask app to SQLAlchemy DB


    @app.route('/')
    def root():
        return render_template('base.html', title='Home', users=User.query.all())

    @app.route('/user', methods=['POST'])
    @app.route('/user/<name>', methods=['GET'])
    def add_or_update_user(name=None, message=''):
        name = name or request.values['user_name']

        try:
            if request.method == 'POST':
                add_user_tweepy(name)
                message = 'User {} successfully added!'.format(name)
            tweets = User.query.filter(User.username == name).one().tweet
        except Exception as e:
            print('Error adding {}: {}'.format(name, e))
            tweets = []

        return render_template('user.html', title=name, tweets=tweets, message=message)

    @app.route('/reset')
    def reset():
        DB.drop_all()
        DB.create_all()
        return render_template('base.html', title='Reset Database!', users=User.query.all())

    @app.route('/update', methods=['GET'])
    def update():
        update_all_users()
        return render_template('base.html', title='All Tweets Updated!', users=User.query.all())

    return app



 #if __name__ == '__main':
 #    app.run(debug=True)   