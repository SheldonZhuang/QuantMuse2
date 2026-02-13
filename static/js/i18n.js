// 多语言支持模块
const translations = {
    en: {
        // Navigation
        'nav.dashboard': 'Dashboard',
        'nav.strategies': 'Strategies',
        'nav.portfolio': 'Portfolio',
        'nav.charts': 'Charts',
        'nav.analysis': 'Analysis',
        'nav.admin': 'Admin',
        'nav.settings': 'Settings',
        'nav.logout': 'Logout',

        // Dashboard
        'dashboard.title': 'Trading System Dashboard',
        'dashboard.system_status': 'System Status',
        'dashboard.active_strategies': 'Active Strategies',
        'dashboard.total_trades': 'Total Trades',
        'dashboard.total_return': 'Total Return',
        'dashboard.sharpe_ratio': 'Sharpe Ratio',
        'dashboard.market_overview': 'Market Overview',
        'dashboard.recent_trades': 'Recent Trades',
        'dashboard.performance': 'Performance',

        // Real-time Data
        'realtime.stock_data': 'Stock Data',
        'realtime.crypto_data': 'Cryptocurrency Data',
        'realtime.price': 'Price',
        'realtime.change': 'Change',
        'realtime.volume': 'Volume',
        'realtime.market_cap': 'Market Cap',
        'realtime.refresh': 'Refresh Data',
        'realtime.last_updated': 'Last Updated',

        // Strategies
        'strategy.name': 'Strategy Name',
        'strategy.status': 'Status',
        'strategy.return': 'Return',
        'strategy.risk': 'Risk',
        'strategy.actions': 'Actions',
        'strategy.start': 'Start',
        'strategy.stop': 'Stop',
        'strategy.edit': 'Edit',

        // Common
        'common.loading': 'Loading...',
        'common.error': 'Error',
        'common.success': 'Success',
        'common.save': 'Save',
        'common.cancel': 'Cancel',
        'common.delete': 'Delete',
        'common.confirm': 'Confirm',
    },
    zh: {
        // Navigation
        'nav.dashboard': '仪表板',
        'nav.strategies': '策略',
        'nav.portfolio': '投资组合',
        'nav.charts': '图表',
        'nav.analysis': '分析',
        'nav.admin': '管理员',
        'nav.settings': '设置',
        'nav.logout': '登出',

        // Dashboard
        'dashboard.title': '交易系统仪表板',
        'dashboard.system_status': '系统状态',
        'dashboard.active_strategies': '活跃策略',
        'dashboard.total_trades': '总交易数',
        'dashboard.total_return': '总收益',
        'dashboard.sharpe_ratio': '夏普比率',
        'dashboard.market_overview': '市场概览',
        'dashboard.recent_trades': '最近交易',
        'dashboard.performance': '业绩表现',

        // Real-time Data
        'realtime.stock_data': '股票数据',
        'realtime.crypto_data': '加密货币数据',
        'realtime.price': '价格',
        'realtime.change': '涨跌幅',
        'realtime.volume': '成交量',
        'realtime.market_cap': '市值',
        'realtime.refresh': '刷新数据',
        'realtime.last_updated': '最后更新',

        // Strategies
        'strategy.name': '策略名称',
        'strategy.status': '状态',
        'strategy.return': '收益',
        'strategy.risk': '风险',
        'strategy.actions': '操作',
        'strategy.start': '启动',
        'strategy.stop': '停止',
        'strategy.edit': '编辑',

        // Common
        'common.loading': '加载中...',
        'common.error': '错误',
        'common.success': '成功',
        'common.save': '保存',
        'common.cancel': '取消',
        'common.delete': '删除',
        'common.confirm': '确认',
    },
    es: {
        // Navigation
        'nav.dashboard': 'Panel',
        'nav.strategies': 'Estrategias',
        'nav.portfolio': 'Cartera',
        'nav.charts': 'Gráficos',
        'nav.analysis': 'Análisis',
        'nav.admin': 'Admin',
        'nav.settings': 'Configuración',
        'nav.logout': 'Cerrar sesión',

        // Dashboard
        'dashboard.title': 'Panel de Trading',
        'dashboard.system_status': 'Estado del Sistema',
        'dashboard.active_strategies': 'Estrategias Activas',
        'dashboard.total_trades': 'Total de Operaciones',
        'dashboard.total_return': 'Retorno Total',
        'dashboard.sharpe_ratio': 'Ratio de Sharpe',
        'dashboard.market_overview': 'Resumen del Mercado',
        'dashboard.recent_trades': 'Operaciones Recientes',
        'dashboard.performance': 'Rendimiento',

        // Real-time Data
        'realtime.stock_data': 'Datos de Acciones',
        'realtime.crypto_data': 'Datos de Criptomonedas',
        'realtime.price': 'Precio',
        'realtime.change': 'Cambio',
        'realtime.volume': 'Volumen',
        'realtime.market_cap': 'Capitalización',
        'realtime.refresh': 'Actualizar Datos',
        'realtime.last_updated': 'Última Actualización',

        // Strategies
        'strategy.name': 'Nombre de Estrategia',
        'strategy.status': 'Estado',
        'strategy.return': 'Retorno',
        'strategy.risk': 'Riesgo',
        'strategy.actions': 'Acciones',
        'strategy.start': 'Iniciar',
        'strategy.stop': 'Detener',
        'strategy.edit': 'Editar',

        // Common
        'common.loading': 'Cargando...',
        'common.error': 'Error',
        'common.success': 'Éxito',
        'common.save': 'Guardar',
        'common.cancel': 'Cancelar',
        'common.delete': 'Eliminar',
        'common.confirm': 'Confirmar',
    },
    fr: {
        // Navigation
        'nav.dashboard': 'Tableau de bord',
        'nav.strategies': 'Stratégies',
        'nav.portfolio': 'Portefeuille',
        'nav.charts': 'Graphiques',
        'nav.analysis': 'Analyse',
        'nav.admin': 'Admin',
        'nav.settings': 'Paramètres',
        'nav.logout': 'Déconnexion',

        // Dashboard
        'dashboard.title': 'Tableau de bord de trading',
        'dashboard.system_status': 'État du système',
        'dashboard.active_strategies': 'Stratégies actives',
        'dashboard.total_trades': 'Total des transactions',
        'dashboard.total_return': 'Rendement total',
        'dashboard.sharpe_ratio': 'Ratio de Sharpe',
        'dashboard.market_overview': 'Aperçu du marché',
        'dashboard.recent_trades': 'Transactions récentes',
        'dashboard.performance': 'Performance',

        // Real-time Data
        'realtime.stock_data': 'Données boursières',
        'realtime.crypto_data': 'Données crypto',
        'realtime.price': 'Prix',
        'realtime.change': 'Changement',
        'realtime.volume': 'Volume',
        'realtime.market_cap': 'Capitalisation',
        'realtime.refresh': 'Actualiser',
        'realtime.last_updated': 'Dernière mise à jour',

        // Strategies
        'strategy.name': 'Nom de la stratégie',
        'strategy.status': 'Statut',
        'strategy.return': 'Rendement',
        'strategy.risk': 'Risque',
        'strategy.actions': 'Actions',
        'strategy.start': 'Démarrer',
        'strategy.stop': 'Arrêter',
        'strategy.edit': 'Modifier',

        // Common
        'common.loading': 'Chargement...',
        'common.error': 'Erreur',
        'common.success': 'Succès',
        'common.save': 'Enregistrer',
        'common.cancel': 'Annuler',
        'common.delete': 'Supprimer',
        'common.confirm': 'Confirmer',
    }
};

