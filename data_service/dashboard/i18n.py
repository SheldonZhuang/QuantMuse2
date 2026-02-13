#!/usr/bin/env python3
"""
Extended Internationalization (i18n) support for Trading Dashboard
Supports: English, Chinese, Spanish, French, German, Japanese, Portuguese
"""

# Language translations
TRANSLATIONS = {
    'en': {
        # Page config
        'page_title': 'Trading System Dashboard',
        'main_header': '📈 Trading System Dashboard',

        # Sidebar
        'sidebar_title': '🎛️ Dashboard Controls',
        'language': 'Language',
        'date_range': '📅 Date Range',
        'start_date': 'Start Date',
        'end_date': 'End Date',
        'strategy': '🎯 Strategy',
        'select_strategy': 'Select Strategy',
        'symbols': '📈 Symbols',
        'select_symbols': 'Select Symbols',
        'capital': '💰 Capital',
        'initial_capital': 'Initial Capital ($)',

        # Asset Selection (NEW)
        'asset_type': 'Asset Type',
        'asset_stock': '📈 Stock',
        'asset_crypto': '₿ Cryptocurrency',
        'quick_select': 'Quick Select',
        'custom_input': 'Custom Input',
        'popular_stocks': 'Popular Stocks',
        'popular_cryptos': 'Popular Cryptocurrencies',
        'enter_stock_symbols': 'Enter stock symbols (comma separated)',
        'enter_crypto_ids': 'Enter CoinGecko IDs (comma separated)',
        'stock_placeholder': 'e.g., AAPL, GOOGL, MSFT',
        'crypto_placeholder': 'e.g., bitcoin, ethereum, solana',
        'crypto_help': 'Visit coingecko.com to find coin IDs',
        'selected': 'Selected',
        'warning_select_asset': 'Please select or enter at least one asset',

        # Tabs
        'tab_performance': '📊 Performance Analysis',
        'tab_backtest': '🎯 Strategy Backtest',
        'tab_market': '📈 Market Data',
        'tab_ai': '🤖 AI Analysis',
        'tab_system': '⚙️ System Status',

        # Performance Analysis
        'performance_title': 'Performance Metrics',
        'current_parameters': 'Current Parameters',
        'run_analysis': 'Run Analysis',
        'analysis_completed': 'Analysis completed successfully!',
        'click_to_calculate': 'Click the button above to calculate performance metrics based on your selected parameters',
        'detailed_metrics': 'Detailed Performance Metrics',
        'total_return': 'Total Return',
        'annualized_return': 'Annualized Return',
        'volatility': 'Volatility',
        'sharpe_ratio': 'Sharpe Ratio',
        'sortino_ratio': 'Sortino Ratio',
        'max_drawdown': 'Max Drawdown',
        'calmar_ratio': 'Calmar Ratio',
        'win_rate': 'Win Rate',
        'profit_factor': 'Profit Factor',
        'total_trades': 'Total Trades',
        'equity_curve': '📈 Equity Curve',
        'drawdown_chart': '📉 Drawdown Analysis',
        'returns_distribution': '📊 Returns Distribution',
        'monthly_returns': '📈 Rolling Metrics',

        # Strategy Backtest
        'backtest_title': 'Strategy Backtest',
        'strategy_parameters': '⚙️ Strategy Parameters',
        'backtest_settings': '📊 Backtest Settings',
        'lookback_period': 'Lookback Period',
        'rebalance_frequency': 'Rebalance Frequency',
        'commission': 'Commission (%)',
        'slippage': 'Slippage (%)',
        'run_backtest': 'Run Backtest',
        'backtest_results': '📈 Backtest Results',
        'backtest_completed': 'Backtest completed successfully!',
        'strategy_comparison': 'Strategy Comparison',

        # Market Data
        'market_title': 'Market Data',
        'select_symbol': 'Select Symbol',
        'time_period': 'Time Period',
        'price_chart': 'Price Chart',
        'volume_analysis': '📊 Volume Analysis',
        'technical_indicators': '📈 Technical Indicators',
        'market_statistics': '📋 Market Statistics',
        'current_price': 'Current Price',
        'daily_return': 'Daily Return',
        'avg_volume': 'Avg Volume',
        'showing_data_points': 'Showing data points for',

        # AI Analysis
        'ai_title': 'AI-Powered Analysis',
        'sentiment_analysis': '📝 Sentiment Analysis',
        'enter_text': 'Enter text for sentiment analysis',
        'analyze': 'Analyze',
        'sentiment': 'Sentiment',
        'confidence': 'Confidence',
        'keywords': 'Keywords',
        'detailed_analysis': '📊 Detailed Analysis',
        'cleaned_text': 'Cleaned Text',
        'topics': 'Topics',
        'language_detected': 'Language',
        'all_keywords': 'All Keywords',
        'factor_analysis': '📈 Factor Analysis',
        'calculate_factors': 'Calculate Factors',
        'factor_performance': '📊 Factor Performance',
        'factor_correlation': '🔥 Factor Correlation',
        'market_prediction': 'Market Prediction',
        'news_analysis': 'News Analysis',
        'recommendation': 'AI Recommendation',

        # System Status
        'system_title': 'System Status',
        'system_metrics': '📊 System Metrics',
        'cpu_usage': 'CPU Usage',
        'memory_usage': 'Memory Usage',
        'active_connections': 'Active Connections',
        'api_calls_per_min': 'API Calls/min',
        'system_health': '🏥 System Health',
        'recent_logs': '📋 Recent Logs',
        'data_sources': 'Data Sources',
        'api_status': 'API Status',
        'last_update': 'Last Update',

        # Strategies
        'momentum_strategy': 'Momentum Strategy',
        'value_strategy': 'Value Strategy',
        'mean_reversion': 'Mean Reversion',
        'custom_strategy': 'Custom',

        # Common
        'loading': 'Loading...',
        'error': 'Error',
        'success': 'Success',
        'warning': 'Warning',
        'info': 'Info',
        'date': 'Date',
        'value': 'Value',
        'change': 'Change',
        'status': 'Status',
        'metric': 'Metric',
        'active': 'Active',
        'inactive': 'Inactive',
        'connected': 'Connected',
        'disconnected': 'Disconnected',
        'days': 'days',
        'daily': 'Daily',
        'weekly': 'Weekly',
        'monthly': 'Monthly',
        'quarterly': 'Quarterly',
    },

    'zh': {
        # Page config
        'page_title': '量化交易系统仪表板',
        'main_header': '📈 量化交易系统仪表板',

        # Sidebar
        'sidebar_title': '🎛️ 控制面板',
        'language': '语言',
        'date_range': '📅 日期范围',
        'start_date': '开始日期',
        'end_date': '结束日期',
        'strategy': '🎯 策略',
        'select_strategy': '选择策略',
        'symbols': '📈 交易品种',
        'select_symbols': '选择交易品种',
        'capital': '💰 资金',
        'initial_capital': '初始资金 ($)',

        # Asset Selection
        'asset_type': '资产类型',
        'asset_stock': '📈 股票',
        'asset_crypto': '₿ 加密货币',
        'quick_select': '快速选择',
        'custom_input': '自定义输入',
        'popular_stocks': '热门股票',
        'popular_cryptos': '热门加密货币',
        'enter_stock_symbols': '输入股票代码（逗号分隔）',
        'enter_crypto_ids': '输入 CoinGecko ID（逗号分隔）',
        'stock_placeholder': '例如：AAPL, GOOGL, MSFT',
        'crypto_placeholder': '例如：bitcoin, ethereum, solana',
        'crypto_help': '访问 coingecko.com 查找币种 ID',
        'selected': '已选择',
        'warning_select_asset': '请至少选择或输入一个资产',

        # Tabs
        'tab_performance': '📊 绩效分析',
        'tab_backtest': '🎯 策略回测',
        'tab_market': '📈 市场数据',
        'tab_ai': '🤖 AI 分析',
        'tab_system': '⚙️ 系统状态',

        # Performance Analysis
        'performance_title': '绩效指标',
        'current_parameters': '当前参数',
        'run_analysis': '运行分析',
        'analysis_completed': '分析成功完成！',
        'click_to_calculate': '请点击上方按钮，根据侧边栏选择的参数计算绩效指标',
        'detailed_metrics': '详细绩效指标',
        'total_return': '总收益率',
        'annualized_return': '年化收益率',
        'volatility': '波动率',
        'sharpe_ratio': '夏普比率',
        'sortino_ratio': '索提诺比率',
        'max_drawdown': '最大回撤',
        'calmar_ratio': '卡玛比率',
        'win_rate': '胜率',
        'profit_factor': '盈亏比',
        'total_trades': '总交易次数',
        'equity_curve': '📈 权益曲线',
        'drawdown_chart': '📉 回撤分析',
        'returns_distribution': '📊 收益分布',
        'monthly_returns': '📈 滚动指标',

        # Strategy Backtest
        'backtest_title': '策略回测',
        'strategy_parameters': '⚙️ 策略参数',
        'backtest_settings': '📊 回测设置',
        'lookback_period': '回看周期',
        'rebalance_frequency': '再平衡频率',
        'commission': '手续费 (%)',
        'slippage': '滑点 (%)',
        'run_backtest': '运行回测',
        'backtest_results': '📈 回测结果',
        'backtest_completed': '回测成功完成！',
        'strategy_comparison': '策略对比',

        # Market Data
        'market_title': '市场数据',
        'select_symbol': '选择品种',
        'time_period': '时间周期',
        'price_chart': '价格走势',
        'volume_analysis': '📊 成交量分析',
        'technical_indicators': '📈 技术指标',
        'market_statistics': '📋 市场统计',
        'current_price': '当前价格',
        'daily_return': '日收益率',
        'avg_volume': '平均成交量',
        'showing_data_points': '显示数据点数',

        # AI Analysis
        'ai_title': 'AI 智能分析',
        'sentiment_analysis': '📝 情绪分析',
        'enter_text': '输入文本进行情绪分析',
        'analyze': '分析',
        'sentiment': '情绪',
        'confidence': '置信度',
        'keywords': '关键词',
        'detailed_analysis': '📊 详细分析',
        'cleaned_text': '清理后文本',
        'topics': '主题',
        'language_detected': '语言',
        'all_keywords': '所有关键词',
        'factor_analysis': '📈 因子分析',
        'calculate_factors': '计算因子',
        'factor_performance': '📊 因子表现',
        'factor_correlation': '🔥 因子相关性',
        'market_prediction': '市场预测',
        'news_analysis': '新闻分析',
        'recommendation': 'AI 推荐',

        # System Status
        'system_title': '系统状态',
        'system_metrics': '📊 系统指标',
        'cpu_usage': 'CPU 使用率',
        'memory_usage': '内存使用',
        'active_connections': '活跃连接',
        'api_calls_per_min': 'API 调用/分钟',
        'system_health': '🏥 系统健康度',
        'recent_logs': '📋 最近日志',
        'data_sources': '数据源',
        'api_status': 'API 状态',
        'last_update': '最后更新',

        # Strategies
        'momentum_strategy': '动量策略',
        'value_strategy': '价值策略',
        'mean_reversion': '均值回归',
        'custom_strategy': '自定义',

        # Common
        'loading': '加载中...',
        'error': '错误',
        'success': '成功',
        'warning': '警告',
        'info': '信息',
        'date': '日期',
        'value': '数值',
        'change': '变化',
        'status': '状态',
        'metric': '指标',
        'active': '活跃',
        'inactive': '未激活',
        'connected': '已连接',
        'disconnected': '未连接',
        'days': '天',
        'daily': '每日',
        'weekly': '每周',
        'monthly': '每月',
        'quarterly': '每季度',
    },

    'es': {
        # Page config
        'page_title': 'Panel de Sistema de Trading',
        'main_header': '📈 Panel de Sistema de Trading',

        # Sidebar
        'sidebar_title': '🎛️ Controles del Panel',
        'language': 'Idioma',
        'date_range': '📅 Rango de Fechas',
        'start_date': 'Fecha de Inicio',
        'end_date': 'Fecha de Fin',
        'strategy': '🎯 Estrategia',
        'select_strategy': 'Seleccionar Estrategia',
        'symbols': '📈 Símbolos',
        'select_symbols': 'Seleccionar Símbolos',
        'capital': '💰 Capital',
        'initial_capital': 'Capital Inicial ($)',

        # Asset Selection
        'asset_type': 'Tipo de Activo',
        'asset_stock': '📈 Acciones',
        'asset_crypto': '₿ Criptomoneda',
        'quick_select': 'Selección Rápida',
        'custom_input': 'Entrada Personalizada',
        'popular_stocks': 'Acciones Populares',
        'popular_cryptos': 'Criptomonedas Populares',
        'enter_stock_symbols': 'Ingrese símbolos de acciones (separados por comas)',
        'enter_crypto_ids': 'Ingrese IDs de CoinGecko (separados por comas)',
        'stock_placeholder': 'ej., AAPL, GOOGL, MSFT',
        'crypto_placeholder': 'ej., bitcoin, ethereum, solana',
        'crypto_help': 'Visite coingecko.com para encontrar IDs de monedas',
        'selected': 'Seleccionado',
        'warning_select_asset': 'Por favor seleccione o ingrese al menos un activo',

        # Tabs
        'tab_performance': '📊 Análisis de Rendimiento',
        'tab_backtest': '🎯 Prueba de Estrategia',
        'tab_market': '📈 Datos de Mercado',
        'tab_ai': '🤖 Análisis IA',
        'tab_system': '⚙️ Estado del Sistema',

        # Performance Analysis
        'performance_title': 'Métricas de Rendimiento',
        'current_parameters': 'Parámetros Actuales',
        'run_analysis': 'Ejecutar Análisis',
        'analysis_completed': '¡Análisis completado con éxito!',
        'click_to_calculate': 'Haga clic en el botón de arriba para calcular las métricas de rendimiento',
        'detailed_metrics': 'Métricas Detalladas de Rendimiento',
        'total_return': 'Retorno Total',
        'annualized_return': 'Retorno Anualizado',
        'volatility': 'Volatilidad',
        'sharpe_ratio': 'Ratio de Sharpe',
        'sortino_ratio': 'Ratio de Sortino',
        'max_drawdown': 'Caída Máxima',
        'calmar_ratio': 'Ratio de Calmar',
        'win_rate': 'Tasa de Éxito',
        'profit_factor': 'Factor de Beneficio',
        'total_trades': 'Total de Operaciones',
        'equity_curve': '📈 Curva de Capital',
        'drawdown_chart': '📉 Análisis de Caída',
        'returns_distribution': '📊 Distribución de Retornos',
        'monthly_returns': '📈 Métricas Móviles',

        # Strategy Backtest
        'backtest_title': 'Prueba de Estrategia',
        'strategy_parameters': '⚙️ Parámetros de Estrategia',
        'backtest_settings': '📊 Configuración de Prueba',
        'lookback_period': 'Período de Retrospección',
        'rebalance_frequency': 'Frecuencia de Rebalanceo',
        'commission': 'Comisión (%)',
        'slippage': 'Deslizamiento (%)',
        'run_backtest': 'Ejecutar Prueba',
        'backtest_results': '📈 Resultados de Prueba',
        'backtest_completed': '¡Prueba completada con éxito!',
        'strategy_comparison': 'Comparación de Estrategias',

        # Market Data
        'market_title': 'Datos de Mercado',
        'select_symbol': 'Seleccionar Símbolo',
        'time_period': 'Período de Tiempo',
        'price_chart': 'Gráfico de Precios',
        'volume_analysis': '📊 Análisis de Volumen',
        'technical_indicators': '📈 Indicadores Técnicos',
        'market_statistics': '📋 Estadísticas de Mercado',
        'current_price': 'Precio Actual',
        'daily_return': 'Retorno Diario',
        'avg_volume': 'Volumen Promedio',
        'showing_data_points': 'Mostrando puntos de datos para',

        # AI Analysis
        'ai_title': 'Análisis Impulsado por IA',
        'sentiment_analysis': '📝 Análisis de Sentimiento',
        'enter_text': 'Ingrese texto para análisis de sentimiento',
        'analyze': 'Analizar',
        'sentiment': 'Sentimiento',
        'confidence': 'Confianza',
        'keywords': 'Palabras Clave',
        'detailed_analysis': '📊 Análisis Detallado',
        'cleaned_text': 'Texto Limpio',
        'topics': 'Temas',
        'language_detected': 'Idioma',
        'all_keywords': 'Todas las Palabras Clave',
        'factor_analysis': '📈 Análisis de Factores',
        'calculate_factors': 'Calcular Factores',
        'factor_performance': '📊 Rendimiento de Factores',
        'factor_correlation': '🔥 Correlación de Factores',
        'market_prediction': 'Predicción de Mercado',
        'news_analysis': 'Análisis de Noticias',
        'recommendation': 'Recomendación IA',

        # System Status
        'system_title': 'Estado del Sistema',
        'system_metrics': '📊 Métricas del Sistema',
        'cpu_usage': 'Uso de CPU',
        'memory_usage': 'Uso de Memoria',
        'active_connections': 'Conexiones Activas',
        'api_calls_per_min': 'Llamadas API/min',
        'system_health': '🏥 Salud del Sistema',
        'recent_logs': '📋 Registros Recientes',
        'data_sources': 'Fuentes de Datos',
        'api_status': 'Estado de API',
        'last_update': 'Última Actualización',

        # Strategies
        'momentum_strategy': 'Estrategia de Momento',
        'value_strategy': 'Estrategia de Valor',
        'mean_reversion': 'Reversión a la Media',
        'custom_strategy': 'Personalizada',

        # Common
        'loading': 'Cargando...',
        'error': 'Error',
        'success': 'Éxito',
        'warning': 'Advertencia',
        'info': 'Información',
        'date': 'Fecha',
        'value': 'Valor',
        'change': 'Cambio',
        'status': 'Estado',
        'metric': 'Métrica',
        'active': 'Activo',
        'inactive': 'Inactivo',
        'connected': 'Conectado',
        'disconnected': 'Desconectado',
        'days': 'días',
        'daily': 'Diario',
        'weekly': 'Semanal',
        'monthly': 'Mensual',
        'quarterly': 'Trimestral',
    },
}


class I18n:
    """Internationalization helper class"""

    def __init__(self, language='en'):
        """
        Initialize i18n with specified language

        Args:
            language: Language code ('en', 'zh', 'es', etc.)
        """
        self.language = language
        self.translations = TRANSLATIONS.get(language, TRANSLATIONS['en'])

    def t(self, key, default=None):
        """
        Get translation for a key

        Args:
            key: Translation key
            default: Default value if key not found

        Returns:
            Translated string
        """
        return self.translations.get(key, default or key)

    def set_language(self, language):
        """
        Change current language

        Args:
            language: New language code
        """
        if language in TRANSLATIONS:
            self.language = language
            self.translations = TRANSLATIONS[language]

    def get_available_languages(self):
        """
        Get list of available languages

        Returns:
            Dictionary of language codes and names
        """
        return {
            'en': 'English',
            'zh': '中文',
            'es': 'Español',
        }


# Singleton instance
_i18n_instance = None


def get_i18n(language='en'):
    """
    Get or create i18n instance

    Args:
        language: Language code

    Returns:
        I18n instance
    """
    global _i18n_instance
    if _i18n_instance is None or _i18n_instance.language != language:
        _i18n_instance = I18n(language)
    return _i18n_instance
