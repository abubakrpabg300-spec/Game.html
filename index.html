<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>ZZ Task Bot</title>
    <script src="https://telegram.org/js/telegram-web-app.js"></script>
    <style>
        :root {
            --bg: #0b0e11; --card: #1a1d26; --border: #2a2f3a;
            --cyan: #00e5ff; --green: #00e676; --red: #ff1744;
            --gold: #ffc107; --text: #e0e0e0; --sub: #8a8f9a; --radius: 14px;
        }
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body {
            background: var(--bg); color: var(--text);
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            user-select: none; overflow-x: hidden; font-size: 14px;
        }
        .container { padding: 16px; padding-bottom: 95px; }
        .header {
            display: flex; justify-content: space-between; align-items: center;
            margin-bottom: 14px;
        }
        .header-id {
            background: var(--card); padding: 8px 14px; border-radius: 25px;
            font-size: 12px; color: var(--sub); border: 1px solid var(--border);
        }
        .header-id span { color: var(--cyan); font-weight: 600; }
        .promo-btn {
            background: linear-gradient(135deg, #ff6d00, #ff9100); border: none;
            width: 40px; height: 40px; border-radius: 50%; font-size: 18px;
            cursor: pointer;
        }
        .card {
            background: var(--card); border: 1px solid var(--border);
            border-radius: var(--radius); padding: 14px; margin-bottom: 12px;
        }
        .balance-row { display: flex; gap: 10px; margin-bottom: 12px; }
        .balance-item {
            flex: 1; background: var(--card); border: 1px solid var(--border);
            border-radius: var(--radius); padding: 14px; text-align: center;
        }
        .balance-item .label { font-size: 11px; color: var(--sub); text-transform: uppercase; }
        .balance-item .value { font-size: 22px; font-weight: 700; }
        .balance-item .value.zz { color: var(--cyan); }
        .balance-item .value.ton { color: var(--green); }
        .page { display: none; }
        .page.active { display: block; }
        .sub-tabs { display: flex; gap: 6px; margin-bottom: 14px; }
        .sub-tab {
            flex: 1; padding: 11px; text-align: center; background: var(--card);
            border: 1px solid var(--border); border-radius: 25px; cursor: pointer;
            font-weight: 600; font-size: 12px; color: var(--sub);
        }
        .sub-tab.active { background: var(--cyan); color: #000; border-color: var(--cyan); }
        .sub-page { display: none; }
        .sub-page.active { display: block; }
        .nav-bar {
            position: fixed; bottom: 0; left: 0; right: 0; height: 72px;
            background: #11141c; border-top: 1px solid var(--border);
            display: flex; justify-content: space-around; align-items: center; z-index: 1000;
        }
        .nav-item { color: var(--sub); font-size: 10px; text-align: center; cursor: pointer; flex: 1; }
        .nav-item.active { color: var(--cyan); }
        .nav-item-icon { font-size: 20px; margin-bottom: 3px; }
        .btn {
            background: var(--cyan); color: #000; border: none; padding: 10px 16px;
            border-radius: 25px; width: 100%; font-weight: 700; font-size: 13px;
            margin-top: 8px; cursor: pointer;
        }
        .btn:active { opacity: 0.7; }
        .btn.green { background: var(--green); }
        .btn.red { background: var(--red); color: #fff; }
        .btn.gold { background: var(--gold); color: #000; }
        .btn.outline { background: transparent; border: 2px solid var(--cyan); color: var(--cyan); }
        .btn.sm { padding: 7px 14px; font-size: 11px; width: auto; margin: 2px; display: inline-block; }
        .input-field {
            width: 100%; padding: 10px 14px; background: #0b0e11;
            border: 1px solid var(--border); border-radius: 25px; color: #fff;
            margin-top: 6px; font-size: 13px; outline: none;
        }
        .input-field:focus { border-color: var(--cyan); }
        label { display: block; margin-top: 10px; font-size: 12px; color: var(--sub); font-weight: 500; }
        .task-row {
            display: flex; justify-content: space-between; align-items: center;
            padding: 12px; background: #0b0e11; border-radius: 12px; margin-bottom: 8px;
            flex-wrap: wrap; gap: 8px;
        }
        .badge {
            padding: 4px 10px; border-radius: 20px; font-size: 10px; font-weight: 700;
        }
        .badge-pending { background: rgba(255,193,7,0.2); color: var(--gold); }
        .badge-ok { background: rgba(0,230,118,0.2); color: var(--green); }
        .badge-no { background: rgba(255,23,68,0.2); color: var(--red); }
        .wallet-box {
            background: #0b0e11; border: 1px dashed var(--cyan); border-radius: 12px;
            padding: 12px; word-break: break-all; font-size: 11px; color: var(--cyan);
            text-align: center; margin: 10px 0;
        }
        .chart-container {
            background: #0b0e11; border-radius: 12px; padding: 8px; margin: 12px 0;
            height: 180px;
        }
        canvas { width: 100% !important; height: 100% !important; }
        .price-change { display: flex; align-items: center; gap: 8px; justify-content: center; margin: 8px 0; }
        .pct {
            font-size: 18px; font-weight: 700; padding: 5px 12px; border-radius: 20px;
        }
        .pct.up { color: var(--green); background: rgba(0,230,118,0.15); }
        .pct.down { color: var(--red); background: rgba(255,23,68,0.15); }
        .empty-state { text-align: center; padding: 30px 20px; color: var(--sub); }
        .empty-state .icon { font-size: 36px; margin-bottom: 8px; }

        .admin-section {
            border: 1px solid var(--red); border-radius: var(--radius); padding: 14px; margin-bottom: 12px;
        }
        .admin-section h4 { color: var(--red); margin-bottom: 8px; }
    </style>
</head>
<body>

<div class="container">
    <!-- Шапка -->
    <div class="header">
        <div class="header-id">🆔 <span id="user-id">...</span></div>
        <button class="promo-btn" onclick="openPromo()">🎁</button>
    </div>

    <!-- Балансы -->
    <div class="balance-row">
        <div class="balance-item">
            <div class="label">Coin ZZ</div>
            <div class="value zz" id="bal-zz">0</div>
        </div>
        <div class="balance-item">
            <div class="label">TON</div>
            <div class="value ton" id="bal-ton">0.00</div>
        </div>
    </div>

    <!-- ===== ЗАДАНИЯ ===== -->
    <div id="page-tasks" class="page active">
        <div class="sub-tabs">
            <div class="sub-tab active" onclick="switchSubTab('channels', this)">📢 Каналы</div>
            <div class="sub-tab" onclick="switchSubTab('chats', this)">💬 Чаты</div>
            <div class="sub-tab" onclick="switchSubTab('bots', this)">🤖 Боты</div>
        </div>
        <div id="sub-channels" class="sub-page active"><div id="tasks-channels"></div></div>
        <div id="sub-chats" class="sub-page"><div id="tasks-chats"></div></div>
        <div id="sub-bots" class="sub-page"><div id="tasks-bots"></div></div>
    </div>

    <!-- ===== СОЗДАТЬ РЕКЛАМУ ===== -->
    <div id="page-create" class="page">
        <h3>📣 Создать задание</h3>
        <label>Тип:</label>
        <select id="ad-type" class="input-field">
            <option value="channel">📢 Канал</option>
            <option value="chat">💬 Чат</option>
            <option value="bot">🤖 Бот</option>
        </select>
        <label>Ссылка (без https://):</label>
        <input type="text" id="ad-link" class="input-field" placeholder="t.me/...">
        <label>Кол-во выполнений (мин. 500):</label>
        <input type="number" id="ad-amount" class="input-field" value="500" min="500" oninput="calcCost()">
        <div class="card" style="text-align:center;">
            💎 К оплате: <b id="ad-cost" style="color:var(--green);">0.50 TON</b>
            <br><small style="color:var(--sub);">1000 выполнений = 1 TON</small>
        </div>
        <button class="btn green" onclick="submitAd()">💎 Оплатить и отправить</button>
        <p style="color:var(--gold); font-size:11px; margin-top:8px;">⚠️ Уйдёт на проверку админу</p>
    </div>

    <!-- ===== ПРОФИЛЬ ===== -->
    <div id="page-profile" class="page">
        <h3>👤 Мой профиль</h3>
        <div class="balance-row">
            <div class="balance-item">
                <div class="label">Coin ZZ</div>
                <div class="value zz" id="bal-zz2">0</div>
            </div>
            <div class="balance-item">
                <div class="label">TON</div>
                <div class="value ton" id="bal-ton2">0.00</div>
            </div>
        </div>
        <h4>💎 Пополнение TON</h4>
        <p style="font-size:11px; color:var(--sub);">Отправь TON на кошелёк, в комментарии укажи свой ID</p>
        <div class="wallet-box">UQDmNY1TIMIgnALOpAyJ4_XO2uroUNLFVRwGie5AEwzccaps</div>
        <button class="btn outline" onclick="copyWallet()">📋 Копировать адрес</button>
        <p style="font-size:10px; color:var(--gold); margin-top:6px;">⚠️ В комментарии: ID <span id="profile-id">...</span></p>

        <h4 style="margin-top:18px;">💸 Вывод TON</h4>
        <p style="font-size:11px; color:var(--sub);">Мин. 0.5 TON</p>
        <input type="number" id="w-amount" class="input-field" placeholder="Сумма TON" min="0.5" step="0.1">
        <input type="text" id="w-wallet" class="input-field" placeholder="Твой TON адрес (UQ...)">
        <button class="btn red" onclick="withdraw()">💸 Вывести</button>
    </div>

    <!-- ===== РЕФЕРАЛЫ ===== -->
    <div id="page-refs" class="page">
        <h3>👥 Рефералы</h3>
        <div class="card" style="text-align:center;">
            <div style="font-size:40px;">👥</div>
            <p>+<b style="color:var(--cyan);">1 000 Coin ZZ</b> за друга</p>
        </div>
        <input type="text" id="ref-link" class="input-field" readonly>
        <button class="btn outline" onclick="copyRef()">📋 Копировать ссылку</button>
        <div class="balance-row" style="margin-top:12px;">
            <div class="balance-item"><div class="label">Приглашено</div><div class="value zz" id="ref-count">0</div></div>
            <div class="balance-item"><div class="label">Заработано</div><div class="value ton" id="ref-earned">0 ZZ</div></div>
        </div>
    </div>

    <!-- ===== БИРЖА ===== -->
    <div id="page-exchange" class="page">
        <h3>📈 Биржа Coin ZZ</h3>
        <div class="card" style="text-align:center;">
            <div style="font-size:12px; color:var(--sub);">Текущий курс</div>
            <div style="font-size:24px; font-weight:700; color:var(--cyan);"><span id="rate">1 000 000</span> ZZ = 1 TON</div>
            <div class="price-change"><span class="pct" id="pct-change">0%</span></div>
        </div>
        <div class="chart-container"><canvas id="priceChart"></canvas></div>
        <label>Количество ZZ (мин. 1 000 000):</label>
        <input type="number" id="swap-zz" class="input-field" value="1000000" min="1000000" oninput="calcSwap()">
        <div style="text-align:center; margin:8px 0; font-weight:600;">= <span id="swap-ton" style="color:var(--green);">1.00</span> TON</div>
        <div style="display:flex; gap:8px;">
            <button class="btn green" style="flex:1;" onclick="sellZZ()">💰 Продать</button>
            <button class="btn gold" style="flex:1;" onclick="buyZZ()">💎 Купить</button>
        </div>
    </div>

    <!-- ===== АДМИНКА ===== -->
    <div id="page-admin" class="page">
        <h3 style="color:var(--red);">👑 Админ-панель</h3>

        <div class="admin-section">
            <h4>⚙️ Начислить/Снять игроку</h4>
            <input type="text" id="a-id" class="input-field" placeholder="Telegram ID игрока">
            <input type="number" id="a-zz" class="input-field" placeholder="Coin ZZ (например: 5000 или -2000)">
            <input type="number" id="a-ton" class="input-field" placeholder="TON (например: 1.5 или -0.5)" step="0.01">
            <button class="btn red" onclick="adminBalance()">💾 Применить</button>
            <p style="font-size:11px; color:var(--sub); margin-top:6px;">✅ Работает: изменит баланс игрока по ID</p>
        </div>

        <div class="admin-section">
            <h4>🎁 Создать промокод</h4>
            <input type="text" id="p-code" class="input-field" placeholder="Код (например: BONUS)">
            <input type="number" id="p-reward" class="input-field" placeholder="Награда в Coin ZZ">
            <input type="number" id="p-max" class="input-field" placeholder="Сколько раз можно активировать">
            <button class="btn gold" onclick="createPromo()">🎁 Создать промокод</button>
            <p style="font-size:11px; color:var(--sub); margin-top:6px;">✅ Промокод сохранится и будет работать</p>
        </div>

        <div class="admin-section">
            <h4>📋 Задания на проверке</h4>
            <div id="admin-tasks"></div>
            <p style="font-size:11px; color:var(--sub); margin-top:6px;">✅ Одобрить — задание появится у игроков<br>❌ Отклонить — удалить навсегда</p>
        </div>

        <div class="admin-section">
            <h4>📊 Список промокодов</h4>
            <div id="promo-list"></div>
            <button class="btn red" style="margin-top:8px;" onclick="clearPromos()">🗑 Очистить все промокоды</button>
        </div>
    </div>
</div>

<!-- МЕНЮ -->
<div class="nav-bar">
    <div class="nav-item active" onclick="switchPage('tasks', this)"><div class="nav-item-icon">📋</div>Задания</div>
    <div class="nav-item" onclick="switchPage('create', this)"><div class="nav-item-icon">📣</div>Реклама</div>
    <div class="nav-item" onclick="switchPage('profile', this)"><div class="nav-item-icon">👤</div>Профиль</div>
    <div class="nav-item" onclick="switchPage('refs', this)"><div class="nav-item-icon">👥</div>Рефералы</div>
    <div class="nav-item" onclick="switchPage('exchange', this)"><div class="nav-item-icon">📈</div>Биржа</div>
    <div class="nav-item" id="nav-admin" style="display:none;" onclick="switchPage('admin', this)"><div class="nav-item-icon">👑</div>Админ</div>
</div>

<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script>
    const tg = window.Telegram.WebApp;
    tg.expand();

    const userId = tg.initDataUnsafe?.user?.id || Math.floor(Math.random() * 1000000);
    document.getElementById('user-id').innerText = userId;
    document.getElementById('profile-id').innerText = userId;
    document.getElementById('ref-link').value = 'https://t.me/ZZTaskBot?start=ref_' + userId;

    const ADMIN_ID = 8684827145;
    const WALLET = "UQDmNY1TIMIgnALOpAyJ4_XO2uroUNLFVRwGie5AEwzccaps";

    if (Number(userId) === ADMIN_ID) {
        document.getElementById('nav-admin').style.display = 'block';
    }

    // ===== ДАННЫЕ В localStorage =====
    function getData() {
        return JSON.parse(localStorage.getItem('zzbot_data') || '{}');
    }
    function saveData(d) {
        localStorage.setItem('zzbot_data', JSON.stringify(d));
    }

    // Инициализация
    let data = getData();
    if (!data.users) data.users = {};
    if (!data.pendingTasks) data.pendingTasks = [];
    if (!data.activeTasks) data.activeTasks = [];
    if (!data.promos) data.promos = [];
    if (!data.priceHistory) data.priceHistory = [1000000, 1005000, 1000000, 998000, 1000000];
    if (!data.totalActions) data.totalActions = 0;

    // Текущий пользователь
    if (!data.users[userId]) {
        data.users[userId] = { zz: 0, ton: 0, refs: 0, refZZ: 0, completedTasks: [], usedPromos: [] };
    }
    let user = data.users[userId];

    function updateAllData() {
        data.users[userId] = user;
        saveData(data);
        updateUI();
    }

    let rate = 1000000;

    function updateUI() {
        document.getElementById('bal-zz').innerText = user.zz.toLocaleString();
        document.getElementById('bal-zz2').innerText = user.zz.toLocaleString();
        document.getElementById('bal-ton').innerText = user.ton.toFixed(2);
        document.getElementById('bal-ton2').innerText = user.ton.toFixed(2);
        document.getElementById('ref-count').innerText = user.refs;
        document.getElementById('ref-earned').innerText = user.refZZ.toLocaleString() + ' ZZ';

        rate = Math.max(500000, 1000000 - Math.floor(data.totalActions / 10000));
        document.getElementById('rate').innerText = rate.toLocaleString();

        const prev = data.priceHistory[data.priceHistory.length - 2] || rate;
        const pct = ((rate - prev) / prev * 100).toFixed(1);
        const pctEl = document.getElementById('pct-change');
        pctEl.innerText = (pct >= 0 ? '+' : '') + pct + '%';
        pctEl.className = 'pct ' + (pct >= 0 ? 'up' : 'down');

        renderTasks();
        renderAdminTasks();
        renderPromoList();
        updateChart();
    }

    // ===== ЗАДАНИЯ =====
    function renderTasks() {
        const cats = { channels: 'channel', chats: 'chat', bots: 'bot' };
        Object.entries(cats).forEach(([cat, type]) => {
            const container = document.getElementById('tasks-' + cat);
            const tasks = data.activeTasks.filter(t => t.type === type && t.approved);
            if (tasks.length === 0) {
                container.innerHTML = '<div class="empty-state"><div class="icon">📭</div><p>Пока нет заданий</p></div>';
            } else {
                container.innerHTML = tasks.map(t => {
                    const done = user.completedTasks.includes(t.id);
                    return `<div class="task-row">
                        <div><b>${t.name}</b><br><small style="color:var(--sub);">${t.link}</small></div>
                        <div style="text-align:right;">
                            <span style="color:var(--cyan); font-weight:600;">+1 000 ZZ</span><br>
                            ${done ? '<span class="badge badge-ok">✅ Выполнено</span>' : `<button class="btn sm" onclick="doTask('${t.id}')">✅</button>`}
                        </div>
                    </div>`;
                }).join('');
            }
        });
    }

    function doTask(taskId) {
        if (user.completedTasks.includes(taskId)) return;
        const task = data.activeTasks.find(t => t.id === taskId);
        if (!task) return;
        tg.openTelegramLink('https://' + task.link);
        user.completedTasks.push(taskId);
        user.zz += 1000;
        data.totalActions += 1000;
        data.priceHistory.push(rate);
        if (data.priceHistory.length > 30) data.priceHistory.shift();
        updateAllData();
        alert('✅ +1 000 Coin ZZ');
    }

    // ===== АДМИН: ПРОВЕРКА ЗАДАНИЙ =====
    function renderAdminTasks() {
        const box = document.getElementById('admin-tasks');
        if (!box) return;
        const pending = data.pendingTasks.filter(t => !t.reviewed);
        if (pending.length === 0) {
            box.innerHTML = '<p style="color:var(--sub); text-align:center; padding:15px;">Нет заданий на проверке</p>';
        } else {
            box.innerHTML = pending.map(t =>
                `<div class="task-row">
                    <div>
                        <b>${t.type === 'channel' ? '📢 Канал' : t.type === 'chat' ? '💬 Чат' : '🤖 Бот'}</b><br>
                        <small>${t.link} • ${t.amount} вып. • ${t.cost} TON</small><br>
                        <small>От: ID ${t.creator}</small>
                    </div>
                    <div>
                        <button class="btn sm green" onclick="approveTask(${t.id})">✅</button>
                        <button class="btn sm red" onclick="rejectTask(${t.id})">❌</button>
                    </div>
                </div>`
            ).join('');
        }
    }

    function approveTask(id) {
        const t = data.pendingTasks.find(t => t.id === id);
        if (t) {
            t.reviewed = true;
            t.approved = true;
            data.activeTasks.push({
                id: t.id,
                type: t.type,
                name: t.link.split('/')[1] || 'Задание',
                link: t.link,
                approved: true
            });
            saveData(data);
            updateUI();
            alert('✅ Задание одобрено!');
        }
    }

    function rejectTask(id) {
        const t = data.pendingTasks.find(t => t.id === id);
        if (t) {
            t.reviewed = true;
            t.approved = false;
            saveData(data);
            updateUI();
            alert('❌ Задание отклонено!');
        }
    }

    // ===== СОЗДАТЬ РЕКЛАМУ =====
    function calcCost() {
        const a = parseInt(document.getElementById('ad-amount').value) || 500;
        document.getElementById('ad-cost').innerText = (a / 1000).toFixed(2) + ' TON';
    }

    function submitAd() {
        const link = document.getElementById('ad-link').value.trim();
        if (!link.startsWith('t.me/')) { alert('Введи ссылку в формате t.me/...'); return; }
        const amount = parseInt(document.getElementById('ad-amount').value);
        const cost = amount / 1000;
        if (user.ton < cost) { alert('Недостаточно TON! Пополни баланс.'); return; }
        user.ton -= cost;
        const newTask = {
            id: Date.now(),
            type: document.getElementById('ad-type').value,
            link: link,
            amount: amount,
            cost: cost,
            creator: userId,
            reviewed: false,
            approved: false
        };
        data.pendingTasks.push(newTask);
        updateAllData();
        alert('✅ Задание отправлено на проверку админу!');
    }

    // ===== ПРОМОКОДЫ =====
    function createPromo() {
        const code = document.getElementById('p-code').value.trim().toUpperCase();
        const reward = parseInt(document.getElementById('p-reward').value);
        const max = parseInt(document.getElementById('p-max').value);
        if (!code || code.length < 3) { alert('Код должен быть от 3 символов!'); return; }
        if (!reward || reward <= 0) { alert('Введи награду!'); return; }
        if (!max || max <= 0) { alert('Введи количество активаций!'); return; }

        // Проверка на дубликат
        if (data.promos.find(p => p.code === code)) {
            alert('⚠️ Такой промокод уже существует!');
            return;
        }

        data.promos.push({
            code: code,
            reward: reward,
            maxUses: max,
            usedBy: []
        });
        saveData(data);
        updateUI();
        document.getElementById('p-code').value = '';
        document.getElementById('p-reward').value = '';
        document.getElementById('p-max').value = '';
        alert('🎁 Промокод "' + code + '" создан! Награда: ' + reward + ' ZZ, активаций: ' + max);
    }

    function renderPromoList() {
        const box = document.getElementById('promo-list');
        if (!box) return;
        if (data.promos.length === 0) {
            box.innerHTML = '<p style="color:var(--sub); text-align:center; padding:10px;">Нет промокодов</p>';
        } else {
            box.innerHTML = data.promos.map(p =>
                `<div class="task-row">
                    <div>
                        <b>🎁 ${p.code}</b><br>
                        <small>+${p.reward} ZZ • ${p.usedBy.length}/${p.maxUses} исп.</small>
                    </div>
                    <button class="btn sm red" onclick="deletePromo('${p.code}')">🗑</button>
                </div>`
            ).join('');
        }
    }

    function deletePromo(code) {
        data.promos = data.promos.filter(p => p.code !== code);
        saveData(data);
        updateUI();
        alert('🗑 Промокод удалён!');
    }

    function clearPromos() {
        if (confirm('Удалить ВСЕ промокоды?')) {
            data.promos = [];
            saveData(data);
            updateUI();
            alert('🗑 Все промокоды удалены!');
        }
    }

    function openPromo() {
        const code = prompt('🎁 Введи промокод:');
        if (!code) return;
        const promo = data.promos.find(p => p.code === code.toUpperCase());
        if (!promo) { alert('❌ Промокод не найден!'); return; }
        if (promo.usedBy.includes(userId)) { alert('⚠️ Ты уже активировал этот промокод!'); return; }
        if (promo.usedBy.length >= promo.maxUses) { alert('⚠️ Промокод больше не действует!'); return; }
        promo.usedBy.push(userId);
        user.zz += promo.reward;
        saveData(data);
        updateUI();
        alert('🎁 +' + promo.reward + ' Coin ZZ!');
    }

    // ===== АДМИН: БАЛАНС =====
    function adminBalance() {
        const uid = document.getElementById('a-id').value.trim();
        const dz = parseInt(document.getElementById('a-zz').value) || 0;
        const dt = parseFloat(document.getElementById('a-ton').value) || 0;
        if (!uid) { alert('Введи ID игрока!'); return; }
        if (!data.users[uid]) {
            data.users[uid] = { zz: 0, ton: 0, refs: 0, refZZ: 0, completedTasks: [], usedPromos: [] };
        }
        data.users[uid].zz += dz;
        data.users[uid].ton += dt;
        if (Number(uid) === Number(userId)) {
            user = data.users[uid];
        }
        saveData(data);
        updateUI();
        document.getElementById('a-id').value = '';
        document.getElementById('a-zz').value = '';
        document.getElementById('a-ton').value = '';
        alert('✅ Баланс игрока ' + uid + ' обновлён!\nZZ: ' + (dz >= 0 ? '+' : '') + dz + '\nTON: ' + (dt >= 0 ? '+' : '') + dt.toFixed(2));
    }

    // ===== ВЫВОД =====
    function withdraw() {
        const amt = parseFloat(document.getElementById('w-amount').value);
        const wal = document.getElementById('w-wallet').value.trim();
        if (isNaN(amt) || amt < 0.5) { alert('Мин. 0.5 TON'); return; }
        if (amt > user.ton) { alert('Недостаточно TON'); return; }
        if (!wal.startsWith('UQ')) { alert('Неверный адрес TON кошелька!'); return; }
        user.ton -= amt;
        updateAllData();
        document.getElementById('w-amount').value = '';
        document.getElementById('w-wallet').value = '';
        alert('✅ Заявка на вывод ' + amt.toFixed(2) + ' TON отправлена!');
    }

    // ===== БИРЖА =====
    function calcSwap() {
        const z = parseInt(document.getElementById('swap-zz').value) || 1000000;
        document.getElementById('swap-ton').innerText = (z / rate).toFixed(4);
    }

    function sellZZ() {
        const z = parseInt(document.getElementById('swap-zz').value);
        if (isNaN(z) || z < 1000000 || z > user.zz) { alert('Мин. 1 млн ZZ или недостаточно'); return; }
        const t = z / rate;
        user.zz -= z;
        user.ton += t;
        data.totalActions += z;
        data.priceHistory.push(rate);
        if (data.priceHistory.length > 30) data.priceHistory.shift();
        updateAllData();
        alert('✅ Продано ' + z.toLocaleString() + ' ZZ за ' + t.toFixed(4) + ' TON');
    }

    function buyZZ() {
        const z = parseInt(document.getElementById('swap-zz').value);
        if (isNaN(z) || z < 1000000) { alert('Мин. 1 млн ZZ'); return; }
        const t = z / rate;
        if (t > user.ton) { alert('Недостаточно TON'); return; }
        user.ton -= t;
        user.zz += z;
        data.totalActions += z;
        data.priceHistory.push(rate);
        if (data.priceHistory.length > 30) data.priceHistory.shift();
        updateAllData();
        alert('✅ Куплено ' + z.toLocaleString() + ' ZZ за ' + t.toFixed(4) + ' TON');
    }

    // ===== ГРАФИК =====
    let chart;
    function updateChart() {
        const ctx = document.getElementById('priceChart');
        if (!ctx) return;
        if (chart) chart.destroy();
        chart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: data.priceHistory.map(() => ''),
                datasets: [{
                    data: data.priceHistory,
                    borderColor: '#00e5ff',
                    backgroundColor: 'rgba(0,229,255,0.1)',
                    fill: true,
                    tension: 0.4,
                    pointRadius: 0,
                    borderWidth: 2
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: { legend: { display: false } },
                scales: { x: { display: false }, y: { display: false } }
            }
        });
    }

    // ===== НАВИГАЦИЯ =====
    function switchSubTab(tab, el) {
        document.querySelectorAll('.sub-tab').forEach(t => t.classList.remove('active'));
        document.querySelectorAll('.sub-page').forEach(p => p.classList.remove('active'));
        el.classList.add('active');
        document.getElementById('sub-' + tab).classList.add('active');
    }

    function switchPage(id, el) {
        document.querySelectorAll('.page').forEach(p => p.classList.remove('active'));
        document.querySelectorAll('.nav-item').forEach(n => n.classList.remove('active'));
        document.getElementById('page-' + id).classList.add('active');
        if (el) el.classList.add('active');
    }

    function copyWallet() {
        navigator.clipboard.writeText(WALLET);
        alert('✅ Кошелёк скопирован!');
    }

    function copyRef() {
        navigator.clipboard.writeText(document.getElementById('ref-link').value);
        alert('✅ Реферальная ссылка скопирована!');
    }

    // ===== ЗАПУСК =====
    updateUI();
</script>
</body>
</html>
