#!/usr/bin/env python3
"""
实时数据 API 端点
提供股票和加密货币的实时数据
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Any, Optional
import logging
from datetime import datetime

# 导入数据获取器
try:
    from ..fetchers.live_data import LiveDataFetcher
except ImportError:
    from data_service.fetchers.live_data import LiveDataFetcher

logger = logging.getLogger(__name__)

# 创建路由器
router = APIRouter(prefix="/api/realtime", tags=["realtime"])

# 初始化数据获取器
data_fetcher = LiveDataFetcher()


class StockRequest(BaseModel):
    """股票数据请求"""
    symbols: List[str]
    period: str = "1mo"


class CryptoRequest(BaseModel):
    """加密货币数据请求"""
    coin_ids: List[str]
    days: int = 30


class MarketDataResponse(BaseModel):
    """市场数据响应"""
    success: bool
    data: Dict[str, Any]
    timestamp: str
    message: Optional[str] = None


@router.get("/health")
async def health_check():
    """健康检查"""
    return {
        "status": "healthy",
        "service": "realtime-data-api",
        "timestamp": datetime.now().isoformat()
    }


@router.post("/stock/data", response_model=MarketDataResponse)
async def get_stock_data(request: StockRequest):
    """
    获取股票历史数据

    Args:
        request: 包含股票代码列表和时间周期的请求

    Returns:
        MarketDataResponse: 包含股票数据的响应
    """
    try:
        result = {}

        for symbol in request.symbols:
            data = data_fetcher.get_stock_data(symbol, period=request.period)

            if not data.empty:
                # 转换为 JSON 格式
                result[symbol] = {
                    "data": data.reset_index().to_dict(orient='records'),
                    "latest": {
                        "close": float(data['Close'].iloc[-1]),
                        "volume": int(data['Volume'].iloc[-1]),
                        "date": data.index[-1].strftime('%Y-%m-%d')
                    }
                }
            else:
                result[symbol] = {"error": "No data available"}

        return MarketDataResponse(
            success=True,
            data=result,
            timestamp=datetime.now().isoformat()
        )

    except Exception as e:
        logger.error(f"Error fetching stock data: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/stock/info/{symbol}")
async def get_stock_info(symbol: str):
    """
    获取股票详细信息

    Args:
        symbol: 股票代码

    Returns:
        股票详细信息
    """
    try:
        info = data_fetcher.get_stock_info(symbol)

        if not info:
            raise HTTPException(status_code=404, detail=f"Stock {symbol} not found")

        return MarketDataResponse(
            success=True,
            data=info,
            timestamp=datetime.now().isoformat()
        )

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error fetching stock info for {symbol}: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/stock/quote/{symbol}")
async def get_stock_quote(symbol: str):
    """
    获取股票实时报价

    Args:
        symbol: 股票代码

    Returns:
        实时报价信息
    """
    try:
        quote = data_fetcher.get_stock_quote(symbol)

        if not quote:
            raise HTTPException(status_code=404, detail=f"Quote for {symbol} not found")

        return MarketDataResponse(
            success=True,
            data=quote,
            timestamp=datetime.now().isoformat()
        )

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error fetching quote for {symbol}: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/crypto/data", response_model=MarketDataResponse)
async def get_crypto_data(request: CryptoRequest):
    """
    获取加密货币历史数据

    Args:
        request: 包含币种 ID 列表和天数的请求

    Returns:
        MarketDataResponse: 包含加密货币数据的响应
    """
    try:
        result = {}

        for coin_id in request.coin_ids:
            data = data_fetcher.get_crypto_history(coin_id, days=request.days)

            if not data.empty:
                result[coin_id] = {
                    "data": data.reset_index().to_dict(orient='records'),
                    "latest": {
                        "price": float(data['price'].iloc[-1]),
                        "market_cap": float(data['market_cap'].iloc[-1]),
                        "volume": float(data['volume'].iloc[-1]),
                        "date": data.index[-1].strftime('%Y-%m-%d')
                    }
                }
            else:
                result[coin_id] = {"error": "No data available"}

        return MarketDataResponse(
            success=True,
            data=result,
            timestamp=datetime.now().isoformat()
        )

    except Exception as e:
        logger.error(f"Error fetching crypto data: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/crypto/price/{coin_id}")
async def get_crypto_price(coin_id: str):
    """
    获取加密货币当前价格

    Args:
        coin_id: CoinGecko 币种 ID

    Returns:
        当前价格信息
    """
    try:
        price_data = data_fetcher.get_crypto_price(coin_id)

        if not price_data:
            raise HTTPException(status_code=404, detail=f"Crypto {coin_id} not found")

        return MarketDataResponse(
            success=True,
            data=price_data,
            timestamp=datetime.now().isoformat()
        )

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error fetching crypto price for {coin_id}: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/crypto/trending")
async def get_trending_cryptos(limit: int = 10):
    """
    获取热门加密货币

    Args:
        limit: 返回数量限制

    Returns:
        热门币种列表
    """
    try:
        trending = data_fetcher.get_trending_cryptos(limit=limit)

        return MarketDataResponse(
            success=True,
            data={"trending": trending},
            timestamp=datetime.now().isoformat()
        )

    except Exception as e:
        logger.error(f"Error fetching trending cryptos: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/crypto/multiple")
async def get_multiple_cryptos(coin_ids: List[str]):
    """
    批量获取多个加密货币信息

    Args:
        coin_ids: 币种 ID 列表

    Returns:
        多个币种的信息
    """
    try:
        cryptos = data_fetcher.get_multiple_cryptos(coin_ids)

        return MarketDataResponse(
            success=True,
            data=cryptos,
            timestamp=datetime.now().isoformat()
        )

    except Exception as e:
        logger.error(f"Error fetching multiple cryptos: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/market/overview")
async def get_market_overview():
    """
    获取市场概览
    包括主要股票指数和加密货币

    Returns:
        市场概览数据
    """
    try:
        # 获取主要股票指数
        indices = ['SPY', 'QQQ', 'DIA', '^GSPC', '^IXIC', '^DJI']
        stock_data = {}

        for symbol in indices:
            try:
                quote = data_fetcher.get_stock_quote(symbol)
                if quote:
                    stock_data[symbol] = quote
            except:
                continue

        # 获取主要加密货币
        crypto_ids = ['bitcoin', 'ethereum', 'binancecoin', 'solana', 'cardano']
        crypto_data = data_fetcher.get_multiple_cryptos(crypto_ids)

        return MarketDataResponse(
            success=True,
            data={
                "stocks": stock_data,
                "cryptos": crypto_data
            },
            timestamp=datetime.now().isoformat()
        )

    except Exception as e:
        logger.error(f"Error fetching market overview: {e}")
        raise HTTPException(status_code=500, detail=str(e))
