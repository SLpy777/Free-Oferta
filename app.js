const tg = window.Telegram.WebApp;

// Сообщаем Telegram, что мини-апп готов
tg.ready();

// Кнопки
const buyBtn = document.getElementById("buyBtn");
const myVpsBtn = document.getElementById("myVpsBtn");
const helpBtn = document.getElementById("helpBtn");

// Купить VPN
buyBtn.addEventListener("click", () => {
  tg.showAlert("Переход к покупке VPN");
});

// Мои VPS
myVpsBtn.addEventListener("click", () => {
  tg.showAlert("Открываем ваши VPS");
});

// Помощь
helpBtn.addEventListener("click", () => {
  tg.showAlert("Связь с поддержкой");
});