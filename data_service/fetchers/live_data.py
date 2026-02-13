#!/usr/bin/env python3
"""
实时数据获取模块
支持股票和加密货币数据
"""

import yfinance as yf
from pycoingecko import CoinGeckoAPI
import pandas as pd
from datetime import datetime, timedelta
import logging

logger = logging.getLogger(__name__)


class LiveDataFetcher:
    """获取实时市场数据"""

    def __init__(self):
        """初始化数据获取器"""
        self.cg = CoinGeckoAPI()
        logger.info("LiveDataFetcher initialized")

    # ==================== 股票数据 ====================

    def get_stock_data(self, symbol, period='1mo'):
        """
        获取股票历史数据

        Args:
            symbol: 股票代码，如 'AAPL'
            period: 时间周期，如 '1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', 'max'

        Returns:
            DataFrame: 包含 Open, High, Low, Close, Volume 的数据
        """
        try:
            ticker = yf.Ticker(symbol)
            data = ticker.history(period=period)

            if data.empty:
                logger.warning(f"No data found for {symbol}")
                return pd.DataFrame()

            logger.info(f"Successfully fetched {len(data)} rows for {symbol}")
            return data

        except Exception as e:
            logger.error(f"Error fetching stock data for {symbol}: {e}")
            return pd.DataFrame()

    def get_stock_info(self, symbol):
        """
        获取股票详细信息

        Args:
            symbol: 股票代码

        Returns:
            dict: 股票信息字典
        """
        try:
            ticker = yf.Ticker(symbol)
            info = ticker.info

            return {
                'symbol': symbol,
                'name': info.get('longName', symbol),
                'price': info.get('currentPrice', info.get('regularMarketPrice', 0)),
                'change': info.get('regularMarketChangePercent', 0),
                'volume': info.get('volume', 0),
                'market_cap': info.get('marketCap', 0),
                'pe_ratio': info.get('trailingPE', 0),
                'dividend_yield': info.get('dividendYield', 0),
                'fifty_two_week_high': info.get('fiftyTwoWeekHigh', 0),
                'fifty_two_week_low': info.get('fiftyTwoWeekLow', 0),
            }

        except Exception as e:
            logger.error(f"Error fetching stock info for {symbol}: {e}")
            return {}

    def get_multiple_stocks(self, symbols, period='1mo'):
        """
        批量获取多只股票数据

        Args:
            symbols: 股票代码列表
            period: 时间周期

        Returns:
            dict: {symbol: DataFrame} 的字典
        """
        result = {}
        for symbol in symbols:
            data = self.get_stock_data(symbol, period)
            if not data.empty:
                result[symbol] = data
        return result

    # ==================== 加密货币数据 ====================

    def get_crypto_price(self, coin_id='bitcoin'):
        """
        获取加密货币当前价格

        Args:
            coin_id: CoinGecko 币种 ID，如 'bitcoin', 'ethereum'

        Returns:
            dict: 价格信息
        """
        try:
            data = self.cg.get_price(
                ids=coin_id,
                vs_currencies='usd',
                include_24hr_change=True,
                include_market_cap=True,
                include_24hr_vol=True
            )

            if coin_id in data:
                return {
                    'coin_id': coin_id,
                    'price': data[coin_id]['usd'],
                    'change_24h': data[coin_id].get('usd_24h_change', 0),
                    'market_cap': data[coin_id].get('usd_market_cap', 0),
                    'volume_24h': data[coin_id].get('usd_24h_vol', 0)
                }
            else:
                logger.warning(f"No data found for {coin_id}")
                return {}

        except Exception as e:
            logger.error(f"Error fetching crypto price for {coin_id}: {e}")
            return {}

    def get_crypto_history(self, coin_id='bitcoin', days=30):
        """
        获取加密货币历史数据

        Args:
            coin_id: CoinGecko 币种 ID
            days: 天数，1-365

        Returns:
            DataFrame: 历史价格数据
        """
        try:
            logger.info(f"Fetching crypto history for {coin_id}, days={days}")

            data = self.cg.get_coin_market_chart_by_id(
                id=coin_id,
                vs_currency='usd',
                days=days
            )

            logger.info(f"API response keys: {data.keys()}")
            logger.info(f"Prices data points: {len(data.get('prices', []))}")

            # 转换价格数据
            df = pd.DataFrame(data['prices'], columns=['timestamp', 'price'])
            df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
            df.set_index('timestamp', inplace=True)

            # 重命名为 close 以匹配股票数据格式
            df['close'] = df['price']

            # 添加其他列以匹配股票数据格式
            df['open'] = df['close']
            df['high'] = df['close']
            df['low'] = df['close']

            # 添加成交量数据
            if 'total_volumes' in data:
                volumes = pd.DataFrame(data['total_volumes'], columns=['timestamp', 'volume'])
                volumes['timestamp'] = pd.to_datetime(volumes['timestamp'], unit='ms')
                volumes.set_index('timestamp', inplace=True)
                df['volume'] = volumes['volume']
            else:
                df['volume'] = 0

            logger.info(f"Successfully fetched {len(df)} rows for {coin_id}")
            logger.info(f"DataFrame shape: {df.shape}, columns: {df.columns.tolist()}")

            return df

        except Exception as e:
            logger.error(f"Error fetching crypto history for {coin_id}: {e}")
            import traceback
            logger.error(traceback.format_exc())
            return pd.DataFrame()

    def get_multiple_cryptos(self, coin_ids):
        """
        批量获取多个加密货币价格

        Args:
            coin_ids: 币种 ID 列表

        Returns:
            dict: {coin_id: price_info} 的字典
        """
        try:
            data = self.cg.get_price(
                ids=coin_ids,
                vs_currencies='usd',
                include_24hr_change=True,
                include_market_cap=True
            )

            result = {}
            for coin_id in coin_ids:
                if coin_id in data:
                    result[coin_id] = {
                        'price': data[coin_id]['usd'],
                        'change_24h': data[coin_id].get('usd_24h_change', 0),
                        'market_cap': data[coin_id].get('usd_market_cap', 0)
                    }

            return result

        except Exception as e:
            logger.error(f"Error fetching multiple cryptos: {e}")
            return {}

    def get_trending_cryptos(self, limit=10):
        """
        获取热门加密货币

        Args:
            limit: 返回数量

        Returns:
            list: 热门币种列表
        """
        try:
            trending = self.cg.get_search_trending()
            coins = []

            for item in trending['coins'][:limit]:
                coin = item['item']
                coins.append({
                    'id': coin['id'],
                    'name': coin['name'],
                    'symbol': coin['symbol'],
                    'market_cap_rank': coin.get('market_cap_rank', 0)
                })

            return coins

        except Exception as e:
            logger.error(f"Error fetching trending cryptos: {e}")
            return []

    # ==================== 通用方法 ====================

    def get_current_price(self, symbol, asset_type='stock'):
        """
        获取当前价格（统一接口）

        Args:
            symbol: 股票代码或加密货币 ID
            asset_type: 'stock' 或 'crypto'

        Returns:
            float: 当前价格
        """
        try:
            if asset_type == 'stock':
                ticker = yf.Ticker(symbol)
                info = ticker.info
                return info.get('currentPrice', info.get('regularMarketPrice', 0))

            elif asset_type == 'crypto':
                data = self.cg.get_price(ids=symbol, vs_currencies='usd')
                return data[symbol]['usd']

        except Exception as e:
            logger.error(f"Error fetching current price for {symbol}: {e}")
            return 0


