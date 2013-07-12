import pyodbc
import config
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
import sys

Base = declarative_base()

class Doctor(Base):
    __tablename__ = "AppAcreditedDoctors"

    id = Column('PhyID',Integer, primary_key = True)
    fullname = Column('FullName', String)
    email = Column('Email', String)
    phone = Column('Phone', String)
    mobile_phone = Column('MobilePhone', String)
    title = Column('Title', String)
    esp_code = Column('EspCode', String)

    def __init__(self, fullname, email, phone, title):
        self.fullname = fullname
        self.email = email
        self.phone = phone
        self.title = title



def connect():
    if os.name == 'posix':
        connectionString = "DRIVER={FreeTDS};Server=%s;Database=%s;UID=%s;PWD=%s;TDS_Version=8.0;Port=1433;" % (config.SERVER, config.DB, config.USER, config.PASS)
    elif os.name == 'nt':
        connectionString = "DRIVER={SQL Server};Server=%s;Database=%s;UID=%s;PWD=%s;TDS_Version=8.0;Port=1433;" % (config.SERVER, config.DB, config.USER, config.PASS)

    print "Connecting string: %s" % (connectionString)

    con = pyodbc.connect(connectionString)
    return con


engine = create_engine('mssql://', creator=connect)

Session = sessionmaker(bind=engine)

session = Session()

for doctor in session.query(Doctor).all():
    print doctor.fullname
