from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.stock_info import Base, StockBaseInfo

engine = create_engine("mysql://root:password@159.75.0.91:3306/stock_data?charset=utf8",
                       encoding='utf8', echo=True)
Base.metadata.create_all(engine)


def add_stock_base_info(sbi):
    Session = sessionmaker(bind=engine)
    session = Session()
    session.add(sbi)
    session.commit()
