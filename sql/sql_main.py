from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.stock_class import Base, StockBaseInfo


class BaseSQL():

    def __init__(self):
        self.engine = create_engine("mysql://root:password@159.75.0.91:3306/stock_data?charset=utf8",
                                    encoding='utf8', echo=True)
        Base.metadata.create_all(self.engine)

    def insert_multi(self, obj_list):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        session.add_all(obj_list)
        session.commit()
