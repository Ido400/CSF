from Users.app.app import db

class SSHKey(db.Model):
    __tablename__ = 'ssh_key'

    id = db.Column(db.Integer, primary_key=True)
    public_key = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)