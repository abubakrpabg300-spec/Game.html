<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>GramTask - Честный Букс</title>
    <!-- Подключаем официальный скрипт Telegram WebApp API -->
    <script src="https://telegram.org/js/telegram-web-app.js"></script>
    <style>
        /* Премиум-стили (Web3 Dark Neon) */
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            -webkit-tap-highlight-color: transparent;
        }

        body {
            background-color: #0B0B16;
            color: #FFFFFF;
            padding-bottom: 80px;
            overflow-x: hidden;
        }

        /* Шапка */
        header {
            background: linear-gradient(135deg, #121225 0%, #0B0B16 100%);
            padding: 20px;
            text-align: center;
            border-bottom: 1px solid rgba(36, 161, 222, 0.2);
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5);
        }

        header h1 {
            font-size: 24px;
            font-weight: 800;
            letter-spacing: 1px;
            background: linear-gradient(90deg, #24A1DE, #00E676);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        /* Контейнеры страниц */
        .page {
            display: none;
            padding: 16px;
            animation: fadeIn 0.3s ease-in-out;
        }

        .page.active {
            display: block;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }

        /* Карточки (Глассморфизм) */
        .card {
            background: rgba(255, 255, 255, 0.03);
            backdrop-filter: blur(10px);
            -webkit-backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.05);
            border-radius: 16px;
            padding: 16px;
            margin-bottom: 16px;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
        }

        .card-title {
            font-size: 18px;
            font-weight: 700;
            margin-bottom: 12px;
            color: #24A1DE;
        }

        /* Внутренние под-вкладки для ЗАДАНИЙ */
        .sub-tabs {
            display: flex;
            background: rgba(255, 255, 255, 0.05);
            padding: 4px;
            border-radius: 30px;
            margin-bottom: 16px;
        }

        .sub-tab {
            flex: 1;
            text-align: center;
            padding: 10px;
            font-size: 14px;
            font-weight: 600;
            border-radius: 25px;
            cursor: pointer;
            transition: all 0.2s ease;
            color: rgba(255, 255, 255, 0.6);
        }

        .sub-tab.active {
            background: #24A1DE;
            color: #fff;
            box-shadow: 0 0 12px rgba(36, 161, 222, 0.4);
        }

        .task-list {
            display: none;
        }

        .task-list.active {
            display: block;
        }

        /* Элемент задания */
        .task-item {
            display: flex;
            justify-content: space-between;
            align-items: center;
            background: rgba(255, 255, 255, 0.02);
            border: 1px solid rgba(255, 255, 255, 0.05);
            padding: 12px;
            border-radius: 12px;
            margin-bottom: 10px;
        }

        .task-info h4 {
            font-size: 15px;
            margin-bottom: 4px;
        }

        .task-reward {
            font-size: 14px;
            color: #00E676;
            font-weight: 700;
        }

        /* Кнопки */
        .btn {
            background: #24A1DE;
            color: #fff;
            border: none;
            padding: 10px 16px;
            border-radius: 8px;
            font-weight: 600;
            cursor: pointer;
            transition: background 0.2s;
        }

        .btn:hover { background: #1a87bc; }
        
        .btn-success { background: #00E676; color: #000; }
        .btn-success:hover { background: #00b35c; }

        .btn-block {
            width: 100%;
            padding: 14px;
            font-size: 16px;
            border-radius: 12px;
            margin-top: 8px;
        }

        /* Формы */
        .form-group {
            margin-bottom: 14px;
        }

        .form-group label {
            display: block;
            font-size: 13px;
            color: rgba(255, 255, 255, 0.6);
            margin-bottom: 6px;
        }

        .form-control {
            width: 100%;
            background: rgba(0, 0, 0, 0.3);
            border: 1px solid rgba(255, 255, 255, 0.1);
            padding: 12px;
            border-radius: 10px;
            color: #fff;
            font-size: 15px;
            outline: none;
        }

        .form-control:focus {
            border-color: #24A1DE;
        }

        /* Ползунок слайдера */
        .range-container {
            margin: 15px 0;
        }

        .range-slider {
            width: 100%;
            -webkit-appearance: none;
            background: rgba(255, 255, 255, 0.1);
            height: 6px;
            border-radius: 5px;
            outline: none;
        }

        .range-slider::-webkit-slider-thumb {
            -webkit-appearance: none;
            width: 20px;
            height: 20px;
            border-radius: 50%;
            background: #24A1DE;
            cursor: pointer;
            box-shadow: 0 0 10px #24A1DE;
        }

        .calc-result {
            display: flex;
            justify-content: space-between;
            background: rgba(36, 161, 222, 0.1);
            padding: 12px;
            border-radius: 8px;
            border: 1px dashed #24A1DE;
            margin-top: 10px;
            font-size: 14px;
        }

        /* Кошелек: карточки балансов */
        .wallet-hub {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 12px;
            margin-bottom: 16px;
        }

        .balance-card {
            background: linear-gradient(135deg, rgba(255,255,255,0.05) 0%, rgba(255,255,255,0.01) 100%);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 14px;
            padding: 14px;
            text-align: center;
        }

        .balance-label {
            font-size: 12px;
            color: rgba(255, 255, 255, 0.5);
            margin-bottom: 6px;
        }

        .balance-value {
            font-size: 18px;
            font-weight: 800;
            color: #00E676;
        }

        .copy-box {
            background: rgba(0,0,0,0.4);
            padding: 10px;
            border-radius: 8px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-size: 13px;
            border: 1px solid rgba(255,255,255,0.05);
            cursor: pointer;
            margin-top: 6px;
        }

        /* Таббар */
        nav {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            background: #111122;
            border-top: 1px solid rgba(255, 255, 255, 0.08);
            display: flex;
            justify-content: space-around;
            padding: 10px 0;
            z-index: 1000;
            box-shadow: 0 -4px 20px rgba(0,0,0,0.4);
        }

        .nav-item {
            display: flex;
            flex-direction: column;
            align-items: center;
            color: rgba(255, 255, 255, 0.4);
            font-size: 11px;
            font-weight: 500;
            cursor: pointer;
            text-decoration: none;
            width: 20%;
        }

        .nav-item.active {
            color: #24A1DE;
        }

        .nav-icon {
            font-size: 20px;
            margin-bottom: 4px;
        }

        /* Уведомления */
        .toast {
            position: fixed;
            bottom: 90px;
            left: 50%;
            transform: translateX(-50%);
            background: rgba(0, 230, 118, 0.9);
            color: #000;
            padding: 10px 20px;
            border-radius: 20px;
            font-size: 14px;
            font-weight: 600;
            display: none;
            z-index: 2000;
            box-shadow: 0 4px 15px rgba(0,230,118,0.3);
        }
    </style>
</head>
<body>

    <div id="toast" class="toast">Скопировано! 📋</div>

    <!-- 1. СТРАНИЦА: ЗАДАНИЯ -->
    <div id="page-tasks" class="page active">
        <div class="sub-tabs">
            <div class="sub-tab active" onclick="switchSubTab('channels')">📢 Каналы</div>
            <div class="sub-tab" onclick="switchSubTab('chats')">💬 Чаты</div>
            <div class="sub-tab" onclick="switchSubTab('bots')">🤖 Боты</div>
        </div>

        <div id="list-channels" class="task-list active">
            <div class="task-item">
                <div class="task-info">
                    <h4>Павел Дуров Блог</h4>
                    <span class="task-reward">+0.001 TON</span>
                </div>
                <button class="btn" onclick="executeTask(this, 'https://t.me/durov')">Выполнить</button>
            </div>
        </div>

        <div id="list-chats" class="task-list">
            <div class="task-item">
                <div class="task-info">
                    <h4>Чат Любителей TON</h4>
                    <span class="task-reward">+0.001 TON</span>
                </div>
                <button class="btn" onclick="executeTask(this, 'https://t.me/telegram')">Выполнить</button>
            </div>
        </div>

        <div id="list-bots" class="task-list">
            <div class="task-item">
                <div class="task-info">
                    <h4>Официальный Игровой Бот</h4>
                    <span class="task-reward">+0.001 TON</span>
                </div>
                <button class="btn" onclick="executeTask(this, 'https://t.me/telegram')">Выполнить</button>
            </div>
        </div>
    </div>

    <!-- 2. СТРАНИЦА: РЕКЛАМА -->
    <div id="page-advertise" class="page">
        <div class="card">
            <div class="card-title">Создать кампанию</div>
            <div class="form-group">
                <label>Тип продвижения</label>
                <select class="form-control" id="ad-type">
                    <option value="channel">📢 Подписка на Канал</option>
                    <option value="chat">💬 Вступление в Чат</option>
                    <option value="bot">🤖 Запуск Бота</option>
                </select>
            </div>
            <div class="form-group">
                <label>Ссылка на ваш ресурс</label>
                <input type="text" class="form-control" id="ad-link" placeholder="https://t.me/...">
            </div>
            <div class="form-group">
                <label>ID ресурса (для автопроверки ботом)</label>
                <input type="text" class="form-control" id="ad-chatid" placeholder="-100xxxxxxxxx">
            </div>
            <div class="range-container">
                <label style="font-size:13px; color:rgba(255,255,255,0.6)">Количество выполнений (500 - 5000)</label>
                <input type="range" class="range-slider" id="ad-count" min="500" max="5000" step="500" value="500" oninput="updateAdCalc()">
                <div class="calc-result">
                    <span>Выполнений: <strong id="view-count">500</strong></span>
                    <span>Стоимость: <strong id="view-cost" style="color:#00E676">0.5 TON</strong></span>
                </div>
            </div>
            <p style="font-size: 11px; color: rgba(255,255,255,0.4); margin: 10px 0;">
                ⚠️ Обязательно добавьте нашего бота в админы вашего канала/чата для автоматических проверок!
            </p>
            <button class="btn btn-success btn-block" onclick="createAdCampaign()">Запустить рекламу</button>
        </div>
    </div>

    <!-- 3. СТРАНИЦА: КОШЕЛЕК -->
    <div id="page-wallet" class="page">
        <div class="wallet-hub">
            <div class="balance-card">
                <div class="balance-label">Заработано</div>
                <div class="balance-value" id="user-balance">0.000 TON</div>
            </div>
            <div class="balance-card">
                <div class="balance-label">Для рекламы</div>
                <div class="balance-value" id="advert-balance" style="color:#24A1DE">0.000 TON</div>
            </div>
        </div>

        <div class="card">
            <div class="card-title">Вывод средств</div>
            <div class="form-group">
                <label>Адрес TON кошелька</label>
                <input type="text" class="form-control" placeholder="UQ...">
            </div>
            <div class="form-group">
                <label>Сумма вывода (мин. 0.5 TON)</label>
                <input type="number" class="form-control" placeholder="0.5">
            </div>
            <button class="btn btn-block" onclick="showNotification('Заявка отправлена администратору!')">Вывести</button>
        </div>

        <div class="card">
            <div class="card-title">Пополнение рекламного баланса</div>
            <p style="font-size:13px; color:rgba(255,255,255,0.7); margin-bottom:10px;">Переведите TON на адрес кошелька проекта. В поле комментарий укажите ваш ID!</p>
            <label style="font-size:12px; color:rgba(255,255,255,0.5)">Адрес для перевода</label>
            <div class="copy-box" onclick="copyText('EQA_YOUR_PROJECT_WALLET_HERE_CHANGE_IT')">
                <span>EQA_YOUR_PROJECT_WALLET...</span>
                <span style="color:#24A1DE; font-weight:600;">КОПИРОВАТЬ</span>
            </div>
            <label style="font-size:12px; color:rgba(255,255,255,0.5); margin-top:10px; display:block;">Ваш ID для комментария</label>
            <div class="copy-box" onclick="copyText(document.getElementById('my-tg-id').innerText)">
                <span id="my-tg-id" style="font-weight:700; color:#00E676;">8684827145</span>
                <span style="color:#24A1DE; font-weight:600;">КОПИРОВАТЬ</span>
            </div>
        </div>
    </div>

    <!-- 4. СТРАНИЦА: РЕФЕРАЛЫ -->
    <div id="page-referrals" class="page">
        <div class="card" style="text-align: center;">
            <div class="card-title">Партнерская сеть</div>
            <p style="font-size: 15px; margin-bottom: 15px;">Получайте <strong style="color:#00E676; font-size:18px;">20%</strong> от чистого заработка ваших рефералов!</p>
            <label style="font-size:12px; color:rgba(255,255,255,0.5); text-align:left; display:block;">Реферальная ссылка</label>
            <div class="copy-box" id="ref-box-container">
                <span id="ref-link-text">https://t.me/YourBot?start=8684827145</span>
                <span style="color:#24A1DE; font-weight:600;" onclick="copyText(document.getElementById('ref-link-text').innerText)">КОПИРОВАТЬ</span>
            </div>
        </div>
    </div>

    <!-- 5. СТРАНИЦА: СКРЫТАЯ АДМИНКА -->
    <div id="page-admin" class="page">
        <div class="card">
            <div class="card-title" style="color:#FF1744">Панель Управления Проектом 👑</div>
            <div style="border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom:14px; margin-bottom:14px;">
                <label>Изменить баланс пользователя (TON)</label>
                <input type="text" class="form-control" placeholder="ID Telegram игрока" style="margin-top:6px;">
                <input type="number" class="form-control" placeholder="Сумма TON" style="margin-top:6px;">
                <div style="display:flex; gap:10px; margin-top:8px;">
                    <button class="btn btn-success" style="flex:1" onclick="showNotification('Баланс успешно начислен!')">Начислить</button>
                    <button class="btn" style="flex:1; background:#FF1744;" onclick="showNotification('Баланс успешно списан!')">Снять</button>
                </div>
            </div>
            <div style="border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom:14px; margin-bottom:14px;">
                <label>Блокировка / Разблокировка по ID</label>
                <input type="text" class="form-control" placeholder="ID юзера" style="margin-top:6px;">
                <div style="display:flex; gap:10px; margin-top:8px;">
                    <button class="btn" style="flex:1; background:#FF1744;" onclick="showNotification('Пользователь забанен!')">ЗАБАНТЬ</button>
                    <button class="btn btn-success" style="flex:1" onclick="showNotification('Пользователь разбанен!')">РАЗБАНТЬ</button>
                </div>
            </div>
            <div>
                <label>Добавить бесплатное задание</label>
                <input type="text" class="form-control" placeholder="Название" style="margin-top:6px;">
                <input type="text" class="form-control" placeholder="Ссылка (https://...)" style="margin-top:6px;">
                <button class="btn btn-block" onclick="showNotification('Админское задание успешно добавлено!')">Создать Бесплатно</button>
            </div>
        </div>
    </div>

    <!-- МЕНЮ НАВИГАЦИИ -->
    <nav>
        <div class="nav-item active" onclick="switchPage('tasks', this)">
            <div class="nav-icon">📋</div>
            <span>Задания</span>
        </div>
        <div class="nav-item" onclick="switchPage('advertise', this)">
            <div class="nav-icon">📣</div>
            <span>Реклама</span>
        </div>
        <div class="nav-item" onclick="switchPage('wallet', this)">
            <div class="nav-icon">💰</div>
            <span>Кошелёк</span>
        </div>
        <div class="nav-item" onclick="switchPage('referrals', this)">
            <div class="nav-icon">👥</div>
            <span>Рефы</span>
        </div>
        <div class="nav-item" id="nav-admin-btn" onclick="switchPage('admin', this)">
            <div class="nav-icon">⚙️</div>
            <span>Админ</span>
        </div>
    </nav>

    <script>
        // Инициализация при старте
        document.addEventListener("DOMContentLoaded", function() {
            const adminBtn = document.getElementById('nav-admin-btn');
            // Изначально прячем админку
            adminBtn.style.display = 'none';

            // Твой жестко зафиксированный ID создателя
            const MY_ADMIN_ID = 8684827145;

            if (window.Telegram && window.Telegram.WebApp) {
                const tg = window.Telegram.WebApp;
                tg.ready();
                tg.expand(); // Открываем WebApp на весь экран телефона
                
                const user = tg.initDataUnsafe ? tg.initDataUnsafe.user : null;
                if (user) {
                    // Подставляем ID текущего юзера
                    document.getElementById('my-tg-id').innerText = user.id;
                    document.getElementById('ref-link-text').innerText = "https://t.me/YourBot?start=r" + user.id;
                    
                    // Если зашел именно ТЫ — открываем админку!
                    if (user.id === MY_ADMIN_ID) {
                        adminBtn.style.display = 'flex';
                        showNotification("Приветствую, Владелец! Панель открыта 👑");
                    }
                }
            } else {
                // Если открыто на ПК в обычном браузере — показываем для тестов
                adminBtn.style.display = 'flex';
            }
        });

        function switchPage(pageId, element) {
            document.querySelectorAll('.page').forEach(p => p.classList.remove('active'));
            document.getElementById('page-' + pageId).classList.add('active');
            document.querySelectorAll('.nav-item').forEach(i => i.classList.remove('active'));
            element.classList.add('active');
        }

        function switchSubTab(category) {
            document.querySelectorAll('.sub-tab').forEach(t => t.classList.remove('active'));
            document.querySelectorAll('.task-list').forEach(l => l.classList.remove('active'));
            event.target.classList.add('active');
            document.getElementById('list-' + category).classList.add('active');
        }

        function executeTask(button, url) {
            window.open(url, '_blank');
            button.innerHTML = "Проверить";
            button.className = "btn btn-success";
            button.onclick = function() {
                button.innerHTML = "Проверка...";
                button.disabled = true;
                setTimeout(() => {
                    showNotification("Задание выполнено! +0.001 TON");
                    button.parentElement.remove();
                }, 1200);
            };
        }

        function updateAdCalc() {
            const count = document.getElementById('ad-count').value;
            document.getElementById('view-count').innerText = count;
            document.getElementById('view-cost').innerText = (count / 1000) + " TON";
        }

        function createAdCampaign() {
            if(!document.getElementById('ad-link').value || !document.getElementById('ad-chatid').value) {
                alert("Заполните поля!");
                return;
            }
            showNotification("Реклама отправлена на проверку!");
        }

        function copyText(text) {
            navigator.clipboard.writeText(text).then(() => {
                const toast = document.getElementById('toast');
                toast.innerText = "Скопировано в буфер! 📋";
                toast.style.display = 'block';
                setTimeout(() => toast.style.display = 'none', 1500);
            });
        }

        function showNotification(msg) {
            const toast = document.getElementById('toast');
            toast.innerText = msg;
            toast.style.display = 'block';
            setTimeout(() => toast.style.display = 'none', 2500);
        }
    </script>
</body>
</html>
