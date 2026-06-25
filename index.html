<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>ZZ Task Bot</title>
    <script src="https://telegram.org/js/telegram-web-app.js"></script>
    <style>
        :root {
            --bg: #06080c; --card: #11151c; --border: #1f2633;
            --cyan: #00e0ff; --green: #00e676; --red: #ff1744;
            --gold: #ffc107; --text: #e8eaed; --sub: #8b90a0;
        }
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body {
            background: var(--bg); color: var(--text);
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            user-select: none; overflow-x: hidden; font-size: 14px;
        }
        .container { padding: 14px; padding-bottom: 90px; }

        /* Шапка */
        .header {
            display: flex; justify-content: space-between; align-items: center;
            margin-bottom: 12px;
        }
        .id-badge {
            background: var(--card); padding: 8px 14px; border-radius: 20px;
            font-size: 11px; color: var(--sub); border: 1px solid var(--border);
        }
        .id-badge span { color: var(--cyan); font-weight: 700; }
        .promo-btn {
            width: 40px; height: 40px; border-radius: 50%; border: none;
            background: linear-gradient(135deg, #ff6d00, #ff9100);
            font-size: 18px; cursor: pointer;
        }

        /* Карточки */
        .card {
            background: var(--card); border: 1px solid var(--border);
            border-radius: 14px; padding: 14px; margin-bottom: 10px;
        }

        /* Баланс */
        .balance-row { display: flex; gap: 8px; margin-bottom: 12px; }
        .bal-item {
            flex: 1; background: var(--card); border: 1px solid var(--border);
            border-radius: 14px; padding: 12px; text-align: center;
        }
        .bal-item .lbl { font-size: 10px; color: var(--sub); text-transform: uppercase; letter-spacing: 1px; }
        .bal-item .val { font-size: 20px; font-weight: 700; }
        .val.zz { color: var(--cyan); }
        .val.ton { color: var(--green); }

        .page { display: none; }
        .page.active { display: block; }

        /* Табы */
        .tabs { display: flex; gap: 6px; margin-bottom: 12px; }
        .tab {
            flex: 1; padding: 10px 6px; text-align: center; background: var(--card);
            border: 1px solid var(--border); border-radius: 20px; cursor: pointer;
            font-weight: 600; font-size: 11px; color: var(--sub); transition: 0.2s;
        }
        .tab.active { background: var(--cyan); color: #000; border-color: var(--cyan); }
        .sub-page { display: none; }
        .sub-page.active { display: block; }

        /* Навбар */
        .nav-bar {
            position: fixed; bottom: 0; left: 0; right: 0; height: 68px;
            background: #0d1017; border-top: 1px solid var(--border);
            display: flex; justify-content: space-around; align-items: center; z-index: 1000;
        }
        .nav-item { color: var(--sub); font-size: 9px; text-align: center; cursor: pointer; flex: 1; }
        .nav-item.active { color: var(--cyan); }
        .nav-ic { font-size: 18px; margin-bottom: 2px; }

        /* Кнопки */
        .btn {
            background: var(--cyan); color: #000; border: none; padding: 11px;
            border-radius: 22px; width: 100%; font-weight: 700; font-size: 13px;
            margin-top: 6px; cursor: pointer; transition: 0.15s;
        }
        .btn:active { transform: scale(0.97); opacity: 0.8; }
        .btn.gr { background: var(--green); color: #000; }
        .btn.rd { background: var(--red); color: #fff; }
        .btn.gd { background: var(--gold); color: #000; }
        .btn.ol { background: transparent; border: 2px solid var(--cyan); color: var(--cyan); }
        .btn.sm { padding: 6px 12px; font-size: 11px; width: auto; margin: 2px; }

        /* Инпуты */
        .inp {
            width: 100%; padding: 10px 14px; background: #080b10;
            border: 1px solid var(--border); border-radius: 20px; color: #fff;
            margin-top: 5px; font-size: 13px; outline: none;
        }
        .inp:focus { border-color: var(--cyan); }
        label { display: block; margin-top: 10px; font-size: 11px; color: var(--sub); font-weight: 500; }

        /* Задания */
        .task-row {
            display: flex; justify-content: space-between; align-items: center;
            padding: 12px; background: #080b10; border-radius: 12px; margin-bottom: 8px;
            gap: 8px;
        }
        .badge {
            padding: 3px 10px; border-radius: 15px; font-size: 10px; font-weight: 700;
        }
        .badge-y { background: rgba(255,193,7,0.2); color: var(--gold); }
        .badge-g { background: rgba(0,230,118,0.2); color: var(--green); }
        .badge-r { background: rgba(255,23,68,0.2); color: var(--red); }

        .wallet-box {
            background: #080b10; border: 1px dashed var(--cyan); border-radius: 12px;
            padding: 10px; word-break: break-all; font-size: 10px; color: var(--cyan);
            text-align: center; margin: 8px 0;
        }

        .chart-wrap {
            background: #080b10; border-radius: 12px; padding: 6px; margin: 10px 0; height: 170px;
        }
        canvas { width: 100% !important; height: 100% !important; }
        .pct-big { font-size: 16px; font-weight: 700; padding: 4px 10px; border-radius: 15px; }
        .pct-up { color: var(--green); background: rgba(0,230,118,0.12); }
        .pct-down { color: var(--red); background: rgba(255,23,68,0.12); }

        .empty { text-align: center; padding: 24px; color: var(--sub); }
        .empty .ic { font-size: 32px; margin-bottom: 6px; }
    </style>
</head>
<body>

<div class="container">
    <!-- Шапка -->
    <div class="header">
        <div class="id-badge">🆔 <span id="uid">...</span></div>
        <button class="promo-btn" onclick="promoOpen()">🎁</button>
    </div>

    <!-- Баланс -->
    <div class="balance-row">
        <div class="bal-item"><div class="lbl">Coin ZZ</div><div class="val zz" id="b-zz">0</div></div>
        <div class="bal-item"><div class="lbl">TON</div><div class="val ton" id="b-ton">0.00</div></div>
    </div>

    <!-- ===== ЗАДАНИЯ ===== -->
    <div id="page-tasks" class="page active">
        <div class="tabs">
            <div class="tab active" onclick="subTab('channels', this)">📢 Каналы</div>
            <div class="tab" onclick="subTab('chats', this)">💬 Чаты</div>
            <div class="tab" onclick="subTab('bots', this)">🤖 Боты</div>
        </div>
        <div id="sub-channels" class="sub-page active"><div id="tasks-channels"></div></div>
        <div id="sub-chats" class="sub-page"><div id="tasks-chats"></div></div>
        <div id="sub-bots" class="sub-page"><div id="tasks-bots"></div></div>
    </div>

    <!-- ===== СОЗДАТЬ РЕКЛАМУ ===== -->
    <div id="page-create" class="page">
        <h3>📣 Создать задание</h3>
        <label>Тип:</label>
        <select id="ad-type" class="inp">
            <option value="channel">📢 Канал</option>
            <option value="chat">💬 Чат</option>
            <option value="bot">🤖 Бот</option>
        </select>
        <label>Ссылка (t.me/...):</label>
        <input type="text" id="ad-link" class="inp" placeholder="t.me/your_channel">
        <label>Выполнений (мин. 500):</label>
        <input type="number" id="ad-amount" class="inp" value="500" min="500" oninput="adCalc()">
        <div class="card" style="text-align:center;">
            💎 К оплате: <b id="ad-cost" style="color:var(--green);">0.50 TON</b>
        </div>
        <button class="btn gr" onclick="adSubmit()">💎 Оплатить и отправить</button>
        <p style="font-size:10px; color:var(--gold); margin-top:6px;">Уйдёт на проверку админу</p>
    </div>

    <!-- ===== ПРОФИЛЬ ===== -->
    <div id="page-profile" class="page">
        <h3>👤 Профиль</h3>
        <div class="card" style="text-align:center;">
            <div style="font-size:12px; color:var(--sub);">Мой баланс</div>
            <div style="font-size:26px; font-weight:700; color:var(--cyan); margin:4px 0;"><span id="p-zz">0</span> ZZ</div>
            <div style="font-size:20px; color:var(--green); font-weight:600;"><span id="p-ton">0.00</span> TON</div>
        </div>

        <h4 style="margin-top:14px;">💎 Пополнение TON</h4>
        <div class="wallet-box">UQDmNY1TIMIgnALOpAyJ4_XO2uroUNLFVRwGie5AEwzccaps</div>
        <button class="btn ol" onclick="copyWallet()">📋 Копировать адрес</button>
        <p style="font-size:10px; color:var(--gold); margin-top:4px;">В комментарии: ID <span id="p-uid">...</span></p>

        <h4 style="margin-top:16px;">💸 Вывод TON</h4>
        <p style="font-size:11px; color:var(--sub);">Мин. 0.5 TON</p>
        <input type="number" id="w-amount" class="inp" placeholder="Сумма" min="0.5" step="0.1">
        <input type="text" id="w-wallet" class="inp" placeholder="Твой кошелёк UQ...">
        <button class="btn rd" onclick="withdraw()">💸 Вывести TON</button>
    </div>

    <!-- ===== РЕФЕРАЛЫ ===== -->
    <div id="page-refs" class="page">
        <h3>👥 Рефералы</h3>
        <div class="card" style="text-align:center;">
            <div style="font-size:40px;">👥</div>
            <p>+<b style="color:var(--cyan);">1 000 ZZ</b> за друга</p>
        </div>
        <input type="text" id="ref-link" class="inp" readonly>
        <button class="btn ol" onclick="copyRef()">📋 Копировать</button>
        <div class="balance-row" style="margin-top:10px;">
            <div class="bal-item"><div class="lbl">Приглашено</div><div class="val zz" id="r-count">0</div></div>
            <div class="bal-item"><div class="lbl">Заработано</div><div class="val ton" id="r-zz">0 ZZ</div></div>
        </div>
    </div>

    <!-- ===== БИРЖА ===== -->
    <div id="page-exchange" class="page">
        <h3>📈 Биржа ZZ</h3>
        <div class="card" style="text-align:center;">
            <div style="font-size:11px; color:var(--sub);">Курс</div>
            <div style="font-size:22px; font-weight:700; color:var(--cyan);"><span id="rate">1 000 000</span> ZZ = 1 TON</div>
            <span class="pct-big" id="pct-badge" style="font-size:14px;">0%</span>
        </div>
        <div class="chart-wrap"><canvas id="chart"></canvas></div>
        <label>Количество ZZ (мин. 1 млн):</label>
        <input type="number" id="swap-zz" class="inp" value="1000000" min="1000000" oninput="swapCalc()">
        <div style="text-align:center; margin:6px 0; font-weight:600;">= <span id="swap-ton" style="color:var(--green);">1.00</span> TON</div>
        <div style="display:flex; gap:8px;">
            <button class="btn gr" style="flex:1;" onclick="sellZZ()">💰 Продать ZZ</button>
            <button class="btn gd" style="flex:1;" onclick="buyZZ()">💎 Купить ZZ</button>
        </div>
    </div>

    <!-- ===== АДМИН ===== -->
    <div id="page-admin" class="page">
        <h3 style="color:var(--red);">👑 Админ</h3>
        <div class="card" style="border-color:var(--red);">
            <h4>⚙️ Игрок</h4>
            <input type="text" id="a-id" class="inp" placeholder="ID">
            <input type="number" id="a-zz" class="inp" placeholder="ZZ +\-">
            <input type="number" id="a-ton" class="inp" placeholder="TON +\-" step="0.01">
            <button class="btn rd" onclick="adminSet()">💾 Применить</button>
        </div>
        <div class="card" style="border-color:var(--red);">
            <h4>🎁 Промокод</h4>
            <input type="text" id="p-code" class="inp" placeholder="Код">
            <input type="number" id="p-rw" class="inp" placeholder="Награда ZZ">
            <input type="number" id="p-max" class="inp" placeholder="Активаций">
            <button class="btn gd" onclick="promoCreate()">Создать</button>
        </div>
        <div class="card" style="border-color:var(--red);">
            <h4>📋 Проверка</h4>
            <div id="admin-tasks"></div>
        </div>
        <div class="card" style="border-color:var(--red);">
            <h4>🎁 Промокоды</h4>
            <div id="promo-list"></div>
            <button class="btn rd sm" onclick="promoClear()">🗑 Очистить</button>
        </div>
    </div>
</div>

<!-- МЕНЮ -->
<div class="nav-bar">
    <div class="nav-item active" onclick="navGo('tasks', this)"><div class="nav-ic">📋</div>Задания</div>
    <div class="nav-item" onclick="navGo('create', this)"><div class="nav-ic">📣</div>Реклама</div>
    <div class="nav-item" onclick="navGo('profile', this)"><div class="nav-ic">👤</div>Профиль</div>
    <div class="nav-item" onclick="navGo('refs', this)"><div class="nav-ic">👥</div>Рефералы</div>
    <div class="nav-item" onclick="navGo('exchange', this)"><div class="nav-ic">📈</div>Биржа</div>
    <div class="nav-item" id="nav-adm" style="display:none;" onclick="navGo('admin', this)"><div class="nav-ic">👑</div>Админ</div>
</div>

<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script>
    const tg = window.Telegram.WebApp;
    tg.expand();
    const uid = tg.initDataUnsafe?.user?.id || Math.floor(Math.random()*1e6);
    document.getElementById('uid').innerText = uid;
    document.getElementById('p-uid').innerText = uid;
    document.getElementById('ref-link').value = 'https://t.me/bot?start=ref_'+uid;
    const ADM = 8684827145;
    if (Number(uid)===ADM) document.getElementById('nav-adm').style.display='block';

    // === ДАННЫЕ ===
    function load(){ return JSON.parse(localStorage.getItem('zzdata')||'{}'); }
    function save(d){ localStorage.setItem('zzdata',JSON.stringify(d)); }
    let D = load();
    if(!D.usr) D.usr={};
    if(!D.pend) D.pend=[];
    if(!D.acts) D.acts=[];
    if(!D.promo) D.promo=[];
    if(!D.hist) D.hist=[1000000,1003000,1001000,998000,1000000,1004000,1002000,1005000,1000000,998000];
    if(!D.total) D.total=0;
    if(!D.usr[uid]) D.usr[uid]={zz:0,ton:0,refs:0,refZZ:0,done:[],usedPromo:[]};
    let U = D.usr[uid];
    let rate = 1000000;

    function saveAll(){ D.usr[uid]=U; save(D); update(); }

    function update(){
        document.getElementById('b-zz').innerText = U.zz.toLocaleString();
        document.getElementById('b-ton').innerText = U.ton.toFixed(2);
        document.getElementById('p-zz').innerText = U.zz.toLocaleString();
        document.getElementById('p-ton').innerText = U.ton.toFixed(2);
        document.getElementById('r-count').innerText = U.refs;
        document.getElementById('r-zz').innerText = U.refZZ.toLocaleString()+' ZZ';

        rate = Math.max(300000, 1000000 - Math.floor(D.total/8000));
        document.getElementById('rate').innerText = rate.toLocaleString();

        const prev = D.hist[D.hist.length-2]||rate;
        const pct = ((rate-prev)/prev*100).toFixed(1);
        const b = document.getElementById('pct-badge');
        b.innerText = (pct>=0?'+':'')+pct+'%';
        b.className = 'pct-big '+(pct>=0?'pct-up':'pct-down');

        renderTasks();
        renderAdmin();
        renderPromos();
        drawChart();
    }

    // === ЗАДАНИЯ ===
    function renderTasks(){
        ['channels','chats','bots'].forEach(cat=>{
            const type = cat==='channels'?'channel':cat==='chats'?'chat':'bot';
            const box = document.getElementById('tasks-'+cat);
            const tasks = D.acts.filter(t=>t.type===type);
            if(!tasks.length){
                box.innerHTML = '<div class="empty"><div class="ic">📭</div>Нет заданий</div>';
            }else{
                box.innerHTML = tasks.map(t=>{
                    const done = U.done.includes(t.id);
                    return `<div class="task-row">
                        <div><b>${t.name}</b><br><small style="color:var(--sub);">${t.link}</small></div>
                        <div style="text-align:right;">
                            <span style="color:var(--cyan);font-weight:600;">+1 000 ZZ</span><br>
                            ${done?'<span class="badge badge-g">✅ Готово</span>':`<button class="btn sm" onclick="doTask('${t.id}')">✅</button>`}
                        </div>
                    </div>`;
                }).join('');
            }
        });
    }

    function doTask(id){
        if(U.done.includes(id)) return;
        const t = D.acts.find(t=>t.id===id);
        if(!t) return;
        tg.openTelegramLink('https://'+t.link);
        U.done.push(id);
        U.zz += 1000;
        D.total += 1000;
        D.hist.push(rate);
        if(D.hist.length>40) D.hist.shift();
        saveAll();
        setTimeout(()=>alert('✅ +1 000 Coin ZZ!'),1500);
    }

    // === АДМИН ПРОВЕРКА ===
    function renderAdmin(){
        const box = document.getElementById('admin-tasks');
        if(!box) return;
        const pend = D.pend.filter(t=>!t.done);
        if(!pend.length){
            box.innerHTML = '<p style="color:var(--sub);text-align:center;padding:10px;">Нет на проверке</p>';
        }else{
            box.innerHTML = pend.map(t=>
                `<div class="task-row">
                    <div><b>${t.type==='channel'?'📢':t.type==='chat'?'💬':'🤖'} ${t.link}</b><br>
                    <small>${t.amt} вып. • ${t.cost} TON • от ${t.creator}</small></div>
                    <div>
                        <button class="btn sm gr" onclick="admApprove(${t.id})">✅</button>
                        <button class="btn sm rd" onclick="admReject(${t.id})">❌</button>
                    </div>
                </div>`
            ).join('');
        }
    }

    function admApprove(id){
        const t = D.pend.find(t=>t.id===id);
        if(t){ t.done=true; D.acts.push({id:t.id, type:t.type, name:t.link.split('/')[1]||'Канал', link:t.link}); saveAll(); }
    }
    function admReject(id){
        D.pend = D.pend.filter(t=>t.id!==id);
        saveAll();
    }

    // === СОЗДАТЬ РЕКЛАМУ ===
    function adCalc(){
        const a = parseInt(document.getElementById('ad-amount').value)||500;
        document.getElementById('ad-cost').innerText = (a/1000).toFixed(2)+' TON';
    }
    function adSubmit(){
        const link = document.getElementById('ad-link').value.trim();
        if(!link.startsWith('t.me/')){ alert('Ссылка: t.me/...'); return; }
        const amt = parseInt(document.getElementById('ad-amount').value);
        const cost = amt/1000;
        if(U.ton < cost){ alert('Недостаточно TON!'); return; }
        U.ton -= cost;
        D.pend.push({id:Date.now(), type:document.getElementById('ad-type').value, link, amt, cost, creator:uid, done:false});
        saveAll();
        alert('✅ Отправлено!');
    }

    // === ПРОМОКОДЫ ===
    function promoCreate(){
        const code = document.getElementById('p-code').value.trim().toUpperCase();
        const rw = parseInt(document.getElementById('p-rw').value);
        const max = parseInt(document.getElementById('p-max').value);
        if(!code||code.length<3) return alert('Код от 3 символов');
        if(!rw||rw<=0) return alert('Введи награду');
        if(!max||max<=0) return alert('Введи макс. активаций');
        if(D.promo.find(p=>p.code===code)) return alert('Такой код уже есть');
        D.promo.push({code,reward:rw,maxUses:max,used:[]});
        saveAll();
        document.getElementById('p-code').value='';
        document.getElementById('p-rw').value='';
        document.getElementById('p-max').value='';
        alert('🎁 Промокод '+code+' создан!');
    }
    function renderPromos(){
        const box = document.getElementById('promo-list');
        if(!box) return;
        if(!D.promo.length) box.innerHTML = '<p style="color:var(--sub);text-align:center;">Нет</p>';
        else box.innerHTML = D.promo.map(p=>
            `<div class="task-row">
                <div><b>🎁 ${p.code}</b><br><small>+${p.reward} ZZ • ${p.used.length}/${p.maxUses}</small></div>
                <button class="btn sm rd" onclick="promoDel('${p.code}')">🗑</button>
            </div>`
        ).join('');
    }
    function promoDel(code){ D.promo = D.promo.filter(p=>p.code!==code); saveAll(); }
    function promoClear(){ if(confirm('Удалить все?')){ D.promo=[]; saveAll(); } }
    function promoOpen(){
        const code = prompt('🎁 Промокод:');
        if(!code) return;
        const p = D.promo.find(p=>p.code===code.toUpperCase());
        if(!p) return alert('❌ Не найден');
        if(p.used.includes(uid)) return alert('⚠️ Уже использован');
        if(p.used.length >= p.maxUses) return alert('⚠️ Закончился');
        p.used.push(uid);
        U.zz += p.reward;
        saveAll();
        alert('🎁 +'+p.reward+' ZZ!');
    }

    // === АДМИН БАЛАНС ===
    function adminSet(){
        const id = document.getElementById('a-id').value.trim();
        const dz = parseInt(document.getElementById('a-zz').value)||0;
        const dt = parseFloat(document.getElementById('a-ton').value)||0;
        if(!id) return alert('Введи ID');
        if(!D.usr[id]) D.usr[id] = {zz:0,ton:0,refs:0,refZZ:0,done:[],usedPromo:[]};
        D.usr[id].zz += dz;
        D.usr[id].ton += dt;
        if(Number(id)===Number(uid)) U = D.usr[id];
        saveAll();
        document.getElementById('a-id').value='';
        document.getElementById('a-zz').value='';
        document.getElementById('a-ton').value='';
        alert('✅ Баланс '+id+' обновлён!');
    }

    // === БИРЖА (цена растёт/падает) ===
    function swapCalc(){
        const z = parseInt(document.getElementById('swap-zz').value)||1000000;
        document.getElementById('swap-ton').innerText = (z/rate).toFixed(4);
    }
    function sellZZ(){
        const z = parseInt(document.getElementById('swap-zz').value);
        if(isNaN(z)||z<1000000||z>U.zz) return alert('Мин. 1 млн или не хватает');
        const t = z/rate;
        U.zz -= z; U.ton += t;
        D.total -= z; // продажа снижает total -> курс падает
        D.hist.push(rate);
        if(D.hist.length>40) D.hist.shift();
        saveAll();
        alert('✅ Продано '+z.toLocaleString()+' ZZ за '+t.toFixed(4)+' TON');
    }
    function buyZZ(){
        const z = parseInt(document.getElementById('swap-zz').value);
        if(isNaN(z)||z<1000000) return alert('Мин. 1 млн');
        const t = z/rate;
        if(t>U.ton) return alert('Не хватает TON');
        U.ton -= t; U.zz += z;
        D.total += z; // покупка повышает total -> курс растёт
        D.hist.push(rate);
        if(D.hist.length>40) D.hist.shift();
        saveAll();
        alert('✅ Куплено '+z.toLocaleString()+' ZZ за '+t.toFixed(4)+' TON');
    }

    // === ГРАФИК ===
    let chart;
    function drawChart(){
        const ctx = document.getElementById('chart');
        if(!ctx) return;
        if(chart) chart.destroy();
        chart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: D.hist.map(()=>''),
                datasets: [{
                    data: D.hist,
                    borderColor: '#00e0ff',
                    backgroundColor: 'rgba(0,224,255,0.08)',
                    fill: true, tension: 0.4, pointRadius: 0, borderWidth: 2
                }]
            },
            options: {
                responsive: true, maintainAspectRatio: false,
                plugins: { legend: { display: false } },
                scales: { x: { display: false }, y: { display: false } }
            }
        });
    }

    // === ВЫВОД ===
    function withdraw(){
        const amt = parseFloat(document.getElementById('w-amount').value);
        const wal = document.getElementById('w-wallet').value.trim();
        if(isNaN(amt)||amt<0.5) return alert('Мин. 0.5 TON');
        if(amt>U.ton) return alert('Не хватает');
        if(!wal.startsWith('UQ')) return alert('Адрес должен начинаться с UQ');
        U.ton -= amt;
        saveAll();
        document.getElementById('w-amount').value='';
        document.getElementById('w-wallet').value='';
        alert('✅ Вывод '+amt.toFixed(2)+' TON');
    }

    // === НАВИГАЦИЯ ===
    function subTab(t,el){
        document.querySelectorAll('.tab').forEach(x=>x.classList.remove('active'));
        document.querySelectorAll('.sub-page').forEach(x=>x.classList.remove('active'));
        el.classList.add('active');
        document.getElementById('sub-'+t).classList.add('active');
    }
    function navGo(id,el){
        document.querySelectorAll('.page').forEach(x=>x.classList.remove('active'));
        document.querySelectorAll('.nav-item').forEach(x=>x.classList.remove('active'));
        document.getElementById('page-'+id).classList.add('active');
        if(el) el.classList.add('active');
    }
    function copyWallet(){
        navigator.clipboard.writeText('UQDmNY1TIMIgnALOpAyJ4_XO2uroUNLFVRwGie5AEwzccaps');
        alert('✅ Скопировано!');
    }
    function copyRef(){
        navigator.clipboard.writeText(document.getElementById('ref-link').value);
        alert('✅ Скопировано!');
    }

    update();
</script>
</body>
</html>
