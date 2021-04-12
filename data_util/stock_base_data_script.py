import akshare as ak
import pandas as pd
from models.stock_info import StockBaseInfo
from sql.sql_main import *

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 10)


# 获取深交所A股基础数据
def get_sz_stock_data1():
    stock_info_sz_df = ak.stock_info_sz_name_code(indicator="A股列表")
    stock_info_sz_df.fillna('', inplace=True)
    for row in stock_info_sz_df.iterrows():
        sbi = StockBaseInfo(code=row[1]['A股代码'], company_name_zh=row[1]["公司全称"],
                            board=row[1]['板块'], share_type="A", share_name=row[1]['A股简称'],
                            industry_blocks=row[1]['所属行业'],
                            exchange="sz", com_site=row[1]['公司网址'])

        add_stock_base_info(sbi)


get_sz_stock_data1()

# 获取上交所A股基础数据
def get_sh_stock_data1():
    stock_info_sz_df = ak.stock_info_sz_name_code(indicator="A股列表")
    stock_info_sz_df.fillna('', inplace=True)
    for row in stock_info_sz_df.iterrows():
        sbi = StockBaseInfo(code=row[1]['A股代码'], company_name_zh=row[1]["公司全称"],
                            board=row[1]['板块'], share_type="A", share_name=row[1]['A股简称'],
                            industry_blocks=row[1]['所属行业'],
                            exchange="sz", com_site=row[1]['公司网址'])

        add_stock_base_info(sbi)