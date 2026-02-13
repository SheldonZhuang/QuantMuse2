@echo off
chcp 65001 >nul
echo ============================================================
echo 重启 Streamlit 仪表板
echo ============================================================
echo.
echo 正在停止旧的 Streamlit 进程...
taskkill /F /IM python.exe /FI "WINDOWTITLE eq *streamlit*" 2>nul
timeout /t 2 /nobreak >nul

echo.
echo 正在启动新的 Streamlit 服务...
cd /d "%~dp0"
start "Streamlit Dashboard" python -m streamlit run data_service/dashboard/dashboard_app.py --server.port 8501 --server.address localhost --browser.gatherUsageStats false

echo.
echo ============================================================
echo Streamlit 仪表板已启动!
echo.
echo 访问地址: http://localhost:8501
echo.
echo 提示: 修复已应用
echo   - 默认时间范围: 90 天
echo   - 加密货币最大: 365 天
echo   - 自动限制超出范围的请求
echo ============================================================
echo.
timeout /t 3
