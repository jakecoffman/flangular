import json
import flask
import flask.views
from sqlalchemy.exc import IntegrityError
from models import db, User


class UserAPI(flask.views.MethodView):
    def get(self, user_id):
        if user_id is None:
            return json.dumps([u.username for u in User.query.all()])
        else:
            user = User.query.get_or_404(user_id)
            return str(user)

    def post(self):
        data = flask.request.get_json(force=True)
        self._validate_user_data(data)
        user = User(data['username'], data['email'])
        db.session.add(user)
        try:
            db.session.commit()
        except IntegrityError:
            return "username already exists", 400
        return "ok"

    def delete(self, user_id):
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return "ok"

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
        if 'username' not in data or 'email' not in data:
            raise flask.abort(400)
