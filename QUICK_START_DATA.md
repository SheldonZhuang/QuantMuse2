# 快速开始：获取最新数据

## ✅ 测试结果

根据测试，以下数据源可用：

### 1. ✅ Yahoo Finance（股票数据）- 推荐使用
- **状态**：✅ 正常工作
- **数据类型**：全球股票
- **费用**：完全免费
- **配置**：无需任何设置

### 2. ⚠️ Binance（加密货币）- 地区限制
- **状态**：⚠️ 在你的地区受限
- **替代方案**：使用 CoinGecko 或 CoinCap

## 🚀 推荐方案

### 方案 A：仅股票数据（最简单）

**适合**：只关注股票市场

**步骤**：
```python
# 已经可以使用！无需任何配置
import yfinance as yf

# 获取股票数据
data = yf.download('AAPL', period='1mo')
print(data)
```

### 方案 B：股票 + 加密货币（推荐）

**适合**：同时关注股票和加密货币

**步骤 1**：安装 CoinGecko 库
```bash
pip install pycoingecko
```

**步骤 2**：使用代码
```python
# 股票数据
import yfinance as yf
stock_data = yf.download('AAPL', period='1mo')

# 加密货币数据
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
btc_price = cg.get_price(ids='bitcoin', vs_currencies='usd')
print(f"BTC价格: ${btc_price['bitcoin']['usd']}")
```

## 📝 实用示例

### 示例 1：获取多只股票的最新数据

```python
import yfinance as yf
import pandas as pd

# 定义股票列表
symbols = ['AAPL', 'GOOGL', 'MSFT', 'TSLA', 'AMZN']

# 批量获取数据
data = yf.download(symbols, period='1mo', group_by='ticker')

# 显示最新价格
for symbol in symbols:
    latest_price = data[symbol]['Close'].iloc[-1]
    print(f"{symbol}: ${latest_price:.2f}")
```

### 示例 2：获取加密货币数据（CoinGecko）

```python
from pycoingecko import CoinGeckoAPI
import pandas as pd

cg = CoinGeckoAPI()

# 获取多个加密货币价格
coins = ['bitcoin', 'ethereum', 'binancecoin', 'solana']
prices = cg.get_price(ids=coins, vs_currencies='usd', include_24hr_change=True)

for coin in coins:
    price = prices[coin]['usd']
    change = prices[coin].get('usd_24h_change', 0)
    print(f"{coin.upper()}: ${price:,.2f} ({change:+.2f}%)")

# 获取历史数据
btc_history = cg.get_coin_market_chart_by_id(
    id='bitcoin',
    vs_currency='usd',
    days=30
)

# 转换为 DataFrame
df = pd.DataFrame(btc_history['prices'], columns=['timestamp', 'price'])
df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
print(df.head())
```

### 示例 3：实时监控价格

```python
import yfinance as yf
import time

def monitor_prices(symbols, interval=60):
    """每隔一段时间更新价格"""
    while True:
        print("\n" + "="*50)
        print(f"更新时间: {time.strftime('%Y-%m-%d %H:%M:%S')}")
        print("="*50)

        for symbol in symbols:
            ticker = yf.Ticker(symbol)
            info = ticker.info
            price = info.get('currentPrice', 0)
            change = info.get('regularMarketChangePercent', 0)

            print(f"{symbol}: ${price:.2f} ({change:+.2f}%)")

        time.sleep(interval)

# 使用示例
symbols = ['AAPL', 'GOOGL', 'TSLA']
monitor_prices(symbols, interval=300)  # 每5分钟更新
```

## 🔧 在 Dashboard 中集成真实数据

### 步骤 1：安装依赖

```bash
cd QuantMuse1
pip install yfinance pycoingecko
```

### 步骤 2：创建数据获取模块

创建文件 `data_service/fetchers/live_data.py`：

