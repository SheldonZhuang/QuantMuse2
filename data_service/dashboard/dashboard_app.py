#!/usr/bin/env python3
"""
Trading System Dashboard
A comprehensive Streamlit dashboard for trading system visualization
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta
import logging
import sys
import os

# Add the parent directory to the path to import our modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

try:
    from data_service.backtest import BacktestEngine, PerformanceAnalyzer
    from data_service.dashboard.charts import ChartGenerator
    from data_service.dashboard.widgets import DashboardWidgets
    from data_service.dashboard.i18n import get_i18n
    from data_service.factors import FactorCalculator, FactorBacktest
    from data_service.strategies import StrategyRegistry
    from data_service.ai import NLPProcessor, SentimentFactorCalculator
except ImportError as e:
    st.error(f"Failed to import required modules: {e}")
    st.info("Please install required dependencies: pip install -e .[ai,visualization]")
    st.stop()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TradingDashboard:
    """Main trading dashboard application"""
    
    def __init__(self):
        self.chart_generator = ChartGenerator()
        self.widgets = DashboardWidgets()
        self.performance_analyzer = PerformanceAnalyzer()
        self.backtest_engine = BacktestEngine()
        self.factor_calculator = FactorCalculator()
        self.factor_backtest = FactorBacktest()
        self.nlp_processor = NLPProcessor()
        self.sentiment_calculator = SentimentFactorCalculator()

        # 初始化实时数据获取器
        try:
            from data_service.fetchers.live_data import LiveDataFetcher
            self.live_fetcher = LiveDataFetcher()
            self.use_live_data = True
            logger.info("Live data fetcher initialized successfully")
        except Exception as e:
            logger.warning(f"Failed to initialize live data fetcher: {e}")
            self.live_fetcher = None
            self.use_live_data = False
        
    def run(self):
        """Run the dashboard application"""
        # Initialize language from session state or default to English
        if 'language' not in st.session_state:
            st.session_state.language = 'en'

        # Get i18n instance
        i18n = get_i18n(st.session_state.language)

        st.set_page_config(
            page_title=i18n.t('page_title'),
            page_icon="📈",
            layout="wide",
            initial_sidebar_state="expanded"
        )
        
        # Custom CSS
        st.markdown("""
        <style>
        .main-header {
            font-size: 2.5rem;
            color: #1f77b4;
            text-align: center;
            margin-bottom: 2rem;
        }
        .metric-card {
            background-color: #f0f2f6;
            padding: 1rem;
            border-radius: 0.5rem;
            border-left: 4px solid #1f77b4;
        }
        .sidebar .sidebar-content {
            background-color: #f8f9fa;
        }
        </style>
        """, unsafe_allow_html=True)
        
        # Header
        st.markdown(f'<h1 class="main-header">{i18n.t("main_header")}</h1>', unsafe_allow_html=True)

        # Sidebar
        self._create_sidebar(i18n)

        # Main content
        tab1, tab2, tab3, tab4, tab5 = st.tabs([
            i18n.t('tab_performance'),
            i18n.t('tab_backtest'),
            i18n.t('tab_market'),
            i18n.t('tab_ai'),
            i18n.t('tab_system')
        ])

        with tab1:
            self._show_performance_analysis(i18n)

        with tab2:
            self._show_strategy_backtest(i18n)

        with tab3:
            self._show_market_data(i18n)

        with tab4:
            self._show_ai_analysis(i18n)

        with tab5:
            self._show_system_status(i18n)
    
    def _create_sidebar(self, i18n):
        """Create sidebar with controls"""
        st.sidebar.title(i18n.t('sidebar_title'))

        # Language selector at the top
        st.sidebar.subheader(i18n.t('language'))
        languages = i18n.get_available_languages()
        current_lang = st.session_state.language

        selected_lang = st.sidebar.selectbox(
            i18n.t('language'),
            options=list(languages.keys()),
            format_func=lambda x: languages[x],
            index=list(languages.keys()).index(current_lang),
            key='language_selector'
        )

        # Update language if changed
        if selected_lang != st.session_state.language:
            st.session_state.language = selected_lang
            st.rerun()

        st.sidebar.markdown("---")

        # Date range selector
        st.sidebar.subheader(i18n.t('date_range'))

        # 默认使用 90 天,避免 API 限制问题
        default_days = 90

        start_date = st.sidebar.date_input(
            i18n.t('start_date'),
            value=datetime.now() - timedelta(days=default_days),
            max_value=datetime.now()
        )
        end_date = st.sidebar.date_input(
            i18n.t('end_date'),
            value=datetime.now(),
            max_value=datetime.now()
        )

        # 检查日期范围
        date_diff = (end_date - start_date).days
        if date_diff > 365:
            st.sidebar.warning("⚠️ 加密货币数据最多支持 365 天")
        elif date_diff > 730:
            st.sidebar.warning("⚠️ 建议使用较短的时间范围以获得更好的性能")

        # Strategy selector
        st.sidebar.subheader(i18n.t('strategy'))
        strategy_options = {
            "Momentum Strategy": i18n.t('momentum_strategy'),
            "Value Strategy": i18n.t('value_strategy'),
            "Mean Reversion": i18n.t('mean_reversion'),
            "Custom": i18n.t('custom_strategy')
        }
        selected_strategy = st.sidebar.selectbox(
            i18n.t('select_strategy'),
            options=list(strategy_options.keys()),
            format_func=lambda x: strategy_options[x]
        )

        # Symbols selector
        st.sidebar.subheader(i18n.t('symbols'))

        # Asset type selection
        asset_type = st.sidebar.radio(
            i18n.t('asset_type'),
            [i18n.t('asset_stock'), i18n.t('asset_crypto')],
            key='sidebar_asset_type'
        )

        if i18n.t('asset_stock') in asset_type:
            # Stock selection
            st.sidebar.write(f"**{i18n.t('quick_select')}:**")
            quick_symbols = st.sidebar.multiselect(
                i18n.t('popular_stocks'),
                ["AAPL", "GOOGL", "MSFT", "TSLA", "AMZN", "NVDA", "META", "NFLX",
                 "JPM", "V", "WMT", "DIS", "BABA", "TSM"],
                default=["AAPL"],
                key='quick_stock_select'
            )

            # Custom input
            st.sidebar.write(f"**{i18n.t('custom_input')}:**")
            custom_input = st.sidebar.text_input(
                i18n.t('enter_stock_symbols'),
                placeholder=i18n.t('stock_placeholder'),
                key='custom_stock_input'
            )

            # Merge selections
            symbols = quick_symbols.copy()
            if custom_input:
                custom_symbols = [s.strip().upper() for s in custom_input.split(',') if s.strip()]
                symbols.extend(custom_symbols)

            # Remove duplicates
            symbols = list(dict.fromkeys(symbols))

            if not symbols:
                st.sidebar.warning(f"⚠️ {i18n.t('warning_select_asset')}")
                symbols = ["AAPL"]

            st.sidebar.success(f"✅ {i18n.t('selected')}: {', '.join(symbols)}")

        else:
            # Cryptocurrency selection
            st.sidebar.write(f"**{i18n.t('quick_select')}:**")
            crypto_map = {
                'Bitcoin (BTC)': 'bitcoin',
                'Ethereum (ETH)': 'ethereum',
                'Binance Coin (BNB)': 'binancecoin',
                'Solana (SOL)': 'solana',
                'Cardano (ADA)': 'cardano',
                'XRP (XRP)': 'ripple',
                'Dogecoin (DOGE)': 'dogecoin',
                'Polkadot (DOT)': 'polkadot'
            }

            selected_cryptos = st.sidebar.multiselect(
                i18n.t('popular_cryptos'),
                list(crypto_map.keys()),
                default=['Bitcoin (BTC)'],
                key='quick_crypto_select'
            )

            # Custom input
            st.sidebar.write(f"**{i18n.t('custom_input')}:**")
            custom_crypto_input = st.sidebar.text_input(
                i18n.t('enter_crypto_ids'),
                placeholder=i18n.t('crypto_placeholder'),
                key='custom_crypto_input',
                help=i18n.t('crypto_help')
            )

            # Merge selections
            symbols = [crypto_map[c] for c in selected_cryptos]
            if custom_crypto_input:
                custom_cryptos = [s.strip().lower() for s in custom_crypto_input.split(',') if s.strip()]
                symbols.extend(custom_cryptos)

            # Remove duplicates
            symbols = list(dict.fromkeys(symbols))

            if not symbols:
                st.sidebar.warning(f"⚠️ {i18n.t('warning_select_asset')}")
                symbols = ["bitcoin"]

            st.sidebar.success(f"✅ {i18n.t('selected')}: {', '.join(symbols)}")

        # Initial capital
        st.sidebar.subheader(i18n.t('capital'))
        initial_capital = st.sidebar.number_input(
            i18n.t('initial_capital'),
            min_value=1000,
            max_value=1000000,
            value=100000,
            step=10000
        )
        
        # Store in session state
        st.session_state.update({
            'start_date': start_date,
            'end_date': end_date,
            'selected_strategy': selected_strategy,
            'symbols': symbols,
            'asset_type': asset_type,
            'initial_capital': initial_capital
        })
    
    def _show_performance_analysis(self, i18n):
        """Show performance analysis tab"""
        st.header(i18n.t('performance_title'))

        # Display current parameters
        symbols = st.session_state.get('symbols', ['AAPL'])
        start_date = st.session_state.get('start_date', datetime.now() - timedelta(days=365))
        end_date = st.session_state.get('end_date', datetime.now())
        selected_strategy = st.session_state.get('selected_strategy', 'Momentum Strategy')
        initial_capital = st.session_state.get('initial_capital', 100000)
        asset_type = st.session_state.get('asset_type', i18n.t('asset_stock'))

        st.info(f"📊 {i18n.t('current_parameters')}: {asset_type} {', '.join(symbols)} | {i18n.t('strategy')} {selected_strategy} | {i18n.t('date')} {start_date} - {end_date} | {i18n.t('initial_capital')} ${initial_capital:,}")

        # Add run analysis button
        if st.button(f"🚀 {i18n.t('run_backtest')}", type="primary", key="run_performance_analysis"):
            with st.spinner(i18n.t('loading')):
                # Get real data and calculate performance
                sample_data = self._calculate_real_performance(
                    symbols, start_date, end_date, selected_strategy, initial_capital, asset_type
                )
                # Store in session state
                st.session_state['performance_data'] = sample_data
                st.session_state['performance_calculated'] = True
                st.success(f"✅ {i18n.t('analysis_completed')}")

        # Check if performance has been calculated
        if st.session_state.get('performance_calculated', False):
            sample_data = st.session_state.get('performance_data')
        else:
            # Show prompt
            st.warning(f"👆 {i18n.t('click_to_calculate')}")
            # Use sample data
            sample_data = self._generate_sample_performance_data()

        # Performance metrics
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric(
                i18n.t('total_return'),
                f"{sample_data['total_return']:.2%}",
                f"{sample_data['total_return_delta']:+.2%}"
            )
        
        with col2:
            st.metric(
                i18n.t('sharpe_ratio'),
                f"{sample_data['sharpe_ratio']:.2f}",
                f"{sample_data['sharpe_delta']:+.2f}"
            )

        with col3:
            st.metric(
                i18n.t('max_drawdown'),
                f"{sample_data['max_drawdown']:.2%}",
                f"{sample_data['drawdown_delta']:+.2%}"
            )

        with col4:
            st.metric(
                i18n.t('win_rate'),
                f"{sample_data['win_rate']:.1%}",
                f"{sample_data['win_rate_delta']:+.1%}"
            )

        # Charts
        col1, col2 = st.columns(2)

        with col1:
            st.subheader(i18n.t('equity_curve'))
            equity_fig = self.chart_generator.create_equity_curve(sample_data['equity_data'])
            st.plotly_chart(equity_fig, use_container_width=True, key='equity_curve_chart')

        with col2:
            st.subheader(i18n.t('drawdown_chart'))
            drawdown_fig = self.chart_generator.create_drawdown_chart(sample_data['drawdown_data'])
            st.plotly_chart(drawdown_fig, use_container_width=True, key='drawdown_chart')

        # Additional charts
        col1, col2 = st.columns(2)

        with col1:
            st.subheader(i18n.t('returns_distribution'))
            returns_fig = self.chart_generator.create_returns_distribution(sample_data['returns'])
            st.plotly_chart(returns_fig, use_container_width=True, key='returns_distribution_chart')

        with col2:
            st.subheader(i18n.t('monthly_returns'))
            rolling_fig = self.chart_generator.create_rolling_metrics(sample_data['returns'])
            st.plotly_chart(rolling_fig, use_container_width=True, key='rolling_metrics_chart')

        # Performance table
        st.subheader(i18n.t('performance_title'))
        metrics_df = pd.DataFrame([
            [i18n.t('total_return'), f"{sample_data['total_return']:.2%}"],
            [i18n.t('annualized_return'), f"{sample_data['annualized_return']:.2%}"],
            [i18n.t('sharpe_ratio'), f"{sample_data['sharpe_ratio']:.2f}"],
            [i18n.t('sortino_ratio'), f"{sample_data['sortino_ratio']:.2f}"],
            [i18n.t('max_drawdown'), f"{sample_data['max_drawdown']:.2%}"],
            [i18n.t('calmar_ratio'), f"{sample_data['calmar_ratio']:.2f}"],
            [i18n.t('win_rate'), f"{sample_data['win_rate']:.1%}"],
            [i18n.t('profit_factor'), f"{sample_data['profit_factor']:.2f}"],
            [i18n.t('total_trades'), str(sample_data['total_trades'])],
        ], columns=[i18n.t('status'), i18n.t('value')])

        st.dataframe(metrics_df, use_container_width=True)
    
    def _show_strategy_backtest(self, i18n):
        """Show strategy backtest tab"""
        st.header(i18n.t('backtest_title'))
        
        # Strategy configuration
        col1, col2 = st.columns(2)

        with col1:
            st.subheader(i18n.t('strategy_parameters'))

            # Strategy type
            strategy_type = st.selectbox(
                i18n.t('select_strategy'),
                ["Momentum", "Mean Reversion", "Value", "Multi-Factor"]
            )

            # Parameters based on strategy type
            if strategy_type == "Momentum":
                lookback_period = st.slider(i18n.t('lookback_period'), 5, 252, 20)
                momentum_threshold = st.slider("Momentum Threshold", 0.01, 0.10, 0.05, 0.01)
            elif strategy_type == "Mean Reversion":
                lookback_period = st.slider(i18n.t('lookback_period'), 5, 252, 20)
                reversion_threshold = st.slider("Reversion Threshold", 1.0, 3.0, 2.0, 0.1)
            elif strategy_type == "Value":
                pe_ratio_max = st.slider("Max P/E Ratio", 10, 50, 25)
                pb_ratio_max = st.slider("Max P/B Ratio", 1, 10, 3)
            else:  # Multi-Factor
                momentum_weight = st.slider("Momentum Weight", 0.0, 1.0, 0.5, 0.1)
                value_weight = st.slider("Value Weight", 0.0, 1.0, 0.3, 0.1)
                quality_weight = st.slider("Quality Weight", 0.0, 1.0, 0.2, 0.1)
        
        with col2:
            st.subheader(i18n.t('backtest_settings'))

            # Commission rate
            commission_rate = st.slider(i18n.t('commission'), 0.0, 1.0, 0.1, 0.01) / 100

            # Rebalancing frequency
            rebalance_freq = st.selectbox(
                i18n.t('rebalance_frequency'),
                [i18n.t('daily'), i18n.t('weekly'), i18n.t('monthly'), "Quarterly"]
            )

            # Position sizing
            position_size = st.slider("Position Size (%)", 1, 100, 10)

        # Run backtest button
        if st.button(f"🚀 {i18n.t('run_backtest')}", type="primary"):
            with st.spinner(i18n.t('loading')):
                # Generate sample backtest results
                backtest_results = self._generate_sample_backtest_results()

                # Display results
                self._display_backtest_results(backtest_results, i18n)
    
    def _show_market_data(self, i18n):
        """Show market data tab"""
        st.header(i18n.t('market_title'))

        # Asset type selection
        asset_type = st.radio(
            i18n.t('asset_type'),
            [i18n.t('asset_stock'), i18n.t('asset_crypto')],
            horizontal=True
        )

        # Display different selectors based on asset type
        if i18n.t('asset_stock') in asset_type:
            # Stock symbol selection
            stock_symbols = ['AAPL', 'GOOGL', 'MSFT', 'TSLA', 'AMZN', 'NVDA', 'META', 'NFLX']
            symbol = st.selectbox(i18n.t('select_symbol'), stock_symbols)

            # Time period selection
            period_map = {
                '1 Day': '1d',
                '5 Days': '5d',
                '1 Month': '1mo',
                '3 Months': '3mo',
                '6 Months': '6mo',
                '1 Year': '1y'
            }
            period_label = st.selectbox(i18n.t('time_period'), list(period_map.keys()), index=2)
            period = period_map[period_label]

            # Get real stock data
            if self.use_live_data and self.live_fetcher:
                with st.spinner(i18n.t('loading')):
                    market_data = self.live_fetcher.get_stock_data(symbol, period=period)
                    stock_info = self.live_fetcher.get_stock_info(symbol)
            else:
                st.warning(f"{i18n.t('warning')}: Live data not available, using sample data")
                market_data = self._generate_sample_market_data(symbol)
                stock_info = {}

        else:
            # Cryptocurrency selection
            crypto_map = {
                'Bitcoin (BTC)': 'bitcoin',
                'Ethereum (ETH)': 'ethereum',
                'Binance Coin (BNB)': 'binancecoin',
                'Solana (SOL)': 'solana',
                'Cardano (ADA)': 'cardano'
            }
            crypto_label = st.selectbox(i18n.t('select_symbol'), list(crypto_map.keys()))
            coin_id = crypto_map[crypto_label]
            symbol = crypto_label.split('(')[1].replace(')', '')

            # Time period selection
            days_map = {
                '7 Days': 7,
                '30 Days': 30,
                '90 Days': 90,
                '180 Days': 180,
                '1 Year': 365
            }
            days_label = st.selectbox(i18n.t('time_period'), list(days_map.keys()), index=1)
            days = days_map[days_label]

            # Get real cryptocurrency data
            if self.use_live_data and self.live_fetcher:
                with st.spinner(i18n.t('loading')):
                    market_data = self.live_fetcher.get_crypto_history(coin_id, days=days)
                    crypto_info = self.live_fetcher.get_crypto_price(coin_id)
            else:
                st.warning(f"{i18n.t('warning')}: Live data not available, using sample data")
                market_data = self._generate_sample_market_data(symbol)
                crypto_info = {}

        # Check if data is valid
        if market_data.empty:
            st.error(f"{i18n.t('error')}: Failed to fetch data. Please try again later.")
            return

        # Standardize column names (Yahoo Finance returns uppercase column names)
        if 'Close' in market_data.columns:
            market_data = market_data.rename(columns={
                'Open': 'open', 'High': 'high',
                'Low': 'low', 'Close': 'close', 'Volume': 'volume'
            })

        # Display data information
        st.info(f"📊 {i18n.t('showing_data_points')} {symbol}: {len(market_data)}")

        # Price chart
        st.subheader(f"📊 {symbol} {i18n.t('price_chart')}")
        price_fig = self.chart_generator.create_real_time_price_chart(market_data, symbol)
        st.plotly_chart(price_fig, use_container_width=True, key='market_price_chart')

        # Technical indicators
        col1, col2 = st.columns(2)

        with col1:
            st.subheader(i18n.t('technical_indicators'))

            # RSI
            if len(market_data) >= 14:  # RSI requires at least 14 data points
                rsi_data = self._calculate_rsi(market_data['close'])
                rsi_fig = go.Figure()
                rsi_fig.add_trace(go.Scatter(x=market_data.index, y=rsi_data, name='RSI'))
                rsi_fig.add_hline(y=70, line_dash="dash", line_color="red", name="Overbought")
                rsi_fig.add_hline(y=30, line_dash="dash", line_color="green", name="Oversold")
                rsi_fig.update_layout(title="RSI (14)", height=300)
                st.plotly_chart(rsi_fig, use_container_width=True, key='rsi_chart')
            else:
                st.info("Not enough data for RSI calculation (need at least 14 points)")

        with col2:
            st.subheader(i18n.t('volume_analysis'))

            # Volume chart
            volume_fig = go.Figure()
            volume_fig.add_trace(go.Bar(
                x=market_data.index,
                y=market_data['volume'],
                name='Volume',
                marker_color='rgba(0, 128, 255, 0.6)'
            ))
            volume_fig.update_layout(title="Trading Volume", height=300)
            st.plotly_chart(volume_fig, use_container_width=True, key='volume_chart')

        # Market statistics
        st.subheader(i18n.t('market_statistics'))

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            current_price = market_data['close'].iloc[-1]
            st.metric(i18n.t('current_price'), f"${current_price:.2f}")

        with col2:
            if len(market_data) >= 2:
                daily_return = (market_data['close'].iloc[-1] / market_data['close'].iloc[-2] - 1) * 100
                st.metric(i18n.t('daily_return'), f"{daily_return:.2f}%")
            else:
                st.metric(i18n.t('daily_return'), "N/A")

        with col3:
            if len(market_data) >= 2:
                volatility = market_data['close'].pct_change().std() * np.sqrt(252) * 100
                st.metric(i18n.t('volatility'), f"{volatility:.2f}%")
            else:
                st.metric(i18n.t('volatility'), "N/A")

        with col4:
            avg_volume = market_data['volume'].mean()
            st.metric(i18n.t('avg_volume'), f"{avg_volume:,.0f}")

        # 显示额外信息（如果有）
        if "Stock" in asset_type and stock_info:
            with st.expander("📋 Detailed Information / 详细信息"):
                info_col1, info_col2, info_col3 = st.columns(3)

                with info_col1:
                    st.write(f"**Company / 公司:** {stock_info.get('name', 'N/A')}")
                    st.write(f"**Market Cap / 市值:** ${stock_info.get('market_cap', 0):,.0f}")
                    st.write(f"**P/E Ratio / 市盈率:** {stock_info.get('pe_ratio', 0):.2f}")

                with info_col2:
                    st.write(f"**Volume / 成交量:** {stock_info.get('volume', 0):,}")
                    st.write(f"**Dividend Yield / 股息率:** {stock_info.get('dividend_yield', 0):.2%}")

                with info_col3:
                    st.write(f"**52W High / 52周最高:** ${stock_info.get('fifty_two_week_high', 0):.2f}")
                    st.write(f"**52W Low / 52周最低:** ${stock_info.get('fifty_two_week_low', 0):.2f}")

        elif "Cryptocurrency" in asset_type and crypto_info:
            with st.expander("📋 Detailed Information / 详细信息"):
                info_col1, info_col2 = st.columns(2)

                with info_col1:
                    st.write(f"**Price / 价格:** ${crypto_info.get('price', 0):,.2f}")
                    st.write(f"**24h Change / 24小时变化:** {crypto_info.get('change_24h', 0):+.2f}%")

                with info_col2:
                    st.write(f"**Market Cap / 市值:** ${crypto_info.get('market_cap', 0):,.0f}")
                    st.write(f"**24h Volume / 24小时成交量:** ${crypto_info.get('volume_24h', 0):,.0f}")
    
    def _show_ai_analysis(self, i18n):
        """Show AI analysis tab"""
        st.header(i18n.t('ai_title'))

        # NLP Analysis
        st.subheader(i18n.t('sentiment_analysis'))

        # Text input for analysis
        text_input = st.text_area(
            i18n.t('enter_text'),
            value="Apple's quarterly earnings exceeded expectations, driving stock price higher by 5%! 🚀",
            height=100
        )

        if st.button(f"🔍 {i18n.t('analyze')}"):
            with st.spinner(i18n.t('loading')):
                # Process text
                processed = self.nlp_processor.preprocess_text(text_input)

                # Display results
                col1, col2, col3 = st.columns(3)

                with col1:
                    st.metric(i18n.t('sentiment'), processed.sentiment_label)

                with col2:
                    st.metric(i18n.t('confidence'), f"{processed.sentiment_score:.3f}")

                with col3:
                    st.metric(i18n.t('keywords'), ", ".join(processed.keywords[:3]))

                # Show detailed analysis
                st.subheader(i18n.t('detailed_analysis'))

                col1, col2 = st.columns(2)

                with col1:
                    st.write(f"**{i18n.t('cleaned_text')}:**")
                    st.write(processed.cleaned_text)

                    st.write(f"**{i18n.t('topics')}:**")
                    st.write(", ".join(processed.topics))

                with col2:
                    st.write(f"**{i18n.t('language_detected')}:**")
                    st.write(processed.language)

                    st.write(f"**{i18n.t('all_keywords')}:**")
                    st.write(", ".join(processed.keywords))

        # Factor Analysis
        st.subheader(i18n.t('factor_analysis'))

        # Factor selection
        factors = st.multiselect(
            "Select Factors to Analyze",
            ["Momentum", "Value", "Quality", "Size", "Volatility", "Sentiment"],
            default=["Momentum", "Value"]
        )

        if st.button(f"📊 {i18n.t('calculate_factors')}"):
            with st.spinner(i18n.t('loading')):
                # Generate sample factor data
                factor_data = self._generate_sample_factor_data()

                # Display factor performance
                st.subheader(i18n.t('factor_performance'))

                # Factor performance table
                factor_perf_df = pd.DataFrame([
                    ["Momentum", 0.15, 0.08, 1.88, 0.65],
                    ["Value", 0.12, 0.06, 2.00, 0.58],
                    ["Quality", 0.10, 0.05, 2.00, 0.52],
                    ["Size", 0.08, 0.07, 1.14, 0.45],
                ], columns=["Factor", "Return", "Volatility", "Sharpe", "IC"])

                st.dataframe(factor_perf_df, use_container_width=True)

                # Factor correlation heatmap
                st.subheader(i18n.t('factor_correlation'))
                correlation_data = np.random.rand(4, 4)
                correlation_data = (correlation_data + correlation_data.T) / 2
                np.fill_diagonal(correlation_data, 1)

                corr_fig = px.imshow(
                    correlation_data,
                    labels=dict(x="Factor", y="Factor", color="Correlation"),
                    x=["Momentum", "Value", "Quality", "Size"],
                    y=["Momentum", "Value", "Quality", "Size"],
                    color_continuous_scale="RdBu",
                    aspect="auto"
                )
                st.plotly_chart(corr_fig, use_container_width=True, key='factor_correlation_chart')
    
    def _show_system_status(self, i18n):
        """Show system status tab"""
        st.header(i18n.t('system_title'))

        # System metrics
        st.subheader(i18n.t('system_metrics'))
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric(i18n.t('cpu_usage'), "45%", "5%")

        with col2:
            st.metric(i18n.t('memory_usage'), "2.3 GB", "0.2 GB")

        with col3:
            st.metric(i18n.t('active_connections'), "12", "2")

        with col4:
            st.metric(i18n.t('api_calls_per_min'), "156", "23")

        # System health
        st.subheader(i18n.t('system_health'))

        # Health indicators
        health_data = {
            "Database Connection": "✅ Healthy",
            "API Services": "✅ Healthy",
            "Data Feeds": "✅ Healthy",
            "Strategy Engine": "✅ Healthy",
            "Risk Management": "✅ Healthy",
            "Order Execution": "⚠️ Warning",
            "Cache System": "✅ Healthy"
        }

        for service, status in health_data.items():
            if "✅" in status:
                st.success(f"{service}: {status}")
            elif "⚠️" in status:
                st.warning(f"{service}: {status}")
            else:
                st.error(f"{service}: {status}")

        # Recent logs
        st.subheader(i18n.t('recent_logs'))
        
        logs = [
            ("2024-01-15 10:30:15", "INFO", "Strategy execution completed successfully"),
            ("2024-01-15 10:29:45", "INFO", "Market data updated for AAPL, GOOGL, MSFT"),
            ("2024-01-15 10:29:30", "WARNING", "High latency detected in order execution"),
            ("2024-01-15 10:28:15", "INFO", "Risk check passed for new order"),
            ("2024-01-15 10:27:30", "INFO", "Sentiment analysis completed for 50 news articles")
        ]
        
        log_df = pd.DataFrame(logs, columns=["Timestamp", "Level", "Message"])
        st.dataframe(log_df, use_container_width=True)
    
    def _generate_sample_performance_data(self):
        """Generate sample performance data for demonstration"""
        dates = pd.date_range(start='2023-01-01', end='2024-01-15', freq='D')
        np.random.seed(42)

        # Generate equity curve
        returns = np.random.normal(0.0005, 0.02, len(dates))
        equity = 100000 * np.cumprod(1 + returns)
        equity_data = pd.DataFrame({'equity': equity}, index=dates)

        # Calculate metrics
        total_return = (equity[-1] / equity[0] - 1)
        annualized_return = total_return * 252 / len(dates)
        volatility = np.std(returns) * np.sqrt(252)
        sharpe_ratio = annualized_return / volatility if volatility > 0 else 0

        # Calculate drawdown - convert equity to Series first
        equity_series = pd.Series(equity, index=dates)
        peak = equity_series.expanding().max()
        drawdown = (equity_series - peak) / peak

        return {
            'equity_data': equity_data,
            'drawdown_data': drawdown,
            'returns': pd.Series(returns, index=dates),
            'total_return': total_return,
            'total_return_delta': 0.05,
            'annualized_return': annualized_return,
            'volatility': volatility,
            'sharpe_ratio': sharpe_ratio,
            'sharpe_delta': 0.1,
            'sortino_ratio': sharpe_ratio * 1.1,
            'max_drawdown': drawdown.min(),
            'drawdown_delta': 0.02,
            'calmar_ratio': annualized_return / abs(drawdown.min()) if drawdown.min() != 0 else 0,
            'win_rate': 0.58,
            'win_rate_delta': 0.03,
            'profit_factor': 1.45,
            'total_trades': 156
        }

    def _calculate_real_performance(self, symbols, start_date, end_date, strategy_name, initial_capital, asset_type="stock"):
        """
        根据真实数据计算绩效指标

        Args:
            symbols: 股票代码或加密货币ID列表
            start_date: 开始日期
            end_date: 结束日期
            strategy_name: 策略名称
            initial_capital: 初始资金
            asset_type: 资产类型（包含 i18n 翻译的文本）

        Returns:
            dict: 绩效指标字典
        """
        try:
            # 判断是否为加密货币（支持多语言）
            # 检查是否包含加密货币的关键字（英文、中文、西班牙语等）
            is_crypto = any(keyword in asset_type.lower() for keyword in ['crypto', '加密', 'cripto'])

            # 确保日期是 datetime 对象
            if hasattr(start_date, 'date'):
                # 已经是 datetime
                pass
            else:
                # 是 date 对象，转换为 datetime
                from datetime import datetime as dt
                start_date = dt.combine(start_date, dt.min.time())
                end_date = dt.combine(end_date, dt.min.time())

            # 获取真实数据
            all_data = []

            # 调试信息
            logger.info(f"use_live_data: {self.use_live_data}, live_fetcher: {self.live_fetcher is not None}")
            st.info(f"🔍 Data source: {'Live API' if self.use_live_data else 'Sample data'}")

            for symbol in symbols:
                if self.use_live_data and self.live_fetcher:
                    if is_crypto:
                        # 获取加密货币数据
                        days_diff = (end_date - start_date).days

                        # CoinGecko 免费 API 限制最多 365 天
                        if days_diff > 365:
                            days_diff = 365
                            st.warning(f"⚠️ CoinGecko 免费 API 限制为 365 天,已自动调整")

                        # 调试信息
                        logger.info(f"Fetching crypto data for {symbol}, days={days_diff}")
                        st.info(f"🔍 Fetching {symbol} data for {days_diff} days...")

                        try:
                            data = self.live_fetcher.get_crypto_history(symbol, days=days_diff)

                            logger.info(f"Received data shape: {data.shape}, empty: {data.empty}")

                            if not data.empty:
                                # 调试：显示数据列
                                logger.info(f"Crypto data columns for {symbol}: {data.columns.tolist()}")

                                # CoinGecko 返回的数据格式处理
                                if 'close' in data.columns:
                                    all_data.append(data['close'])
                                    logger.info(f"Successfully added {symbol} close data, {len(data)} points")
                                    st.success(f"✅ {symbol}: {len(data)} data points")
                                elif 'price' in data.columns:
                                    all_data.append(data['price'])
                                    logger.info(f"Successfully added {symbol} price data, {len(data)} points")
                                    st.success(f"✅ {symbol}: {len(data)} data points")
                                else:
                                    st.warning(f"⚠️ Warning: {symbol} - Data columns do not contain 'close' or 'price', columns: {data.columns.tolist()}")
                            else:
                                st.warning(f"⚠️ Warning: {symbol} - Returned data is empty")
                        except Exception as e:
                            st.error(f"❌ Error: Failed to fetch {symbol} data: {str(e)}")
                            logger.error(f"Error fetching crypto data for {symbol}: {e}")
                            import traceback
                            logger.error(traceback.format_exc())
                    else:
                        # 获取股票数据
                        days_diff = (end_date - start_date).days
                        if days_diff <= 7:
                            period = '5d'
                        elif days_diff <= 30:
                            period = '1mo'
                        elif days_diff <= 90:
                            period = '3mo'
                        elif days_diff <= 180:
                            period = '6mo'
                        elif days_diff <= 365:
                            period = '1y'
                        else:
                            period = '2y'

                        data = self.live_fetcher.get_stock_data(symbol, period=period)
                        if not data.empty:
                            # 标准化列名
                            if 'Close' in data.columns:
                                data = data.rename(columns={
                                    'Open': 'open', 'High': 'high',
                                    'Low': 'low', 'Close': 'close', 'Volume': 'volume'
                                })
                            all_data.append(data['close'])
                            logger.info(f"Successfully added {symbol} stock data, {len(data)} points")
                        else:
                            st.warning(f"⚠️ Warning: Unable to fetch data for {symbol}")
                else:
                    # 使用示例数据
                    data = self._generate_sample_market_data(symbol)
                    all_data.append(data['close'])

            if not all_data:
                logger.warning("No data available, using sample data")
                error_msg = """❌ Error: Unable to fetch any data

