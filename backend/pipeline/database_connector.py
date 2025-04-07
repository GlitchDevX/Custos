from sqlalchemy import create_engine, text
from app.config import Config, DevelopmentConfig

class DatabaseConnector:
    
    def __init__(self):
        db_uri = DevelopmentConfig.SQLALCHEMY_DATABASE_URI
        print(db_uri)
        self.engine = create_engine(db_uri)

    def get_all_reported_content(self):
        with self.engine.connect() as connection:
            result = connection.execute(text("SELECT * FROM reported_content;"))

            mapped_response = []
            for row in result:
                mapped_response.append({"reportId": row[0], "userId": row[1], "content": row[2]})
            
            return mapped_response
