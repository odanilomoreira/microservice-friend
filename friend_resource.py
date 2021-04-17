from flask_restful import Resource, reqparse
from friend_model import FriendModel
from my_cache import cache
from producer import publish

body_request = reqparse.RequestParser()
body_request.add_argument('id', type=int)
body_request.add_argument('friend_name', type=str)
body_request.add_argument('entity_id', type=int)


class Friends(Resource):
    def post(self):
        data = body_request.parse_args()
        friend_name = data.get('friend_name')
        
        friend = FriendModel(**data)
        try:
            friend.save()
            publish('friend_added', friend.json())

        except:
            return {'message': 'An internal error ocurred trying to create a new friend.'}, 500
        return friend.json()


class Friend(Resource):
    # @cache.cached(timeout=300)
    def get(self, id):
        friends = FriendModel.find_by_entity_id(id)
        if friends:
            friends = [friend.friend_name for friend in friends]
            return {'friends': friends}
            
        return {'message': 'Friend not found.'}, 404 # not found

class FriendByName(Resource):
    def delete(self, friend_name):
        friend = FriendModel.find(friend_name)
        if friend:
            friend.delete()
            publish('friend_deleted', friend.json())
            return {'message':'Friend deleted.'}
        return {'message': 'Friend not found.'}, 404