Please check:
1. Network connection
2. Stock/Crypto ID is correct
3. Date range is reasonable"""
                st.error(error_msg)
                return self._generate_sample_performance_data()

            # 计算等权重组合收益
            portfolio_prices = pd.concat(all_data, axis=1).mean(axis=1)
            portfolio_returns = portfolio_prices.pct_change().dropna()

            if len(portfolio_returns) == 0:
                st.error("❌ 数据不足，无法计算收益")
                return self._generate_sample_performance_data()

            # 根据策略调整收益（简化版）
            if strategy_name == "Momentum Strategy":
                # 动量策略：放大正收益
                strategy_returns = portfolio_returns * 1.2
            elif strategy_name == "Value Strategy":
                # 价值策略：稳定收益
                strategy_returns = portfolio_returns * 0.9
            elif strategy_name == "Mean Reversion":
                # 均值回归：反向操作
                strategy_returns = -portfolio_returns * 0.8
            else:
                strategy_returns = portfolio_returns

            # 计算权益曲线
            equity = initial_capital * (1 + strategy_returns).cumprod()
            equity_data = pd.DataFrame({'equity': equity})

            # 计算绩效指标
            total_return = (equity.iloc[-1] / initial_capital - 1)
            trading_days = len(strategy_returns)
            annualized_return = (1 + total_return) ** (252 / trading_days) - 1
            volatility = strategy_returns.std() * np.sqrt(252)
            sharpe_ratio = annualized_return / volatility if volatility > 0 else 0

            # 计算回撤
            peak = equity.expanding().max()
            drawdown = (equity - peak) / peak
            max_drawdown = drawdown.min()

            # 计算 Sortino 比率（只考虑下行波动）
            downside_returns = strategy_returns[strategy_returns < 0]
            downside_std = downside_returns.std() * np.sqrt(252) if len(downside_returns) > 0 else volatility
            sortino_ratio = annualized_return / downside_std if downside_std > 0 else 0

            # 计算胜率
            win_rate = (strategy_returns > 0).sum() / len(strategy_returns) if len(strategy_returns) > 0 else 0

            # 计算盈亏比
            winning_returns = strategy_returns[strategy_returns > 0]
            losing_returns = strategy_returns[strategy_returns < 0]
            avg_win = winning_returns.mean() if len(winning_returns) > 0 else 0
            avg_loss = abs(losing_returns.mean()) if len(losing_returns) > 0 else 1
            profit_factor = (avg_win * len(winning_returns)) / (avg_loss * len(losing_returns)) if avg_loss > 0 and len(losing_returns) > 0 else 0

            # Calmar 比率
            calmar_ratio = annualized_return / abs(max_drawdown) if max_drawdown != 0 else 0

            return {
                'equity_data': equity_data,
                'drawdown_data': drawdown,
                'returns': strategy_returns,
                'total_return': total_return,
                'total_return_delta': 0.0,  # 没有历史对比
                'annualized_return': annualized_return,
                'volatility': volatility,
                'sharpe_ratio': sharpe_ratio,
                'sharpe_delta': 0.0,
                'sortino_ratio': sortino_ratio,
                'max_drawdown': max_drawdown,
                'drawdown_delta': 0.0,
                'calmar_ratio': calmar_ratio,
                'win_rate': win_rate,
                'win_rate_delta': 0.0,
                'profit_factor': profit_factor,
                'total_trades': len(strategy_returns)
            }

        except Exception as e:
            logger.error(f"Error calculating real performance: {e}")
            st.error(f"❌ Error calculating performance: {e}")
            import traceback
            st.error(traceback.format_exc())
            return self._generate_sample_performance_data()
    
    def _generate_sample_backtest_results(self):
        """Generate sample backtest results"""
        return {
            'total_return': 0.25,
            'sharpe_ratio': 1.8,
            'max_drawdown': -0.12,
            'win_rate': 0.65,
            'total_trades': 89,
            'equity_curve': self._generate_sample_performance_data()['equity_data']
        }
    
    def _generate_sample_market_data(self, symbol):
        """Generate sample market data"""
        dates = pd.date_range(start='2023-01-01', end='2024-01-15', freq='D')
        np.random.seed(42)
        
        # Generate price data
        returns = np.random.normal(0.0005, 0.02, len(dates))
        prices = 100 * np.cumprod(1 + returns)
        
        # Generate volume data
        volume = np.random.lognormal(10, 0.5, len(dates))
        
        return pd.DataFrame({
            'open': prices * (1 + np.random.normal(0, 0.005, len(dates))),
            'high': prices * (1 + np.abs(np.random.normal(0, 0.01, len(dates)))),
            'low': prices * (1 - np.abs(np.random.normal(0, 0.01, len(dates)))),
            'close': prices,
            'volume': volume
        }, index=dates)
    
    def _generate_sample_factor_data(self):
        """Generate sample factor data"""
        return pd.DataFrame({
            'momentum': np.random.normal(0, 1, 100),
            'value': np.random.normal(0, 1, 100),
            'quality': np.random.normal(0, 1, 100),
            'size': np.random.normal(0, 1, 100)
        })
    
    def _calculate_rsi(self, prices, period=14):
        """Calculate RSI indicator"""
        delta = prices.diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
        rs = gain / loss
        rsi = 100 - (100 / (1 + rs))
        return rsi
    
    def _display_backtest_results(self, results, i18n):
        """Display backtest results"""
        st.success(i18n.t('backtest_completed'))

        # Results summary
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric(i18n.t('total_return'), f"{results['total_return']:.2%}")

        with col2:
            st.metric(i18n.t('sharpe_ratio'), f"{results['sharpe_ratio']:.2f}")

        with col3:
            st.metric(i18n.t('max_drawdown'), f"{results['max_drawdown']:.2%}")

        with col4:
            st.metric(i18n.t('win_rate'), f"{results['win_rate']:.1%}")

        # Equity curve
        st.subheader(i18n.t('backtest_results'))
        equity_fig = self.chart_generator.create_equity_curve(results['equity_curve'])
        st.plotly_chart(equity_fig, use_container_width=True, key='backtest_equity_curve')

def main():
    """Main function to run the dashboard"""
    try:
        dashboard = TradingDashboard()
        dashboard.run()
    except Exception as e:
        st.error(f"Error running dashboard: {e}")
        logger.exception("Dashboard error")

if __name__ == "__main__":
    main() 