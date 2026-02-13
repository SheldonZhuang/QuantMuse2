# 真实数据集成完成指南

## ✅ 集成完成！

Dashboard 现已成功集成真实的股票和加密货币数据！

## 🎯 新功能

### 1. 资产类型切换
在"市场数据"标签页中，现在可以选择：
- 📈 **Stock / 股票** - 使用 Yahoo Finance 数据
- ₿ **Cryptocurrency / 加密货币** - 使用 CoinGecko 数据

### 2. 支持的股票
- AAPL (Apple)
- GOOGL (Google)
- MSFT (Microsoft)
- TSLA (Tesla)
- AMZN (Amazon)
- NVDA (NVIDIA)
- META (Meta)
- NFLX (Netflix)

### 3. 支持的加密货币
- Bitcoin (BTC)
- Ethereum (ETH)
- Binance Coin (BNB)
- Solana (SOL)
- Cardano (ADA)

### 4. 时间周期选择

**股票：**
- 1 Day (1天)
- 5 Days (5天)
- 1 Month (1个月)
- 3 Months (3个月)
- 6 Months (6个月)
- 1 Year (1年)

**加密货币：**
- 7 Days (7天)
- 30 Days (30天)
- 90 Days (90天)
- 180 Days (180天)
- 1 Year (1年)

## 🚀 使用方法

### 步骤 1：访问 Dashboard
```
http://localhost:8501
```

### 步骤 2：切换到"市场数据"标签
点击顶部的 **"📈 Market Data / 市场数据"** 标签

### 步骤 3：选择资产类型
- 点击 **"📈 Stock / 股票"** 查看股票数据
- 点击 **"₿ Cryptocurrency / 加密货币"** 查看加密货币数据

### 步骤 4：选择品种和时间周期
- 从下拉菜单选择股票代码或加密货币
- 选择时间周期
- 数据会自动加载并显示

## 📊 显示的数据

### 价格图表
- 完整的历史价格走势
- 交互式图表（可缩放、悬停查看详情）
- 实时数据更新

### 技术指标
- **RSI (相对强弱指标)**
  - 超买线：70
  - 超卖线：30
  - 14周期计算

### 成交量分析
- 历史成交量柱状图
- 平均成交量统计

### 市场统计
- **当前价格** - 最新收盘价
- **日收益率** - 当日涨跌幅
- **波动率** - 年化波动率
- **平均成交量** - 期间平均成交量

### 详细信息（展开查看）

**股票：**
- 公司名称
- 市值
- 市盈率 (P/E)
- 成交量
- 股息率
- 52周最高/最低价

**加密货币：**
- 当前价格
- 24小时变化
- 市值
- 24小时成交量

## 🎨 界面示例

### 查看股票数据
```
📈 Market Data / 市场数据

Asset Type: [📈 Stock / 股票] [₿ Cryptocurrency / 加密货币]

Select Symbol: AAPL ▼
Time Period: 1 Month ▼

📊 Showing 21 data points for AAPL

📊 AAPL Price Chart
[交互式价格走势图]

📈 Technical Indicators        📊 Volume Analysis
[RSI 指标图]                   [成交量柱状图]

📋 Market Statistics
Current Price    Daily Return    Volatility    Avg Volume
$275.50         +0.67%          18.5%         51,397,410

📋 Detailed Information ▼
Company: Apple Inc.
Market Cap: $4,049,278,599,168
P/E Ratio: 34.83
...
```

### 查看加密货币数据
```
📈 Market Data / 市场数据

Asset Type: [📈 Stock / 股票] [₿ Cryptocurrency / 加密货币]

Select Symbol: Bitcoin (BTC) ▼
Time Period: 30 Days ▼

📊 Showing 169 data points for BTC

📊 BTC Price Chart
[交互式价格走势图]

📈 Technical Indicators        📊 Volume Analysis
[RSI 指标图]                   [成交量柱状图]

📋 Market Statistics
Current Price    Daily Return    Volatility    Avg Volume
$67,156.00      +0.51%          45.2%         50,442,589,743

📋 Detailed Information ▼
Price: $67,156.00
24h Change: +0.51%
Market Cap: $1,342,326,203,239
24h Volume: $50,442,589,743
```

