# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from email.policy import default
from apps import db
from sqlalchemy.exc import SQLAlchemyError
from apps.exceptions.exception import InvalidUsage
import datetime as dt
from sqlalchemy.orm import relationship
from enum import Enum

class CURRENCY_TYPE(Enum):
    usd = 'usd'
    eur = 'eur'

class Product(db.Model):

    __tablename__ = 'products'

    id            = db.Column(db.Integer,      primary_key=True)
    name          = db.Column(db.String(128),  nullable=False)
    info          = db.Column(db.Text,         nullable=True)
    price         = db.Column(db.Integer,      nullable=False)
    currency      = db.Column(db.Enum(CURRENCY_TYPE), default=CURRENCY_TYPE.usd, nullable=False)

    date_created  = db.Column(db.DateTime,     default=dt.datetime.utcnow())
    date_modified = db.Column(db.DateTime,     default=db.func.current_timestamp(),
                                               onupdate=db.func.current_timestamp())
    
    def __init__(self, **kwargs):
        super(Product, self).__init__(**kwargs)

    def __repr__(self):
        return f"{self.name} / ${self.price}"

    @classmethod
    def find_by_id(cls, _id: int) -> "Product":
        return cls.query.filter_by(id=_id).first() 

    def save(self) -> None:
        try:
            db.session.add(self)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            db.session.close()
            error = str(e.__dict__['orig'])
            raise InvalidUsage(error, 422)

    def delete(self) -> None:
        try:
            db.session.delete(self)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            db.session.close()
            error = str(e.__dict__['orig'])
            raise InvalidUsage(error, 422)
        return


#__MODELS__
class Employee(db.Model):

    __tablename__ = 'Employee'

    id = db.Column(db.Integer, primary_key=True)

    #__Employee_FIELDS__
    id = db.Column(db.Integer, nullable=True)
    account_id = db.Column(db.String(255),  nullable=True)
    forename = db.Column(db.String(255),  nullable=True)
    surname = db.Column(db.String(255),  nullable=True)
    email_address = db.Column(db.String(255),  nullable=True)

    #__Employee_FIELDS__END

    def __init__(self, **kwargs):
        super(Employee, self).__init__(**kwargs)


class Auth_User(db.Model):

    __tablename__ = 'Auth_User'

    id = db.Column(db.Integer, primary_key=True)

    #__Auth_User_FIELDS__
    is_active = db.Column(db.Boolean, nullable=True)
    created_date = db.Column(db.DateTime, default=db.func.current_timestamp())
    last_login = db.Column(db.DateTime, default=db.func.current_timestamp())

    #__Auth_User_FIELDS__END

    def __init__(self, **kwargs):
        super(Auth_User, self).__init__(**kwargs)


class User(db.Model):

    __tablename__ = 'User'

    id = db.Column(db.Integer, primary_key=True)

    #__User_FIELDS__
    id = db.Column(db.Integer, nullable=True)

    #__User_FIELDS__END

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)


class Business_Group(db.Model):

    __tablename__ = 'Business_Group'

    id = db.Column(db.Integer, primary_key=True)

    #__Business_Group_FIELDS__
    name = db.Column(db.String(255),  nullable=True)
    id = db.Column(db.Integer, nullable=True)

    #__Business_Group_FIELDS__END

    def __init__(self, **kwargs):
        super(Business_Group, self).__init__(**kwargs)


class User_Group(db.Model):

    __tablename__ = 'User_Group'

    id = db.Column(db.Integer, primary_key=True)

    #__User_Group_FIELDS__
    administrator = db.Column(db.Boolean, nullable=True)

    #__User_Group_FIELDS__END

    def __init__(self, **kwargs):
        super(User_Group, self).__init__(**kwargs)


class Client(db.Model):

    __tablename__ = 'Client'

    id = db.Column(db.Integer, primary_key=True)

    #__Client_FIELDS__
    id = db.Column(db.Integer, nullable=True)
    forename = db.Column(db.String(255),  nullable=True)
    surname = db.Column(db.String(255),  nullable=True)
    email = db.Column(db.String(255),  nullable=True)
    address_1 = db.Column(db.String(255),  nullable=True)
    address_2 = db.Column(db.String(255),  nullable=True)
    telephone_number = db.Column(db.Integer, nullable=True)
    postcode = db.Column(db.String(255),  nullable=True)
    d_o_b = db.Column(db.DateTime, default=db.func.current_timestamp())
    d_o_d = db.Column(db.DateTime, default=db.func.current_timestamp())

    #__Client_FIELDS__END

    def __init__(self, **kwargs):
        super(Client, self).__init__(**kwargs)


class Change_Type(db.Model):

    __tablename__ = 'Change_Type'

    id = db.Column(db.Integer, primary_key=True)

    #__Change_Type_FIELDS__
    id = db.Column(db.Integer, nullable=True)
    name = db.Column(db.String(255),  nullable=True)
    sla_hours = db.Column(db.Integer, nullable=True)

    #__Change_Type_FIELDS__END

    def __init__(self, **kwargs):
        super(Change_Type, self).__init__(**kwargs)


class Status(db.Model):

    __tablename__ = 'Status'

    id = db.Column(db.Integer, primary_key=True)

    #__Status_FIELDS__
    sequence_number = db.Column(db.Integer, nullable=True)
    description = db.Column(db.String(255),  nullable=True)

    #__Status_FIELDS__END

    def __init__(self, **kwargs):
        super(Status, self).__init__(**kwargs)


class Change_Request(db.Model):

    __tablename__ = 'Change_Request'

    id = db.Column(db.Integer, primary_key=True)

    #__Change_Request_FIELDS__
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_updated = db.Column(db.DateTime, default=db.func.current_timestamp())
    notes = db.Column(db.Text, nullable=True)

    #__Change_Request_FIELDS__END

    def __init__(self, **kwargs):
        super(Change_Request, self).__init__(**kwargs)



#__MODELS__END
