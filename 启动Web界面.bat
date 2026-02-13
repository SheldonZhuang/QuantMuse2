@echo off
chcp 65001 >nul
echo ========================================
echo 🚀 启动量化交易系统 Web 界面
echo ========================================
echo.
echo 📊 Web 界面将在浏览器中打开
echo 🌐 访问地址: http://localhost:8000
echo ⏹️  按 Ctrl+C 停止服务
echo.
echo ========================================
echo.

cd /d "%~dp0"
python run_web_interface.py

pause
