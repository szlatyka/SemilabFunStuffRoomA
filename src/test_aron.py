import Api
import DbConnection
import Entities

import json

from sqlalchemy import MetaData
#
# def truncate_db(engine):
#     # delete all table data (but keep tables)
#     # we do cleanup before test 'cause if previous test errored,
#     # DB can contain dust
#     meta = MetaData(bind=engine, reflect=True)
#     con = engine.connect()
#     trans = con.begin()
#     for table in meta.sorted_tables:
#         con.execute(f'ALTER TABLE "{table.name}" DISABLE TRIGGER ALL;')
#         con.execute(table.delete())
#         con.execute(f'ALTER TABLE "{table.name}" ENABLE TRIGGER ALL;')
#     trans.commit()
#
#
# truncate_db(DbConnection.engine)


Api.Group.Create('Analysis')
Api.Group.Create('Sorter')
Api.Group.Create('Lókötők')

for group in Api.Group.All():
    print(group.name())

Api.Question.Create(id = 1,
                    question = 'Hány húrja van a gitárnak?',
                    answer= '6',
                    hint='Kettővel több mint a hegedűnek.',
                    image=None)

Api.Question.Create(id = 2,
                    question = 'Hány húrja van a hegedűnek?',
                    answer= '4',
                    hint='Kettővel kevesebb mint a gitárnak.',
                    image=None)

Api.User.Create(name='Elemér', passwordHash='13')
Api.User.Create(name='Boldizsár', passwordHash='133')

Api.Group.ByName('Analysis').assign(Api.User.ByName('Elemér'))
Api.Group.ByName('Sorter').assign(Api.User.ByName('Boldizsár'))


questions = DbConnection.session.query(Entities.Question).all()
rounds = DbConnection.session.query(Entities.Round).all()
groups = DbConnection.session.query(Entities.Group).all()

def list_hint_stat(rounds, group_id):
    g_rounds = [round for round in rounds if round.group_id == group_id]
    question_ids = {round.question_id for round in g_rounds}
    return [
        {
            'question_id': q_id,
            'hints_used': len([round
                               for round
                               in g_rounds
                               if round.question_id == q_id and round.hint_used])}
        for q_id in question_ids]


stat = {group.id: {'name': group.name, 'hints': list_hint_stat(rounds, group.id)} for group in groups}

stat_string = json.dumps(stat)

print(stat_string)