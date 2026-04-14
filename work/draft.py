import requests

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
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9,ja;q=0.8,en;q=0.7',
    'origin': 'https://finance.yahoo.com',
    'priority': 'u=1, i',
    'referer': 'https://finance.yahoo.com/markets/crypto/all/?start=25&count=25',
    'sec-ch-ua': '"Google Chrome";v="147", "Not.A/Brand";v="8", "Chromium";v="147"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
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

response = requests.get(
    'https://query1.finance.yahoo.com/v1/finance/screener/predefined/saved',
    params=params,
    cookies=cookies,
    headers=headers,
)