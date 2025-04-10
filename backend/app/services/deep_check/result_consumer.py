
from datetime import date, datetime, timedelta
from sqlalchemy import Delete, Select, delete, select

from app.config_reader import ConfigReader
from app.models.flagged_content import FlaggedContent
from app.utils.common_responses import ENDPOINT_DISABLED
from app.utils.sqlalchemy_utils import SQLAlchemySingleton
from app.utils.helpers import snake_to_camel_case


class ResultConsumer:
    db = SQLAlchemySingleton()

    def __init__(self):
        self.config = ConfigReader("pipeline")

    def consume_results(self, report_id: str, reported_at: date, processed_at: date, remove: bool):
        if not self.config.get("enabled"):
            return ENDPOINT_DISABLED

        select_query = select(FlaggedContent)
        select_query = self.apply_filters(select_query, report_id, reported_at, processed_at)

        result = self.db.session.scalars(select_query)

        if remove:
            delete_query = delete(FlaggedContent)
            delete_query = self.apply_filters(delete_query, report_id, reported_at, processed_at)
            self.db.session.execute(delete_query)
            self.db.session.commit()
        
        return self.map_result(result)

    def apply_filters(self, query: Delete | Select, report_id: str, reported_at: date, processed_at: date):
        if report_id is not None:
            # noinspection PyTypeChecker
            query = query.where(FlaggedContent.report_id == report_id)
        
        if reported_at is not None:
            query = query.where(FlaggedContent.reported_at.between(reported_at, reported_at + timedelta(hours=24)))

        if processed_at is not None:
            query = query.where(FlaggedContent.processed_at.between(processed_at, processed_at + timedelta(hours=24)))

        return query

    def map_result(self, result):
        mapped_result = []
        for row in result:
            obj = {}
            for key, value in row.__dict__.items():
                if not key.startswith('_'):
                    if isinstance(value, datetime):
                        obj[snake_to_camel_case(key)] = value.strftime("%Y-%m-%d %H:%M:%S")
                    else:
                        obj[snake_to_camel_case(key)] = value
            
            obj["flags"] = list(filter(lambda s: s != "", obj["flags"].split(',')))
            mapped_result.append(obj)

        return mapped_result
