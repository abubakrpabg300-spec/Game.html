<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Click & Earn</title>
    <script src="https://telegram.org/js/telegram-web-app.js"></script>
    <style>
        :root {
            --bg: #0a0a14;
            --card: #12122a;
            --border: #1e1e3a;
            --purple: #7c3aed;
            --gold: #ffc107;
            --green: #00e676;
            --cyan: #00e5ff;
            --red: #ff1744;
            --text: #e0e0e0;
            --sub: #9ca3af;
        }
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body {
            background: var(--bg); color: var(--text);
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            user-select: none; overflow-x: hidden; font-size: 13px;
        }
        .container { padding: 10px; padding-bottom: 80px; }

        .header {
            display: flex; justify-content: space-between; align-items: center;
            margin-bottom: 8px;
        }
        .id-badge {
            background: var(--card); padding: 6px 12px; border-radius: 16px;
            font-size: 10px; color: var(--sub); border: 1px solid var(--border);
        }
        .id-badge span { color: var(--cyan); font-weight: 700; }
        .promo-btn {
            width: 34px; height: 34px; border-radius: 50%; border: none;
            background: var(--purple); font-size: 15px; cursor: pointer; color: #fff;
        }

        .bal-row { display: flex; gap: 6px; margin-bottom: 8px; }
        .bal-item {
            flex: 1; background: var(--card); border: 1px solid var(--border);
            border-radius: 10px; padding: 8px; text-align: center;
        }
        .bal-item .lbl { font-size: 9px; color: var(--sub); text-transform: uppercase; }
        .bal-item .val { font-size: 16px; font-weight: 700; }
        .val.gms { color: var(--gold); }
        .val.ton { color: var(--green); }

        .page { display: none; }
        .page.active { display: block; }

        .card {
            background: var(--card); border: 1px solid var(--border);
            border-radius: 10px; padding: 10px; margin-bottom: 6px;
        }
        .card.purple { border-color: var(--purple); }

        .nav-bar {
            position: fixed; bottom: 0; left: 0; right: 0; height: 60px;
            background: #0d0d20; border-top: 1px solid var(--border);
            display: flex; overflow-x: auto; z-index: 1000;
        }
        .nav-item {
            color: var(--sub); font-size: 8px; text-align: center;
            cursor: pointer; flex: 1; min-width: 45px; padding: 5px 1px;
        }
        .nav-item.active { color: var(--purple); }
        .nav-ic { font-size: 15px; margin-bottom: 1px; }

        .btn {
            background: var(--purple); color: #fff; border: none; padding: 9px;
            border-radius: 18px; width: 100%; font-weight: 700; font-size: 11px;
            margin-top: 4px; cursor: pointer; transition: 0.15s;
        }
        .btn:active { transform: scale(0.96); opacity: 0.8; }
        .btn.gr { background: var(--green); color: #000; }
        .btn.gd { background: var(--gold); color: #000; }
        .btn.cy { background: var(--cyan); color: #000; }
        .btn.rd { background: var(--red); }
        .btn.ol { background: transparent; border: 2px solid var(--purple); color: var(--purple); }
        .btn.sm { padding: 5px 10px; font-size: 10px; width: auto; margin: 2px; display: inline-block; }

        .inp {
            width: 100%; padding: 8px 10px; background: #0a0a1a;
            border: 1px solid var(--border); border-radius: 14px; color: #fff;
            margin-top: 3px; font-size: 11px; outline: none;
        }
        .inp:focus { border-color: var(--purple); }
        label { display: block; margin-top: 6px; font-size: 10px; color: var(--sub); font-weight: 500; }

        .click-btn {
            width: 140px; height: 140px; border-radius: 50%; border: 4px solid var(--purple);
            background: radial-gradient(circle, #1a1a40, #0a0a1a);
            margin: 15px auto; display: flex; align-items: center; justify-content: center;
            font-size: 14px; font-weight: 700; color: var(--gold); cursor: pointer;
            box-shadow: 0 0 30px rgba(124,58,237,0.4); transition: 0.1s;
            flex-direction: column;
        }
        .click-btn:active { transform: scale(0.9); box-shadow: 0 0 50px rgba(124,58,237,0.8); }

        .task-row {
            display: flex; justify-content: space-between; align-items: center;
            padding: 8px; background: #0a0a1a; border-radius: 8px; margin-bottom: 4px;
            gap: 6px; flex-wrap: wrap;
        }
        .badge {
            padding: 2px 7px; border-radius: 10px; font-size: 8px; font-weight: 700;
        }
        .badge-g { background: rgba(0,230,118,0.2); color: var(--green); }
        .badge-y { background: rgba(255,193,7,0.2); color: var(--gold); }

        .wallet-box {
            background: #0a0a1a; border: 1px dashed var(--gold); border-radius: 8px;
            padding: 7px; word-break: break-all; font-size: 8px; color: var(--gold);
            text-align: center; margin: 5px 0;
        }

        .chart-wrap {
            background: #0a0a1a; border-radius: 8px; padding: 3px; margin: 6px 0; height: 130px;
        }
        canvas { width: 100% !important; height: 100% !important; }
        .pct-big { font-size: 12px; font-weight: 700; padding: 2px 7px; border-radius: 10px; }
        .pct-up { color: var(--green); background: rgba(0,230,118,0.12); }
        .pct-down { color: var(--red); background: rgba(255,23,68,0.12); }

        .hp-bar { height: 6px; background: #222; border-radius: 3px; overflow: hidden; margin: 3px 0; }
        .hp-fill { height: 100%; background: var(--purple); }
        .plus-anim {
            position: fixed; pointer-events: none; color: var(--gold);
            font-weight: 700; font-size: 18px; animation: floatUp 0.8s forwards; z-index: 999;
        }
        @keyframes floatUp {
            0% { opacity: 1; transform: translateY(0); }
            100% { opacity: 0; transform: translateY(-80px); }
        }
    </style>
</head>
<body>

<div class="container">
    <div class="header">
        <div class="id-badge">🆔 <span id="uid">...</span></div>
        <button class="promo-btn" onclick="promoOpen()">🎁</button>
    </div>

    <div class="bal-row">
        <div class="bal-item"><div class="lbl">💎 GMS</div><div class="val gms" id="b-gms">0</div></div>
        <div class="bal-item"><div class="lbl">💰 TON</div><div class="val ton" id="b-ton">0.00</div></div>
    </div>

    <!-- КЛИКЕР -->
    <div id="page-clicker" class="page active" style="text-align:center;">
        <div class="click-btn" id="clickBtn" onclick="clickGMS(event)">
            <div style="font-size:30px;">💎</div>
            <div>НАЖМИ</div>
        </div>
        <div style="color:var(--cyan);">💪 +<span id="click-power">1</span> GMS за клик</div>
        <div style="color:var(--sub); font-size:10px;">🤖 Пассив: +<span id="passive-info">0</span> GMS</div>
        <div id="booster-info" style="color:var(--gold); font-size:10px; margin-top:3px;"></div>
        <div style="margin-top:8px; font-size:10px; color:var(--sub);">👆 Кликов: <span id="total-clicks">0</span></div>
    </div>

    <!-- УЛУЧШЕНИЯ -->
    <div id="page-upgrades" class="page">
        <h3>🏪 Улучшения</h3>
        <p style="font-size:10px; color:var(--sub);">💰 Твой TON: <b id="upg-ton">0.00</b></p>
        <div class="card"><h4>💪 Сила клика</h4><div id="upg-click"></div></div>
        <div class="card"><h4>🤖 Пассивный доход</h4><div id="upg-passive"></div></div>
        <div class="card"><h4>🔥 Бустеры</h4><div id="upg-boost"></div></div>
    </div>

    <!-- БИРЖА -->
    <div id="page-exchange" class="page">
        <h3>📈 Биржа GMS ↔ TON</h3>
        <div class="card" style="text-align:center;">
            <div style="font-size:10px; color:var(--sub);">Курс</div>
            <div style="font-size:18px; font-weight:700; color:var(--gold);"><span id="rate">1 000 000</span> GMS = 1 TON</div>
            <span class="pct-big" id="pct-badge">0%</span><br>
            <small style="color:var(--sub);">Комиссия: 5%</small>
        </div>
        <div class="chart-wrap"><canvas id="chart"></canvas></div>
        <label>GMS (мин. 100 000):</label>
        <input type="number" id="swap-gms" class="inp" value="100000" min="100000" oninput="swapCalc()">
        <div style="text-align:center; margin:4px 0;">= <span id="swap-ton" style="color:var(--green);">0.10</span> TON</div>
        <div style="display:flex; gap:5px;">
            <button class="btn gr" style="flex:1;" onclick="sellGMS()">💰 Продать</button>
            <button class="btn gd" style="flex:1;" onclick="buyGMS()">💎 Купить</button>
        </div>
    </div>

    <!-- БОНУСЫ -->
    <div id="page-bonus" class="page">
        <h3>🎁 Бонусы</h3>
        <div class="card"><h4>📅 Ежедневный бонус</h4><div id="daily-bonus"></div></div>
        <div class="card"><h4>🎁 Промокод</h4>
            <input type="text" id="promo-input" class="inp" placeholder="Введи код">
            <button class="btn gd" onclick="promoOpen()">Активировать</button>
        </div>
        <div class="card"><h4>💎 VIP Пак (за TON)</h4><div id="vip-packs"></div></div>
        <div class="card"><h4>📋 Задания</h4><div id="tasks-list"></div></div>
    </div>

    <!-- ПРОФИЛЬ -->
    <div id="page-profile" class="page">
        <h3>👤 Профиль</h3>
        <div class="card" style="text-align:center;">
            <div style="font-size:22px; font-weight:700; color:var(--gold);"><span id="p-gms">0</span> GMS</div>
            <div style="font-size:16px; color:var(--green);"><span id="p-ton">0.00</span> TON</div>
            <div style="font-size:10px; color:var(--sub);">👆 Кликов: <span id="p-clicks">0</span> | 💪 Сила: +<span id="p-power">1</span></div>
        </div>
        <h4>💎 Пополнение</h4>
        <p style="font-size:9px; color:var(--sub);">Мин: 0.1 TON = 100 000 GMS</p>
        <div class="wallet-box">UQDmNY1TIMIgnALOpAyJ4_XO2uroUNLFVRwGie5AEwzccaps</div>
        <button class="btn ol" onclick="copyWallet()">📋 Копировать</button>
        <p style="font-size:8px; color:var(--gold);">В комментарии: ID <span id="p-uid">...</span></p>
        <h4 style="margin-top:8px;">💸 Вывод TON</h4>
        <p style="font-size:9px; color:var(--sub);">Мин: 100 000 GMS | Комиссия 5%</p>
        <input type="number" id="w-amount" class="inp" placeholder="Сумма TON" min="0.01" step="0.01">
        <input type="text" id="w-wallet" class="inp" placeholder="Кошелёк UQ...">
        <button class="btn rd" onclick="withdraw()">💸 Вывести</button>
    </div>

    <!-- АДМИН -->
    <div id="page-admin" class="page">
        <h3 style="color:var(--purple);">👑 Админ</h3>
        <div class="card purple"><h4>⚙️ Игрок</h4>
            <input type="text" id="a-id" class="inp" placeholder="ID">
            <input type="number" id="a-gms" class="inp" placeholder="GMS +/-">
            <input type="number" id="a-ton" class="inp" placeholder="TON +/-">
            <button class="btn" onclick="adminSet()">💾 Применить</button>
        </div>
        <div class="card purple"><h4>🎁 Промокод</h4>
            <input type="text" id="pc-code" class="inp" placeholder="Код">
            <input type="number" id="pc-gms" class="inp" placeholder="GMS">
            <input type="number" id="pc-max" class="inp" placeholder="Активаций">
            <button class="btn gd" onclick="promoCreate()">Создать</button>
        </div>
        <div class="card purple"><h4>💎 VIP Пак</h4>
            <input type="text" id="vp-name" class="inp" placeholder="Название">
            <input type="number" id="vp-price" class="inp" placeholder="Цена TON">
            <input type="number" id="vp-gms" class="inp" placeholder="Даёт GMS">
            <button class="btn gd" onclick="vipAdd()">Добавить</button>
        </div>
        <div class="card purple"><h4>📋 Задание</h4>
            <select id="t-type" class="inp"><option value="channel">📢 Канал</option><option value="chat">💬 Чат</option><option value="bot">🤖 Бот</option></select>
            <input type="text" id="t-link" class="inp" placeholder="Ссылка t.me/...">
            <input type="number" id="t-gms" class="inp" placeholder="Награда GMS">
            <button class="btn gd" onclick="taskAdd()">Добавить</button>
        </div>
    </div>
</div>

<div class="nav-bar">
    <div class="nav-item active" onclick="navGo('clicker',this)"><div class="nav-ic">🎮</div>Кликер</div>
    <div class="nav-item" onclick="navGo('upgrades',this)"><div class="nav-ic">🏪</div>Улучш</div>
    <div class="nav-item" onclick="navGo('exchange',this)"><div class="nav-ic">📈</div>Биржа</div>
    <div class="nav-item" onclick="navGo('bonus',this)"><div class="nav-ic">🎁</div>Бонус</div>
    <div class="nav-item" onclick="navGo('profile',this)"><div class="nav-ic">👤</div>Проф</div>
    <div class="nav-item" id="nav-adm" style="display:none;" onclick="navGo('admin',this)"><div class="nav-ic">👑</div>Адм</div>
</div>

<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script>
    const tg = window.Telegram.WebApp;
    tg.expand();
    const uid = tg.initDataUnsafe?.user?.id || Math.floor(Math.random()*1e6);
    document.getElementById('uid').innerText = uid;
    document.getElementById('p-uid').innerText = uid;
    const ADM = 8684827145;
    const WALLET = "UQDmNY1TIMIgnALOpAyJ4_XO2uroUNLFVRwGie5AEwzccaps";
    if(Number(uid)===ADM) document.getElementById('nav-adm').style.display='block';

    function load(){ return JSON.parse(localStorage.getItem('clicker_data')||'{}'); }
    function save(d){ localStorage.setItem('clicker_data',JSON.stringify(d)); }
    let D = load();
    if(!D.usr) D.usr={};
    if(!D.tasks) D.tasks=[];
    if(!D.promo) D.promo=[];
    if(!D.vip) D.vip=[];
    if(!D.hist) D.hist=[1000000,1002000,998000,1005000,1010000,1000000];
    if(!D.total) D.total=0;
    if(!D.usr[uid]) D.usr[uid] = {
        gms:0, ton:0.5, clicks:0,
        clickLvl:0, passiveLvl:0,
        boosterMult:1, boosterEnd:0,
        done:[], usedPromo:[], dailyDay:0, dailyTime:0
    };
    let U = D.usr[uid];
    let rate = 1000000;
    const clickCosts = [0.1,0.5,1,2,5,10];
    const clickGains = [1,2,5,10,25,50];
    const passiveCosts = [0.1,0.5,1,2,5];
    const passiveGains = [1,1,1,1,1];
    const passiveIntervals = [20,15,10,5,1];
    const dailyRewards = [100,200,500,1000,2000,5000,10000];

    function saveAll(){ D.usr[uid]=U; save(D); update(); }

    function update(){
        document.getElementById('b-gms').innerText = U.gms.toLocaleString();
        document.getElementById('b-ton').innerText = U.ton.toFixed(2);
        document.getElementById('p-gms').innerText = U.gms.toLocaleString();
        document.getElementById('p-ton').innerText = U.ton.toFixed(2);
        document.getElementById('p-clicks').innerText = U.clicks;
        document.getElementById('total-clicks').innerText = U.clicks;
        document.getElementById('upg-ton').innerText = U.ton.toFixed(2);
        let cp = 1 + (U.clickLvl>0?clickGains[U.clickLvl-1]:0);
        document.getElementById('click-power').innerText = cp;
        document.getElementById('p-power').innerText = cp;
        let pi = U.passiveLvl>0 ? passiveIntervals[U.passiveLvl-1] : 0;
        document.getElementById('passive-info').innerText = pi>0 ? '+1 / '+pi+' сек' : '0';
        if(U.boosterEnd > Date.now()){
            let sec = Math.ceil((U.boosterEnd-Date.now())/1000);
            document.getElementById('booster-info').innerText = '🔥 x'+U.boosterMult+' ('+sec+'с)';
        }else{
            U.boosterMult=1; document.getElementById('booster-info').innerText = '';
        }
        rate = Math.max(500000, 1000000 - Math.floor(D.total/5000));
        document.getElementById('rate').innerText = rate.toLocaleString();
        let prev = D.hist[D.hist.length-2]||rate;
        let pct = ((rate-prev)/prev*100).toFixed(1);
        let pb = document.getElementById('pct-badge');
        pb.innerText = (pct>=0?'+':'')+pct+'%';
        pb.className = 'pct-big '+(pct>=0?'pct-up':'pct-down');
        renderUpgrades(); renderDaily(); renderVip(); renderTasks(); drawChart();
    }

    function clickGMS(e){
        U.clicks++; U.gms += (1+(U.clickLvl>0?clickGains[U.clickLvl-1]:0)) * U.boosterMult;
        D.total++;
        if(e){ let el=document.createElement('div'); el.className='plus-anim';
            el.innerText='+'+(1+(U.clickLvl>0?clickGains[U.clickLvl-1]:0))*U.boosterMult;
            el.style.left=e.clientX+'px'; el.style.top=e.clientY+'px';
            document.body.appendChild(el); setTimeout(()=>el.remove(),800); }
        saveAll();
    }

    function renderUpgrades(){
        let cbox=document.getElementById('upg-click');
        cbox.innerHTML = clickCosts.map((c,i)=>
            `<div class="task-row"><div>${['🥇Бронза','🥈Серебро','💎Золото','🔮Миф','🐉Легенда','🌌Космос'][i]} +${clickGains[i]}</div>
            <div>${U.clickLvl>i?'✅':U.clickLvl===i?`<button class="btn sm cy" onclick="buyClick(${i})">${c} TON</button>`:'🔒'}</div></div>`
        ).join('');
        let pbox=document.getElementById('upg-passive');
        pbox.innerHTML = passiveCosts.map((c,i)=>
            `<div class="task-row"><div>${['🤖Робот','⚙️Механизм','🏭Фабрика','⚡Станция','🌌Дыра'][i]} 1/${passiveIntervals[i]}с</div>
            <div>${U.passiveLvl>i?'✅':U.passiveLvl===i?`<button class="btn sm cy" onclick="buyPassive(${i})">${c} TON</button>`:'🔒'}</div></div>`
        ).join('');
        let bbox=document.getElementById('upg-boost');
        bbox.innerHTML = `
            <div class="task-row"><div>🔥 x5 (30с)</div><button class="btn sm cy" onclick="buyBoost(5,30,0.1)">0.1 TON</button></div>
            <div class="task-row"><div>💣 x10 (1мин)</div><button class="btn sm cy" onclick="buyBoost(10,60,0.5)">0.5 TON</button></div>`;
    }

    function buyClick(i){ if(U.clickLvl!==i) return; if(U.ton<clickCosts[i]) return alert('Недостаточно TON!'); U.ton-=clickCosts[i]; U.clickLvl++; saveAll(); alert('✅ Улучшено!'); }
    function buyPassive(i){ if(U.passiveLvl!==i) return; if(U.ton<passiveCosts[i]) return alert('Недостаточно TON!'); U.ton-=passiveCosts[i]; U.passiveLvl++; saveAll(); alert('✅ Пассив улучшен!'); }
    function buyBoost(mult,dur,cost){ if(U.ton<cost) return alert('Недостаточно TON!'); U.ton-=cost; U.boosterMult=mult; U.boosterEnd=Date.now()+dur*1000; saveAll(); alert('✅ Бустер активен!'); }

    function renderDaily(){
        let box=document.getElementById('daily-bonus');
        let now=Date.now();
        if(U.dailyTime && now-U.dailyTime<86400000 && U.dailyDay>=7){
            box.innerHTML='<p style="text-align:center;color:var(--green);">✅ Все бонусы собраны! Жди новый цикл.</p>'; return;
        }
        if(U.dailyTime && now-U.dailyTime<86400000){
            let next = new Date(U.dailyTime+86400000);
            box.innerHTML=`<p style="text-align:center;">Следующий через: ${Math.ceil((next-now)/3600000)}ч</p>`; return;
        }
        box.innerHTML = dailyRewards.map((r,i)=>
            `<div class="task-row"><div>День ${i+1}: +${r} GMS</div>
            ${i<U.dailyDay?'✅':i===U.dailyDay?`<button class="btn sm gd" onclick="claimDaily()">Забрать</button>`:'🔒'}</div>`
        ).join('');
    }
    function claimDaily(){ U.gms+=dailyRewards[U.dailyDay]; U.dailyDay++; U.dailyTime=Date.now(); saveAll(); alert('🎁 +'+dailyRewards[U.dailyDay-1]+' GMS!'); }

    function renderVip(){
        let box=document.getElementById('vip-packs');
        if(!D.vip.length){ box.innerHTML='<p style="color:var(--sub);text-align:center;">Нет пакетов</p>'; return; }
        box.innerHTML = D.vip.map((v,i)=>
            `<div class="task-row"><div><b>${v.name}</b><br>${v.gms.toLocaleString()} GMS</div>
            <button class="btn sm gd" onclick="buyVip(${i})">${v.price} TON</button></div>`
        ).join('');
    }
    function buyVip(i){ let v=D.vip[i]; if(U.ton<v.price) return alert('Недостаточно TON!'); U.ton-=v.price; U.gms+=v.gms; saveAll(); alert('✅ +'+v.gms.toLocaleString()+' GMS!'); }

    function renderTasks(){
        let box=document.getElementById('tasks-list');
        if(!D.tasks.length){ box.innerHTML='<p style="color:var(--sub);text-align:center;">Нет заданий</p>'; return; }
        box.innerHTML = D.tasks.map(t=>{
            let done=U.done.includes(t.id);
            return `<div class="task-row"><div><b>${t.type==='channel'?'📢':t.type==='chat'?'💬':'🤖'} ${t.link}</b><br>+${t.gms} GMS</div>
            ${done?'<span class="badge badge-g">✅</span>':`<button class="btn sm cy" onclick="doTask('${t.id}')">✅</button>`}</div>`;
        }).join('');
    }
    function doTask(id){ if(U.done.includes(id)) return; let t=D.tasks.find(t=>t.id===id); if(!t) return; tg.openTelegramLink('https://'+t.link); U.done.push(id); U.gms+=t.gms; saveAll(); setTimeout(()=>alert('✅ +'+t.gms+' GMS!'),1500); }

    function swapCalc(){ let z=parseInt(document.getElementById('swap-gms').value)||100000; document.getElementById('swap-ton').innerText=(z/rate).toFixed(4); }
    function sellGMS(){ let z=parseInt(document.getElementById('swap-gms').value); if(isNaN(z)||z<100000||z>U.gms) return alert('Мин. 100 000 GMS'); let t=z/rate*0.95; U.gms-=z; U.ton+=t; D.total-=z; D.hist.push(rate); if(D.hist.length>30) D.hist.shift(); saveAll(); alert('✅ Продано! +'+t.toFixed(4)+' TON'); }
    function buyGMS(){ let z=parseInt(document.getElementById('swap-gms').value); if(isNaN(z)||z<100000) return alert('Мин. 100 000 GMS'); let t=z/rate; if(t>U.ton) return alert('Недостаточно TON'); U.ton-=t; U.gms+=z; D.total+=z; D.hist.push(rate); if(D.hist.length>30) D.hist.shift(); saveAll(); alert('✅ Куплено!'); }

    function promoOpen(){ let code=document.getElementById('promo-input').value.trim()||prompt('🎁 Промокод:'); if(!code) return; let p=D.promo.find(p=>p.code===code.toUpperCase()); if(!p) return alert('❌ Не найден'); if(p.used.includes(uid)) return alert('⚠️ Уже использован'); if(p.used.length>=p.max) return alert('⚠️ Закончился'); p.used.push(uid); U.gms+=p.gms; saveAll(); alert('🎁 +'+p.gms+' GMS!'); }
    function promoCreate(){ let c=document.getElementById('pc-code').value.trim().toUpperCase(); let g=parseInt(document.getElementById('pc-gms').value); let m=parseInt(document.getElementById('pc-max').value); if(!c||c.length<3) return alert('Код от 3 символов'); if(!g||!m) return alert('Заполни всё'); if(D.promo.find(p=>p.code===c)) return alert('Уже есть'); D.promo.push({code:c,gms:g,max:m,used:[]}); saveAll(); alert('✅ Создан!'); }
    function vipAdd(){ let n=document.getElementById('vp-name').value.trim(); let p=parseFloat(document.getElementById('vp-price').value); let g=parseInt(document.getElementById('vp-gms').value); if(!n||!p||!g) return alert('Заполни всё'); D.vip.push({name:n,price:p,gms:g}); saveAll(); alert('✅ Пак добавлен!'); }
    function taskAdd(){ let l=document.getElementById('t-link').value.trim(); let g=parseInt(document.getElementById('t-gms').value); if(!l.startsWith('t.me/')||!g) return alert('Ссылка t.me/... и награда'); D.tasks.push({id:Date.now(),type:document.getElementById('t-type').value,link:l,gms:g}); saveAll(); alert('✅ Задание добавлено!'); }
    function adminSet(){ let id=document.getElementById('a-id').value.trim(); let dg=parseInt(document.getElementById('a-gms').value)||0; let dt=parseFloat(document.getElementById('a-ton').value)||0; if(!id) return alert('Введи ID'); if(!D.usr[id]) D.usr[id]={gms:0,ton:0,clicks:0,clickLvl:0,passiveLvl:0,boosterMult:1,boosterEnd:0,done:[],usedPromo:[],dailyDay:0,dailyTime:0}; D.usr[id].gms+=dg; D.usr[id].ton+=dt; if(Number(id)===Number(uid)) U=D.usr[id]; saveAll(); alert('✅ Обновлён!'); }

    let chart;
    function drawChart(){
        let ctx=document.getElementById('chart'); if(!ctx) return;
        if(chart) chart.destroy();
        chart=new Chart(ctx,{type:'line',data:{labels:D.hist.map(()=>''),datasets:[{data:D.hist,borderColor:'#7c3aed',backgroundColor:'rgba(124,58,237,0.08)',fill:true,tension:0.4,pointRadius:0,borderWidth:2}]},options:{responsive:true,maintainAspectRatio:false,plugins:{legend:{display:false}},scales:{x:{display:false},y:{display:false}}}});
    }

    function navGo(id,el){
        document.querySelectorAll('.page').forEach(x=>x.classList.remove('active'));
        document.querySelectorAll('.nav-item').forEach(x=>x.classList.remove('active'));
        document.getElementById('page-'+id).classList.add('active');
        if(el) el.classList.add('active');
    }
    function copyWallet(){ navigator.clipboard.writeText(WALLET); alert('✅ Скопировано!'); }
    function withdraw(){
        let amt=parseFloat(document.getElementById('w-amount').value);
        let wal=document.getElementById('w-wallet').value.trim();
        if(isNaN(amt)||amt<0.01) return alert('Мин. 0.01 TON');
        let gmsNeeded=amt*rate/0.95;
        if(gmsNeeded>U.gms) return alert('Недостаточно GMS! Нужно: '+Math.ceil(gmsNeeded).toLocaleString());
        if(!wal.startsWith('UQ')) return alert('Адрес должен начинаться с UQ');
        U.gms-=gmsNeeded; U.ton-=amt;
        saveAll();
        alert('✅ Вывод '+amt.toFixed(2)+' TON отправлен!');
    }

    // Пассивный доход
    setInterval(()=>{
        if(U.passiveLvl>0){
            let pi=passiveIntervals[U.passiveLvl-1];
            U.gms += 1/pi * (U.boosterMult||1);
            D.total += 1/pi;
            saveAll();
        }
    },1000);

    update();
</script>
</body>
</html>
