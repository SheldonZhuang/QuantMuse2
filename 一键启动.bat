@echo off
chcp 65001 >nul
title QuantMuse 量化交易系统

:menu
cls
echo ╔══════════════════════════════════════════════════════════════╗
echo ║                                                              ║
echo ║          QuantMuse 量化交易系统 - 启动菜单                  ║
echo ║                                                              ║
echo ╚══════════════════════════════════════════════════════════════╝
echo.
echo 请选择要启动的服务:
echo.
echo   [1] 启动 Streamlit 仪表板 (推荐)
echo       → 多语言界面 + 实时数据 + 图表分析
echo       → 访问地址: http://localhost:8501
echo.
echo   [2] 启动 FastAPI 服务器
echo       → RESTful API 接口
echo       → 访问地址: http://localhost:8000
echo.
echo   [3] 同时启动两个服务
echo       → 完整功能体验
echo.
echo   [4] 运行系统测试
echo       → 测试所有功能是否正常
echo.
echo   [0] 退出
echo.
echo ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
set /p choice=请输入选项 (0-4):

if "%choice%"=="1" goto streamlit
if "%choice%"=="2" goto fastapi
if "%choice%"=="3" goto both
if "%choice%"=="4" goto test
if "%choice%"=="0" goto end
goto menu

:streamlit
cls
echo ========================================
echo 🚀 启动 Streamlit 仪表板
echo ========================================
echo.
cd /d "%~dp0"
python run_dashboard.py
pause
goto menu

:fastapi
cls
echo ========================================
echo 🚀 启动 FastAPI 服务器
echo ========================================
echo.
cd /d "%~dp0"
python run_simple_server.py
pause
goto menu

:both
cls
echo ========================================
echo 🚀 启动所有服务
echo ========================================
echo.
echo 正在启动 FastAPI 服务器...
cd /d "%~dp0"
start "FastAPI Server" cmd /k python run_simple_server.py
timeout /t 3 /nobreak >nul
echo.
echo 正在启动 Streamlit 仪表板...
start "Streamlit Dashboard" cmd /k python run_dashboard.py
echo.
echo ✓ 所有服务已启动
echo.
echo 访问地址:
echo   • Streamlit: http://localhost:8501
echo   • FastAPI:   http://localhost:8000
echo.
pause
goto menu

:test
cls
echo ========================================
echo 🧪 运行系统测试
echo ========================================
echo.
cd /d "%~dp0"
python test_system.py
echo.
pause
goto menu

:end
echo.
echo 感谢使用 QuantMuse 量化交易系统！
echo.
timeout /t 2 /nobreak >nul
exit
