// Проверка, что MiniApp открывается через Telegram WebApp
if (!window.Telegram || !window.Telegram.WebApp) {
    document.body.innerHTML = "<h2>Доступ запрещён</h2>";
} else {
    const tg = window.Telegram.WebApp;
    tg.expand(); // Раскрываем окно WebApp полностью
}

function getVPS(name) {
    const resultDiv = document.getElementById("result");

    // Выдаём ссылку на конфигурацию из папки configs
    resultDiv.innerHTML = `
        <p>Вы выбрали <b>${name}</b>.</p>
        <p><a href="configs/${name}.ovpn" target="_blank">Скачать конфигурацию</a></p>
    `;
}