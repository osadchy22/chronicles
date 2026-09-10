const TelegramApp = {
    init() {
        if (!window.Telegram || !window.Telegram.WebApp) {
            console.warn("Telegram WebApp SDK is not available");
            return null;
        }

        const tg = window.Telegram.WebApp;

        tg.ready();
        tg.expand();

        return tg;
    },

    getInitData() {
        if (!window.Telegram || !window.Telegram.WebApp) {
            return null;
        }

        return window.Telegram.WebApp.initData;
    },

    getUserUnsafe() {
        if (!window.Telegram || !window.Telegram.WebApp) {
            return null;
        }

        return window.Telegram.WebApp.initDataUnsafe?.user || null;
    }
};

window.TelegramApp = TelegramApp;