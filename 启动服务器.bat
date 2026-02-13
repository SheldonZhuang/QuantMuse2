@echo off
chcp 65001 >nul
echo ============================================================
echo QuantMuse 量化交易系统
echo ============================================================
echo.
echo 正在启动服务器...
echo.
cd /d "%~dp0"
python run_simple_server.py
pause
