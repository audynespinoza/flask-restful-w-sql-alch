from db import db
from sqlalchemy.dialects.postgresql

class ItemModel(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))
    expire = db.Column(db.String(80)),
    ip_cidr = db.Column(postgresql.CIDR, index=True, nullable=True)


    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    store = db.relationship('StoreModel')

    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id
        self.expire = expire
        self.ip_cidr = ip_cidr

    def json(self):
        return {
        'name': self.name,
        'price': self.price,
        'store_id':self.store_id,
        'expire':self.expire,
        'ip_cidr':self.ip_cidr
        }

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

