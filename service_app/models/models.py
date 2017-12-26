# -*- coding: utf-8 -*-

from pyramid.security import Allow, Everyone

from sqlalchemy import (
    Column,
    Integer,
    Text,
    Float,
    String,
    Boolean,
    ForeignKey,
    DateTime,
)

from sqlalchemy.orm import relationship, backref, class_mapper

from . import DBSession, Base


class Landlord(Base):
    __tablename__ = 'landlord'

    uid = Column(Integer, primary_key=True)
    login = Column(String, unique=True, doc="Login")
    email = Column(String, unique=True, doc="Email")
    password = Column(String, doc="Password")
    full_name = Column(String, doc="Full Name")
    phone_number = Column(String, doc="Phone")
    
    created = Column(DateTime, doc="Created At")
    updated = Column(DateTime, doc="Updated At")


class LandlordAddress(Base):
    __tablename__ = 'landlord_address'

    uid = Column(Integer, primary_key=True)

    landlord_id = Column(Integer, ForeignKey('landlord.uid', onupdate='CASCADE', ondelete='CASCADE'), nullable=False, index=True)
    address = Column(String, unique=True, doc="Address")
    number_of_seats = Column(Integer, doc="Number of seats")
    has_dinner = Column(Boolean, doc="Dinner")
    has_language_cources = Column(Boolean, doc="Language Cources")
    has_transfer = Column(Boolean, doc="Transfer")
    additional = Column(Text, doc="Additional")
    price = Column(Float, doc="Price")
    special_price = Column(Float, doc="Special Price")
    special_price_min_num = Column(Float, doc="Special Price Minimum Order Number")

    created = Column(DateTime, doc="Created At")
    updated = Column(DateTime, doc="Updated At")

    landlord = relationship(Landlord, backref=backref('addresses', cascade='all, delete-orphan', passive_deletes=True, doc='Addresses'), doc='LandLord')


class Student(Base):
    __tablename__ = 'student'

    uid = Column(Integer, primary_key=True)
    login = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(String, doc="Password")
    full_name = Column(String, doc="Full Name")
    phone_number = Column(String, doc="Phone")
    
    created = Column(DateTime, doc="Created At")
    updated = Column(DateTime, doc="Updated At")


class Order(Base):
    __tablename__ = 'orders'

    uid = Column(Integer, primary_key=True)
    status = Column(Integer)
    student_id = Column(Integer, ForeignKey('student.uid', onupdate='CASCADE', ondelete='CASCADE'), nullable=False, index=True)
    landlord_address_id = Column(Integer, ForeignKey('landlord_address.uid', onupdate='CASCADE', ondelete='CASCADE'), nullable=False, index=True)
    amount_of_days = Column(Integer)
    arrival_date = Column(DateTime)
    number_of_persons = Column(Integer)
    additional = Column(Text)
    additional_price = Column(Text)
    total = Column(Float)
    comment = Column(Text)

    created = Column(DateTime, doc="Created At")
    updated = Column(DateTime, doc="Updated At")
    
    student = relationship(Student, backref=backref('orders', cascade='all, delete-orphan', passive_deletes=True, doc='Orders'), doc='Student')
    landlord_address = relationship(LandlordAddress, backref=backref('orders', cascade='all, delete-orphan', passive_deletes=True, doc='Orders'), doc='LandLord Address')
