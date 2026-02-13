#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
简化版 Web 服务启动脚本
用于快速测试和部署
"""

import sys
import os
import io

# 设置 UTF-8 编码输出 (Windows 兼容)
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

# 添加项目路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# 创建 FastAPI 应用
app = FastAPI(
    title="QuantMuse Trading System",
    description="量化交易系统 - 支持股票和加密货币实时数据",
    version="1.0.0"
)

# 配置 CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 挂载静态文件
app.mount("/static", StaticFiles(directory="static"), name="static")

# 导入实时数据 API
try:
    from data_service.web.realtime_api import router as realtime_router
    app.include_router(realtime_router)
    print("[OK] 实时数据 API 已加载")
except Exception as e:
    print(f"[WARNING] 实时数据 API 加载失败: {e}")


@app.get("/")
async def root():
    """返回主页"""
    return FileResponse("static/index.html")


@app.get("/api/health")
async def health():
    """健康检查"""
    return {
        "status": "healthy",
        "service": "QuantMuse Trading System",
        "features": [
            "实时股票数据 (Yahoo Finance)",
            "实时加密货币数据 (CoinGecko)",
            "多语言支持 (中文/英文/西班牙语/法语)",
            "量化策略回测",
            "因子分析"
        ]
    }


@app.get("/api/info")
async def info():
    """系统信息"""
    return {
        "name": "QuantMuse Trading System",
        "version": "1.0.0",
        "description": "生产级量化交易系统",
        "supported_languages": ["en", "zh", "es", "fr"],
        "data_sources": {
            "stocks": "Yahoo Finance (免费,无需 API 密钥)",
            "crypto": "CoinGecko (免费,无需 API 密钥)"
        },
        "endpoints": {
            "health": "/api/health",
            "stock_data": "/api/realtime/stock/data",
            "stock_info": "/api/realtime/stock/info/{symbol}",
            "stock_quote": "/api/realtime/stock/quote/{symbol}",
            "crypto_data": "/api/realtime/crypto/data",
            "crypto_price": "/api/realtime/crypto/price/{coin_id}",
            "crypto_trending": "/api/realtime/crypto/trending"
        }
    }


def main():
    """启动服务器"""
    print("=" * 60)
    print("QuantMuse 量化交易系统")
    print("=" * 60)
    print("功能:")
    print("  [OK] 实时股票数据 (Yahoo Finance)")
    print("  [OK] 实时加密货币数据 (CoinGecko)")
    print("  [OK] 多语言支持 (中文/英文/西班牙语/法语)")
    print("  [OK] 量化策略回测")
    print("  [OK] 因子分析")
    print()
    print("访问地址:")
    print("  本地: http://localhost:8000")
    print("  网络: http://0.0.0.0:8000")
    print()
    print("API 文档:")
    print("  Swagger UI: http://localhost:8000/docs")
    print("  ReDoc: http://localhost:8000/redoc")
    print()
    print("按 Ctrl+C 停止服务器")
    print("=" * 60)
    print()

    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        log_level="info"
    )


if __name__ == "__main__":
    main()
