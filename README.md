<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>ZZ Task Bot</title>
    <script src="https://telegram.org/js/telegram-web-app.js"></script>
    <style>
        body {
            background-color: #0d0f12;
            color: #ffffff;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            margin: 0;
            padding: 0;
            user-select: none;
        }
        .container {
            padding: 15px;
            padding-bottom: 90px;
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
        
        /* Фильтры типов заданий */
        .type-filter {
            display: flex;
            gap: 10px;
            margin-bottom: 15px;
        }
        .filter-btn {
            flex: 1;
            background-color: #1e2530;
            color: #8892b0;
            border: 1px solid #2c3545;
            padding: 8px;
            border-radius: 6px;
            cursor: pointer;
            font-size: 12px;
        }
        .filter-btn.active {
            background-color: #0088cc;
            color: #fff;
            border-color: #0088cc;
        }

        /* Список заданий */
        .task-item {
            background: #131822;
            border: 1px solid #2c3545;
            border-radius: 10px;
            padding: 12px;
            margin-bottom: 10px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        
        /* Навигация */
        .nav-bar {
            position: fixed;
            bottom: 0; left: 0; right: 0;
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
            cursor: pointer;
            flex: 1;
        }
        .nav-item.active { color: #00ffff; }
        .nav-item-icon { font-size: 20px; margin-bottom: 2px; }
        
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
        .btn-sm { width: auto; margin: 0; padding: 6px 12px; font-size: 12px; }
        .btn-danger { background-color: #ef4444 !important; }
        
        .input-field, select {
            width: 100%;
            padding: 10px;
            background-color: #1e2530;
            border: 1px solid #2c3545;
            border-radius: 6px;
            color: white;
            margin-top: 5px;
            margin-bottom: 10px;
            box-sizing: border-box;
        }
    </style>
</head>
<body>

<div class="container">
    <div class="header">
        <div>ID: <span id="user-id">Loading...</span></div>
        <div style="cursor: pointer; font-size: 20px;" onclick="openPromo()">🎁</div>
    </div>

    <div class="balance-card">
        <div>Заработано:</div>
        <div class="balance-val" id="bal-zz">0 Coin ZZ</div>
        <div style="margin-top: 10px; color: #8892b0; font-size: 13px;">Для рекламы: <span id="bal-ton" style="color:#00ff88">0.00 TON</span></div>
    </div>

    <div id="page-tasks" class="page active">
        <h3>📋 Лента заданий</h3>
        <div class="type-filter">
            <button class="filter-btn active" onclick="filterTasks('channel', this)">Каналы</button>
            <button class="filter-btn" onclick="filterTasks('chat', this)">Чаты</button>
            <button class="filter-btn" onclick="filterTasks('bot', this)">Боты</button>
        </div>
        <div id="tasks-list">
            </div>
    </div>

    <div id="page-create" class="page">
        <h3>📣 Создать задание</h3>
        
        <label>Тип продвижения:</label>
        <select id="new-task-type">
            <option value="channel">📢 Telegram Канал</option>
            <option value="chat">💬 Telegram Чат</option>
            <option value="bot">🤖 Telegram Бот</option>
        </select>

        <label>Ссылка на ресурс:</label>
        <input type="text" id="new-task-link" class="input-field" placeholder="https://t.me/...">
        
        <label>Количество выполнений (мин. 500):</label>
        <input type="number" id="task-amount" class="input-field" value="500" min="500" oninput="calcCost()">
        
        <div style="margin-top: 5px; background: #131822; padding: 10px; border-radius: 6px;">
            Стоимость: <span id="task-cost" style="color: #00ff88; font-weight: bold;">0.50 TON</span>
        </div>
        <button class="btn" style="background-color: #00ff88; color: #0d0f12;" onclick="submitTask()">Оплатить и отправить на модерацию</button>
    </div>

    <div id="page-refs" class="page">
        <h3>👥 Партнерская программа</h3>
        <p>Ваша ссылка для приглашений (+5 000 ZZ за друга):</p>
        <input type="text" id="ref-link" class="input-field" readonly>
        <button class="btn" onclick="copyRef()">Копировать ссылку</button>
    </div>

    <div id="page-exchange" class="page">
        <h3>📈 Обменник Coin ZZ</h3>
        <p>Цена растет от активности игроков! <br>Текущий курс: <b>1 000 000 ZZ = 1 TON</b></p>
        <button class="btn" onclick="buyCoins()">Купить 1 000 000 ZZ (1 TON)</button>
        <button class="btn btn-danger" onclick="sellCoins()">Продать свои ZZ в TON</button>
    </div>

    <div id="page-admin" class="page">
        <h3 style="color: #ff3366;">👑 Панель Управления</h3>
        
        <div style="border: 1px solid #ff3366; padding: 10px; border-radius: 8px; margin-bottom: 15px;">
            <h4>📝 Удаление / Модерация активных заданий</h4>
            <div id="admin-tasks-list">
                </div>
        </div>
    </div>
</div>

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
    <div class="nav-item" id="nav-admin" style="display:none;" onclick="switchPage('admin', this)">
        <div class="nav-item-icon">👑</div><div>Админ</div>
    </div>
</div>

<script>
    const tg = window.Telegram.WebApp;
    tg.expand();

    const userId = tg.initDataUnsafe?.user?.id || 8684827145; // Твой ID по дефолту
    document.getElementById('user-id').innerText = userId;
    document.getElementById('ref-link').value = "https://t.me/YOUR_BOT_USERNAME?start=" + userId;

    const ADMIN_ID = 8684827145;
    if (Number(userId) === ADMIN_ID) {
        document.getElementById('nav-admin').style.display = 'block';
    }

    // Имитация базы данных в оперативной памяти Web App (для демонстрации кликов)
    let userBalanceZZ = 25000;
    let userBalanceTON = 5.00;
    
    // Временный список заданий (канал, чат, бот)
    let globalTasks = [
        { id: 1, type: "channel", name: "Канал Про Крипту", link: "https://t.me/crypto", prize: 1000 },
        { id: 2, type: "chat", name: "Чат Общения ZZ", link: "https://t.me/chat", prize: 1000 },
        { id: 3, type: "bot", name: "Игровой Бот X", link: "https://t.me/bot", prize: 1000 }
    ];

    let currentFilter = "channel";

    function updateUI() {
        document.getElementById('bal-zz').innerText = userBalanceZZ.toLocaleString() + ' Coin ZZ';
        document.getElementById('bal-ton').innerText = userBalanceTON.toFixed(2) + ' TON';
        renderTasks();
        renderAdminTasks();
    }

    function switchPage(pageId, element) {
        document.querySelectorAll('.page').forEach(p => p.classList.remove('active'));
        document.querySelectorAll('.nav-item').forEach(i => i.classList.remove('active'));
        document.getElementById('page-' + pageId).classList.add('active');
        element.classList.add('active');
    }

    function filterTasks(type, element) {
        document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
        element.classList.add('active');
        currentFilter = type;
        renderTasks();
    }

    // Отображение списка заданий для пользователей
    function renderTasks() {
        const container = document.getElementById('tasks-list');
        container.innerHTML = "";
        const filtered = globalTasks.filter(t => t.type === currentFilter);
        
        if(filtered.length === 0) {
            container.innerHTML = "<p style='color:#8892b0; text-align:center;'>Нет активных заданий в этой категории</p>";
            return;
        }

        filtered.forEach(t => {
            container.innerHTML += `
                <div class="task-item">
                    <div><b>${t.name}</b><br><small style="color: #00ff88;">+${t.prize} ZZ</small></div>
                    <button class="btn btn-sm" onclick="doTask('${t.link}', ${t.id})">Выполнить</button>
                </div>
            `;
        });
    }

    // Отображение списка заданий в админке с возможностью удаления
    function renderAdminTasks() {
        const container = document.getElementById('admin-tasks-list');
        container.innerHTML = "";
        
        if(globalTasks.length === 0) {
            container.innerHTML = "<p>Активных заданий нет</p>";
            return;
        }

        globalTasks.forEach(t => {
            container.innerHTML += `
                <div class="task-item" style="border-color: #ff3366;">
                    <div>[${t.type.toUpperCase()}] ${t.name}</div>
                    <button class="btn btn-sm btn-danger" onclick="deleteTask(${t.id})">Удалить ❌</button>
                </div>
            `;
        });
    }

    // Функция выполнения задания кнопкой
    function doTask(link, id) {
        tg.openTelegramLink(link); // Открывает канал/чат/бот прямо в ТГ
        setTimeout(() => {
            userBalanceZZ += 1000;
            alert("Успешно проверено! +1 000 Coin ZZ начислено.");
            updateUI();
        }, 2000);
    }

    // Функция создания задания пользователем
    function submitTask() {
        const type = document.getElementById('new-task-type').value;
        const link = document.getElementById('new-task-link').value;
        const amount = parseInt(document.getElementById('task-amount').value);
        const cost = amount / 1000;

        if(!link.includes("t.me/")) {
            alert("Введите правильную ссылку на Telegram!");
            return;
        }
        if(userBalanceTON < cost) {
            alert("Недостаточно TON на балансе рекламы!");
            return;
        }

        userBalanceTON -= cost;
        // Добавляем в список
        const newId = globalTasks.length + 1;
        globalTasks.push({ id: newId, type: type, name: "Реклама: " + link.split('/').pop(), link: link, prize: 1000 });
        
        alert("Задание успешно оплачено и отправлено!");
        document.getElementById('new-task-link').value = "";
        updateUI();
    }

    // АДМИН: Удаление задания
    function deleteTask(id) {
        globalTasks = globalTasks.filter(t => t.id !== id);
        alert("Задание полностью удалено из бота!");
        updateUI();
    }

    function calcCost() {
        const amount = document.getElementById('task-amount').value;
        document.getElementById('task-cost').innerText = (amount / 1000).toFixed(2) + ' TON';
    }

    function openPromo() {
        let code = prompt("Введите 4-значный промокод:");
        if (code === "7777") {
            userBalanceZZ += 50000;
            alert("Промокод активирован! +50,000 Coin ZZ");
            updateUI();
        } else if (code) {
            alert("Неверный код или лимит исчерпан.");
        }
    }

    function copyRef() {
        navigator.clipboard.writeText(document.getElementById('ref-link').value);
        alert("Реферальная ссылка скопирована!");
    }

    function buyCoins() {
        if(userBalanceTON >= 1) {
            userBalanceTON -= 1;
            userBalanceZZ += 1000000;
            updateUI();
            alert("Куплено 1 000 000 Coin ZZ!");
        } else { alert("Не нужно баланса в TON!"); }
    }

    function sellCoins() {
        if(userBalanceZZ >= 1000000) {
            userBalanceZZ -= 1000000;
            userBalanceTON += 1;
            updateUI();
            alert("1 000 000 ZZ успешно обменяны на 1 TON!");
        } else { alert("Минимум для обмена — 1 000 000 ZZ!"); }
    }

    // Старт
    updateUI();
</script>
</body>
</html>
