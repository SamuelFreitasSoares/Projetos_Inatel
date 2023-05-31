class Query:
    def __init__(self, db):
        self.db = db
    # QUESTÃO 1 ([a] até [d])
    def q1a(self):
        query = "MATCH (n:Teacher {name: 'Renzo'}) RETURN n.ano_nasc,n.cpf"
        result = self.db.execute_query(query)
        return ["Ano de nascimento: "+str(node["n.ano_nasc"])+" - CPF: "+node["n.cpf"] for node in result]

    def q1b(self):
        query = "MATCH (n:Teacher) WHERE n.name =~ 'M.*' return n.name,n.cpf"
        result = self.db.execute_query(query)
        return ["Nome: "+node["n.name"]+" - CPF: "+node["n.cpf"] for node in result]

    def q1c(self):
        query = "MATCH (n:City) return n.name"
        result = self.db.execute_query(query)
        return ["Nome: "+node["n.name"] for node in result]

    def q1d(self):
        query = "MATCH (n:School) WHERE n.number >= 150 AND n.number <= 550 return n.name,n.address,n.number"
        result = self.db.execute_query(query)
        return ["Nome: "+node["n.name"]+" - Endereco: "+node["n.address"]+" - Numero: "+str(node["n.number"]) for node in result]

    # QUESTÃO 2 ([a] até [d])
    def q2a(self):
        query = "MATCH (t:Teacher) RETURN HEAD(COLLECT({name: t.name, ano_nasc: t.ano_nasc})).name as youngest_prof, " \
                "HEAD(COLLECT({name: t.name, ano_nasc: t.ano_nasc})).ano_nasc as " \
                "youngest_prof_year, LAST(COLLECT({name: t.name, ano_nasc: t.ano_nasc})).name as oldest_prof, " \
                "LAST(COLLECT({name: t.name, ano_nasc: t.ano_nasc})).ano_nasc as " \
                "oldest_prof_year "
        result = self.db.execute_query(query)
        return [node for node in result]

    def q2b(self):
        query = "MATCH (n:City) RETURN AVG(n.population) as MEDIA"
        result = self.db.execute_query(query)
        return ["Média da população: "+str(node["MEDIA"]) for node in result]

    def q2c(self):
        query = "MATCH (c:City {cep: '37540-000'}) RETURN REPLACE(c.name, 'a', 'A') as new_name"
        result = self.db.execute_query(query)
        return [node["new_name"] for node in result]

    def q2d(self):
        query = "MATCH (t:Teacher) RETURN SUBSTRING(t.name, 3, 1) AS new_name"
        result = self.db.execute_query(query)
        return [node["new_name"] for node in result]
