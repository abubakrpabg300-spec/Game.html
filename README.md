<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>ZZ Task Bot</title>
    <script src="https://telegram.org/js/telegram-web-app.js"></script>
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body {
            background-color: #0d0f12;
            color: #ffffff;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            user-select: none;
            overflow-x: hidden;
            font-size: 14px;
        }
        .container { padding: 15px; padding-bottom: 90px; }
        .header {
            display: flex; justify-content: space-between; align-items: center;
            border-bottom: 1px solid #1f232b; padding-bottom: 10px; margin-bottom: 15px;
        }
        .balance-card {
            background: linear-gradient(135deg, #1e2530 0%, #131822 100%);
            border: 1px solid #2c3545; border-radius: 12px; padding: 15px;
            margin-bottom: 15px; text-align: center;
        }
        .balance-val { font-size: 24px; font-weight: bold; color: #00ffff; text-shadow: 0 0 10px rgba(0,255,255,0.3); }
        .page { display: none; }
        .page.active { display: block; }

        .sub-tabs { display: flex; gap: 6px; margin-bottom: 15px; }
        .sub-tab {
            flex: 1; padding: 10px 5px; text-align: center; background: #1e2530;
            border: 1px solid #2c3545; border-radius: 8px; cursor: pointer;
            font-weight: bold; font-size: 12px; color: #8892b0;
        }
        .sub-tab.active { background: #00ffff; color: #0d0f12; border-color: #00ffff; }
        .sub-page { display: none; }
        .sub-page.active { display: block; }

        .nav-bar {
            position: fixed; bottom: 0; left: 0; right: 0; height: 75px;
            background-color: #131822; border-top: 1px solid #2c3545;
            display: flex; justify-content: space-around; align-items: center; z-index: 1000;
        }
        .nav-item { color: #8892b0; font-size: 10px; text-align: center; cursor: pointer; flex: 1; }
        .nav-item.active { color: #00ffff; }
        .nav-item-icon { font-size: 20px; margin-bottom: 3px; }

        .btn {
            background-color: #0088cc; color: white; border: none;
            padding: 12px; border-radius: 8px; width: 100%; font-weight: bold;
            font-size: 14px; margin-top: 10px; cursor: pointer;
        }
        .btn.green { background-color: #00ff88; color: #0d0f12; }
        .btn.red { background-color: #ef4444; }
        .btn.purple { background-color: #a855f7; }
        .btn.gold { background-color: #f59e0b; color: #000; }
        .btn:active { opacity: 0.8; }

        .input-field {
            width: 100%; padding: 10px; background-color: #1e2530;
            border: 1px solid #2c3545; border-radius: 6px; color: white;
            margin-top: 5px; font-size: 14px;
        }
        select.input-field { appearance: none; }

        .task-card {
            background: #131822; border: 1px solid #2c3545; border-radius: 10px;
            padding: 12px; margin-bottom: 10px; display: flex;
            justify-content: space-between; align-items: center;
        }
        .task-info small { color: #8892b0; }
        .task-reward { color: #00ffff; font-weight: bold; }

        .candles-mock {
            height: 120px; border-left: 2px solid #334155; border-bottom: 2px solid #334155;
            margin: 15px 0; display: flex; align-items: flex-end; justify-content: space-around;
            padding: 10px 5px;
        }
        .candle { width: 12px; background-color: #10b981; border-radius: 2px; }
        .candle.red { background-color: #ef4444; }

        .status-badge {
            display: inline-block; padding: 3px 8px; border-radius: 4px; font-size: 11px;
            font-weight: bold;
        }
        .status-pending { background: #f59e0b; color: #000; }
        .status-approved { background: #10b981; color: #fff; }
        .status-rejected { background: #ef4444; color: #fff; }

        label { display: block; margin-top: 10px; font-size: 13px; color: #8892b0; }

        .wallet-address {
            background: #131822; border: 1px dashed #00ffff; border-radius: 8px;
            padding: 10px; word-break: break-all; font-size: 12px; color: #00ffff;
            text-align: center; margin: 10px 0;
        }

        .copy-btn {
            background: #00ffff; color: #000; border: none; padding: 6px 14px;
            border-radius: 6px; font-weight: bold; cursor: pointer; font-size: 12px;
        }
    </style>
</head>
<body>

<div class="container">
    <!-- Шапка -->
    <div class="header">
        <div>🆔 ID: <span id="user-id">...</span></div>
        <div style="cursor: pointer; font-size: 22px;" onclick="openPromo()">🎁</div>
    </div>

    <!-- Баланс -->
    <div class="balance-card">
        <div>💰 Баланс</div>
        <div class="balance-val"><span id="bal-zz">0</span> Coin ZZ</div>
        <div style="margin-top: 6px; font-size: 13px; color: #00ff88;">💎 <span id="bal-ton">0.00</span> TON</div>
    </div>

    <!-- ===== 1. ЗАДАНИЯ ===== -->
    <div id="page-tasks" class="page active">
        <div class="sub-tabs">
            <div class="sub-tab active" onclick="switchSubTab('channels', this)">📢 Каналы</div>
            <div class="sub-tab" onclick="switchSubTab('chats', this)">💬 Чаты</div>
            <div class="sub-tab" onclick="switchSubTab('bots', this)">🤖 Боты</div>
        </div>

        <div id="sub-channels" class="sub-page active">
            <p style="color:#8892b0; font-size:13px; margin-bottom:10px;">Подпишись на канал — получи 1 000 Coin ZZ</p>
            <div id="tasks-channels">
                <div class="task-card">
                    <div class="task-info"><strong>📢 Telegram Канал 1</strong><br><small>t.me/channel_one</small></div>
                    <div><span class="task-reward">+1 000 ZZ</span><br><button class="btn" style="padding:6px 14px; font-size:12px; margin-top:4px;">✅ Выполнить</button></div>
                </div>
                <div class="task-card">
                    <div class="task-info"><strong>📢 Telegram Канал 2</strong><br><small>t.me/channel_two</small></div>
                    <div><span class="task-reward">+1 000 ZZ</span><br><button class="btn" style="padding:6px 14px; font-size:12px; margin-top:4px;">✅ Выполнить</button></div>
                </div>
                <div class="task-card">
                    <div class="task-info"><strong>📢 Telegram Канал 3</strong><br><small>t.me/channel_three</small></div>
                    <div><span class="task-reward">+1 000 ZZ</span><br><button class="btn" style="padding:6px 14px; font-size:12px; margin-top:4px;">✅ Выполнить</button></div>
                </div>
            </div>
        </div>
        <div id="sub-chats" class="sub-page">
            <p style="color:#8892b0; font-size:13px; margin-bottom:10px;">Вступи в чат — получи 1 000 Coin ZZ</p>
            <div id="tasks-chats">
                <div class="task-card">
                    <div class="task-info"><strong>💬 Telegram Чат 1</strong><br><small>t.me/chat_one</small></div>
                    <div><span class="task-reward">+1 000 ZZ</span><br><button class="btn" style="padding:6px 14px; font-size:12px; margin-top:4px;">✅ Выполнить</button></div>
                </div>
                <div class="task-card">
                    <div class="task-info"><strong>💬 Telegram Чат 2</strong><br><small>t.me/chat_two</small></div>
                    <div><span class="task-reward">+1 000 ZZ</span><br><button class="btn" style="padding:6px 14px; font-size:12px; margin-top:4px;">✅ Выполнить</button></div>
                </div>
                <div class="task-card">
                    <div class="task-info"><strong>💬 Telegram Чат 3</strong><br><small>t.me/chat_three</small></div>
                    <div><span class="task-reward">+1 000 ZZ</span><br><button class="btn" style="padding:6px 14px; font-size:12px; margin-top:4px;">✅ Выполнить</button></div>
                </div>
            </div>
        </div>
        <div id="sub-bots" class="sub-page">
            <p style="color:#8892b0; font-size:13px; margin-bottom:10px;">Запусти бота — получи 1 000 Coin ZZ</p>
            <div id="tasks-bots">
                <div class="task-card">
                    <div class="task-info"><strong>🤖 Telegram Бот 1</strong><br><small>t.me/bot_one</small></div>
                    <div><span class="task-reward">+1 000 ZZ</span><br><button class="btn" style="padding:6px 14px; font-size:12px; margin-top:4px;">✅ Выполнить</button></div>
                </div>
                <div class="task-card">
                    <div class="task-info"><strong>🤖 Telegram Бот 2</strong><br><small>t.me/bot_two</small></div>
                    <div><span class="task-reward">+1 000 ZZ</span><br><button class="btn" style="padding:6px 14px; font-size:12px; margin-top:4px;">✅ Выполнить</button></div>
                </div>
                <div class="task-card">
                    <div class="task-info"><strong>🤖 Telegram Бот 3</strong><br><small>t.me/bot_three</small></div>
                    <div><span class="task-reward">+1 000 ZZ</span><br><button class="btn" style="padding:6px 14px; font-size:12px; margin-top:4px;">✅ Выполнить</button></div>
                </div>
            </div>
        </div>
    </div>

    <!-- ===== 2. СОЗДАТЬ РЕКЛАМУ ===== -->
    <div id="page-create" class="page">
        <h3>📣 Создать рекламное задание</h3>
        <label>Тип задания:</label>
        <select id="ad-type" class="input-field">
            <option value="channel">📢 Канал</option>
            <option value="chat">💬 Чат</option>
            <option value="bot">🤖 Бот</option>
        </select>
        <label>Ссылка:</label>
        <input type="text" id="ad-link" class="input-field" placeholder="https://t.me/...">
        <label>Количество выполнений (мин. 500):</label>
        <input type="number" id="ad-amount" class="input-field" value="500" min="500" oninput="calcCost()">
        <div style="margin-top:12px; background:#131822; padding:12px; border-radius:8px;">
            💎 Стоимость: <span id="ad-cost" style="color:#00ff88; font-weight:bold;">0.50 TON</span>
            <br><small style="color:#8892b0;">1000 выполнений = 1 TON</small>
        </div>
        <button class="btn green" onclick="submitAd()">💎 Оплатить и отправить на проверку</button>
        <p style="color:#f59e0b; font-size:12px; margin-top:8px;">⚠️ Задание уйдёт на проверку админу</p>
    </div>

    <!-- ===== 3. ПОПОЛНЕНИЕ ===== -->
    <div id="page-deposit" class="page">
        <h3>💎 Пополнение TON</h3>
        <p style="margin-bottom:10px;">Отправь TON на кошелёк ниже и укажи <span style="color:#00ffff;">свой Telegram ID в комментарии</span> к транзакции</p>
        <div class="wallet-address" id="wallet-address">UQDmNY1TIMIgnALOpAyJ4_XO2uroUNLFVRwGie5AEwzccaps</div>
        <button class="copy-btn" onclick="copyWallet()">📋 Копировать адрес</button>
        <div class="balance-card" style="margin-top:15px;">
            <div>📌 Твой Telegram ID:</div>
            <div style="font-size:18px; color:#00ffff; font-weight:bold;" id="deposit-user-id">...</div>
            <small style="color:#f59e0b;">⚠️ Обязательно укажи этот ID в комментарии к платежу!</small>
        </div>
        <div style="margin-top:12px; background:#131822; padding:12px; border-radius:8px;">
            <p>📋 Инструкция:</p>
            <ol style="padding-left:20px; color:#8892b0; font-size:13px;">
                <li>Скопируй адрес кошелька</li>
                <li>Отправь TON (мин. 0.5 TON)</li>
                <li>В комментарии укажи: <span id="deposit-comment" style="color:#00ffff;"></span></li>
                <li>Баланс зачислится после проверки</li>
            </ol>
        </div>
    </div>

    <!-- ===== 4. ВЫВОД ===== -->
    <div id="page-withdraw" class="page">
        <h3>💸 Вывод TON</h3>
        <p style="color:#8892b0; font-size:13px;">Минимальная сумма вывода: <span style="color:#00ff88;">0.5 TON</span></p>
        <label>Сумма TON для вывода:</label>
        <input type="number" id="withdraw-amount" class="input-field" placeholder="0.5" min="0.5" step="0.1">
        <label>Адрес твоего TON кошелька:</label>
        <input type="text" id="withdraw-wallet" class="input-field" placeholder="UQ...">
        <button class="btn red" onclick="withdrawTON()">💸 Вывести TON</button>
        <p style="color:#f59e0b; font-size:12px; margin-top:8px;">⚠️ Вывод обрабатывается вручную</p>
    </div>

    <!-- ===== 5. РЕФЕРАЛЫ ===== -->
    <div id="page-refs" class="page">
        <h3>👥 Реферальная система</h3>
        <p style="margin:10px 0;">Приглашай друзей и получай <span style="color:#00ffff;">1 000 Coin ZZ</span> за каждого!</p>
        <input type="text" id="ref-link" class="input-field" readonly value="https://t.me/ZZTaskBot?start=ref_USER_ID">
        <button class="btn" onclick="copyRef()">📋 Копировать ссылку</button>
        <div class="balance-card" style="margin-top:15px;">
            <div>👥 Приглашено: <span id="ref-count" style="color:#00ffff;">0</span></div>
            <div style="margin-top:5px;">💰 Заработано: <span id="ref-earned" style="color:#00ff88;">0 Coin ZZ</span></div>
        </div>
    </div>

    <!-- ===== 6. БИРЖА ===== -->
    <div id="page-exchange" class="page">
        <h3>📈 Биржа Coin ZZ</h3>
        <div class="balance-card">
            <div>Текущий курс:</div>
            <div style="font-size:20px; color:#00ffff; font-weight:bold;"><span id="exchange-rate">1 000 000</span> ZZ = 1 TON</div>
            <small style="color:#8892b0;">Курс растёт с активностью игроков</small>
        </div>
        <div class="candles-mock" id="candles-box">
            <div class="candle" style="height:30px;"></div><div class="candle" style="height:50px;"></div>
            <div class="candle red" style="height:25px;"></div><div class="candle" style="height:70px;"></div>
            <div class="candle" style="height:100px;"></div><div class="candle" style="height:55px;"></div>
            <div class="candle" style="height:90px;"></div>
        </div>

        <!-- Продать ZZ -->
        <label>Продать ZZ (мин. 1 000 000):</label>
        <input type="number" id="sell-zz-amount" class="input-field" value="1000000" min="1000000" oninput="calcSellZZ()">
        <div style="margin:6px 0; color:#00ff88;">Вы получите: <span id="sell-result">1.00</span> TON</div>
        <button class="btn" onclick="sellZZ()">💰 Продать ZZ → TON</button>

        <!-- Купить ZZ -->
        <label style="margin-top:12px;">Купить ZZ за TON (мин. 1 000 000 ZZ):</label>
        <input type="number" id="buy-zz-amount" class="input-field" value="1000000" min="1000000" oninput="calcBuyZZ()">
        <div style="margin:6px 0; color:#f59e0b;">Спишется: <span id="buy-cost">1.00</span> TON</div>
        <button class="btn gold" onclick="buyZZ()">💎 Купить ZZ за TON</button>
    </div>

    <!-- ===== 7. ОБМЕН (Модерация) ===== -->
    <div id="page-moderation" class="page">
        <h3>🔍 Проверка рекламы</h3>
        <p style="color:#f59e0b; font-size:13px; margin-bottom:10px;">Админ одобряет или отклоняет задания</p>
        <div id="mod-list">
            <div class="task-card">
                <div class="task-info"><strong>📢 Канал</strong><br><small>t.me/test_channel</small><br><small>500 выполнений • 0.50 TON</small></div>
                <div>
                    <span class="status-badge status-pending">⏳ Ждёт</span><br><br>
                    <button class="btn green" style="padding:5px 12px; font-size:11px; margin:2px;">✅ Одобрить</button>
                    <button class="btn red" style="padding:5px 12px; font-size:11px; margin:2px;">❌ Отклонить</button>
                </div>
            </div>
        </div>
    </div>

    <!-- ===== 8. АДМИНКА ===== -->
    <div id="page-admin" class="page">
        <h3 style="color:#ff3366;">👑 Админ-панель</h3>
        <div style="border:1px solid #ff3366; padding:12px; border-radius:10px; margin-bottom:15px;">
            <h4>⚙️ Управление игроком</h4>
            <label>Telegram ID:</label>
            <input type="text" id="admin-user-id" class="input-field" placeholder="ID игрока">
            <label>Coin ZZ (+/-):</label>
            <input type="number" id="admin-zz" class="input-field" placeholder="5000 или -2000">
            <label>TON (+/-):</label>
            <input type="number" id="admin-ton" class="input-field" placeholder="1.5 или -0.5" step="0.01">
            <button class="btn red" onclick="adminUpdateBalance()">💾 Применить</button>
        </div>
        <div style="border:1px solid #ff3366; padding:12px; border-radius:10px;">
            <h4>🎁 Создать промокод</h4>
            <label>Код (4+ символов):</label>
            <input type="text" id="promo-code" class="input-field" placeholder="BONUS500">
            <label>Награда (Coin ZZ):</label>
            <input type="number" id="promo-reward" class="input-field" placeholder="10000">
            <label>Макс. активаций:</label>
            <input type="number" id="promo-max" class="input-field" placeholder="100">
            <button class="btn purple" onclick="createPromo()">🎁 Создать промокод</button>
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
    <div class="nav-item" onclick="switchPage('deposit', this)">
        <div class="nav-item-icon">💎</div><div>Пополнить</div>
    </div>
    <div class="nav-item" onclick="switchPage('withdraw', this)">
        <div class="nav-item-icon">💸</div><div>Вывод</div>
    </div>
    <div class="nav-item" onclick="switchPage('refs', this)">
        <div class="nav-item-icon">👥</div><div>Рефералы</div>
    </div>
    <div class="nav-item" onclick="switchPage('exchange', this)">
        <div class="nav-item-icon">📈</div><div>Биржа</div>
    </div>
    <div class="nav-item" id="nav-moderation" style="display:none;" onclick="switchPage('moderation', this)">
        <div class="nav-item-icon">🔍</div><div>Обмен</div>
    </div>
    <div class="nav-item" id="nav-admin" style="display:none;" onclick="switchPage('admin', this)">
        <div class="nav-item-icon">👑</div><div>Админ</div>
    </div>
</div>

<script>
    const tg = window.Telegram.WebApp;
    tg.expand();

    const userId = tg.initDataUnsafe?.user?.id || "Гость";
    document.getElementById('user-id').innerText = userId;
    document.getElementById('deposit-user-id').innerText = userId;
    document.getElementById('deposit-comment').innerText = "ID: " + userId;

    const ADMIN_ID = 8684827145;
    const WALLET_ADDRESS = "UQDmNY1TIMIgnALOpAyJ4_XO2uroUNLFVRwGie5AEwzccaps";

    if (Number(userId) === ADMIN_ID) {
        document.getElementById('nav-admin').style.display = 'block';
        document.getElementById('nav-moderation').style.display = 'block';
    }

    // Данные (заменишь на backend)
    let userZZ = 50000;
    let userTON = 0.75;
    let refCount = 3;
    let refEarned = 3000;
    let exchangeRate = 1000000;
    let totalPlatformActions = 15000000;

    function updateUI() {
        document.getElementById('bal-zz').innerText = userZZ.toLocaleString();
        document.getElementById('bal-ton').innerText = userTON.toFixed(2);
        document.getElementById('ref-count').innerText = refCount;
        document.getElementById('ref-earned').innerText = refEarned.toLocaleString() + ' Coin ZZ';

        exchangeRate = Math.max(500000, 1000000 - Math.floor(totalPlatformActions / 10000));
        document.getElementById('exchange-rate').innerText = exchangeRate.toLocaleString();
    }

    function switchSubTab(tab, el) {
        document.querySelectorAll('.sub-tab').forEach(t => t.classList.remove('active'));
        document.querySelectorAll('.sub-page').forEach(p => p.classList.remove('active'));
        el.classList.add('active');
        document.getElementById('sub-' + tab).classList.add('active');
    }

    function switchPage(pageId, el) {
        document.querySelectorAll('.page').forEach(p => p.classList.remove('active'));
        document.querySelectorAll('.nav-item').forEach(i => i.classList.remove('active'));
        document.getElementById('page-' + pageId).classList.add('active');
        if (el) el.classList.add('active');
    }

    function calcCost() {
        const amount = parseInt(document.getElementById('ad-amount').value) || 500;
        document.getElementById('ad-cost').innerText = (amount / 1000).toFixed(2) + ' TON';
    }

    function submitAd() {
        const link = document.getElementById('ad-link').value;
        if (!link.startsWith('https://t.me/')) { alert('Введи корректную ссылку Telegram!'); return; }
        const amount = parseInt(document.getElementById('ad-amount').value);
        const cost = amount / 1000;
        if (userTON < cost) { alert('Недостаточно TON! Пополни баланс.'); return; }
        userTON -= cost;
        alert('✅ Задание отправлено на проверку админу!');
        updateUI();
    }

    // Пополнение
    function copyWallet() {
        navigator.clipboard.writeText(WALLET_ADDRESS);
        alert('✅ Адрес кошелька скопирован!');
    }

    // Вывод
    function withdrawTON() {
        const amount = parseFloat(document.getElementById('withdraw-amount').value);
        const wallet = document.getElementById('withdraw-wallet').value.trim();
        if (isNaN(amount) || amount < 0.5) { alert('Минимальная сумма вывода: 0.5 TON'); return; }
        if (amount > userTON) { alert('Недостаточно TON!'); return; }
        if (!wallet.startsWith('UQ')) { alert('Введи корректный адрес TON кошелька!'); return; }
        userTON -= amount;
        alert('✅ Заявка на вывод ' + amount.toFixed(2) + ' TON отправлена!');
        updateUI();
    }

    // Рефералы
    function copyRef() {
        navigator.clipboard.writeText(document.getElementById('ref-link').value);
        alert('✅ Реферальная ссылка скопирована!');
    }

    // Биржа
    function calcSellZZ() {
        const zz = parseInt(document.getElementById('sell-zz-amount').value) || 1000000;
        document.getElementById('sell-result').innerText = (zz / exchangeRate).toFixed(2);
    }

    function calcBuyZZ() {
        const zz = parseInt(document.getElementById('buy-zz-amount').value) || 1000000;
        document.getElementById('buy-cost').innerText = (zz / exchangeRate).toFixed(2);
    }

    function sellZZ() {
        const zz = parseInt(document.getElementById('sell-zz-amount').value);
        if (isNaN(zz) || zz < 1000000) { alert('Минимум 1 000 000 ZZ!'); return; }
        if (zz > userZZ) { alert('Недостаточно Coin ZZ!'); return; }
        const ton = zz / exchangeRate;
        userZZ -= zz;
        userTON += ton;
        totalPlatformActions += zz;
        alert('✅ Продано ' + zz.toLocaleString() + ' ZZ за ' + ton.toFixed(2) + ' TON!');
        updateUI();
    }

    function buyZZ() {
        const zz = parseInt(document.getElementById('buy-zz-amount').value);
        if (isNaN(zz) || zz < 1000000) { alert('Минимум 1 000 000 ZZ!'); return; }
        const ton = zz / exchangeRate;
        if (ton > userTON) { alert('Недостаточно TON! Пополни баланс.'); return; }
        userTON -= ton;
        userZZ += zz;
        totalPlatformActions += zz;
        alert('✅ Куплено ' + zz.toLocaleString() + ' ZZ за ' + ton.toFixed(2) + ' TON!');
        updateUI();
    }

    // Промокод
    function openPromo() {
        let code = prompt("🎁 Введи промокод:");
        if (code) {
            tg.sendData(JSON.stringify({action: "use_promo", code: code}));
            alert("✅ Промокод отправлен на проверку!");
        }
    }

    // Админка
    function adminUpdateBalance() {
        const uid = document.getElementById('admin-user-id').value;
        const zz = parseInt(document.getElementById('admin-zz').value) || 0;
        const ton = parseFloat(document.getElementById('admin-ton').value) || 0;
        if (!uid) { alert('Введи ID игрока!'); return; }
        alert('✅ Баланс игрока ' + uid + ' обновлён!\nZZ: ' + (zz >= 0 ? '+' : '') + zz + '\nTON: ' + (ton >= 0 ? '+' : '') + ton.toFixed(2));
    }

    function createPromo() {
        const code = document.getElementById('promo-code').value.trim();
        const reward = document.getElementById('promo-reward').value;
        const max = document.getElementById('promo-max').value;
        if (!code || code.length < 4) { alert('Код должен быть от 4 символов!'); return; }
        alert('🎁 Промокод "' + code + '" создан!\nНаграда: ' + reward + ' ZZ\nАктиваций: ' + max);
    }

    updateUI();
</script>
</body>
</html>
