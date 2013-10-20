from models import User
import app

ctx = app.app.test_request_context()
ctx.push()
app.db.create_all()
admin = User('admin', 'jake@jakecoffman.com')
app.db.session.add(admin)
app.db.session.commit()
ctx.pop()
