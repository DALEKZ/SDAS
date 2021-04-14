from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Date, Float

Base = declarative_base()


# 通常不会改动的股票属性
class StockBaseInfo(Base):
    __tablename__ = "share_base_info"

    # 主键
    id = Column(Integer, primary_key=True, autoincrement=True)
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

    def get_info_by_code(self, code):
        ...


# stock_zh_a_spot
class StockDataInfo(Base):
    __table__ = 'stock_data_info'
    # 主键
    id = Column(Integer, primary_key=True)
    # 日期
    date = Column(Date())
    # 昨收
    close = Column(Float)
    # 代码
    code = Column(String(50), unique=True)
    # 股票简称
    share_name = Column(String(50))
    # 最新价
    newest = Column(Float)
    # 最高价
    high = Column(Float)
    # 最低价
    low = Column(Float)
    # 成交量 单位：股
    volume = Column(Float)
    # 成交额
    turn_over = Column(Float)
    # 今开
    open = Column(Float)
    # 买进
    buy_in = Column(Float)
    # 卖出
    sell_out = Column(Float)
    # 涨跌额
    change_amount = Column(Float)
    # 涨跌幅
    change_rate = Column(Float)

    def __repr__(self):
        return "<StockDataInfo(code='%s', share_name='%s', newest='%s')>" % (
            self.code, self.share_name, self.newest)
