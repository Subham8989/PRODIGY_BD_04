from flask_restful import Resource, reqparse
from ...models import User
from ....extensions import db, cache

parser = reqparse.RequestParser()
parser.add_argument("name", type=str, required=True, help="Name must be provided!")

class UsersRoute(Resource):
    @cache.cached(key_prefix="all_users")
    def get(self):
        users = db.session.execute(db.select(User))
        user_list = list()

        for user in users:
            user_list.append({ "id": user[0].id, "name": user[0].name })

        return user_list, 200
    
    def post(self):
        args = parser.parse_args()
        name = args["name"]

        new_user = User(name=name)
        db.session.add(new_user)
        cache.delete("all_users")
        db.session.commit()

        return { "message": "User Created!" }, 201