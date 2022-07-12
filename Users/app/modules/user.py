from Users.app.app import db

class User(db.Model):
    __tablename__ = 'user'

    user_name = db.Column(db.String, primary_key=True)
    name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    ssh_keys = db.relationship('SSHKey', backref='user')