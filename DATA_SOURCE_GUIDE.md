# 数据源配置指南

## 📊 概述

QuantMuse1 支持多种数据源来获取最新的股票和虚拟货币数据。本指南将帮助你配置这些数据源。

## 🎯 支持的数据源

### 1. **免费数据源（推荐新手）**

#### Yahoo Finance（股票数据 - 完全免费）
- **优点**：
  - ✅ 完全免费，无需 API 密钥
  - ✅ 覆盖全球主要股票市场
  - ✅ 实时数据（延迟 15 分钟）
  - ✅ 历史数据完整
- **缺点**：
  - ⚠️ 有请求频率限制
  - ⚠️ 不支持虚拟货币
- **使用方法**：
  ```python
  # 无需配置，直接使用
  import yfinance as yf

  # 获取股票数据
  data = yf.download('AAPL', start='2024-01-01', end='2024-12-31')

  # 获取实时价格
  ticker = yf.Ticker('AAPL')
  price = ticker.info['currentPrice']
  ```

#### Binance Public API（虚拟货币 - 免费）
- **优点**：
  - ✅ 完全免费（公开接口无需 API 密钥）
  - ✅ 实时虚拟货币数据
  - ✅ 支持数百种加密货币
  - ✅ 高频率更新
- **缺点**：
  - ⚠️ 仅限虚拟货币
  - ⚠️ 需要 API 密钥才能交易
- **使用方法**：
  ```python
  from binance.client import Client

  # 无需 API 密钥获取公开数据
  client = Client()

  # 获取 BTC 价格
  price = client.get_symbol_ticker(symbol="BTCUSDT")

  # 获取历史数据
  klines = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_1DAY, "1 Jan, 2024")
  ```

### 2. **付费/限量免费数据源**

#### Alpha Vantage（股票 + 外汇）
- **免费额度**：每天 25 次请求，每分钟 5 次
- **付费计划**：$49.99/月起（500 次/天）
- **注册地址**：https://www.alphavantage.co/support/#api-key
- **优点**：
  - ✅ 高质量股票数据
  - ✅ 支持技术指标
  - ✅ 外汇数据
- **配置方法**：
  ```json
  {
    "api_keys": {
      "alpha_vantage": {
        "api_key": "YOUR_API_KEY_HERE"
      }
    }
  }
  ```

#### Binance API（虚拟货币交易）
- **免费额度**：无限制（仅查询）
- **注册地址**：https://www.binance.com/zh-CN/my/settings/api-management
- **优点**：
  - ✅ 实时交易数据
  - ✅ 支持自动交易
  - ✅ WebSocket 实时推送
- **配置方法**：
  ```json
  {
    "api_keys": {
      "binance": {
        "api_key": "YOUR_API_KEY",
        "secret_key": "YOUR_SECRET_KEY",
        "testnet": false
      }
    }
  }
  ```

### 3. **其他推荐数据源**

#### Polygon.io（股票 + 加密货币）
- **免费额度**：每分钟 5 次请求
- **付费计划**：$29/月起
- **注册地址**：https://polygon.io/
- **特点**：
  - ✅ 美股实时数据
  - ✅ 加密货币数据
  - ✅ 新闻和情绪数据

#### Finnhub（股票 + 新闻）
- **免费额度**：每分钟 60 次请求
- **注册地址**：https://finnhub.io/
- **特点**：
  - ✅ 实时股票数据
  - ✅ 财经新闻
  - ✅ 公司基本面数据

#### CoinGecko（虚拟货币 - 免费）
- **免费额度**：每分钟 10-50 次
- **API 文档**：https://www.coingecko.com/en/api
- **特点**：
  - ✅ 完全免费
  - ✅ 支持 10,000+ 加密货币
  - ✅ 市场数据和历史价格

## 🚀 快速开始（推荐配置）

### 方案 1：完全免费方案

**适合**：个人学习、小规模测试

**配置**：
1. **股票数据**：使用 Yahoo Finance（无需配置）
2. **虚拟货币**：使用 Binance Public API（无需配置）

