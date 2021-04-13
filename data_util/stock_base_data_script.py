import akshare as ak
import pandas as pd
from models.stock_info import StockBaseInfo
from sql.sql_main import *

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 10)


def get_sz_stock_by_indictor(indicator: str):
    """
        获取深交所股票数据
        :param indicator: str {'A股列表', 'B股列表', 'CDR列表', 'AB股列表'}
        :return sbi_list: 一个StockBaseInfo列表
    """
    stock_info_sz_df = ak.stock_info_sz_name_code(indicator=indicator)
    stock_info_sz_df.fillna('', inplace=True)
    sbi_list = []

    if indicator == 'A股列表':
        for row in stock_info_sz_df.iterrows():
            sbi_list.append(StockBaseInfo(code=row[1]['A股代码'], company_name_zh=row[1]["公司全称"],
                                          board=row[1]['板块'], share_type="A", share_name=row[1]['A股简称'],
                                          industry_blocks=row[1]['所属行业'],
                                          exchange="sz", com_site=row[1]['公司网址']))

    elif indicator == 'B股列表':
        for row in stock_info_sz_df.iterrows():
            sbi_list.append(StockBaseInfo(code=row[1]['B股代码'], company_name_zh=row[1]["公司全称"],
                                          board=row[1]['板块'], share_type="B", share_name=row[1]['B股简称'],
                                          industry_blocks=row[1]['所属行业'],
                                          exchange="sz", com_site=row[1]['公司网址']))

    return sbi_list


def get_sh_stock_by_indictor(indictor: str):
    """
        获取上交所股票数据
        :param indictor:{'主板A股', '主板B股', '科创板'}
        :return sbi_list: 一个StockBaseInfo列表
    """
    stock_info_sh_name_code = ak.stock_info_sh_name_code(indicator=indictor)
    stock_info_sh_name_code.fillna('', inplace=True)
    sbi_list = []

    if indictor == '主板A股':
        for row in stock_info_sh_name_code.iterrows():
            sbi_list.append(StockBaseInfo(code=row[1]['COMPANY_CODE'],
                                          board='主板', share_type="A", share_name=row[1]['COMPANY_ABBR'],
                                          exchange="sh", listing_date=row[1]['LISTING_DATE']))
        return sbi_list

    elif indictor == '主板B股':
        for row in stock_info_sh_name_code.iterrows():
            sbi_list.append(StockBaseInfo(code=row[1]['COMPANY_CODE'],
                                          board='主板', share_type="B", share_name=row[1]['COMPANY_ABBR'],
                                          exchange="sh", listing_date=row[1]['LISTING_DATE']))
        return sbi_list

    elif indictor == '科创板':
        for row in stock_info_sh_name_code.iterrows():
            sbi_list.append(StockBaseInfo(code=row[1]['COMPANY_CODE'],
                                          board='科创板', share_type="", share_name=row[1]['COMPANY_ABBR'],
                                          exchange="sh", listing_date=row[1]['LISTING_DATE']))
        return sbi_list


def main():
    dao = BaseSQL()
    # sbi_list = get_sh_stock_by_indictor("主板A股")
    sbi_list_B = get_sh_stock_by_indictor("主板B股")
    sbi_list_c = get_sh_stock_by_indictor("科创板")

    dao.insert_multi(sbi_list_B)
    dao.insert_multi(sbi_list_c)


if __name__ == '__main__':
    main()
