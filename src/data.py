# data.py | IntelliFusion Version 0.1.9(202308032000) Developer Alpha
from pathlib import Path
from peewee import *

# 基础类
APP_DIR = Path(__file__).parent
DATA_DIR = APP_DIR / "data"
DATABASE_FILE = DATA_DIR / "models.sqlite"

from peewee import *

db = SqliteDatabase(DATABASE_FILE)

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = db

class Models(BaseModel):
    # order = IntegerField(column_name="order")
    api_key = IntegerField(column_name="APIkey", null=True)
    display = CharField(column_name="Display", null=True)
    launch_compiler = CharField(column_name="LaunchCompiler", null=True)
    launch_path = CharField(column_name="LaunchPath", null=True)
    name = CharField()
    type = CharField()
    url = CharField()

    class Meta:
        table_name = 'models'

class Widgets(BaseModel):
    order = IntegerField(column_name="order",)
    avaliable =  BooleanField(column_name="avliable")
    widgets_url = CharField(column_name="URL",)

def SetupDatabase():
    db.create_tables([Models])
    BaseModel = Models(
        order=1,
        type="OpenAI",
        name="gpt-3.5-turbo",
        url="https://ai.fakeopen.com/v1",
        APIkey="sk-frdfhfdrghdsu5tt5sgyuyy",
        LaunchCompiler="NONE",
        LaunchUrl="NONE",
    )
    BaseModel.save()