**示例代码**：
```python
# 股票数据
import yfinance as yf
aapl = yf.download('AAPL', period='1mo')

# 虚拟货币数据
from binance.client import Client
client = Client()
btc_price = client.get_symbol_ticker(symbol="BTCUSDT")
```

### 方案 2：混合方案（推荐）

**适合**：认真的量化交易研究

**配置**：
1. **股票数据**：Yahoo Finance（免费）+ Alpha Vantage（免费额度）
2. **虚拟货币**：Binance API（注册免费 API 密钥）

**步骤**：

#### 步骤 1：注册 Alpha Vantage
1. 访问：https://www.alphavantage.co/support/#api-key
2. 填写邮箱获取免费 API 密钥
3. 每天可以请求 25 次

#### 步骤 2：注册 Binance API（可选）
1. 访问：https://www.binance.com/zh-CN/my/settings/api-management
2. 创建 API 密钥
3. **重要**：仅启用"读取"权限，不要启用交易权限

#### 步骤 3：配置项目
```bash
# 复制配置文件
cd QuantMuse1
cp config.example.json config.json

# 编辑 config.json
notepad config.json  # Windows
# 或
nano config.json     # Linux/Mac
```

#### 步骤 4：填写 API 密钥
```json
{
  "api_keys": {
    "alpha_vantage": {
      "api_key": "YOUR_ALPHA_VANTAGE_KEY"
    },
    "binance": {
      "api_key": "YOUR_BINANCE_KEY",
      "secret_key": "YOUR_BINANCE_SECRET",
      "testnet": false
    }
  }
}
```

## 📝 使用示例

### 示例 1：获取股票数据（Yahoo Finance）

```python
import yfinance as yf
import pandas as pd

# 获取单只股票
aapl = yf.Ticker("AAPL")

# 获取历史数据
hist = aapl.history(period="1mo")
print(hist.head())

# 获取实时信息
info = aapl.info
print(f"当前价格: ${info['currentPrice']}")
print(f"市值: ${info['marketCap']:,}")

# 批量获取多只股票
symbols = ['AAPL', 'GOOGL', 'MSFT', 'TSLA']
data = yf.download(symbols, start='2024-01-01', end='2024-12-31')
print(data['Close'].head())
```

### 示例 2：获取虚拟货币数据（Binance）

```python
from binance.client import Client
import pandas as pd

# 无需 API 密钥（公开数据）
client = Client()

# 获取实时价格
btc_price = client.get_symbol_ticker(symbol="BTCUSDT")
print(f"BTC 价格: ${btc_price['price']}")

# 获取多个币种价格
symbols = ['BTCUSDT', 'ETHUSDT', 'BNBUSDT']
prices = client.get_all_tickers()
for price in prices:
    if price['symbol'] in symbols:
        print(f"{price['symbol']}: ${price['price']}")

# 获取历史 K 线数据
klines = client.get_historical_klines(
    "BTCUSDT",
    Client.KLINE_INTERVAL_1DAY,
    "1 Jan, 2024"
)

# 转换为 DataFrame
df = pd.DataFrame(klines, columns=[
    'timestamp', 'open', 'high', 'low', 'close', 'volume',
    'close_time', 'quote_volume', 'trades', 'taker_buy_base',
    'taker_buy_quote', 'ignore'
])
df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
print(df.head())
```

### 示例 3：使用 Alpha Vantage

```python
from alpha_vantage.timeseries import TimeSeries
import pandas as pd

# 需要 API 密钥
api_key = 'YOUR_API_KEY'
ts = TimeSeries(key=api_key, output_format='pandas')

# 获取日线数据
data, meta_data = ts.get_daily(symbol='AAPL', outputsize='full')
print(data.head())

# 获取实时数据
data, meta_data = ts.get_intraday(symbol='AAPL', interval='5min')
print(data.head())
```

## 🔧 在 Dashboard 中使用实时数据

### 修改 Dashboard 使用真实数据

创建一个新文件 `data_service/fetchers/real_data_fetcher.py`：

