# -*- coding: utf-8 -*-
# @Author  : relakkes@gmail.com
# @Name    : 程序员阿江-Relakkes
# @Time    : 2024/4/7 20:54
# @Desc    : 存放一些公共的函数
from typing import List


class SymbolContent:
    symbol: str = ""
    name: str = ""
    price: str = ""  # 价格（盘中）
    change_price: str = ""  # 跌涨价格
    change_percent: str = ""  # 跌涨幅
    market_price: str = ""  # 市值

    @classmethod
    def get_fields(cls) -> List[str]:
        return [key for key in cls.__dict__.keys() if not key.startswith('__') and key != "get_fields"]

    def __str__(self):
        return f"""
Symbol: {self.symbol}
Name: {self.name}
Price: {self.price}
Change Price: {self.change_price}        
Change Percent: {self.change_percent}        
Market Price: {self.market_price}        
"""


def make_req_params_and_headers():
    headers = {
        # cookies是必须的,并且和common_params的crumb参数绑定的。
        'cookie': 'GUC=AQEBCAFmDYVmOUIdcARM&s=AQAAANxlE2ny&g=Zgw0yA; A1=d=AQABBBB0fGQCEKnzzPnIHq8Lm4HEj-GCp50FEgEBCAGFDWY5Zliia3sB_eMBAAcIEHR8ZOGCp50&S=AQAAAgF-nCWw8AxSZ-gyIaeg4aI; A3=d=AQABBBB0fGQCEKnzzPnIHq8Lm4HEj-GCp50FEgEBCAGFDWY5Zliia3sB_eMBAAcIEHR8ZOGCp50&S=AQAAAgF-nCWw8AxSZ-gyIaeg4aI; axids=gam=y-lf5u4KlE2uJWDQYbXyUTkKMC2GVH7OUj~A&dv360=eS1XSElPM3l4RTJ1SHVVV3hNZVBDeG9aTDlDYXdaQ1dPNX5B&ydsp=y-_wiZU4RE2uIAxUbGalyjvJCoR6Le9iVT~A&tbla=y-gt2Wyc1E2uI4nvAYanhnPTMrhn4c3edZ~A; tbla_id=fde33964-c427-4b9c-b849-90a304938e21-tuctb84a272; cmp=t=1712472060&j=0&u=1YNN; gpp=DBABBg~BVoIgACA.QA; gpp_sid=8; A1S=d=AQABBBB0fGQCEKnzzPnIHq8Lm4HEj-GCp50FEgEBCAGFDWY5Zliia3sB_eMBAAcIEHR8ZOGCp50&S=AQAAAgF-nCWw8AxSZ-gyIaeg4aI&j=WORLD',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    }
    common_params = {
        'crumb': 'UllRf10isbP',
        'lang': 'en-US',
        'region': 'US',
        'formatted': 'true',
        'corsDomain': 'finance.yahoo.com',
    }
    common_payload_data = {
        'offset': 0,  # 这个是分页其实位置
        'size': 25,  # 这个是分页数量
        'sortType': 'DESC',
        'sortField': 'intradaymarketcap',
        'quoteType': 'CRYPTOCURRENCY',
        'query': {
            'operator': 'and',
            'operands': [
                {
                    'operator': 'eq',
                    'operands': [
                        'currency',
                        'USD',
                    ],
                },
                {
                    'operator': 'eq',
                    'operands': [
                        'exchange',
                        'CCC',
                    ],
                },
            ],
        },
        'userId': '',
        'userIdType': 'guid',
    }
    return common_params, headers, common_payload_data

