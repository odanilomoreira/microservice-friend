from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from friend_resource import Friend, Friends, FriendByName

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['CACHE_TYPE'] = 'simple'
api = Api(app)

@app.route('/')
def index():
    return '<h1>Up and running...</h1>'

api.add_resource(Friends, '/friends')
api.add_resource(Friend, '/entities/<int:id>/friends')
api.add_resource(FriendByName, '/entities/<string:friend_name>/friends')


if __name__ == '__main__':
    from sql_alchemy import db
    from my_cache import cache
    db.init_app(app)
    cache.init_app(app)
    app.run(host="0.0.0.0", port=8001,debug=True)