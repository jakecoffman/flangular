import flask
import flask.views
from models import User


class UserAPI(flask.views.MethodView):
    def get(self, user_id):
        if user_id is None:
            return str([u.username for u in User.query.all()])
        else:
            if user_id < len(flask.g.users):
                return str(flask.g.users[user_id])
            else:
                return str("User not found")

    def post(self):
        data = flask.request.get_json()
        self._validate_user_data(data)
        flask.g.users.append({
            'name': data['name'],
            'hair': data['hair']
        })

    def delete(self, user_id):
        if user_id >= len(flask.g.users):
            flask.abort(400)
        flask.g.users[user_id]['disabled'] = True

    def put(self, user_id):
        data = flask.request.get_json()
        self._validate_user_data(data)
        update = {
            'name': data['name'],
            'hair': data['hair']
        }
        if 'disabled' in data:
            if not isinstance(data['disabled'], bool):  # TODO: authorize
                flask.abort(400)
            update['disabled'] = data['disabled']
        flask.g.users[user_id] = update

    @staticmethod
    def _validate_user_data(data):
        if not isinstance(data, dict):
            raise flask.abort(400)
        if 'name' not in data or 'hair' not in data:
            raise flask.abort(400)
