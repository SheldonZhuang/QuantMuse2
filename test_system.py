#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
QuantMuse 系统测试脚本
测试所有主要功能
"""

import requests
import json
import sys
import io

# 设置 UTF-8 编码输出 (Windows 兼容)
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

print("=" * 60)
print("QuantMuse 系统功能测试")
print("=" * 60)
print()

# 测试 1: 健康检查
print("【测试 1】健康检查")
try:
    response = requests.get("http://localhost:8000/api/health")
    if response.status_code == 200:
        print("[OK] API 服务正常运行")
        print(f"  响应: {response.json()}")
    else:
        print("[FAIL] API 服务异常")
except Exception as e:
    print(f"[FAIL] 连接失败: {e}")
print()

# 测试 2: 股票数据
print("【测试 2】股票数据获取")
test_stocks = ["AAPL", "GOOGL", "MSFT"]
for symbol in test_stocks:
    try:
        response = requests.get(f"http://localhost:8000/api/realtime/stock/info/{symbol}")
        if response.status_code == 200:
            data = response.json()['data']
            print(f"[OK] {symbol}: ${data['price']:.2f} ({data['change']:+.2f}%)")
        else:
            print(f"[FAIL] {symbol}: 获取失败")
    except Exception as e:
        print(f"[FAIL] {symbol}: {e}")
print()

# 测试 3: 加密货币数据
print("【测试 3】加密货币数据获取")
test_cryptos = ["bitcoin", "ethereum", "solana"]
for coin_id in test_cryptos:
    try:
        response = requests.get(f"http://localhost:8000/api/realtime/crypto/price/{coin_id}")
        if response.status_code == 200:
            data = response.json()['data']
            print(f"[OK] {coin_id}: ${data['price']:,.2f} ({data['change_24h']:+.2f}%)")
        else:
            print(f"[FAIL] {coin_id}: 获取失败")
    except Exception as e:
        print(f"[FAIL] {coin_id}: {e}")
print()

# 测试 4: 热门加密货币
print("【测试 4】热门加密货币")
try:
    response = requests.get("http://localhost:8000/api/realtime/crypto/trending?limit=5")
    if response.status_code == 200:
        trending = response.json()['data']['trending']
        print("[OK] 热门币种:")
        for i, coin in enumerate(trending, 1):
            print(f"  {i}. {coin['name']} ({coin['symbol']}) - 排名 #{coin['market_cap_rank']}")
    else:
        print("[FAIL] 获取失败")
except Exception as e:
    print(f"[FAIL] {e}")
print()

# 测试 5: Streamlit 仪表板
print("【测试 5】Streamlit 仪表板")
try:
    response = requests.get("http://localhost:8501")
    if response.status_code == 200:
        print("[OK] Streamlit 仪表板正常运行")
        print("  访问地址: http://localhost:8501")
    else:
        print("[FAIL] Streamlit 仪表板异常")
except Exception as e:
    print(f"[FAIL] 连接失败: {e}")
print()

print("=" * 60)
print("测试完成!")
print("=" * 60)
print()
print("访问地址:")
print("  • Streamlit 仪表板: http://localhost:8501")
print("  • API 文档: http://localhost:8000/docs")
print("  • Web 界面: http://localhost:8000")
