<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Click & Earn</title>
    <script src="https://telegram.org/js/telegram-web-app.js"></script>
    <style>
        *{box-sizing:border-box;margin:0;padding:0}
        body{background:#0a0a14;color:#e0e0e0;font-family:-apple-system,BlinkMacSystemFont,sans-serif;user-select:none;font-size:13px}
        .container{padding:10px 10px 75px}
        .header{display:flex;justify-content:space-between;align-items:center;margin-bottom:8px}
        .id-badge{background:#12122a;padding:6px 12px;border-radius:14px;font-size:10px;color:#9ca3af;border:1px solid #1e1e3a}
        .id-badge span{color:#00e5ff;font-weight:700}
        .promo-btn{width:32px;height:32px;border-radius:50%;border:none;background:#7c3aed;font-size:14px;cursor:pointer;color:#fff}
        .bal-row{display:flex;gap:6px;margin-bottom:8px}
        .bal-item{flex:1;background:#12122a;border:1px solid #1e1e3a;border-radius:10px;padding:8px;text-align:center}
        .bal-item .lbl{font-size:9px;color:#9ca3af}
        .bal-item .val{font-size:16px;font-weight:700}
        .val.gms{color:#ffc107}.val.ton{color:#00e676}
        .page{display:none}.page.active{display:block}
        .card{background:#12122a;border:1px solid #1e1e3a;border-radius:10px;padding:10px;margin-bottom:6px}
        .nav-bar{position:fixed;bottom:0;left:0;right:0;height:58px;background:#0d0d20;border-top:1px solid #1e1e3a;display:flex;z-index:1000}
        .nav-item{color:#9ca3af;font-size:7px;text-align:center;cursor:pointer;flex:1;padding:4px 1px}
        .nav-item.active{color:#7c3aed}.nav-ic{font-size:14px;margin-bottom:1px}
        .btn{background:#7c3aed;color:#fff;border:none;padding:9px;border-radius:16px;width:100%;font-weight:700;font-size:11px;margin-top:4px;cursor:pointer}
        .btn:active{opacity:.8}.btn.gr{background:#00e676;color:#000}.btn.gd{background:#ffc107;color:#000}.btn.cy{background:#00e5ff;color:#000}.btn.rd{background:#ff1744}.btn.ol{background:transparent;border:2px solid #7c3aed;color:#7c3aed}.btn.sm{padding:5px 10px;font-size:10px;width:auto;margin:2px;display:inline-block}
        .inp{width:100%;padding:8px 10px;background:#0a0a1a;border:1px solid #1e1e3a;border-radius:12px;color:#fff;margin-top:3px;font-size:11px;outline:none}.inp:focus{border-color:#7c3aed}
        label{display:block;margin-top:5px;font-size:10px;color:#9ca3af}
        .click-btn{width:130px;height:130px;border-radius:50%;border:3px solid #7c3aed;background:radial-gradient(circle,#1a1a40,#0a0a1a);margin:12px auto;display:flex;align-items:center;justify-content:center;flex-direction:column;font-size:13px;font-weight:700;color:#ffc107;cursor:pointer;box-shadow:0 0 25px rgba(124,58,237,.4)}.click-btn:active{transform:scale(.9)}
        .task-row{display:flex;justify-content:space-between;align-items:center;padding:7px;background:#0a0a1a;border-radius:7px;margin-bottom:3px;gap:5px;flex-wrap:wrap}
        .badge{padding:2px 6px;border-radius:8px;font-size:8px;font-weight:700}.badge-g{background:rgba(0,230,118,.2);color:#00e676}
        .wallet-box{background:#0a0a1a;border:1px dashed #ffc107;border-radius:8px;padding:6px;word-break:break-all;font-size:8px;color:#ffc107;text-align:center;margin:5px 0}
        .chart-wrap{background:#0a0a1a;border-radius:8px;padding:3px;margin:5px 0;height:110px}
        canvas{width:100%!important;height:100%!important}
        .pct-big{font-size:11px;font-weight:700;padding:2px 6px;border-radius:8px}.pct-up{color:#00e676;background:rgba(0,230,118,.12)}.pct-down{color:#ff1744;background:rgba(255,23,68,.12)}
        .plus-anim{position:fixed;pointer-events:none;color:#ffc107;font-weight:700;font-size:16px;animation:floatUp .7s forwards;z-index:999}
        @keyframes floatUp{0%{opacity:1;transform:translateY(0)}100%{opacity:0;transform:translateY(-70px)}}
    </style>
</head>
<body>
<div class="container">
    <div class="header"><div class="id-badge">🆔 <span id="uid">...</span></div><button class="promo-btn" onclick="promoOpen()">🎁</button></div>
    <div class="bal-row"><div class="bal-item"><div class="lbl">💎 GMS</div><div class="val gms" id="b-gms">0</div></div><div class="bal-item"><div class="lbl">💰 TON</div><div class="val ton" id="b-ton">0.00</div></div></div>

    <!-- Кликер -->
    <div id="page-clicker" class="page active" style="text-align:center">
        <div class="click-btn" id="clickBtn" onclick="clickGMS(event)"><div style="font-size:28px">💎</div><div>НАЖМИ</div></div>
        <div style="color:#00e5ff">💪 +<span id="click-power">1</span> GMS/клик</div>
        <div style="color:#9ca3af;font-size:10px">🤖 Пассив: +<span id="passive-info">0</span></div>
        <div id="booster-info" style="color:#ffc107;font-size:10px;margin-top:2px"></div>
    </div>

    <!-- Улучшения -->
    <div id="page-upgrades" class="page"><h3>🏪 Улучшения</h3><p style="font-size:10px;color:#9ca3af">💰 TON: <b id="upg-ton">0.00</b></p>
        <div class="card"><h4>💪 Сила клика</h4><div id="upg-click"></div></div>
        <div class="card"><h4>🤖 Пассив</h4><div id="upg-passive"></div></div>
        <div class="card"><h4>🔥 Бустеры</h4><div id="upg-boost"></div></div>
    </div>

    <!-- Биржа -->
    <div id="page-exchange" class="page"><h3>📈 Биржа</h3>
        <div class="card" style="text-align:center"><div style="font-size:10px;color:#9ca3af">Курс</div><div style="font-size:18px;font-weight:700;color:#ffc107"><span id="rate">1M</span> GMS = 1 TON</div><span class="pct-big" id="pct-badge">0%</span><br><small style="color:#9ca3af">Комиссия 5%</small></div>
        <div class="chart-wrap"><canvas id="chart"></canvas></div>
        <label>GMS (мин 100K):</label><input type="number" id="swap-gms" class="inp" value="100000" min="100000" oninput="swapCalc()">
        <div style="text-align:center;margin:4px 0">= <span id="swap-ton" style="color:#00e676">0.10</span> TON</div>
        <div style="display:flex;gap:5px"><button class="btn gr" style="flex:1" onclick="sellGMS()">💰 Продать</button><button class="btn gd" style="flex:1" onclick="buyGMS()">💎 Купить</button></div>
    </div>

    <!-- Бонусы -->
    <div id="page-bonus" class="page"><h3>🎁 Бонусы</h3>
        <div class="card"><h4>📅 Ежедневный</h4><div id="daily-bonus"></div></div>
        <div class="card"><h4>🎁 Промокод</h4><input type="text" id="promo-input" class="inp" placeholder="Код"><button class="btn gd" onclick="promoOpen()">Активировать</button></div>
        <div class="card"><h4>💎 VIP Пак</h4><div id="vip-packs"></div></div>
        <div class="card"><h4>📋 Задания</h4><div id="tasks-list"></div></div>
    </div>

    <!-- Профиль -->
    <div id="page-profile" class="page"><h3>👤 Профиль</h3>
        <div class="card" style="text-align:center"><div style="font-size:20px;font-weight:700;color:#ffc107"><span id="p-gms">0</span> GMS</div><div style="font-size:15px;color:#00e676"><span id="p-ton">0.00</span> TON</div></div>
        <h4>💎 Пополнение</h4><p style="font-size:9px;color:#9ca3af">Мин: 0.1 TON = 100K GMS</p>
        <div class="wallet-box">UQDmNY1TIMIgnALOpAyJ4_XO2uroUNLFVRwGie5AEwzccaps</div>
        <button class="btn ol" onclick="copyWallet()">📋 Копировать</button>
        <p style="font-size:8px;color:#ffc107">В комментарии: ID <span id="p-uid">...</span></p>
        <h4 style="margin-top:8px">💸 Вывод TON</h4><p style="font-size:9px;color:#9ca3af">Мин: 100K GMS | 5% комиссия</p>
        <input type="number" id="w-amount" class="inp" placeholder="Сумма TON" step="0.01">
        <input type="text" id="w-wallet" class="inp" placeholder="Кошелёк UQ...">
        <button class="btn rd" onclick="withdraw()">💸 Вывести</button>
    </div>

    <!-- Админ -->
    <div id="page-admin" class="page"><h3 style="color:#7c3aed">👑 Админ</h3>
        <div class="card" style="border-color:#7c3aed"><h4>⚙️ Игрок</h4><input type="text" id="a-id" class="inp" placeholder="ID"><input type="number" id="a-gms" class="inp" placeholder="GMS"><input type="number" id="a-ton" class="inp" placeholder="TON"><button class="btn" onclick="adminSet()">💾 Применить</button></div>
        <div class="card" style="border-color:#7c3aed"><h4>🎁 Промокод</h4><input type="text" id="pc-code" class="inp" placeholder="Код"><input type="number" id="pc-gms" class="inp" placeholder="GMS"><input type="number" id="pc-max" class="inp" placeholder="Активаций"><button class="btn gd" onclick="promoCreate()">Создать</button></div>
        <div class="card" style="border-color:#7c3aed"><h4>💎 VIP</h4><input type="text" id="vp-name" class="inp" placeholder="Название"><input type="number" id="vp-price" class="inp" placeholder="Цена TON"><input type="number" id="vp-gms" class="inp" placeholder="GMS"><button class="btn gd" onclick="vipAdd()">Добавить</button></div>
        <div class="card" style="border-color:#7c3aed"><h4>📋 Задание</h4><select id="t-type" class="inp"><option value="channel">📢 Канал</option><option value="chat">💬 Чат</option><option value="bot">🤖 Бот</option></select><input type="text" id="t-link" class="inp" placeholder="t.me/..."><input type="number" id="t-gms" class="inp" placeholder="GMS"><button class="btn gd" onclick="taskAdd()">Добавить</button></div>
    </div>
</div>

<div class="nav-bar">
    <div class="nav-item active" onclick="navGo('clicker',this)"><div class="nav-ic">🎮</div>Кликер</div>
    <div class="nav-item" onclick="navGo('upgrades',this)"><div class="nav-ic">🏪</div>Улучш</div>
    <div class="nav-item" onclick="navGo('exchange',this)"><div class="nav-ic">📈</div>Биржа</div>
    <div class="nav-item" onclick="navGo('bonus',this)"><div class="nav-ic">🎁</div>Бонус</div>
    <div class="nav-item" onclick="navGo('profile',this)"><div class="nav-ic">👤</div>Проф</div>
    <div class="nav-item" id="nav-adm" style="display:none" onclick="navGo('admin',this)"><div class="nav-ic">👑</div>Адм</div>
</div>

<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script>
const tg=window.Telegram.WebApp;tg.expand();
const uid=tg.initDataUnsafe?.user?.id||Math.floor(Math.random()*1e6);
document.getElementById('uid').innerText=uid;
document.getElementById('p-uid').innerText=uid;
const ADM=8684827145,WALLET="UQDmNY1TIMIgnALOpAyJ4_XO2uroUNLFVRwGie5AEwzccaps";
if(Number(uid)===ADM) document.getElementById('nav-adm').style.display='block';

function load(){return JSON.parse(localStorage.getItem('cd')||'{}')}
function save(d){localStorage.setItem('cd',JSON.stringify(d))}
let D=load();
if(!D.u) D.u={};
if(!D.t) D.t=[];
if(!D.p) D.p=[];
if(!D.v) D.v=[];
if(!D.h) D.h=[1e6,1.002e6,998e3,1.005e6,1.01e6,1e6];
if(!D.tot) D.tot=0;
if(!D.u[uid]) D.u[uid]={g:0,tn:.5,cl:0,cl:0,pl:0,bm:1,be:0,dn:[],up:[],dd:0,dt:0};
let U=D.u[uid],rate=1e6;
const cc=[.1,.5,1,2,5,10],cg=[1,2,5,10,25,50],pc=[.1,.5,1,2,5],pi=[20,15,10,5,1],dr=[100,200,500,1e3,2e3,5e3,1e4];
function saveAll(){D.u[uid]=U;save(D);update()}

function update(){
    document.getElementById('b-gms').innerText=U.g.toLocaleString();
    document.getElementById('b-ton').innerText=U.tn.toFixed(2);
    document.getElementById('p-gms').innerText=U.g.toLocaleString();
    document.getElementById('p-ton').innerText=U.tn.toFixed(2);
    document.getElementById('upg-ton').innerText=U.tn.toFixed(2);
    let cp=1+(U.cl>0?cg[U.cl-1]:0);
    document.getElementById('click-power').innerText=cp;
    let pv=U.pl>0?pi[U.pl-1]:0;
    document.getElementById('passive-info').innerText=pv>0?'1/'+pv+'с':'0';
    if(U.be>Date.now()){
        document.getElementById('booster-info').innerText='🔥 x'+U.bm+' ('+Math.ceil((U.be-Date.now())/1000)+'с)';
    }else{U.bm=1;document.getElementById('booster-info').innerText=''}
    rate=Math.max(5e5,1e6-Math.floor(D.tot/5e3));
    document.getElementById('rate').innerText=(rate/1e6).toFixed(1)+'M';
    let prev=D.h[D.h.length-2]||rate,pct=((rate-prev)/prev*100).toFixed(1);
    let pb=document.getElementById('pct-badge');pb.innerText=(pct>=0?'+':'')+pct+'%';
    pb.className='pct-big '+(pct>=0?'pct-up':'pct-down');
    renderUpgrades();renderDaily();renderVip();renderTasks();drawChart();
}

function clickGMS(e){
    U.cl++;U.g+=(1+(U.cl>0?cg[U.cl-1]:0))*U.bm;D.tot++;
    if(e){let el=document.createElement('div');el.className='plus-anim';
    el.innerText='+'+(1+(U.cl>0?cg[U.cl-1]:0))*U.bm;
    el.style.left=e.clientX+'px';el.style.top=e.clientY+'px';
    document.body.appendChild(el);setTimeout(()=>el.remove(),700)}
    saveAll();
}

function renderUpgrades(){
    document.getElementById('upg-click').innerHTML=cc.map((c,i)=>`<div class="task-row"><div>${['🥇Бронза','🥈Серебро','💎Золото','🔮Миф','🐉Легенда','🌌Космос'][i]} +${cg[i]}</div><div>${U.cl>i?'✅':U.cl===i?`<button class="btn sm cy" onclick="buyClick(${i})">${c} TON</button>`:'🔒'}</div></div>`).join('');
    document.getElementById('upg-passive').innerHTML=pc.map((c,i)=>`<div class="task-row"><div>${['🤖Робот','⚙️Мех','🏭Фабрика','⚡Станция','🌌Дыра'][i]} 1/${pi[i]}с</div><div>${U.pl>i?'✅':U.pl===i?`<button class="btn sm cy" onclick="buyPassive(${i})">${c} TON</button>`:'🔒'}</div></div>`).join('');
    document.getElementById('upg-boost').innerHTML=`<div class="task-row"><div>🔥 x5 (30с)</div><button class="btn sm cy" onclick="buyBoost(5,30,.1)">0.1 TON</button></div><div class="task-row"><div>💣 x10 (1мин)</div><button class="btn sm cy" onclick="buyBoost(10,60,.5)">0.5 TON</button></div>`;
}

function buyClick(i){if(U.cl!==i||U.tn<cc[i]) return;U.tn-=cc[i];U.cl++;saveAll()}
function buyPassive(i){if(U.pl!==i||U.tn<pc[i]) return;U.tn-=pc[i];U.pl++;saveAll()}
function buyBoost(m,d,c){if(U.tn<c) return;U.tn-=c;U.bm=m;U.be=Date.now()+d*1000;saveAll()}

function renderDaily(){
    let n=Date.now(),b=document.getElementById('daily-bonus');
    if(U.dt&&n-U.dt<864e5&&U.dd>=7){b.innerHTML='<p style="text-align:center;color:#00e676">✅ Все собраны!</p>';return}
    if(U.dt&&n-U.dt<864e5){b.innerHTML=`<p style="text-align:center">Следующий через ${Math.ceil((U.dt+864e5-n)/36e5)}ч</p>`;return}
    b.innerHTML=dr.map((r,i)=>`<div class="task-row"><div>День ${i+1}: +${r}</div>${i<U.dd?'✅':i===U.dd?`<button class="btn sm gd" onclick="claimDaily()">Забрать</button>`:'🔒'}</div>`).join('');
}
function claimDaily(){U.g+=dr[U.dd];U.dd++;U.dt=Date.now();saveAll()}

function renderVip(){
    let b=document.getElementById('vip-packs');
    b.innerHTML=D.v.length?D.v.map((v,i)=>`<div class="task-row"><div><b>${v.n}</b><br>${v.g.toLocaleString()} GMS</div><button class="btn sm gd" onclick="buyVip(${i})">${v.p} TON</button></div>`).join(''):'<p style="color:#9ca3af;text-align:center">Нет пакетов</p>';
}
function buyVip(i){let v=D.v[i];if(U.tn<v.p) return;U.tn-=v.p;U.g+=v.g;saveAll()}

function renderTasks(){
    let b=document.getElementById('tasks-list');
    b.innerHTML=D.t.length?D.t.map(t=>{let d=U.dn.includes(t.id);return `<div class="task-row"><div><b>${t.ty==='channel'?'📢':t.ty==='chat'?'💬':'🤖'} ${t.lk}</b><br>+${t.gs}</div>${d?'<span class="badge badge-g">✅</span>':`<button class="btn sm cy" onclick="doTask('${t.id}')">✅</button>`}</div>`}).join(''):'<p style="color:#9ca3af;text-align:center">Нет</p>';
}
function doTask(id){if(U.dn.includes(id)) return;let t=D.t.find(t=>t.id===id);if(!t) return;tg.openTelegramLink('https://'+t.lk);U.dn.push(id);U.g+=t.gs;saveAll()}

function swapCalc(){document.getElementById('swap-ton').innerText=(parseInt(document.getElementById('swap-gms').value)||1e5/rate).toFixed(4)}
function sellGMS(){let z=parseInt(document.getElementById('swap-gms').value);if(isNaN(z)||z<1e5||z>U.g) return;U.g-=z;U.tn+=z/rate*.95;D.tot-=z;D.h.push(rate);if(D.h.length>30) D.h.shift();saveAll()}
function buyGMS(){let z=parseInt(document.getElementById('swap-gms').value);if(isNaN(z)||z<1e5) return;let t=z/rate;if(t>U.tn) return;U.tn-=t;U.g+=z;D.tot+=z;D.h.push(rate);if(D.h.length>30) D.h.shift();saveAll()}

function promoOpen(){
    let c=document.getElementById('promo-input').value.trim()||prompt('🎁 Промокод:');if(!c) return;
    let p=D.p.find(p=>p.c===c.toUpperCase());if(!p) return alert('❌');
    if(p.u.includes(uid)) return alert('⚠️ Уже использован');if(p.u.length>=p.m) return alert('⚠️ Закончился');
    p.u.push(uid);U.g+=p.g;saveAll();alert('🎁 +'+p.g+' GMS!');
}
function promoCreate(){let c=document.getElementById('pc-code').value.trim().toUpperCase(),g=parseInt(document.getElementById('pc-gms').value),m=parseInt(document.getElementById('pc-max').value);if(!c||!g||!m) return;D.p.push({c,g,m,u:[]});saveAll();alert('✅')}
function vipAdd(){let n=document.getElementById('vp-name').value.trim(),p=parseFloat(document.getElementById('vp-price').value),g=parseInt(document.getElementById('vp-gms').value);if(!n||!p||!g) return;D.v.push({n,p,g});saveAll();alert('✅')}
function taskAdd(){let l=document.getElementById('t-link').value.trim(),g=parseInt(document.getElementById('t-gms').value);if(!l.startsWith('t.me/')||!g) return;D.t.push({id:Date.now(),ty:document.getElementById('t-type').value,lk:l,gs:g});saveAll();alert('✅')}
function adminSet(){let id=document.getElementById('a-id').value.trim(),dg=parseInt(document.getElementById('a-gms').value)||0,dt=parseFloat(document.getElementById('a-ton').value)||0;if(!id) return;if(!D.u[id]) D.u[id]={g:0,tn:0,cl:0,cl:0,pl:0,bm:1,be:0,dn:[],up:[],dd:0,dt:0};D.u[id].g+=dg;D.u[id].tn+=dt;if(Number(id)===Number(uid)) U=D.u[id];saveAll();alert('✅')}

let chart;
function drawChart(){
    let ctx=document.getElementById('chart');if(!ctx) return;
    if(chart) chart.destroy();
    chart=new Chart(ctx,{type:'line',data:{labels:D.h.map(()=>''),datasets:[{data:D.h,borderColor:'#7c3aed',backgroundColor:'rgba(124,58,237,.08)',fill:true,tension:.4,pointRadius:0,borderWidth:2}]},options:{responsive:true,maintainAspectRatio:false,plugins:{legend:{display:false}},scales:{x:{display:false},y:{display:false}}});
}

function navGo(id,el){document.querySelectorAll('.page').forEach(x=>x.classList.remove('active'));document.querySelectorAll('.nav-item').forEach(x=>x.classList.remove('active'));document.getElementById('page-'+id).classList.add('active');if(el) el.classList.add('active')}
function copyWallet(){navigator.clipboard.writeText(WALLET);alert('✅')}
function withdraw(){let a=parseFloat(document.getElementById('w-amount').value),w=document.getElementById('w-wallet').value.trim();if(isNaN(a)||a<.01) return;let n=a*rate/.95;if(n>U.g) return alert('Не хватает GMS!');if(!w.startsWith('UQ')) return alert('Неверный адрес');U.g-=n;saveAll();alert('✅ Вывод '+a.toFixed(2)+' TON')}

setInterval(()=>{if(U.pl>0){U.g+=1/pi[U.pl-1]*U.bm;D.tot+=1/pi[U.pl-1];saveAll()}},1000);
update();
</script>
</body>
</html>