```python
import yfinance as yf
from binance.client import Client
import pandas as pd
from datetime import datetime, timedelta

class RealDataFetcher:
    """获取真实市场数据"""

    def __init__(self):
        self.binance_client = Client()  # 公开 API，无需密钥

    def get_stock_data(self, symbol, period='1mo'):
        """获取股票数据（Yahoo Finance）"""
        try:
            ticker = yf.Ticker(symbol)
            data = ticker.history(period=period)
            return data
        except Exception as e:
            print(f"获取股票数据失败: {e}")
            return None

    def get_crypto_data(self, symbol='BTCUSDT', days=30):
        """获取虚拟货币数据（Binance）"""
        try:
            # 获取历史 K 线
            start_date = (datetime.now() - timedelta(days=days)).strftime("%d %b, %Y")
            klines = self.binance_client.get_historical_klines(
                symbol,
                Client.KLINE_INTERVAL_1DAY,
                start_date
            )

            # 转换为 DataFrame
            df = pd.DataFrame(klines, columns=[
                'timestamp', 'open', 'high', 'low', 'close', 'volume',
                'close_time', 'quote_volume', 'trades', 'taker_buy_base',
                'taker_buy_quote', 'ignore'
            ])

            df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
            df.set_index('timestamp', inplace=True)

            # 转换数据类型
            for col in ['open', 'high', 'low', 'close', 'volume']:
                df[col] = df[col].astype(float)

            return df
        except Exception as e:
            print(f"获取虚拟货币数据失败: {e}")
            return None

    def get_current_price(self, symbol, asset_type='stock'):
        """获取当前价格"""
        try:
            if asset_type == 'stock':
                ticker = yf.Ticker(symbol)
                return ticker.info.get('currentPrice', 0)
            elif asset_type == 'crypto':
                price = self.binance_client.get_symbol_ticker(symbol=symbol)
                return float(price['price'])
        except Exception as e:
            print(f"获取价格失败: {e}")
            return 0
```

## 📊 数据源对比

| 数据源 | 股票 | 加密货币 | 免费额度 | 实时性 | 推荐度 |
|--------|------|----------|----------|--------|--------|
| Yahoo Finance | ✅ | ❌ | 无限制 | 15分钟延迟 | ⭐⭐⭐⭐⭐ |
| Binance Public | ❌ | ✅ | 无限制 | 实时 | ⭐⭐⭐⭐⭐ |
| Alpha Vantage | ✅ | ❌ | 25次/天 | 实时 | ⭐⭐⭐⭐ |
| Polygon.io | ✅ | ✅ | 5次/分钟 | 实时 | ⭐⭐⭐⭐ |
| Finnhub | ✅ | ❌ | 60次/分钟 | 实时 | ⭐⭐⭐⭐ |
| CoinGecko | ❌ | ✅ | 50次/分钟 | 5分钟延迟 | ⭐⭐⭐⭐ |

## 🎯 推荐方案总结

### 初学者（完全免费）
```
股票：Yahoo Finance
加密货币：Binance Public API
配置：无需任何 API 密钥
```

### 进阶用户（混合方案）
```
股票：Yahoo Finance + Alpha Vantage（免费额度）
加密货币：Binance API（注册免费密钥）
配置：仅需 Alpha Vantage 和 Binance API 密钥
```

### 专业用户（付费方案）
```
股票：Polygon.io 或 Alpha Vantage（付费）
加密货币：Binance API（完整功能）
新闻：Finnhub
配置：需要付费订阅
```

## 🔐 安全提示

1. **永远不要**将 API 密钥提交到 Git 仓库
2. **永远不要**启用 Binance API 的交易权限（除非你真的要交易）
3. **使用环境变量**存储敏感信息
4. **定期轮换** API 密钥
5. **设置 IP 白名单**（如果平台支持）

## 📞 获取帮助

如果遇到问题：
1. 检查 API 密钥是否正确
2. 确认网络连接正常
3. 查看 API 使用额度是否用完
4. 阅读官方 API 文档

---

**更新日期**：2026-02-12
**版本**：1.0.0
