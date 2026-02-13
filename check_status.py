#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
系统状态检查脚本
检查所有服务和功能是否正常运行
"""

import requests
import sys
import io

# 设置 UTF-8 编码输出 (Windows 兼容)
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

print("=" * 60)
print("QuantMuse 系统状态检查")
print("=" * 60)
print()

# 检查 FastAPI 服务
print("【1】FastAPI 服务 (端口 8000)")
try:
    response = requests.get("http://localhost:8000/api/health", timeout=5)
    if response.status_code == 200:
        print("  状态: [OK] 正常运行")
        print(f"  地址: http://localhost:8000")
    else:
        print(f"  状态: [FAIL] 异常 (状态码: {response.status_code})")
except Exception as e:
    print(f"  状态: [FAIL] 无法连接")
    print(f"  错误: {e}")
print()

# 检查 Streamlit 服务
print("【2】Streamlit 仪表板 (端口 8501)")
try:
    response = requests.get("http://localhost:8501/_stcore/health", timeout=5)
    if response.status_code == 200 or response.text == "ok":
        print("  状态: [OK] 正常运行")
        print(f"  地址: http://localhost:8501")
    else:
        print(f"  状态: [FAIL] 异常")
except Exception as e:
    print(f"  状态: [FAIL] 无法连接")
    print(f"  错误: {e}")
print()

# 检查股票数据 API
print("【3】股票数据 API")
try:
    response = requests.get("http://localhost:8000/api/realtime/stock/info/AAPL", timeout=10)
    if response.status_code == 200:
        data = response.json()['data']
        print(f"  状态: [OK] 正常")
        print(f"  测试: AAPL = ${data['price']:.2f}")
    else:
        print(f"  状态: [FAIL] 异常")
except Exception as e:
    print(f"  状态: [FAIL] 错误: {e}")
print()

# 检查加密货币数据 API
print("【4】加密货币数据 API")
try:
    response = requests.get("http://localhost:8000/api/realtime/crypto/price/bitcoin", timeout=10)
    if response.status_code == 200:
        data = response.json()['data']
        print(f"  状态: [OK] 正常")
        print(f"  测试: BTC = ${data['price']:,.2f}")
    else:
        print(f"  状态: [FAIL] 异常")
except Exception as e:
    print(f"  状态: [FAIL] 错误: {e}")
print()

# 检查数据获取功能
print("【5】数据获取功能测试")
try:
    from data_service.fetchers.live_data import LiveDataFetcher
    fetcher = LiveDataFetcher()

    # 测试 30 天数据
    data = fetcher.get_crypto_history('bitcoin', days=30)
    if not data.empty:
        print(f"  30 天数据: [OK] {len(data)} 条")
    else:
        print(f"  30 天数据: [FAIL] 空数据")

    # 测试 90 天数据
    data = fetcher.get_crypto_history('ethereum', days=90)
    if not data.empty:
        print(f"  90 天数据: [OK] {len(data)} 条")
    else:
        print(f"  90 天数据: [FAIL] 空数据")

except Exception as e:
    print(f"  状态: [FAIL] 错误: {e}")
print()

print("=" * 60)
print("检查完成!")
print("=" * 60)
print()
print("访问地址:")
print("  • Streamlit 仪表板: http://localhost:8501")
print("  • API 文档: http://localhost:8000/docs")
print()
print("提示:")
print("  • 如果服务未运行,请双击 '启动服务器.bat'")
print("  • 如果需要重启 Streamlit,请双击 '重启Streamlit.bat'")
print("  • 加密货币数据最多支持 365 天")
print()
