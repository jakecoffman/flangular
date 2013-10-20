from models import User
import app

with app.app.test_request_context():
    app.db.create_all()
    admin = User('admin', 'jake@jakecoffman.com')
    app.db.session.add(admin)
    app.db.session.commit()
