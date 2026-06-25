<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Click & Earn</title>
    <script src="https://telegram.org/js/telegram-web-app.js"></script>
    <style>
        *{box-sizing:border-box;margin:0;padding:0}
        body{background:#0a0a14;color:#e0e0e0;font-family:-apple-system,BlinkMacSystemFont,sans-serif;user-select:none;font-size:14px}
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
        .btn.gr{background:#00e676;color:#000}.btn.gd{background:#ffc107;color:#000}.btn.cy{background:#00e5ff;color:#000}.btn.rd{background:#ff1744}.btn.ol{background:transparent;border:2px solid #7c3aed;color:#7c3aed}.btn.sm{padding:5px 10px;font-size:10px;width:auto;margin:2px;display:inline-block}
        .inp{width:100%;padding:8px 10px;background:#0a0a1a;border:1px solid #1e1e3a;border-radius:12px;color:#fff;margin-top:3px;font-size:11px;outline:none}.inp:focus{border-color:#7c3aed}
        label{display:block;margin-top:5px;font-size:10px;color:#9ca3af}
        .click-btn{width:150px;height:150px;border-radius:50%;border:4px solid #7c3aed;background:radial-gradient(circle,#1e1e40,#0a0a1a);margin:15px auto;display:flex;align-items:center;justify-content:center;flex-direction:column;font-size:14px;font-weight:700;color:#ffc107;cursor:pointer;box-shadow:0 0 25px rgba(124,58,237,.4)}.click-btn:active{transform:scale(.9)}
        .task-row{display:flex;justify-content:space-between;align-items:center;padding:7px;background:#0a0a1a;border-radius:7px;margin-bottom:3px;gap:5px}
        .badge{padding:2px 6px;border-radius:8px;font-size:8px;font-weight:700}.badge-g{background:rgba(0,230,118,.2);color:#00e676}
        .wallet-box{background:#0a0a1a;border:1px dashed #ffc107;border-radius:8px;padding:6px;word-break:break-all;font-size:8px;color:#ffc107;text-align:center;margin:5px 0}
        .chart-wrap{background:#0a0a1a;border-radius:8px;padding:3px;margin:5px 0;height:110px}
        canvas{width:100%!important;height:100%!important}
        .pct-big{font-size:11px;font-weight:700;padding:2px 6px;border-radius:8px}.pct-up{color:#00e676;background:rgba(0,230,118,.12)}.pct-down{color:#ff1744;background:rgba(255,23,68,.12)}
        .plus-anim{position:fixed;pointer-events:none;color:#ffc107;font-weight:700;font-size:16px;animation:floatUp .7s forwards;z-index:999}
        @keyframes floatUp{0%{opacity:1;transform:translateY(0)}100%{opacity:0;transform:translateY(-70px)}}
        h3{margin-bottom:6px;font-size:15px}h4{font-size:12px;margin-bottom:4px;color:#c0c0d0}
    </style>
</head>
<body>
<div class="container">
    <div class="header"><div class="id-badge">🆔 <span id="uid">...</span></div><button class="promo-btn" onclick="promoOpen()">🎁</button></div>
    <div class="bal-row"><div class="bal-item"><div class="lbl">💎 GMS</div><div class="val gms" id="b-gms">0</div></div><div class="bal-item"><div class="lbl">💰 TON</div><div class="val ton" id="b-ton">0.00</div></div></div>

    <!-- КЛИКЕР -->
    <div id="page-clicker" class="page active" style="text-align:center">
        <div class="click-btn" id="clickBtn"><div style="font-size:35px">💎</div><div>НАЖМИ</div></div>
        <div style="color:#00e5ff">💪 +<span id="cp">1</span> GMS/клик</div>
        <div style="color:#9ca3af;font-size:10px">🤖 Пассив: <span id="pi">0</span></div>
        <div id="bi" style="color:#ffc107;font-size:10px;margin-top:2px"></div>
        <div style="font-size:10px;color:#9ca3af;margin-top:5px">👆 <span id="tc">0</span> кликов</div>
    </div>

    <!-- УЛУЧШЕНИЯ -->
    <div id="page-upgrades" class="page"><h3>🏪 Улучшения</h3><p style="font-size:10px;color:#9ca3af;margin-bottom:5px">💰 TON: <b id="ut">0.00</b></p>
        <div class="card"><h4>💪 Сила</h4><div id="uc"></div></div>
        <div class="card"><h4>🤖 Пассив</h4><div id="up"></div></div>
        <div class="card"><h4>🔥 Бустеры</h4><div id="ub"></div></div>
    </div>

    <!-- БИРЖА -->
    <div id="page-exchange" class="page"><h3>📈 Биржа</h3>
        <div class="card" style="text-align:center"><div style="font-size:10px;color:#9ca3af">Курс</div><div style="font-size:18px;font-weight:700;color:#ffc107"><span id="rt">1M</span> GMS = 1 TON</div><span class="pct-big" id="pb">0%</span><br><small style="color:#9ca3af">Комиссия 5%</small></div>
        <div class="chart-wrap"><canvas id="chart"></canvas></div>
        <label>GMS (мин 100K):</label><input type="number" id="sg" class="inp" value="100000" min="100000" oninput="sc()">
        <div style="text-align:center;margin:4px 0">= <span id="st" style="color:#00e676">0.10</span> TON</div>
        <div style="display:flex;gap:5px"><button class="btn gr" style="flex:1" id="btn-sell">💰 Продать</button><button class="btn gd" style="flex:1" id="btn-buy">💎 Купить</button></div>
    </div>

    <!-- БОНУСЫ -->
    <div id="page-bonus" class="page"><h3>🎁 Бонусы</h3>
        <div class="card"><h4>📅 Ежедневный</h4><div id="db"></div></div>
        <div class="card"><h4>🎁 Промокод</h4><input type="text" id="pcode" class="inp" placeholder="Код"><button class="btn gd" id="btn-promo">Активировать</button></div>
        <div class="card"><h4>💎 VIP Пак</h4><div id="vp"></div></div>
        <div class="card"><h4>📋 Задания</h4><div id="tl"></div></div>
    </div>

    <!-- ПРОФИЛЬ -->
    <div id="page-profile" class="page"><h3>👤 Профиль</h3>
        <div class="card" style="text-align:center"><div style="font-size:22px;font-weight:700;color:#ffc107"><span id="pg">0</span> GMS</div><div style="font-size:15px;color:#00e676"><span id="pt">0.00</span> TON</div></div>
        <h4>💎 Пополнение</h4><p style="font-size:9px;color:#9ca3af">Мин: 0.1 TON = 100K GMS</p>
        <div class="wallet-box">UQDmNY1TIMIgnALOpAyJ4_XO2uroUNLFVRwGie5AEwzccaps</div>
        <button class="btn ol" id="btn-copy">📋 Копировать</button>
        <p style="font-size:8px;color:#ffc107">⚠️ ID: <span id="puid">...</span></p>
        <h4 style="margin-top:8px">💸 Вывод</h4><p style="font-size:9px;color:#9ca3af">Мин: 100K GMS | 5%</p>
        <input type="number" id="wa" class="inp" placeholder="Сумма TON" step="0.01"><input type="text" id="ww" class="inp" placeholder="Кошелёк UQ...">
        <button class="btn rd" id="btn-wd">💸 Вывести</button>
    </div>

    <!-- АДМИН -->
    <div id="page-admin" class="page"><h3 style="color:#7c3aed">👑 Админ</h3>
        <div class="card" style="border-color:#7c3aed"><h4>⚙️ Игрок</h4><input type="text" id="ai" class="inp" placeholder="ID"><input type="number" id="ag" class="inp" placeholder="GMS"><input type="number" id="at" class="inp" placeholder="TON"><button class="btn" id="btn-as">💾 Применить</button></div>
        <div class="card" style="border-color:#7c3aed"><h4>🎁 Промокод</h4><input type="text" id="pcc" class="inp" placeholder="Код"><input type="number" id="pcg" class="inp" placeholder="GMS"><input type="number" id="pcm" class="inp" placeholder="Активаций"><button class="btn gd" id="btn-pc">Создать</button></div>
        <div class="card" style="border-color:#7c3aed"><h4>💎 VIP</h4><input type="text" id="vn" class="inp" placeholder="Название"><input type="number" id="vp" class="inp" placeholder="Цена TON" step="0.01"><input type="number" id="vg" class="inp" placeholder="GMS"><button class="btn gd" id="btn-va">Добавить</button></div>
        <div class="card" style="border-color:#7c3aed"><h4>📋 Задание</h4><select id="tt" class="inp"><option value="channel">📢 Канал</option><option value="chat">💬 Чат</option><option value="bot">🤖 Бот</option></select><input type="text" id="tlk" class="inp" placeholder="t.me/..."><input type="number" id="tg" class="inp" placeholder="GMS"><button class="btn gd" id="btn-ta">Добавить</button></div>
    </div>
</div>

<div class="nav-bar">
    <div class="nav-item active" id="nav-clicker"><span class="nav-ic">🎮</span>Кликер</div>
    <div class="nav-item" id="nav-upgrades"><span class="nav-ic">🏪</span>Улучш</div>
    <div class="nav-item" id="nav-exchange"><span class="nav-ic">📈</span>Биржа</div>
    <div class="nav-item" id="nav-bonus"><span class="nav-ic">🎁</span>Бонус</div>
    <div class="nav-item" id="nav-profile"><span class="nav-ic">👤</span>Проф</div>
    <div class="nav-item" id="nav-admin" style="display:none"><span class="nav-ic">👑</span>Адм</div>
</div>

<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
<script>
// Инициализация
var tg = window.Telegram.WebApp;
tg.ready();
tg.expand();

var uid = tg.initDataUnsafe?.user?.id || 123456789;
document.getElementById('uid').innerText = uid;
document.getElementById('puid').innerText = uid;

var ADMIN = 8684827145;
var WALLET = "UQDmNY1TIMIgnALOpAyJ4_XO2uroUNLFVRwGie5AEwzccaps";

if(uid === ADMIN) {
    document.getElementById('nav-admin').style.display = 'block';
}

// Данные
var DB = JSON.parse(localStorage.getItem('cdb') || '{"u":{},"t":[],"p":[],"v":[],"h":[1000000,1002000,998000,1005000,1010000,1000000],"tot":0}');
if(!DB.u[uid]) DB.u[uid] = {g:0,tn:0.5,cl:0,clv:0,plv:0,bm:1,be:0,dn:[],up:[],dd:0,dt:0};
var U = DB.u[uid];
var rate = 1000000;

var cc = [0.1,0.5,1,2,5,10];
var cg = [1,2,5,10,25,50];
var cn = ['🥇Бронза','🥈Серебро','💎Золото','🔮Миф','🐉Легенда','🌌Космос'];
var pc = [0.1,0.5,1,2,5];
var pit = [20,15,10,5,1];
var pn = ['🤖Робот','⚙️Мех','🏭Фабрика','⚡Станция','🌌Дыра'];
var dr = [100,200,500,1000,2000,5000,10000];

function save(){ DB.u[uid]=U; localStorage.setItem('cdb',JSON.stringify(DB)); upd(); }

function upd(){
    document.getElementById('b-gms').innerText = U.g.toLocaleString();
    document.getElementById('b-ton').innerText = U.tn.toFixed(2);
    document.getElementById('pg').innerText = U.g.toLocaleString();
    document.getElementById('pt').innerText = U.tn.toFixed(2);
    document.getElementById('ut').innerText = U.tn.toFixed(2);
    document.getElementById('tc').innerText = U.cl;
    var cpv = 1+(U.clv>0?cg[U.clv-1]:0);
    document.getElementById('cp').innerText = cpv;
    var pv = U.plv>0?'1/'+pit[U.plv-1]+'с':'выкл';
    document.getElementById('pi').innerText = pv;
    if(U.be > Date.now()){
        document.getElementById('bi').innerText = '🔥 x'+U.bm+' ('+Math.ceil((U.be-Date.now())/1000)+'с)';
    }else{U.bm=1;document.getElementById('bi').innerText='';}
    rate = Math.max(500000,1000000-Math.floor(DB.tot/5000));
    document.getElementById('rt').innerText = (rate/1000000).toFixed(1)+'M';
    var prev = DB.h[DB.h.length-2]||rate;
    var pct = ((rate-prev)/prev*100).toFixed(1);
    var pbe = document.getElementById('pb');
    pbe.innerText = (pct>=0?'+':'')+pct+'%';
    pbe.className = 'pct-big '+(pct>=0?'pct-up':'pct-down');
    renderUpg(); renderDaily(); renderVip(); renderTasks(); drawChart();
}

// КЛИК
document.getElementById('clickBtn').onclick = function(e){
    U.cl++;
    var earned = (1+(U.clv>0?cg[U.clv-1]:0))*U.bm;
    U.g += earned;
    DB.tot++;
    var el = document.createElement('div');
    el.className = 'plus-anim';
    el.innerText = '+'+earned;
    el.style.left = (e.clientX||100)+'px';
    el.style.top = (e.clientY||200)+'px';
    document.body.appendChild(el);
    setTimeout(function(){el.remove();},700);
    save();
};

// УЛУЧШЕНИЯ
function renderUpg(){
    var h='';
    for(var i=0;i<cc.length;i++){
        h+='<div class="task-row"><div>'+cn[i]+' +'+cg[i]+'</div><div>'+(U.clv>i?'✅':U.clv===i?'<button class="btn sm cy" onclick="buyC('+i+')">'+cc[i]+' TON</button>':'🔒')+'</div></div>';
    }
    document.getElementById('uc').innerHTML = h;
    h='';
    for(var i=0;i<pc.length;i++){
        h+='<div class="task-row"><div>'+pn[i]+' 1/'+pit[i]+'с</div><div>'+(U.plv>i?'✅':U.plv===i?'<button class="btn sm cy" onclick="buyP('+i+')">'+pc[i]+' TON</button>':'🔒')+'</div></div>';
    }
    document.getElementById('up').innerHTML = h;
    document.getElementById('ub').innerHTML = '<div class="task-row"><div>🔥 x5 (30с)</div><button class="btn sm cy" onclick="buyB(5,30,0.1)">0.1 TON</button></div><div class="task-row"><div>💣 x10 (1м)</div><button class="btn sm cy" onclick="buyB(10,60,0.5)">0.5 TON</button></div>';
}

function buyC(i){ if(U.clv!==i||U.tn<cc[i]) return; U.tn-=cc[i]; U.clv++; save(); }
function buyP(i){ if(U.plv!==i||U.tn<pc[i]) return; U.tn-=pc[i]; U.plv++; save(); }
function buyB(m,d,c){ if(U.tn<c) return; U.tn-=c; U.bm=m; U.be=Date.now()+d*1000; save(); }

// ЕЖЕДНЕВНЫЙ
function renderDaily(){
    var now = Date.now(), h='';
    if(U.dt&&now-U.dt<86400000&&U.dd>=7){ document.getElementById('db').innerHTML='<p style="text-align:center;color:#00e676">✅ Все!</p>'; return; }
    if(U.dt&&now-U.dt<86400000){ document.getElementById('db').innerHTML='<p style="text-align:center">Жди '+Math.ceil((U.dt+86400000-now)/3600000)+'ч</p>'; return; }
    for(var i=0;i<dr.length;i++){ h+='<div class="task-row"><div>День '+(i+1)+': +'+dr[i]+'</div>'+(i<U.dd?'✅':i===U.dd?'<button class="btn sm gd" onclick="claimD()">Забрать</button>':'🔒')+'</div>'; }
    document.getElementById('db').innerHTML = h;
}
function claimD(){ U.g+=dr[U.dd]; U.dd++; U.dt=Date.now(); save(); }

// VIP
function renderVip(){
    var h='';
    if(!DB.v.length){ document.getElementById('vp').innerHTML='<p style="color:#9ca3af;text-align:center">Нет</p>'; return; }
    for(var i=0;i<DB.v.length;i++){ h+='<div class="task-row"><div><b>'+DB.v[i].n+'</b><br>'+DB.v[i].g.toLocaleString()+' GMS</div><button class="btn sm gd" onclick="buyV('+i+')">'+DB.v[i].p+' TON</button></div>'; }
    document.getElementById('vp').innerHTML = h;
}
function buyV(i){ if(U.tn<DB.v[i].p) return; U.tn-=DB.v[i].p; U.g+=DB.v[i].g; save(); }

// ЗАДАНИЯ
function renderTasks(){
    var h='';
    if(!DB.t.length){ document.getElementById('tl').innerHTML='<p style="color:#9ca3af;text-align:center">Нет</p>'; return; }
    for(var i=0;i<DB.t.length;i++){
        var t=DB.t[i], done=U.dn.includes(t.id);
        h+='<div class="task-row"><div><b>'+(t.ty==='channel'?'📢':t.ty==='chat'?'💬':'🤖')+' '+t.lk+'</b><br>+'+t.gs+' GMS</div>'+(done?'<span class="badge badge-g">✅</span>':'<button class="btn sm cy" onclick="doT(\''+t.id+'\')">✅</button>')+'</div>';
    }
    document.getElementById('tl').innerHTML = h;
}
function doT(id){ if(U.dn.includes(id)) return; var t=DB.t.find(function(x){return x.id===id}); if(!t) return; tg.openTelegramLink('https://'+t.lk); U.dn.push(id); U.g+=t.gs; save(); }

// БИРЖА
function sc(){ document.getElementById('st').innerText = ((parseInt(document.getElementById('sg').value)||100000)/rate).toFixed(4); }
document.getElementById('btn-sell').onclick = function(){
    var g = parseInt(document.getElementById('sg').value);
    if(isNaN(g)||g<100000||g>U.g) return;
    U.g-=g; U.tn+=g/rate*0.95; DB.tot-=g; DB.h.push(rate); if(DB.h.length>30) DB.h.shift(); save();
};
document.getElementById('btn-buy').onclick = function(){
    var g = parseInt(document.getElementById('sg').value);
    if(isNaN(g)||g<100000) return;
    var t = g/rate; if(t>U.tn) return;
    U.tn-=t; U.g+=g; DB.tot+=g; DB.h.push(rate); if(DB.h.length>30) DB.h.shift(); save();
};

// ПРОМОКОД
document.getElementById('btn-promo').onclick = function(){
    var c = document.getElementById('pcode').value.trim() || prompt('🎁 Код:');
    if(!c) return;
    var p = DB.p.find(function(x){return x.c===c.toUpperCase()});
    if(!p){alert('❌ Не найден');return;}
    if(p.u.includes(uid)){alert('⚠️ Уже использован');return;}
    if(p.u.length>=p.m){alert('⚠️ Закончился');return;}
    p.u.push(uid); U.g+=p.g; save(); alert('🎁 +'+p.g+' GMS!');
};
document.getElementById('btn-pc').onclick = function(){
    var c=document.getElementById('pcc').value.trim().toUpperCase(),g=parseInt(document.getElementById('pcg').value),m=parseInt(document.getElementById('pcm').value);
    if(!c||!g||!m) return;
    DB.p.push({c:c,g:g,m:m,u:[]}); save(); alert('✅');
};

// VIP ДОБАВИТЬ
document.getElementById('btn-va').onclick = function(){
    var n=document.getElementById('vn').value.trim(),p=parseFloat(document.getElementById('vp').value),g=parseInt(document.getElementById('vg').value);
    if(!n||!p||!g) return;
    DB.v.push({n:n,p:p,g:g}); save(); alert('✅');
};

// ЗАДАНИЕ ДОБАВИТЬ
document.getElementById('btn-ta').onclick = function(){
    var l=document.getElementById('tlk').value.trim(),g=parseInt(document.getElementById('tg').value);
    if(!l.startsWith('t.me/')||!g) return;
    DB.t.push({id:Date.now().toString(),ty:document.getElementById('tt').value,lk:l,gs:g}); save(); alert('✅');
};

// АДМИН
document.getElementById('btn-as').onclick = function(){
    var id=document.getElementById('ai').value.trim(),dg=parseInt(document.getElementById('ag').value)||0,dt=parseFloat(document.getElementById('at').value)||0;
    if(!id) return;
    if(!DB.u[id]) DB.u[id]={g:0,tn:0,cl:0,clv:0,plv:0,bm:1,be:0,dn:[],up:[],dd:0,dt:0};
    DB.u[id].g+=dg; DB.u[id].tn+=dt;
    if(id==uid) U=DB.u[id];
    save(); alert('✅');
};

// КОПИРОВАТЬ
document.getElementById('btn-copy').onclick = function(){ navigator.clipboard.writeText(WALLET); alert('✅'); };

// ВЫВОД
document.getElementById('btn-wd').onclick = function(){
    var a=parseFloat(document.getElementById('wa').value),w=document.getElementById('ww').value.trim();
    if(isNaN(a)||a<0.01) return;
    var n=a*rate/0.95; if(n>U.g) return alert('Не хватает GMS!');
    if(!w.startsWith('UQ')) return;
    U.g-=n; save(); alert('✅ Вывод '+a.toFixed(2)+' TON');
};

// ГРАФИК
var chart;
function drawChart(){
    var ctx=document.getElementById('chart'); if(!ctx) return;
    if(chart) chart.destroy();
    chart=new Chart(ctx,{type:'line',data:{labels:DB.h.map(function(){return''}),datasets:[{data:DB.h,borderColor:'#7c3aed',backgroundColor:'rgba(124,58,237,.08)',fill:true,tension:.4,pointRadius:0,borderWidth:2}]},options:{responsive:true,maintainAspectRatio:false,plugins:{legend:{display:false}},scales:{x:{display:false},y:{display:false}}});
}

// НАВИГАЦИЯ
var navs = {
    'clicker': document.getElementById('nav-clicker'),
    'upgrades': document.getElementById('nav-upgrades'),
    'exchange': document.getElementById('nav-exchange'),
    'bonus': document.getElementById('nav-bonus'),
    'profile': document.getElementById('nav-profile'),
    'admin': document.getElementById('nav-admin')
};

for(var key in navs){
    (function(k){
        navs[k].onclick = function(){
            var pages = document.querySelectorAll('.page');
            for(var i=0;i<pages.length;i++) pages[i].classList.remove('active');
            document.getElementById('page-'+k).classList.add('active');
            for(var n in navs) navs[n].classList.remove('active');
            navs[k].classList.add('active');
        };
    })(key);
}

// ПАССИВ
setInterval(function(){
    if(U.plv>0){ U.g += (1/pit[U.plv-1])*U.bm; DB.tot += (1/pit[U.plv-1]); save(); }
},1000);

// Промокод через шапку
document.querySelector('.promo-btn').onclick = function(){
    var c = prompt('🎁 Промокод:');
    if(!c) return;
    var p = DB.p.find(function(x){return x.c===c.toUpperCase()});
    if(!p){alert('❌');return;}
    if(p.u.includes(uid)){alert('⚠️');return;}
    if(p.u.length>=p.m){alert('⚠️');return;}
    p.u.push(uid); U.g+=p.g; save(); alert('🎁 +'+p.g+' GMS!');
};

upd();
</script>
</body>
</html>
