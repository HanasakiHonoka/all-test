from peewee import *

database = SqliteDatabase('D:\\PyWorkSpace\\all-test\\db\\sql_lite.db')

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class SqliteSequence(BaseModel):
    name = BareField(null=True)
    seq = BareField(null=True)

    class Meta:
        table_name = 'sqlite_sequence'
        primary_key = False

class TBtq(BaseModel):
    create_time = DateTimeField(null=True)
    name = TextField(null=True)
    resource_id = TextField(null=True)

    class Meta:
        table_name = 't_btq'

class TBtqResource(BaseModel):


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)



    collect = IntegerField(null=True)
    createTime = CharField(column_name='createTime', null=True)
    dirLevel = IntegerField(column_name='dirLevel', null=True)
    dirType = IntegerField(column_name='dirType', null=True)
    hidden = IntegerField(null=True)
    isView = IntegerField(column_name='isView', null=True)
    name = CharField(null=True)
    parentId = CharField(column_name='parentId', null=True)
    resourceId = CharField(column_name='resourceId', null=True)
    resourceType = IntegerField(column_name='resourceType', null=True)
    resourceUid = CharField(column_name='resourceUid', null=True)
    sort = CharField(null=True)
    updateTime = CharField(column_name='updateTime', null=True)
    extName = CharField(column_name='extName', null=True)
    size = IntegerField(column_name='size', null=True)
    type = CharField(column_name='type', null=True)
    fileMd5 = CharField(column_name='fileMd5', null=True)
    src = CharField(column_name='src', null=True)
    viewUrl = CharField(column_name='viewUrl', null=True)

    class Meta:
        table_name = 't_btq_resource'

class TVoice(BaseModel):
    cv = TextField(null=True)
    rj_num = TextField(null=True)
    title = TextField(null=True)

    class Meta:
        table_name = 't_voice'

