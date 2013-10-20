from models import User
import app

ctx = app.app.test_request_context()
ctx.push()
app.db.create_all()
ctx.pop()
