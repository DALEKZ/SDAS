from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Date, DateTime

Base = declarative_base()


# 通常不会改动的股票属性
class StockBaseInfo(Base):
    __tablename__ = "share_base_info"

    # 主键
    id = Column(Integer, primary_key=True)
    # 股票代码
    code = Column(String(50))
    # 公司全称
    company_name_zh = Column(String(225))
    # 英文名称
    company_name_en = Column(String(225))
    # 板块:主板/c创业板...
    board = Column(String(50))
    # 股票类型：A\B
    share_type = Column(String(50))
    # 股票简称
    share_name = Column(String(50))
    # 行业板块
    industry_blocks = Column(String(50))
    # 交易所类型
    exchange = Column(String(50))
    # 公司网页
    com_site = Column(String(50))
    # 上市日期
    listing_date = Column(Date())

    def __repr__(self):
        return "<StockBaseInfo(code='%s', share_name='%s', exchange='%s')>" % (
            self.code, self.share_name, self.exchange)

