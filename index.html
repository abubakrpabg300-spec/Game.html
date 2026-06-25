<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Miner ZZ</title>
    <script src="https://telegram.org/js/telegram-web-app.js"></script>
    <style>
        :root {
            --bg-color: #080810;
            --panel-color: #121225;
            --accent-cyan: #00f2fe;
            --accent-blue: #4facfe;
            --crypto-green: #00e676;
            --crypto-red: #ff1744;
            --text-main: #ffffff;
            --text-gray: #85859e;
        }

        * { box-sizing: border-box; user-select: none; -webkit-user-select: none; }
        body { 
            margin: 0; 
            padding: 0; 
            font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; 
            background-color: var(--bg-color); 
            color: var(--text-main); 
            overflow: hidden;
        }

        /* Главный контейнер скролла */
        .app-container {
            height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }

        /* Общий анимированный верхний баланс */
        .top-bar {
            text-align: center;
            padding: 20px 15px 10px 15px;
            background: linear-gradient(to bottom, rgba(18,18,37,0.8), transparent);
            position: relative;
        }
        .main-balance {
            font-size: 32px;
            font-weight: 800;
            background: linear-gradient(45deg, var(--accent-cyan), var(--accent-blue));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-shadow: 0 0 20px rgba(0, 242, 254, 0.3);
            letter-spacing: 1px;
        }
        .balance-label {
            font-size: 12px;
            color: var(--text-gray);
            text-transform: uppercase;
            letter-spacing: 2px;
            margin-top: 4px;
        }

        /* Кнопка ТОП-Кубок */
        .top-cup-btn {
            position: absolute;
            top: 20px;
            right: 20px;
            background: var(--panel-color);
            border: 1px solid rgba(0, 242, 254, 0.3);
            border-radius: 50%;
            width: 45px;
            height: 45px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 22px;
            cursor: pointer;
            box-shadow: 0 4px 10px rgba(0,0,0,0.3);
            animation: pulse 2s infinite;
        }

        @keyframes pulse {
            0% { transform: scale(1); box-shadow: 0 0 0 0 rgba(0, 242, 254, 0.4); }
            70% { transform: scale(1.05); box-shadow: 0 0 0 10px rgba(0, 242, 254, 0); }
            100% { transform: scale(1); box-shadow: 0 0 0 0 rgba(0, 242, 254, 0); }
        }

        /* Контент вкладок */
        .tab-content { 
            display: none; 
            flex-gradient: 1;
            padding: 15px; 
            overflow-y: auto; 
            height: calc(100vh - 160px);
        }
        .active-tab { display: block; }

        /* Стиль карточек-панелей */
        .card {
            background: var(--panel-color);
            border-radius: 20px;
            padding: 20px;
            margin-bottom: 15px;
            border: 1px solid rgba(255,255,255,0.03);
            box-shadow: 0 8px 24px rgba(0,0,0,0.2);
        }

        /* РАЗДЕЛ МАЙНЕР (Новый Дизайн) */
        .miner-wrapper {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 65%;
        }
        .miner-glow-circle {
            width: 230px;
            height: 230px;
            border-radius: 50%;
            background: radial-gradient(circle, #1e1e38 0%, #0d0d1a 100%);
            border: 6px solid #1c1c3a;
            box-shadow: 0 0 40px rgba(79, 172, 254, 0.2), inset 0 0 20px rgba(0, 242, 254, 0.1);
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            position: relative;
            transition: transform 0.05s ease-in-out;
        }
        .miner-glow-circle:active {
            transform: scale(0.94);
            border-color: var(--accent-cyan);
            box-shadow: 0 0 50px rgba(0, 242, 254, 0.5);
        }
        .miner-glow-circle span {
            font-size: 90px;
            filter: drop-shadow(0 0 15px rgba(0, 242, 254, 0.6));
        }

        /* Кнопки */
        .btn {
            background: linear-gradient(135deg, var(--accent-blue), var(--accent-cyan));
            color: #000;
            border: none;
            border-radius: 14px;
            padding: 15px 20px;
            font-size: 16px;
            font-weight: 700;
            width: 100%;
            cursor: pointer;
            box-shadow: 0 4px 15px rgba(0, 242, 254, 0.2);
            transition: all 0.2s;
        }
        .btn:active { transform: scale(0.98); opacity: 0.9; }
        .btn-secondary { background: #222244; color: var(--text-main); box-shadow: none; }
        .btn-danger { background: linear-gradient(135deg, var(--crypto-red), #b3002d); color: white; box-shadow: none; }
        .btn-success { background: linear-gradient(135deg, var(--crypto-green), #009943); color: black; box-shadow: none; }

        /* Поля ввода */
        input {
            width: 100%;
            background: #1a1a36;
            border: 1px solid rgba(255,255,255,0.08);
            padding: 14px;
            border-radius: 12px;
            color: white;
            font-size: 15px;
            margin: 10px 0;
            outline: none;
        }
        input:focus { border-color: var(--accent-cyan); }

        /* Японские Свечи (График) */
        .candles-container {
            height: 180px;
            display: flex;
            align-items: flex-end;
            justify-content: space-between;
            padding: 20px 10px;
            background: #0b0b16;
            border-radius: 15px;
            border-bottom: 2px solid #222244;
            margin: 15px 0;
            position: relative;
        }
        .candle {
            display: flex;
            flex-direction: column;
            align-items: center;
            width: 8%;
            height: 100%;
            justify-content: center;
            position: relative;
        }
        .wick {
            width: 2px;
            background-color: var(--text-gray);
            position: absolute;
            height: 80%;
        }
        .candle-body {
            width: 100%;
            border-radius: 3px;
            z-index: 2;
        }
        .candle.up .candle-body { background-color: var(--crypto-green); box-shadow: 0 0 8px var(--crypto-green); }
        .candle.down .candle-body { background-color: var(--crypto-red); box-shadow: 0 0 8px var(--crypto-red); }

        /* Список Лидерборда / Рефералов */
        .list-item {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 12px 0;
            border-bottom: 1px solid rgba(255,255,255,0.05);
        }
        .list-item:last-child { border-bottom: none; }

        /* Всплывающее окно ТОР-100 */
        .modal-overlay {
            display: none;
            position: fixed;
            top: 0; left: 0; right: 0; bottom: 0;
            background: rgba(0,0,0,0.85);
            z-index: 100;
            backdrop-filter: blur(8px);
        }
        .modal-box {
            position: fixed;
            bottom: 0; left: 0; right: 0;
            background: var(--panel-color);
            border-top-left-radius: 30px;
            border-top-right-radius: 30px;
            padding: 25px 20px;
            max-height: 80vh;
            overflow-y: auto;
            border-top: 2px solid rgba(0, 242, 254, 0.2);
        }
        .modal-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 20px;
        }

        /* Нижнее меню */
        .nav-bar {
            height: 75px;
            background: #0f0f22;
            border-top: 1px solid rgba(255,255,255,0.05);
            display: flex;
            justify-content: space-around;
            align-items: center;
            padding-bottom: env(safe-area-inset-bottom);
        }
        .nav-btn {
            display: flex;
            flex-direction: column;
            align-items: center;
            color: var(--text-gray);
            font-size: 11px;
            font-weight: 500;
            cursor: pointer;
            width: 16%;
            transition: color 0.2s;
        }
        .nav-btn span { font-size: 22px; margin-bottom: 4px; transition: transform 0.2s; }
        .nav-btn.active { color: var(--accent-cyan); }
        .nav-btn.active span { transform: translateY(-2px); text-shadow: 0 0 10px var(--accent-cyan); }
        
        /* Скрытие админки по умолчанию */
        #adminTabBtn { display: none; }
    </style>
</head>
<body>

    <div class="app-container">
        
        <div class="top-bar">
            <div class="main-balance" id="topBalance">0</div>
            <div class="balance-label">Баланс Монет ZZ</div>
            <div class="top-cup-btn" onclick="openLeaderboard()">🏆</div>
        </div>

        <div id="minerTab" class="tab-content active-tab">
            <div class="miner-wrapper">
                <div class="miner-glow-circle" id="clickButton">
                    <span>⛏️</span>
                </div>
            </div>
            <div class="card" style="margin-top: 20px;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <div>
                        <div style="font-weight: bold; font-size: 16px;">Мультиклик</div>
                        <div style="color: var(--text-gray); font-size: 13px;">Уровень <span id="minerLvl">1</span></div>
                    </div>
                    <button class="btn" style="width: auto; padding: 10px 20px;" onclick="upgradeMiner()">Прокачать (-1000)</button>
                </div>
            </div>
        </div>

        <div id="tasksTab" class="tab-content">
            <h2 style="margin-top: 0;">Задания проекта</h2>
            <div class="card" style="background: linear-gradient(135deg, #1c1c3a, #0f0f22); border-left: 4px solid var(--accent-cyan);">
                <div style="font-weight: bold; color: var(--accent-cyan);">🔥 Реферальный бонус</div>
                <div style="font-size: 14px; margin-top: 5px; color: var(--text-gray);">Приглашай друзей и забирай по <span style="color: #fff; font-weight: bold;">1 000 ZZ</span> за каждого!</div>
            </div>
            
            <div id="tasksContainer">
                <div class="card" id="task-default">
                    <div style="font-weight: bold; font-size: 16px; margin-bottom: 5px;">Вступить в официальное сообщество</div>
                    <div style="color: var(--crypto-green); font-size: 14px; font-weight: bold; margin-bottom: 15px;">+2500 ZZ</div>
                    <button class="btn btn-secondary" id="btn-task-default" onclick="handleTaskClick('task-default', 'https://t.me/miner_zz_bot', 2500)">Выполнить задание</button>
                </div>
            </div>
        </div>

        <div id="refsTab" class="tab-content">
            <h2 style="margin-top: 0;">Реферальная система</h2>
            <div class="card">
                <div style="font-size: 14px; color: var(--text-gray); margin-bottom: 8px;">Твоя персональная ссылка:</div>
                <input type="text" id="referralLinkInput" readonly value="Загрузка...">
                <button class="btn btn-success" style="margin-top: 5px;" onclick="copyReferralLink()">Копировать ссылку</button>
            </div>

            <h3>Приглашенные друзья (<span id="refCount">0</span>)</h3>
            <div class="card" id="refsList">
                <div style="color: var(--text-gray); text-align: center; padding: 10px 0;">У тебя пока нет рефералов</div>
            </div>
        </div>

        <div id="balanceTab" class="tab-content">
            <h2 style="margin-top: 0;">Крипто-Кошелек</h2>
            <div class="card" style="text-align: center; padding: 30px 20px;">
                <div style="font-size: 14px; color: var(--text-gray); text-transform: uppercase;">Доступные активы</div>
                <h1 style="font-size: 36px; margin: 15px 0; color: #ffd700;" id="walletCoinsDisplay">0 ZZ</h1>
                
                <div style="display: flex; gap: 15px; margin-top: 25px;">
                    <button class="btn btn-success" style="flex: 1;" onclick="walletAlert()">Ввод</button>
                    <button class="btn btn-danger" style="flex: 1;" onclick="walletAlert()">Вывод</button>
                </div>
                <p style="color: var(--text-gray); font-size: 13px; margin-top: 20px; line-height: 1.4;">
                    ℹ️ Функции ввода и вывода средств станут активными сразу после прохождения официального листинга монеты ZZ на биржах.
                </p>
            </div>
        </div>

        <div id="priceTab" class="tab-content">
            <h2 style="margin-top: 0;">Рыночный курс ZZ / TON</h2>
            <div class="card">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <div>
                        <div style="color: var(--text-gray); font-size: 13px;">Текущая цена 1 ZZ:</div>
                        <div style="font-size: 20px; font-weight: bold; color: var(--accent-cyan);" id="currentPriceDisplay">0.00000010 TON</div>
                    </div>
                    <div style="text-align: right;">
                        <div style="color: var(--crypto-green); font-weight: bold; font-size: 16px;" id="growthPercentDisplay">+0.00% 🚀</div>
                        <div style="color: var(--text-gray); font-size: 12px;">Ликвидность растет</div>
                    </div>
                </div>

                <div class="candles-container">
                    <div class="candle up" style="height: 60%;"><div class="wick" style="height: 120%;"></div><div class="candle-body" style="height: 40px;"></div></div>
                    <div class="candle down" style="height: 55%;"><div class="wick" style="height: 110%;"></div><div class="candle-body" style="height: 25px;"></div></div>
                    <div class="candle up" style="height: 70%;"><div class="wick" style="height: 130%;"></div><div class="candle-body" style="height: 50px;"></div></div>
                    <div class="candle up" style="height: 80%;"><div class="wick" style="height: 140%;"></div><div class="candle-body" style="height: 35px;"></div></div>
                    <div class="candle down" style="height: 72%;"><div class="wick" style="height: 115%;"></div><div class="candle-body" style="height: 20px;"></div></div>
                    <div class="candle up" style="height: 90%;" id="liveCandle"><div class="wick" style="height: 130%;"></div><div class="candle-body" style="height: 55px;"></div></div>
                </div>

                <div style="background: #111122; padding: 15px; border-radius: 12px; margin-top: 15px;">
                    <div style="font-size: 14px; color: var(--text-gray);">Оценка твоего капитала:</div>
                    <div style="font-size: 24px; font-weight: bold; color: var(--crypto-green); margin-top: 5px;"><span id="tonCapitalDisplay">0.0000</span> TON</div>
                    <div style="font-size: 12px; color: var(--text-gray); margin-top: 4px;">Расчет по формуле: 1 000 000 ZZ = 1 TON (с учетом динамики цен)</div>
                </div>
            </div>
        </div>

        <div id="adminTab" class="tab-content">
            <h2 style="margin-top: 0; color: var(--crypto-red);">Центр Управления Админа</h2>
            
            <div class="card">
                <h3>Глобальный эмиссионный баланс</h3>
                <input type="number" id="adminCoinsAmount" placeholder="Количество монет ZZ">
                <div style="display: gap; flex-direction: row; gap: 10px; display: flex;">
                    <button class="btn btn-success" onclick="adminModifyCoins(true)">Начислить всем</button>
                    <button class="btn btn-danger" onclick="adminModifyCoins(false)">Снять у всех</button>
                </div>
            </div>

            <div class="card">
                <h3>Создать моментальное задание</h3>
                <input type="text" id="newAdminTaskName" placeholder="Название задания (например: Подписка на чат)">
                <input type="text" id="newAdminTaskLink" placeholder="Ссылка на Telegram (https://t.me/...)">
                <input type="number" id="newAdminTaskReward" placeholder="Сумма награды в ZZ">
                <button class="btn" onclick="adminCreateCustomTask()">Запустить задание</button>
            </div>

            <div class="card">
                <h3>Активные заявки на вывод средств</h3>
                <div style="color: var(--text-gray); font-size: 14px; text-align: center; padding: 10px 0;">
                    📭 Список пуст. Игроки не могут отправлять заявки до проведения листинга.
                </div>
            </div>
        </div>

        <div class="nav-bar">
            <div class="nav-btn active" onclick="switchTab('minerTab', this)"><span>⛏️</span>Майнер</div>
            <div class="nav-btn" onclick="switchTab('tasksTab', this)"><span>📋</span>Задания</div>
            <div class="nav-btn" onclick="switchTab('refsTab', this)"><span>👥</span>Рефы</div>
            <div class="nav-btn" onclick="switchTab('balanceTab', this)"><span>💰</span>Баланс</div>
            <div class="nav-btn" onclick="switchTab('priceTab', this)"><span>📈</span>Курс</div>
            <div class="nav-btn" id="adminTabBtn" onclick="switchTab('adminTab', this)"><span>⚙️</span>Админ</div>
        </div>

    </div>

    <div class="modal-overlay" id="leaderboardModal">
        <div class="modal-box">
            <div class="modal-header">
                <h2 style="margin: 0; background: linear-gradient(to right, #ffd700, #ffb300); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">🏆 Зал славы ZZ (Топ 100)</h2>
                <div style="font-size: 24px; cursor: pointer; color: var(--text-gray);" onclick="closeLeaderboard()">✕</div>
            </div>
            <p style="color: var(--text-gray); font-size: 13px; margin-bottom: 20px;">Список обновляется в реальном времени. Призовые места определяются исключительно по количеству добытых монет.</p>
            <div id="leaderboardList">
                </div>
        </div>
    </div>

    <script>
        // Инициализация Telegram WebApp
        const tg = window.Telegram?.WebApp;
        if (tg) {
            tg.expand();
            tg.ready();
        }

        // ДАННЫЕ ПРИЛОЖЕНИЯ (Стартовые значения)
        const MASTER_ADMIN_ID = 8684827145; 
        let userTelegramId = 0;
        let userTelegramName = "Игрок (Вы)";

        let balance = 386808852018; // Красивое стартовое число как на скринах
        let clickPower = 1;
        let minerLevel = 1;
        
        // Переменные для динамики курса
        let totalClicksEver = 0;
        let basePriceTON = 0.0000001; 
        let currentPriceTON = 0.0000001;

        // Получение данных пользователя из Телеграм
        if (tg && tg.initDataUnsafe && tg.initDataUnsafe.user) {
            userTelegramId = tg.initDataUnsafe.user.id;
            userTelegramName = tg.initDataUnsafe.user.first_name || "Пользователь";
        } else {
            // Фейковый ID для тестов в обычном веб-браузере
            userTelegramId = 8684827145; 
        }

        // Защита админки: Показываем панель строго владельцу ID
        if (userTelegramId === MASTER_ADMIN_ID) {
            document.getElementById('adminTabBtn').style.display = 'flex';
        }

        // Генерация реферальной ссылки
        const refLink = `https://t.me/miner_zz_bot?start=ref${userTelegramId}`;
        document.getElementById('referralLinkInput').value = refLink;

        // ОБНОВЛЕНИЕ ИНТЕРФЕЙСА
        function refreshUI() {
            document.getElementById('topBalance').innerText = balance.toLocaleString('ru-RU');
            document.getElementById('walletCoinsDisplay').innerText = balance.toLocaleString('ru-RU') + " ZZ";
            
            // Расчет и обновление курса
            let growth = (totalClicksEver * 0.00002); // 1 клик = небольшой рост курса
            let growthPercent = (growth * 100);
            currentPriceTON = basePriceTON + (basePriceTON * growth);

            document.getElementById('currentPriceDisplay').innerText = currentPriceTON.toFixed(8) + " TON";
            document.getElementById('growthPercentDisplay').innerText = "+" + growthPercent.toFixed(2) + "% 🚀";

            // Расчет капитала в TON
            let tonCapital = (balance / 1000000) * (currentPriceTON / basePriceTON);
            document.getElementById('tonCapitalDisplay').innerText = tonCapital.toFixed(4);
        }

        // КЛИК ПО МАЙНЕРУ
        document.getElementById('clickButton').addEventListener('click', (e) => {
            balance += clickPower;
            totalClicksEver += 1;
            refreshUI();
            
            if (navigator.vibrate) navigator.vibrate(40); // Мягкий тактильный отклик
            animateLiveCandle();
        });

        // Анимация свечи при кликах
        function animateLiveCandle() {
            const liveCandle = document.getElementById('liveCandle');
            if(liveCandle) {
                let randomHeight = Math.min(60 + (totalClicksEver % 40), 100);
                liveCandle.style.height = randomHeight + "%";
            }
        }

        // АПГРЕЙД МАЙНЕРА
        function upgradeMiner() {
            if (balance >= 1000) {
                balance -= 1000;
                minerLevel += 1;
                clickPower += 1;
                document.getElementById('minerLvl').innerText = minerLevel;
                refreshUI();
                alert("Уровень клика повышен! Теперь вы добываете больше за один тап.");
            } else {
                alert("Недостаточно монет ZZ для проведения апгрейда.");
            }
        }

        // ПЕРЕКЛЮЧЕНИЕ ВКЛАДОК
        function switchTab(tabId, element) {
            document.querySelectorAll('.tab-content').forEach(tab => tab.classList.remove('active-tab'));
            document.getElementById(tabId).classList.add('active-tab');
            
            document.querySelectorAll('.nav-btn').forEach(btn => btn.classList.remove('active'));
            element.classList.add('active');
        }

        // КОПИРОВАНИЕ ССЫЛКИ
        function copyReferralLink() {
            const input = document.getElementById('referralLinkInput');
            input.select();
            document.execCommand('copy');
            alert("Ваша реферальная ссылка скопирована в буфер обмена!");
            
            // Имитация добавления реферала для демонстрации списка
            addFakeReferral();
        }

        // Имитация добавления друга
        let fakeRefsCount = 0;
        function addFakeReferral() {
            fakeRefsCount++;
            balance += 1000; // Награда за друга
            refreshUI();

            document.getElementById('refCount').innerText = fakeRefsCount;
            const refsList = document.getElementById('refsList');
            
            if(fakeRefsCount === 1) refsList.innerHTML = ''; // Очищаем дефолтную надпись
            
            refsList.innerHTML += `
                <div class="list-item">
                    <div style="font-weight:bold;">👤 Друг #${fakeRefsCount} (ID: ${Math.floor(100000 + Math.random() * 900000)})</div>
                    <div style="color: var(--crypto-green);">+1000 ZZ</div>
                </div>
            `;
        }

        // ЛОГИКА ЗАДАНИЙ С ПОДПИСКОЙ И ПРОВЕРКОЙ
        let taskStates = {};
        function handleTaskClick(taskId, link, reward) {
            if (!taskStates[taskId]) {
                // ШАГ 1: Перенаправляем на канал/ссылку
                alert("Переходим к каналу/чату для выполнения подписки. Подпишитесь и возвращайтесь для проверки!");
                window.open(link, '_blank');
                
                // Меняем состояние кнопки на Проверку
                const btn = document.getElementById('btn-' + taskId);
                btn.innerText = "Проверить подписку";
                btn.className = "btn btn-success";
                taskStates[taskId] = 'checking';
            } else if (taskStates[taskId] === 'checking') {
                // ШАГ 2: Имитация проверки подписки
                const btn = document.getElementById('btn-' + taskId);
                btn.innerText = "Сверка данных...";
                btn.disabled = true;
                
                setTimeout(() => {
                    balance += reward;
                    refreshUI();
                    btn.innerText = "Получено ✓";
                    btn.className = "btn btn-secondary";
                    alert(`Успешно! Награда +${reward} ZZ зачислена на баланс.`);
                    taskStates[taskId] = 'done';
                }, 1500);
            }
        }

        // КОШЕЛЕК ПРЕДУПРЕЖДЕНИЕ
        function walletAlert() {
            alert("Операции ввода и вывода станут доступны сразу после листинга монеты ZZ на криптовалютных биржах!");
        }

        // ФУНКЦИИ АДМИНИСТРАТОРА
        function adminModifyCoins(isAdd) {
            const amountInput = document.getElementById('adminCoinsAmount');
            const value = Number(amountInput.value);
            if (!value || value <= 0) {
                alert("Введите корректное число монет!");
                return;
            }
            if (isAdd) {
                balance += value;
                alert(`Успешно! Всем игрокам (включая ваш баланс) начислено ${value} ZZ`);
            } else {
                balance = Math.max(0, balance - value);
                alert(`Успешно! У всех игроков списано ${value} ZZ`);
            }
            refreshUI();
            amountInput.value = '';
        }

        function adminCreateCustomTask() {
            const name = document.getElementById('newAdminTaskName').value;
            const link = document.getElementById('newAdminTaskLink').value || 'https://t.me/';
            const reward = Number(document.getElementById('newAdminTaskReward').value);

            if (!name || !reward) {
                alert("Заполните название задания и сумму награды!");
                return;
            }

            const taskId = 'task-' + Date.now();
            const taskHtml = `
                <div class="card" id="${taskId}">
                    <div style="font-weight: bold; font-size: 16px; margin-bottom: 5px;">${name}</div>
                    <div style="color: var(--crypto-green); font-size: 14px; font-weight: bold; margin-bottom: 15px;">+${reward} ZZ</div>
                    <button class="btn btn-secondary" id="btn-${taskId}" onclick="handleTaskClick('${taskId}', '${link}', ${reward})">Выполнить задание</button>
                </div>
            `;

            document.getElementById('tasksContainer').innerHTML += taskHtml;
            alert("Новое глобальное задание успешно создано и запущено для игроков!");
            
            // Очистка полей
            document.getElementById('newAdminTaskName').value = '';
            document.getElementById('newAdminTaskReward').value = '';
        }

        // МОДАЛЬНОЕ ОКНО ЛИДЕРБОРДА ДО 100 МЕСТ
        function openLeaderboard() {
            const listContainer = document.getElementById('leaderboardList');
            listContainer.innerHTML = ''; // Очистка перед генерацией
            
            // Генерируем 100 мест рейтинга
            // Наш текущий игрок будет стоять на почетном 3-м месте для демонстрации баланса
            for (let i = 1; i <= 100; i++) {
                let name, coinsValue, itemStyle = "";
                
                if (i === 1) {
                    name = "🥇 CryptoKing";
                    coinsValue = 999888777666555;
                } else if (i === 2) {
                    name = "🥈 WhalesHunter";
                    coinsValue = 555444333222111;
                } else if (i === 3) {
                    name = `🥉 ${userTelegramName} (Вы)`;
                    coinsValue = balance;
                    itemStyle = "background: rgba(0, 242, 254, 0.1); padding: 10px; border-radius: 10px; border: 1px solid rgba(0,242,254,0.3);";
                } else {
                    name = `👤 Miner_User_${Math.floor(1000 + Math.random() * 9000)}`;
                    coinsValue = Math.floor(balance / (i * 0.8));
                }

                listContainer.innerHTML += `
                    <div class="list-item" style="${itemStyle}">
                        <div style="font-weight: 600; font-size: 15px;">${i}. ${name}</div>
                        <div style="font-weight: 700; color: var(--accent-cyan); font-size: 14px;">${coinsValue.toLocaleString('ru-RU')} ZZ</div>
                    </div>
                `;
            }

            document.getElementById('leaderboardModal').style.display = 'block';
        }

        function closeLeaderboard() {
            document.getElementById('leaderboardModal').style.display = 'none';
        }

        // Старт системы
        refreshUI();
    </script>
</body>
</html>
