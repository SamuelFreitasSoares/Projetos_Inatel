from database import Database
from query import Query
from teacher_crud import TeacherCRUD
from cli import Professor

db = Database("bolt://54.172.43.136:7687", "neo4j", "gaps-pupil-mail")

query_db = Query(db)
teacher_crud = TeacherCRUD(db)

print("Primeira questão - letra a")
a = query_db.q1a()
for i in a:
    print(i)


print("Primeira questão - letra b")
b = query_db.q1b()
for i in b:
    print(i)


print("Primeira questão - letra c")
c = query_db.q1c()
for i in c:
    print(i)


print("Primeira questão - letra d")
d = query_db.q1d()
for i in d:
    print(i)

print("Segunda questão - letra a")
a2 = query_db.q2a()
for record in a2:
    print("Professor mais jovem:", record["youngest_prof"])
    print("Ano de nascimento do mais jovem:", record["youngest_prof_year"])
    print("Professor mais velho:", record["oldest_prof"])
    print("Ano de nascimento do mais velho:", record["oldest_prof_year"])

print("Segunda questão - letra b")
b2 = query_db.q2b()
for i in b2:
    print(i)

print("Segunda questão - letra c")
result_c = query_db.q2c()
for i in result_c:
    print(i)

print("Segunda questão - letra d")
result_d = query_db.q2d()
for i in result_d:
    print(i)

print("Terceira questão")
teacher_crud.create(
    "Chris Lima",
    1956,
    "189.052.396-66"
)
result = teacher_crud.read("Chris Lima")
for i in result:
    print("Nome: ", i["t.name"])
    print("Ano de nascimento: ", i["t.ano_nasc"])
    print("Cpf: ", i["t.cpf"])
teacher_crud.update("Chris Lima", "162.052.777-77")
teacher_crud.delete("Chris Lima")

cli = Professor(teacher_crud)
cli.run()

db.close()
