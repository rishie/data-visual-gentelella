from mongoengine import Document
from mongoengine.fields import (
    StringField, DecimalField, DateTimeField, IntField
)


class LACollision(Document):
    meta = {'collection': 'LACollision'}
    X = DecimalField()
    Y = DecimalField()
    OBJECTID = IntField()
    case_id = IntField()
    accident_year = IntField()
    proc_date = DateTimeField()
    juris = IntField()
    collision_date = DateTimeField()
    collision_time = IntField()
    officer_id = IntField()
    reporting_district = IntField()
    day_of_week = IntField()
    chp_shift = IntField()
    population = IntField()
    cnty_city_loc = IntField()
    special_cond = IntField()
    beat_type = IntField()
    chp_beat_type = IntField()
    city_division_lapd = StringField()
    chp_beat_class = IntField()
    beat_number = StringField()
    primary_rd = StringField()
    secondary_rd = StringField()
    distance = IntField()