## 🔄 数据更新

### 自动更新
- Dashboard 会在每次切换品种或时间周期时自动获取最新数据
- 刷新页面可以获取最新数据

### 手动刷新
- 按 `R` 键刷新页面
- 或点击浏览器刷新按钮

### 更新频率
- **股票数据**：15分钟延迟（Yahoo Finance 限制）
- **加密货币数据**：1-2分钟延迟（CoinGecko）

## 💡 使用技巧

1. **对比分析**
   - 在不同时间周期查看同一品种
   - 观察短期和长期趋势

2. **技术分析**
   - 使用 RSI 判断超买超卖
   - 观察成交量变化
   - 分析波动率

3. **多品种监控**
   - 快速切换不同股票
   - 对比不同加密货币表现

4. **数据导出**
   - 可以在代码中使用 `live_fetcher` 导出数据
   - 用于进一步分析或回测

## 🛠️ 技术细节

### 数据来源
- **股票**：Yahoo Finance API (yfinance)
- **加密货币**：CoinGecko API (pycoingecko)

### 数据格式
所有数据统一为 pandas DataFrame 格式：
```
Columns: Open, High, Low, Close, Volume
Index: Timestamp
```

### 错误处理
- 网络错误：显示错误消息，建议重试
- 数据为空：显示提示信息
- API 限制：自动降级到示例数据

## 📝 代码示例

### 在其他地方使用实时数据

```python
from data_service.fetchers.live_data import LiveDataFetcher

# 创建获取器
fetcher = LiveDataFetcher()

# 获取股票数据
aapl = fetcher.get_stock_data('AAPL', period='1mo')
print(f"AAPL 数据点数: {len(aapl)}")
print(f"最新价格: ${aapl['Close'].iloc[-1]:.2f}")

# 获取加密货币数据
btc = fetcher.get_crypto_history('bitcoin', days=30)
print(f"BTC 数据点数: {len(btc)}")
print(f"最新价格: ${btc['close'].iloc[-1]:.2f}")

# 批量获取
stocks = fetcher.get_multiple_stocks(['AAPL', 'GOOGL', 'MSFT'], period='1mo')
for symbol, data in stocks.items():
    print(f"{symbol}: {len(data)} 个数据点")

# 获取热门加密货币
trending = fetcher.get_trending_cryptos(10)
for coin in trending:
    print(f"{coin['name']} ({coin['symbol']})")
```

## ⚠️ 注意事项

1. **数据延迟**
   - 股票数据有 15 分钟延迟
   - 加密货币数据有 1-2 分钟延迟
   - 不适合高频交易

2. **请求限制**
   - Yahoo Finance：建议每分钟不超过 2000 次请求
   - CoinGecko：免费版每分钟 10-50 次请求
   - 建议添加缓存机制

3. **网络连接**
   - 需要稳定的互联网连接
   - 如果无法连接，会显示错误消息

4. **数据准确性**
   - 数据来自第三方 API
   - 仅供参考，不构成投资建议

## 🎉 总结

Dashboard 现已集成真实数据！

**主要改进：**
- ✅ 支持真实股票数据（Yahoo Finance）
- ✅ 支持真实加密货币数据（CoinGecko）
- ✅ 资产类型切换功能
- ✅ 多时间周期选择
- ✅ 详细信息展示
- ✅ 完整的错误处理

**立即体验：**
访问 http://localhost:8501，进入"市场数据"标签页，选择股票或加密货币，查看最新的真实数据！

---

**更新日期**：2026-02-12
**版本**：3.0.0
**状态**：✅ 已完成并测试通过
