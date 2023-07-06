from peewee import *
from os import path

from peewee import SqliteDatabase

#creating our first database
connection = path.dirname(path.realpath((__file__)))
db = SqliteDatabase(path.join(connection, "emobilis.db"))

#creating table inside db
class student(Model):
    name = CharField()
    age = CharField()
    phone = CharField()
    gender = CharField()
    code = CharField()


    class Meta:
        database = db
student.create_table(fail_silently=True)




