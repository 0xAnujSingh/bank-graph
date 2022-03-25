from main import db

class Bank(db.Model):
    __tablename__ = 'bank'

    name = db.Column(db.String)
    id = db.Column(db.Integer, primary_key = True)

    def to_dict(self):
        return {
            "name": self.name,
            "id": self.id,
        }

class Branch(db.Model):
    __tablename__ = 'branch'
    # __mapper_args__ = ['id']

    id = db.Column(db.Integer, primary_key=True)
    ifsc = db.Column(db.String)       
    bank_id = db.Column(db.Integer)
    branch = db.Column(db.String)
    address = db.Column(db.String)
    city = db.Column(db.String)
    district = db.Column(db.String)
    state = db.Column(db.String)

    def to_dict(self):
        return {
            "ifsc": self.ifsc,
            "bank_id": self.bank_id,
            "branch": self.branch,
            "address" : self.branch,
            "city" : self.city,
            "district": self.district,
            "state": self.state,
        }