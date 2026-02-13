# 多语言切换功能说明

## 功能概述

QuantMuse1 量化交易系统 Dashboard 现已支持多语言切换功能，目前支持：
- 🇬🇧 English (英语)
- 🇨🇳 中文 (简体中文)

## 如何使用

### 切换语言

1. 打开 Dashboard：http://localhost:8501
2. 在左侧边栏顶部找到 **"Language / 语言"** 下拉菜单
3. 选择您想要的语言：
   - **English** - 英语界面
   - **中文** - 中文界面
4. 页面会自动刷新并应用新语言

### 支持的界面元素

所有主要界面元素都已翻译，包括：

#### 侧边栏控制
- 语言选择器
- 日期范围选择
- 策略选择
- 交易品种选择
- 初始资金设置

#### 主要标签页
- 📊 绩效分析 / Performance Analysis
- 🎯 策略回测 / Strategy Backtest
- 📈 市场数据 / Market Data
- 🤖 AI 分析 / AI Analysis
- ⚙️ 系统状态 / System Status

#### 绩效指标
- 总收益率 / Total Return
- 年化收益率 / Annualized Return
- 夏普比率 / Sharpe Ratio
- 索提诺比率 / Sortino Ratio
- 最大回撤 / Max Drawdown
- 卡玛比率 / Calmar Ratio
- 胜率 / Win Rate
- 盈亏比 / Profit Factor
- 总交易次数 / Total Trades

#### 图表标题
- 权益曲线 / Equity Curve
- 回撤分析 / Drawdown Analysis
- 收益分布 / Returns Distribution
- 月度收益热力图 / Monthly Returns Heatmap

## 技术实现

### 文件结构

```
data_service/dashboard/
├── dashboard_app.py    # 主应用文件（已更新支持 i18n）
├── i18n.py            # 国际化配置文件（新增）
├── charts.py          # 图表生成器
└── widgets.py         # 小部件
```

### 添加新语言

如果需要添加更多语言，请编辑 `data_service/dashboard/i18n.py` 文件：

```python
TRANSLATIONS = {
    'en': { ... },
    'zh': { ... },
    'ja': {  # 添加日语
        'page_title': '取引システムダッシュボード',
        'main_header': '📈 取引システムダッシュボード',
        # ... 更多翻译
    }
}
```

然后在 `get_available_languages()` 方法中添加新语言：

```python
def get_available_languages(self):
    return {
        'en': 'English',
        'zh': '中文',
        'ja': '日本語'  # 添加日语
    }
```

### 添加新的翻译键

在 `i18n.py` 的 `TRANSLATIONS` 字典中为每种语言添加新的键值对：

```python
TRANSLATIONS = {
    'en': {
        'new_feature': 'New Feature',
        # ...
    },
    'zh': {
        'new_feature': '新功能',
        # ...
    }
}
```

在代码中使用：

```python
st.header(i18n.t('new_feature'))
```

## 注意事项

1. **语言持久化**：语言选择会保存在 Streamlit 的 session state 中，在同一会话期间保持不变
2. **自动刷新**：切换语言时页面会自动刷新以应用新语言
3. **默认语言**：首次访问时默认使用英语
4. **图表标签**：部分图表库生成的标签可能仍为英文，这是图表库本身的限制

## 示例截图说明

### 英文界面
- 侧边栏显示 "Language" 和 "English"
- 标签页显示 "Performance Analysis", "Strategy Backtest" 等
- 指标显示 "Total Return", "Sharpe Ratio" 等

### 中文界面
- 侧边栏显示 "语言" 和 "中文"
- 标签页显示 "绩效分析", "策略回测" 等
- 指标显示 "总收益率", "夏普比率" 等

## 反馈与改进

如果发现翻译不准确或需要添加新的翻译，请：
1. 编辑 `data_service/dashboard/i18n.py` 文件
2. 修改相应的翻译文本
3. 重启 Dashboard 以应用更改

---

**更新日期**：2026-02-12
**版本**：1.0.0