# 使用示例
if __name__ == "__main__":
    import sys
    import io

    # Set UTF-8 encoding for Windows console
    if sys.platform == 'win32':
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

    # 配置日志
    logging.basicConfig(level=logging.INFO)

    # 创建数据获取器
    fetcher = LiveDataFetcher()

    print("=" * 60)
    print("实时数据获取测试")
    print("=" * 60)
    print()

    # 测试股票数据
    print("📊 股票数据测试")
    print("-" * 60)
    aapl_data = fetcher.get_stock_data('AAPL', period='5d')
    print(f"AAPL 数据: {len(aapl_data)} 行")
    print(aapl_data.tail())
    print()

    aapl_info = fetcher.get_stock_info('AAPL')
    print(f"AAPL 信息: {aapl_info}")
    print()

    # 测试加密货币数据
    print("₿ 加密货币数据测试")
    print("-" * 60)
    btc_price = fetcher.get_crypto_price('bitcoin')
    print(f"BTC 价格: {btc_price}")
    print()

    btc_history = fetcher.get_crypto_history('bitcoin', days=7)
    print(f"BTC 历史数据: {len(btc_history)} 行")
    print(btc_history.tail())
    print()

    # 测试批量获取
    print("📈 批量获取测试")
    print("-" * 60)
    cryptos = fetcher.get_multiple_cryptos(['bitcoin', 'ethereum', 'solana'])
    for coin_id, info in cryptos.items():
        print(f"{coin_id}: ${info['price']:,.2f} ({info['change_24h']:+.2f}%)")
    print()

    # 测试热门币种
    print("🔥 热门币种")
    print("-" * 60)
    trending = fetcher.get_trending_cryptos(5)
    for i, coin in enumerate(trending, 1):
        print(f"{i}. {coin['name']} ({coin['symbol'].upper()}) - 排名 #{coin['market_cap_rank']}")