def make_request():
    cookies = {
        'GUC': 'AQEBCAFp2PFp_0IePgSR&s=AQAAAPmpJ397&g=adejCw',
        'A1': 'd=AQABBBXGwmkCEPMfnRPQ6G_ZNgv7tZg6NmIFEgEBCAHx2Gn_aViia3sB_eMDAAcIFcbCaZg6NmI&S=AQAAAk90QGzfjWV5zyT6BuQebio',
        'A3': 'd=AQABBBXGwmkCEPMfnRPQ6G_ZNgv7tZg6NmIFEgEBCAHx2Gn_aViia3sB_eMDAAcIFcbCaZg6NmI&S=AQAAAk90QGzfjWV5zyT6BuQebio',
        '_ga': 'GA1.1.1641363869.1775739659',
        'axids': 'gam=y-77i3g4dE2uIWm5OJ6l5vazfn9oef925a~A&dv360=eS1xaVZLTVYxRTJ1RWxqaktSTkxHUDRab3M2UUlFS3o5V35B&ydsp=y-ePS8CpVE2uJUEGr4p9KMNVIT0XmrCtX_~A&tbla=y-So6aYdJE2uKkvNpj3N5wRlHPIMYIwWPm~A',
        'tbla_id': 'e63f4759-cef7-403f-b881-d7c1f93696fd-tuct10d1288d',
        'PRF': 'dock-collapsed%3Dtrue',
        'fes-ds-PolymarketStream2026-5': '1',
        'gpp': 'DBAA',
        'gpp_sid': '-1',
        'fes-ds-PolymarketStream2026-12': '1',
        'A1S': 'd=AQABBBXGwmkCEPMfnRPQ6G_ZNgv7tZg6NmIFEgEBCAHx2Gn_aViia3sB_eMDAAcIFcbCaZg6NmI&S=AQAAAk90QGzfjWV5zyT6BuQebio',
        'fes-ds-session': 'pv%3D1',
        '_ga_YD9K1W9DLN': 'GS2.1.s1775995791$o9$g0$t1775995791$j60$l0$h0',
        'cmp': 't=1775996900&j=0&u=1---',
    }

    headers = {
        'accept-language': 'zh-CN,zh;q=0.9,ja;q=0.8,en;q=0.7',
        'origin': 'https://finance.yahoo.com',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36',
        # 'cookie': 'GUC=AQEBCAFp2PFp_0IePgSR&s=AQAAAPmpJ397&g=adejCw; A1=d=AQABBBXGwmkCEPMfnRPQ6G_ZNgv7tZg6NmIFEgEBCAHx2Gn_aViia3sB_eMDAAcIFcbCaZg6NmI&S=AQAAAk90QGzfjWV5zyT6BuQebio; A3=d=AQABBBXGwmkCEPMfnRPQ6G_ZNgv7tZg6NmIFEgEBCAHx2Gn_aViia3sB_eMDAAcIFcbCaZg6NmI&S=AQAAAk90QGzfjWV5zyT6BuQebio; _ga=GA1.1.1641363869.1775739659; axids=gam=y-77i3g4dE2uIWm5OJ6l5vazfn9oef925a~A&dv360=eS1xaVZLTVYxRTJ1RWxqaktSTkxHUDRab3M2UUlFS3o5V35B&ydsp=y-ePS8CpVE2uJUEGr4p9KMNVIT0XmrCtX_~A&tbla=y-So6aYdJE2uKkvNpj3N5wRlHPIMYIwWPm~A; tbla_id=e63f4759-cef7-403f-b881-d7c1f93696fd-tuct10d1288d; PRF=dock-collapsed%3Dtrue; fes-ds-PolymarketStream2026-5=1; gpp=DBAA; gpp_sid=-1; fes-ds-PolymarketStream2026-12=1; A1S=d=AQABBBXGwmkCEPMfnRPQ6G_ZNgv7tZg6NmIFEgEBCAHx2Gn_aViia3sB_eMDAAcIFcbCaZg6NmI&S=AQAAAk90QGzfjWV5zyT6BuQebio; fes-ds-session=pv%3D1; _ga_YD9K1W9DLN=GS2.1.s1775995791$o9$g0$t1775995791$j60$l0$h0; cmp=t=1775996900&j=0&u=1---',
    }

    params = {
        'count': '25',
        'formatted': 'true',
        'scrIds': 'ALL_CRYPTOCURRENCIES_US',
        'sortField': 'intradaymarketcap',
        'sortType': 'DESC',
        'start': '50',
        'useRecordsResponse': 'true',
        'fields': 'ticker,logoUrl,symbol,longName,sparkline,shortName,regularMarketPrice,regularMarketChange,regularMarketChangePercent,marketCap,regularMarketVolume,volume24Hr,volumeAllCurrencies,circulatingSupply,fiftyTwoWeekChangePercent,fiftyTwoWeekRange',
        'lang': 'en-US',
        'region': 'US',
    }

    return cookies, headers, params

def make_request2():
    params = {
        "count": 25,
        "start": 0,
        "scrIds": "ALL_CRYPTOCURRENCIES_US",
        "sortField": "intradaymarketcap",
        "sortType": "DESC",
        "lang": "en-US",
        "region": "US"
    }

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    return params, headers

if __name__ == '__main__':
    print(SymbolContent.get_fields())
