from bson import ObjectId
from classes import *
from database import Database
class MotoristaDAO:
    def __init__(self, database: Database):
        self.db = database

    def create(self, motorista: Motorista):
        try:
            motorista_dict = {
                "nota": motorista.nota,
                "corridas": [corrida.__dict__ for corrida in motorista.corridas]
            }
            result = self.db.collection.insert_one(motorista_dict)
            motorista.id = str(result.inserted_id)
            print("id: ",motorista.id)
        except Exception as e:
            print(e)

    def read(self, id_motorista: str) -> Motorista:
        result = self.db.collection.find_one({"_id": ObjectId(id_motorista)})
        return result

    def update(self, id: str,nota:float, corridas):
        try:
            ''' Atualizando nota média do motorista '''
            motorista = self.db.collection.find_one({"_id": ObjectId(id)})
            motorista['corridas'].extend(corridas)
            motorista['nota'] = nota
            res = self.db.collection.update_one({"_id": ObjectId(id)}, {'$set': motorista})

            print(f"Motorista atualizado!")
            return res.modified_count
        except Exception as e:
            print(f"Erro: {e}")
            return None

    def delete(self, id: str):
        res = self.db.collection.delete_one({"_id": ObjectId(id)})
        print(f"motorista deleted: {res.deleted_count} document(s) deleted")
        return res.deleted_count