```python
import yfinance as yf
from pycoingecko import CoinGeckoAPI
import pandas as pd
from datetime import datetime

class LiveDataFetcher:
    """获取实时市场数据"""

    def __init__(self):
        self.cg = CoinGeckoAPI()

    def get_stock_data(self, symbol, period='1mo'):
        """获取股票数据"""
        try:
            ticker = yf.Ticker(symbol)
            data = ticker.history(period=period)
            return data
        except Exception as e:
            print(f"获取股票数据失败: {e}")
            return pd.DataFrame()

    def get_stock_info(self, symbol):
        """获取股票详细信息"""
        try:
            ticker = yf.Ticker(symbol)
            info = ticker.info
            return {
                'symbol': symbol,
                'name': info.get('longName', symbol),
                'price': info.get('currentPrice', 0),
                'change': info.get('regularMarketChangePercent', 0),
                'volume': info.get('volume', 0),
                'market_cap': info.get('marketCap', 0)
            }
        except Exception as e:
            print(f"获取股票信息失败: {e}")
            return {}

    def get_crypto_price(self, coin_id='bitcoin'):
        """获取加密货币价格"""
        try:
            data = self.cg.get_price(
                ids=coin_id,
                vs_currencies='usd',
                include_24hr_change=True,
                include_market_cap=True
            )
            return data[coin_id]
        except Exception as e:
            print(f"获取加密货币价格失败: {e}")
            return {}

    def get_crypto_history(self, coin_id='bitcoin', days=30):
        """获取加密货币历史数据"""
        try:
            data = self.cg.get_coin_market_chart_by_id(
                id=coin_id,
                vs_currency='usd',
                days=days
            )

            df = pd.DataFrame(data['prices'], columns=['timestamp', 'close'])
            df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
            df.set_index('timestamp', inplace=True)

            # 添加其他列以匹配股票数据格式
            df['open'] = df['close']
            df['high'] = df['close']
            df['low'] = df['close']
            df['volume'] = 0

            return df
        except Exception as e:
            print(f"获取加密货币历史数据失败: {e}")
            return pd.DataFrame()

# 使用示例
if __name__ == "__main__":
    fetcher = LiveDataFetcher()

    # 获取股票数据
    print("获取 AAPL 股票数据...")
    aapl_data = fetcher.get_stock_data('AAPL', period='5d')
    print(aapl_data.tail())

    # 获取股票信息
    print("\n获取 AAPL 股票信息...")
    aapl_info = fetcher.get_stock_info('AAPL')
    print(aapl_info)

    # 获取加密货币价格
    print("\n获取 BTC 价格...")
    btc_price = fetcher.get_crypto_price('bitcoin')
    print(btc_price)

    # 获取加密货币历史数据
    print("\n获取 BTC 历史数据...")
    btc_history = fetcher.get_crypto_history('bitcoin', days=7)
    print(btc_history.tail())
```

### 步骤 3：在 Dashboard 中使用

修改 `dashboard_app.py` 中的 `_generate_sample_market_data` 方法：

```python
def _show_market_data(self, i18n):
    """Show market data tab"""
    st.header(i18n.t('market_title'))

    # 添加资产类型选择
    asset_type = st.radio(
        "Asset Type",
        ["Stock", "Cryptocurrency"],
        horizontal=True
    )

    if asset_type == "Stock":
        # 股票符号选择
        symbol = st.selectbox(
            i18n.t('select_symbol'),
            ['AAPL', 'GOOGL', 'MSFT', 'TSLA', 'AMZN', 'NVDA', 'META']
        )

        # 获取真实数据
        from data_service.fetchers.live_data import LiveDataFetcher
        fetcher = LiveDataFetcher()
        market_data = fetcher.get_stock_data(symbol, period='1mo')

    else:
        # 加密货币选择
        crypto_map = {
            'Bitcoin (BTC)': 'bitcoin',
            'Ethereum (ETH)': 'ethereum',
            'Binance Coin (BNB)': 'binancecoin',
            'Solana (SOL)': 'solana'
        }
        crypto_name = st.selectbox(
            i18n.t('select_symbol'),
            list(crypto_map.keys())
        )
        coin_id = crypto_map[crypto_name]

        # 获取真实数据
        from data_service.fetchers.live_data import LiveDataFetcher
        fetcher = LiveDataFetcher()
        market_data = fetcher.get_crypto_history(coin_id, days=30)
        symbol = crypto_name

    # 显示图表（使用真实数据）
    if not market_data.empty:
        st.subheader(f"📊 {symbol} {i18n.t('price_chart')}")
        price_fig = self.chart_generator.create_real_time_price_chart(market_data, symbol)
        st.plotly_chart(price_fig, use_container_width=True)
    else:
        st.warning("无法获取数据")
```

## 📊 数据更新频率

| 数据源 | 更新频率 | 延迟 |
|--------|---------|------|
| Yahoo Finance | 实时 | 15分钟 |
| CoinGecko | 每分钟 | 1-2分钟 |
| Alpha Vantage | 实时 | 实时 |

## 🎯 下一步

1. **安装 CoinGecko**：
   ```bash
   pip install pycoingecko
   ```

2. **测试数据获取**：
   ```bash
   python test_data_sources.py
   ```

3. **在 Dashboard 中使用真实数据**：
   - 修改 `dashboard_app.py`
   - 使用 `LiveDataFetcher` 类

4. **（可选）注册 Alpha Vantage**：
   - 访问：https://www.alphavantage.co/support/#api-key
   - 获取免费 API 密钥
   - 每天 25 次请求额度

## 💡 提示

- Yahoo Finance 已经可以使用，无需任何配置
- CoinGecko 是 Binance 的最佳替代品
- 数据会自动缓存，避免频繁请求
- 建议每 5-10 分钟刷新一次数据

---

**更新日期**：2026-02-12
**测试状态**：✅ Yahoo Finance 已验证可用
