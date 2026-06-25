<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>ZZ Task Bot</title>
    <!-- Подключаем официальный скрипт Telegram WebApp -->
    <script src="https://telegram.org/js/telegram-web-app.js"></script>
    <style>
        body {
            background-color: #0d0f12;
            color: #ffffff;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            margin: 0;
            padding: 0;
            user-select: none;
        }
        .container {
            padding: 15px;
            padding-bottom: 80px;
        }
        .header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid #1f232b;
            padding-bottom: 10px;
            margin-bottom: 15px;
        }
        .balance-card {
            background: linear-gradient(135deg, #1e2530 0%, #131822 100%);
            border: 1px solid #2c3545;
            border-radius: 12px;
            padding: 15px;
            margin-bottom: 15px;
            text-align: center;
        }
        .balance-val {
            font-size: 24px;
            font-weight: bold;
            color: #00ffff;
            text-shadow: 0 0 10px rgba(0,255,255,0.3);
        }
        .page { display: none; }
        .page.active { display: block; }
        
        /* Нижнее меню */
        .nav-bar {
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            height: 65px;
            background-color: #131822;
            border-top: 1px solid #2c3545;
            display: flex;
            justify-content: space-around;
            align-items: center;
            z-index: 1000;
        }
        .nav-item {
            color: #8892b0;
            font-size: 11px;
            text-align: center;
            text-decoration: none;
            cursor: pointer;
            flex: 1;
        }
        .nav-item.active {
            color: #00ffff;
        }
        .nav-item-icon {
            font-size: 20px;
            margin-bottom: 2px;
        }
        
        /* Кнопки и формы */
        .btn {
            background-color: #0088cc;
            color: white;
            border: none;
            padding: 12px;
            border-radius: 8px;
            width: 100%;
            font-weight: bold;
            font-size: 14px;
            margin-top: 10px;
            cursor: pointer;
        }
        .input-field {
            width: 100%;
            padding: 10px;
            background-color: #1e2530;
            border: 1px solid #2c3545;
            border-radius: 6px;
            color: white;
            margin-top: 5px;
            box-sizing: border-box;
        }
        
        /* Свечи для курса */
        .candles-mock {
            height: 150px;
            border-left: 2px solid #334155;
            border-bottom: 2px solid #334155;
            margin: 20px 0;
            display: flex;
            align-items: flex-end;
            justify-content: space-around;
            padding-top: 20px;
        }
        .candle { width: 15px; background-color: #10b981; border-radius: 2px; }
        .candle.red { background-color: #ef4444; }
    </style>
</head>
<body>

<div class="container">
    <!-- Шапка профиля -->
    <div class="header">
        <div>ID: <span id="user-id">Loading...</span></div>
        <div style="cursor: pointer; font-size: 20px;" onclick="openPromo()">🎁</div>
    </div>

    <!-- БАЛАНСЫ -->
    <div class="balance-card">
        <div>Заработано:</div>
        <div class="balance-val" id="bal-zz">0 Coin ZZ</div>
        <div style="margin-top: 10px; color: #8892b0; font-size: 13px;">Для рекламы: <span id="bal-ton" style="color:#00ff88">0.00 TON</span></div>
    </div>

    <!-- 1. РАЗДЕЛ ЗАДАНИЯ -->
    <div id="page-tasks" class="page active">
        <h3>📋 Доступные задания</h3>
        <p style="color: #8892b0; font-size: 13px;">Подпишись на канал и получи 1 000 Coin ZZ</p>
        <div id="tasks-list">
            <!-- Сюда будут прилетать задания -->
            <div class="balance-card" style="text-align: left; display: flex; justify-content: space-between; align-items: center;">
                <div>🗣 Спонсорский канал<br><small style="color: #8892b0;">+1 000 Coin ZZ</small></div>
                <button class="btn" style="width: auto; margin: 0; padding: 6px 12px;">Выполнить</button>
            </div>
        </div>
    </div>

    <!-- 2. РАЗДЕЛ СОЗДАТЬ ЗАДАНИЕ -->
    <div id="page-create" class="page">
        <h3>📣 Создать задание</h3>
        <label>Ссылка на Telegram канал:</label>
        <input type="text" class="input-field" placeholder="https://t.me/your_channel">
        
        <label style="margin-top: 10px; display: block;">Количество подписок (мин. 500):</label>
        <input type="number" id="task-amount" class="input-field" value="500" min="500" oninput="calcCost()">
        
        <div style="margin-top: 15px; background: #131822; padding: 10px; border-radius: 6px;">
            Итого к оплате: <span id="task-cost" style="color: #00ff88; font-weight: bold;">0.50 TON</span>
        </div>
        <button class="btn" style="background-color: #00ff88; color: #0d0f12;">Оплатить TON и отправить</button>
    </div>

    <!-- 3. РАЗДЕЛ РЕФЕРАЛЫ -->
    <div id="page-refs" class="page">
        <h3>👥 Реферальная ссылка</h3>
        <p>Приглашай друзей и получай бонусы за каждого!</p>
        <input type="text" id="ref-link" class="input-field" readonly value="https://t.me/bot?start=id">
        <button class="btn" onclick="copyRef()">Копировать ссылку</button>
    </div>

    <!-- 4. РАЗДЕЛ КУРС ZZ -->
    <div id="page-exchange" class="page">
        <h3>📈 Биржа Coin ZZ</h3>
        <div>Текущий курс: <span style="color: #00ffff; font-weight: bold;">1 000 000 ZZ = 1 TON</span></div>
        
        <!-- Свечи -->
        <div class="candles-mock">
            <div class="candle" style="height: 40px;"></div>
            <div class="candle" style="height: 60px;"></div>
            <div class="candle red" style="height: 35px;"></div>
            <div class="candle" style="height: 80px;"></div>
            <div class="candle" style="height: 110px;"></div>
        </div>

        <button class="btn" style="margin-bottom: 8px;">Купить ZZ (Мин. 1 млн)</button>
        <button class="btn" style="background-color: #ef4444;">Продать ZZ на TON</button>
    </div>

    <!-- 5. РАЗДЕЛ АДМИНКА (Видит только админ) -->
    <div id="page-admin" class="page">
        <h3 style="color: #ff3366;">👑 Админ-панель</h3>
        
        <div style="border: 1px solid #ff3366; padding: 10px; border-radius: 8px; margin-bottom: 15px;">
            <h4>⚙️ Управление по Telegram ID</h4>
            <input type="text" class="input-field" placeholder="Введи ID игрока">
            <button class="btn" style="background: #ff3366;">Изменить баланс / Бан</button>
        </div>

        <div style="border: 1px solid #ff3366; padding: 10px; border-radius: 8px;">
            <h4>🎁 Создать промокод</h4>
            <input type="text" class="input-field" placeholder="Код (например, 5555)">
            <input type="number" class="input-field" placeholder="Кол-во активаций" style="margin-top: 5px;">
            <button class="btn" style="background: #ff3366;">Сохранить промокод</button>
        </div>
    </div>
</div>

<!-- НИЖНЕЕ МЕНЮ -->
<div class="nav-bar">
    <div class="nav-item active" onclick="switchPage('tasks', this)">
        <div class="nav-item-icon">📋</div><div>Задания</div>
    </div>
    <div class="nav-item" onclick="switchPage('create', this)">
        <div class="nav-item-icon">📣</div><div>Реклама</div>
    </div>
    <div class="nav-item" onclick="switchPage('refs', this)">
        <div class="nav-item-icon">👥</div><div>Рефералы</div>
    </div>
    <div class="nav-item" onclick="switchPage('exchange', this)">
        <div class="nav-item-icon">📈</div><div>Курс ZZ</div>
    </div>
    <!-- Эта вкладка включится только для твоего ID через JS -->
    <div class="nav-item" id="nav-admin" style="display:none;" onclick="switchPage('admin', this)">
        <div class="nav-item-icon">👑</div><div>Админ</div>
    </div>
</div>

<script>
    // Инициализация Telegram WebApp API
    const tg = window.Telegram.WebApp;
    tg.expand(); // Расширяем на весь экран телефона

    // Получаем реальный ID пользователя из телеграма
    const userId = tg.initDataUnsafe?.user?.id || "Сканер ID";
    document.getElementById('user-id').innerText = userId;

    // ТВОЙ ID ДЛЯ ОТКРЫТИЯ АДМИНКИ
    const ADMIN_ID = 8684827145;
    if (Number(userId) === ADMIN_ID) {
        document.getElementById('nav-admin').style.display = 'block';
    }

    // Переключение вкладок
    function switchPage(pageId, element) {
        document.querySelectorAll('.page').forEach(p => p.classList.remove('active'));
        document.querySelectorAll('.nav-item').forEach(i => i.classList.remove('active'));
        
        document.getElementById('page-' + pageId).classList.add('active');
        element.classList.add('active');
    }

    // Динамический расчет стоимости рекламы (1000 выполнений = 1 TON)
    function calcCost() {
        const amount = document.getElementById('task-amount').value;
        const cost = amount / 1000;
        document.getElementById('task-cost').innerText = cost.toFixed(2) + ' TON';
    }

    // Ввод промокода через подарок
    function openPromo() {
        let code = prompt("Введите 4-значный промокод:");
        if (code) {
            tg.sendData(JSON.stringify({action: "use_promo", code: code}));
            alert("Код отправлен на проверку!");
        }
    }

    function copyRef() {
        alert("Ссылка скопирована!");
    }
</script>
</body>
</html>