// 语言管理类
class I18n {
    constructor() {
        this.currentLanguage = localStorage.getItem('language') || 'en';
        this.translations = translations;
    }

    // 获取翻译文本
    t(key) {
        const keys = key.split('.');
        let value = this.translations[this.currentLanguage];

        for (const k of keys) {
            if (value && typeof value === 'object') {
                value = value[k];
            } else {
                return key; // 如果找不到翻译，返回键名
            }
        }

        return value || key;
    }

    // 切换语言
    setLanguage(lang) {
        if (this.translations[lang]) {
            this.currentLanguage = lang;
            localStorage.setItem('language', lang);
            this.updatePageLanguage();
            return true;
        }
        return false;
    }

    // 获取当前语言
    getCurrentLanguage() {
        return this.currentLanguage;
    }

    // 更新页面所有翻译文本
    updatePageLanguage() {
        // 更新所有带有 data-i18n 属性的元素
        document.querySelectorAll('[data-i18n]').forEach(element => {
            const key = element.getAttribute('data-i18n');
            element.textContent = this.t(key);
        });

        // 更新所有带有 data-i18n-placeholder 属性的输入框
        document.querySelectorAll('[data-i18n-placeholder]').forEach(element => {
            const key = element.getAttribute('data-i18n-placeholder');
            element.placeholder = this.t(key);
        });

        // 更新当前语言显示
        const languageNames = {
            'en': 'English',
            'zh': '中文',
            'es': 'Español',
            'fr': 'Français'
        };
        const currentLangElement = document.getElementById('current-language');
        if (currentLangElement) {
            currentLangElement.textContent = languageNames[this.currentLanguage];
        }

        // 触发语言切换事件
        document.dispatchEvent(new CustomEvent('languageChanged', {
            detail: { language: this.currentLanguage }
        }));
    }

    // 初始化语言切换器
    initLanguageSwitcher() {
        // 设置初始语言
        this.updatePageLanguage();

        // 绑定语言切换按钮
        document.querySelectorAll('.language-option').forEach(option => {
            option.addEventListener('click', (e) => {
                e.preventDefault();
                const lang = e.currentTarget.getAttribute('data-lang');
                this.setLanguage(lang);
            });
        });
    }
}

// 创建全局 i18n 实例
const i18n = new I18n();

// 页面加载完成后初始化
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => {
        i18n.initLanguageSwitcher();
    });
} else {
    i18n.initLanguageSwitcher();
}
