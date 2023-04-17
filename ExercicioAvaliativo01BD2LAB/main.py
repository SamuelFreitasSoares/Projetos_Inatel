from database import Database
from motoristaDAO import MotoristaDAO
from motoristaCLI import MotoristaCLI

db = Database(database="atlas-cluster", collection="Motoristas")
motorista_dao = MotoristaDAO(db)
motorista_cli = MotoristaCLI(db)
motorista_cli.menu()