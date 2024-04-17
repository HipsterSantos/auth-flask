from extension import db,jwt
from werkzeug.security import generate_password_hash,check_password_hash
class User:
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64),unique=True,nullable=False)
    password_hash = db.Column(db.String(128),nullable=False)
    def generate_password_hash(self,password):
        self.password_hash = generate_password_hash(password,method='sha256')
    def check_password_hash(self,password):
        return check_password_hash(self.password_hash,password)