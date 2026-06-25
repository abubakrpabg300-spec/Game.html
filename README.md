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
            background-color: #0d0f12; color: #ffffff;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            user-select: none; overflow-x: hidden; font-size: 14px;
        }
        .container { padding: 15px; padding-bottom: 90px; }
        .header {
            display: flex; justify-content: space-between; align-items: center;
            border-bottom: 1px solid #1f232b; padding-bottom: 10px; margin-bottom: 15px;
        }
        .card {
            background: #131822; border: 1px solid #2c3545;
            border-radius: 10px; padding: 15px; margin-bottom: 12px;
        }
        .balance-big { font-size: 26px; font-weight: bold; color: #00ffff; }
        .page { display: none; }
        .page.active { display: block; }

        .sub-tabs { display: flex; gap: 6px; margin-bottom: 12px; }
        .sub-tab {
            flex: 1; padding: 10px; text-align: center; background: #1e2530;
            border: 1px solid #2c3545; border-radius: 8px; cursor: pointer;
            font-weight: bold; font-size: 12px; color: #8892b0;
        }
        .sub-tab.active { background: #00ffff; color: #0d0f12; border-color: #00ffff; }
        .sub-page { display: none; }
        .sub-page.active { display: block; }

        .nav-bar {
            position: fixed; bottom: 0; left: 0; right: 0; height: 70px;
            background: #131822; border-top: 1px solid #2c3545;
            display: flex; justify-content: space-around; align-items: center; z-index: 1000;
        }
        .nav-item { color: #8892b0; font-size: 10px; text-align: center; cursor: pointer; flex: 1; }
        .nav-item.active { color: #00ffff; }
        .nav-item-icon { font-size: 18px; margin-bottom: 2px; }

        .btn {
            background: #0088cc; color: #fff; border: none; padding: 10px;
            border-radius: 8px; width: 100%; font-weight: bold; font-size: 13px;
            margin-top: 8px; cursor: pointer;
        }
        .btn.green { background: #00ff88; color: #000; }
        .btn.red { background: #ef4444; }
        .btn.purple { background: #a855f7; }
        .btn.small { padding: 6px 12px; font-size: 11px; width: auto; margin: 2px; }

        .input-field {
            width: 100%; padding: 10px; background: #1e2530;
            border: 1px solid #2c3545; border-radius: 6px; color: #fff;
            margin-top: 5px; font-size: 13px;
        }
        label { display: block; margin-top: 10px; font-size: 12px; color: #8892b0; }

        .task-row {
            display: flex; justify-content: space-between; align-items: center;
            padding: 12px; background: #1e2530; border-radius: 8px; margin-bottom: 8px;
        }
        .badge { padding: 3px 8px; border-radius: 4px; font-size: 10px; font-weight: bold; }
        .badge-pending { background: #f59e0b; color: #000; }
        .badge-ok { background: #10b981; color: #fff; }
        .badge-no { background: #ef4444; color: #fff; }

        .wallet-box {
            background: #0d0f12; border: 1px dashed #00ffff; border-radius: 8px;
            padding: 10px; word-break: break-all; font-size: 11px; color: #00ffff;
            text-align: center; margin: 8px 0;
        }
    </style>
</head>
<body>

<div class="container">
    <div class="header">
        <div>🆔 <span id="user-id">...</span></div>
        <div style="cursor:pointer; font-size:20px;" onclick="openPromo()">🎁</div>
    </div>

    <!-- ===== ЗАДАНИЯ ===== -->
    <div id="page-tasks" class="page active">
        <div class="sub-tabs">
            <div class="sub-tab active" onclick="switchSubTab('channels', this)">📢 Каналы</div>
            <div class="sub-tab" onclick="switchSubTab('chats', this)">💬 Чаты</div>
            <div class="sub-tab" onclick="switchSubTab('bots', this)">🤖 Боты</div>
        </div>
        <div id="sub-channels" class="sub-page active">
            <div id="tasks-channels"></div>
        </div>
        <div id="sub-chats" class="sub-page">
            <div id="tasks-chats"></div>
        </div>
        <div id="sub-bots" class="sub-page">
            <div id="tasks-bots"></div>
        </div>
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
        <label>Ссылка:</label>
        <input type="text" id="ad-link" class="input-field" placeholder="https://t.me/...">
        <label>Кол-во выполнений (мин. 500):</label>
        <input type="number" id="ad-amount" class="input-field" value="500" min="500" oninput="calcCost()">
        <div class="card">
            💎 К оплате: <b id="ad-cost" style="color:#00ff88;">0.50 TON</b>
            <br><small style="color:#8892b0;">1000 выполнений = 1 TON</small>
        </div>
        <button class="btn green" onclick="submitAd()">💎 Оплатить и отправить</button>
        <p style="color:#f59e0b; font-size:11px; margin-top:6px;">Уйдёт на проверку админу</p>
    </div>

    <!-- ===== МОЙ ПРОФИЛЬ ===== -->
    <div id="page-profile" class="page">
        <h3>👤 Мой профиль</h3>
        <div class="card" style="text-align:center;">
            <div>💰 Coin ZZ</div>
            <div class="balance-big" id="bal-zz">0</div>
            <div style="margin-top:8px;">💎 TON</div>
            <div style="font-size:20px; color:#00ff88; font-weight:bold;" id="bal-ton">0.00</div>
        </div>

        <h4 style="margin-top:15px;">💎 Пополнение TON</h4>
        <p style="font-size:12px; color:#8892b0;">Отправь TON на кошелёк, в комментарии укажи свой ID</p>
        <div class="wallet-box">UQDmNY1TIMIgnALOpAyJ4_XO2uroUNLFVRwGie5AEwzccaps</div>
        <button class="btn small" onclick="copyWallet()">📋 Копировать</button>
        <p style="font-size:11px; color:#f59e0b; margin-top:4px;">⚠️ В комментарии пиши: ID <span id="profile-id">...</span></p>

        <h4 style="margin-top:15px;">💸 Вывод TON</h4>
        <p style="font-size:12px; color:#8892b0;">Мин. 0.5 TON</p>
        <input type="number" id="w-amount" class="input-field" placeholder="Сумма TON" min="0.5" step="0.1">
        <input type="text" id="w-wallet" class="input-field" placeholder="Твой TON адрес">
        <button class="btn red" onclick="withdraw()">💸 Вывести</button>
    </div>

    <!-- ===== РЕФЕРАЛЫ ===== -->
    <div id="page-refs" class="page">
        <h3>👥 Рефералы</h3>
        <p style="font-size:13px;">+1 000 Coin ZZ за друга</p>
        <input type="text" id="ref-link" class="input-field" readonly value="https://t.me/bot?start=ID">
        <button class="btn" onclick="copyRef()">📋 Копировать ссылку</button>
        <div class="card" style="text-align:center; margin-top:12px;">
            👥 Приглашено: <b id="ref-count" style="color:#00ffff;">0</b><br>
            💰 Заработано: <b id="ref-earned" style="color:#00ff88;">0 Coin ZZ</b>
        </div>
    </div>

    <!-- ===== БИРЖА ===== -->
    <div id="page-exchange" class="page">
        <h3>📈 Биржа Coin ZZ</h3>
        <div class="card" style="text-align:center;">
            <div>Курс:</div>
            <div style="font-size:20px; color:#00ffff; font-weight:bold;"><span id="rate">1 000 000</span> ZZ = 1 TON</div>
            <small style="color:#8892b0;">Меняется автоматически</small>
        </div>
        <label>Количество ZZ (мин. 1 млн):</label>
        <input type="number" id="swap-zz" class="input-field" value="1000000" min="1000000" oninput="calcSwap()">
        <div style="margin:6px 0; color:#00ff88;">Сумма TON: <b id="swap-ton">1.00</b></div>
        <button class="btn green" onclick="sellZZ()">💰 Продать ZZ → TON</button>
        <button class="btn" onclick="buyZZ()" style="margin-top:6px;">💎 Купить ZZ за TON</button>
    </div>

    <!-- ===== АДМИНКА ===== -->
    <div id="page-admin" class="page">
        <h3 style="color:#ff3366;">👑 Админ</h3>
        <div class="card" style="border-color:#ff3366;">
            <h4>⚙️ Игрок по ID</h4>
            <input type="text" id="a-id" class="input-field" placeholder="Telegram ID">
            <input type="number" id="a-zz" class="input-field" placeholder="Coin ZZ (+/-)">
            <input type="number" id="a-ton" class="input-field" placeholder="TON (+/-)" step="0.01">
            <button class="btn red" onclick="adminBalance()">💾 Применить</button>
        </div>
        <div class="card" style="border-color:#ff3366;">
            <h4>🎁 Промокод</h4>
            <input type="text" id="p-code" class="input-field" placeholder="Код">
            <input type="number" id="p-reward" class="input-field" placeholder="Награда ZZ">
            <input type="number" id="p-max" class="input-field" placeholder="Активаций">
            <button class="btn purple" onclick="createPromo()">Создать</button>
        </div>
        <div class="card" style="border-color:#ff3366;">
            <h4>📋 Задания на проверке</h4>
            <div id="admin-tasks"></div>
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

<script>
    const tg = window.Telegram.WebApp;
    tg.expand();
    const userId = tg.initDataUnsafe?.user?.id || "Гость";
    document.getElementById('user-id').innerText = userId;
    document.getElementById('profile-id').innerText = userId;
    const ADMIN_ID = 8684827145;
    const WALLET = "UQDmNY1TIMIgnALOpAyJ4_XO2uroUNLFVRwGie5AEwzccaps";

    if (Number(userId) === ADMIN_ID) {
        document.getElementById('nav-admin').style.display = 'block';
    }

    // Данные
    let zz = 50000, ton = 0.75, refs = 3, refZZ = 3000, rate = 1000000, totalActions = 15000000;
    let pendingTasks = [
        { id:1, type:'📢 Канал', link:'t.me/test1', amount:500, cost:0.5 },
        { id:2, type:'💬 Чат', link:'t.me/test2', amount:1000, cost:1.0 }
    ];
    let activeTasks = [
        { type:'channel', name:'Канал 1', link:'t.me/ch1' },
        { type:'channel', name:'Канал 2', link:'t.me/ch2' },
        { type:'channel', name:'Канал 3', link:'t.me/ch3' },
        { type:'chat', name:'Чат 1', link:'t.me/chat1' },
        { type:'chat', name:'Чат 2', link:'t.me/chat2' },
        { type:'chat', name:'Чат 3', link:'t.me/chat3' },
        { type:'bot', name:'Бот 1', link:'t.me/bot1' },
        { type:'bot', name:'Бот 2', link:'t.me/bot2' },
        { type:'bot', name:'Бот 3', link:'t.me/bot3' }
    ];

    function updateUI() {
        document.getElementById('bal-zz').innerText = zz.toLocaleString();
        document.getElementById('bal-ton').innerText = ton.toFixed(2);
        document.getElementById('ref-count').innerText = refs;
        document.getElementById('ref-earned').innerText = refZZ.toLocaleString() + ' ZZ';
        rate = Math.max(500000, 1000000 - Math.floor(totalActions / 10000));
        document.getElementById('rate').innerText = rate.toLocaleString();
        renderTasks();
        renderAdminTasks();
    }

    function renderTasks() {
        ['channels','chats','bots'].forEach(cat => {
            const type = cat === 'channels' ? 'channel' : cat === 'chats' ? 'chat' : 'bot';
            const container = document.getElementById('tasks-' + cat);
            container.innerHTML = activeTasks.filter(t => t.type === type).map(t =>
                `<div class="task-row">
                    <div><b>${t.name}</b><br><small style="color:#8892b0;">${t.link}</small></div>
                    <div style="text-align:right;">
                        <span style="color:#00ffff;">+1 000 ZZ</span><br>
                        <button class="btn small" onclick="doTask('${t.link}')">✅ Выполнить</button>
                    </div>
                </div>`
            ).join('');
        });
    }

    function renderAdminTasks() {
        const box = document.getElementById('admin-tasks');
        box.innerHTML = pendingTasks.map(t =>
            `<div class="task-row">
                <div><b>${t.type}</b><br><small>${t.link} • ${t.amount} вып. • ${t.cost} TON</small></div>
                <div>
                    <button class="btn small green" onclick="approveTask(${t.id})">✅</button>
                    <button class="btn small red" onclick="rejectTask(${t.id})">❌</button>
                </div>
            </div>`
        ).join('') || '<p style="color:#8892b0;">Нет заданий на проверке</p>';
    }

    function doTask(link) {
        // Открываем ссылку, бот проверит подписку
        tg.openTelegramLink('https://' + link);
        // Имитация: бот проверил подписку и начислил
        setTimeout(() => {
            zz += 1000;
            totalActions += 1000;
            updateUI();
            alert('✅ Задание выполнено! +1 000 Coin ZZ');
        }, 2000);
    }

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

    function calcCost() {
        const a = parseInt(document.getElementById('ad-amount').value) || 500;
        document.getElementById('ad-cost').innerText = (a / 1000).toFixed(2) + ' TON';
    }

    function submitAd() {
        const link = document.getElementById('ad-link').value;
        if (!link.startsWith('https://t.me/')) { alert('Введи ссылку Telegram!'); return; }
        const amount = parseInt(document.getElementById('ad-amount').value);
        const cost = amount / 1000;
        if (ton < cost) { alert('Недостаточно TON!'); return; }
        ton -= cost;
        pendingTasks.push({ id: Date.now(), type: document.getElementById('ad-type').value === 'channel' ? '📢 Канал' : document.getElementById('ad-type').value === 'chat' ? '💬 Чат' : '🤖 Бот', link: link.replace('https://',''), amount, cost });
        updateUI();
        alert('✅ Отправлено на проверку!');
    }

    function approveTask(id) {
        const t = pendingTasks.find(t => t.id === id);
        if (t) {
            activeTasks.push({ type: t.type.includes('Канал') ? 'channel' : t.type.includes('Чат') ? 'chat' : 'bot', name: t.link.split('/')[1] || 'Новый', link: t.link });
            pendingTasks = pendingTasks.filter(t => t.id !== id);
            updateUI();
        }
    }

    function rejectTask(id) {
        pendingTasks = pendingTasks.filter(t => t.id !== id);
        updateUI();
    }

    function copyWallet() { navigator.clipboard.writeText(WALLET); alert('✅ Скопировано!'); }
    function copyRef() { navigator.clipboard.writeText(document.getElementById('ref-link').value); alert('✅ Скопировано!'); }

    function withdraw() {
        const amt = parseFloat(document.getElementById('w-amount').value);
        const wal = document.getElementById('w-wallet').value.trim();
        if (isNaN(amt) || amt < 0.5) { alert('Мин. 0.5 TON'); return; }
        if (amt > ton) { alert('Недостаточно TON'); return; }
        if (!wal.startsWith('UQ')) { alert('Неверный адрес'); return; }
        ton -= amt;
        updateUI();
        alert('✅ Заявка на вывод ' + amt.toFixed(2) + ' TON отправлена!');
    }

    function calcSwap() {
        const z = parseInt(document.getElementById('swap-zz').value) || 1000000;
        document.getElementById('swap-ton').innerText = (z / rate).toFixed(2);
    }

    function sellZZ() {
        const z = parseInt(document.getElementById('swap-zz').value);
        if (isNaN(z) || z < 1000000 || z > zz) { alert('Недостаточно ZZ или меньше 1 млн'); return; }
        const t = z / rate;
        zz -= z; ton += t; totalActions += z;
        updateUI();
        alert('✅ Продано ' + z.toLocaleString() + ' ZZ за ' + t.toFixed(2) + ' TON');
    }

    function buyZZ() {
        const z = parseInt(document.getElementById('swap-zz').value);
        if (isNaN(z) || z < 1000000) { alert('Мин. 1 млн ZZ'); return; }
        const t = z / rate;
        if (t > ton) { alert('Недостаточно TON'); return; }
        ton -= t; zz += z; totalActions += z;
        updateUI();
        alert('✅ Куплено ' + z.toLocaleString() + ' ZZ за ' + t.toFixed(2) + ' TON');
    }

    function openPromo() {
        const code = prompt('🎁 Промокод:');
        if (code) { tg.sendData(JSON.stringify({action:'promo',code})); alert('✅ Отправлен!'); }
    }

    function adminBalance() {
        const id = document.getElementById('a-id').value;
        const dz = parseInt(document.getElementById('a-zz').value) || 0;
        const dt = parseFloat(document.getElementById('a-ton').value) || 0;
        if (!id) { alert('Введи ID'); return; }
        alert('✅ Игрок ' + id + ': ZZ ' + (dz>=0?'+':'') + dz + ', TON ' + (dt>=0?'+':'') + dt.toFixed(2));
    }

    function createPromo() {
        const c = document.getElementById('p-code').value.trim();
        if (c.length < 4) { alert('Код от 4 символов'); return; }
        alert('🎁 Промокод "' + c + '" создан!');
    }

    updateUI();
</script>
</body>
</html>
