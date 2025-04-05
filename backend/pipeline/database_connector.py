# from sqlalchemy import create_engine
# from app.config import Config
# from backend.app.models.flagged_content import ReportedContent

class DatabaseConnector:
    
    def __init__(self):
        pass
        # db_uri = Config.SQLALCHEMY_DATABASE_URI
        # self.engine = create_engine(db_uri)

    def get_all(self):
        return [{"reportId": "someUUID", "userId": "someUserId", "content": "Fuck you man"}]
        # mockup data
        connection = self.engine.connect()
        connection.execute()
