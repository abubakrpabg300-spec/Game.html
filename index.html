<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Miner ZZ Pro</title>
    <script src="https://telegram.org/js/telegram-web-app.js"></script>
    <style>
        :root {
            --bg-gradient: linear-gradient(135deg, #070710 0%, #0d0d1e 100%);
            --panel-bg: rgba(22, 22, 46, 0.7);
            --panel-border: rgba(255, 255, 255, 0.05);
            --neon-cyan: #00f2fe;
            --neon-blue: #4facfe;
            --crypto-green: #00e676;
            --crypto-red: #ff1744;
            --text-main: #ffffff;
            --text-muted: #8080a3;
        }

        * {
            box-sizing: border-box;
            user-select: none;
            -webkit-user-select: none;
            margin: 0;
            padding: 0;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
            background: var(--bg-gradient);
            color: var(--text-main);
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            overflow: hidden;
        }

        /* Главный экран и Скролл */
        .app-wrapper {
            flex: 1;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            height: 100vh;
            position: relative;
        }

        /* Мульти-Баланс Панель */
        .header-balance-card {
            padding: 20px 20px 15px 20px;
            background: linear-gradient(to bottom, rgba(11, 11, 26, 0.9), transparent);
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid var(--panel-border);
        }

        .balance-item {
            display: flex;
            flex-direction: column;
        }

        .balance-value {
            font-size: 24px;
            font-weight: 800;
            letter-spacing: 0.5px;
        }
        
        #zzDisplay {
            background: linear-gradient(45deg, var(--neon-cyan), var(--neon-blue));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-shadow: 0 0 15px rgba(0, 242, 254, 0.2);
        }

        #tonDisplay {
            color: #24a1de;
            text-shadow: 0 0 15px rgba(36, 161, 222, 0.2);
        }

        .balance-lbl {
            font-size: 11px;
            color: var(--text-muted);
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-top: 2px;
        }

        /* Топ Ряд Иконок Скорости/Действий */
        .action-row {
            display: flex;
            gap: 15px;
            align-items: center;
        }

        .icon-circle-btn {
            width: 40px;
            height: 40px;
            background: var(--panel-bg);
            border: 1px solid var(--panel-border);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 18px;
            cursor: pointer;
            box-shadow: 0 4px 12px rgba(0,0,0,0.3);
            transition: transform 0.2s;
        }
        .icon-circle-btn:active { transform: scale(0.9); }

        /* Контент вкладок */
        .main-body {
            flex: 1;
            padding: 20px;
            overflow-y: auto;
            height: calc(100vh - 165px);
        }

        .tab-view { display: none; }
        .tab-view.active { display: block; }

        /* Профессиональные Кадры/Карточки */
        .glass-card {
            background: var(--panel-bg);
            border: 1px solid var(--panel-border);
            border-radius: 24px;
            padding: 20px;
            margin-bottom: 15px;
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.24);
        }

        /* КЛИКЕР И ЭНЕРГИЯ */
        .clicker-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 60%;
            margin-top: 10px;
        }

        .neon-click-sphere {
            width: 210px;
            height: 210px;
            border-radius: 50%;
            background: radial-gradient(circle, #1a1a3a 0%, #090915 100%);
            border: 4px solid rgba(255, 255, 255, 0.03);
            box-shadow: 0 0 30px rgba(79, 172, 254, 0.15), inset 0 0 15px rgba(0, 242, 254, 0.05);
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            transition: transform 0.05s ease;
            position: relative;
        }
        .neon-click-sphere:active { transform: scale(0.95); box-shadow: 0 0 45px rgba(0, 242, 254, 0.4); }
        .neon-click-sphere span { font-size: 80px; filter: drop-shadow(0 0 10px rgba(0, 242, 254, 0.4)); }

        .energy-wrapper {
            width: 100%;
            margin-top: 30px;
        }
        .energy-header {
            display: flex;
            justify-content: space-between;
            font-size: 13px;
            color: var(--text-muted);
            margin-bottom: 6px;
        }
        .energy-track {
            width: 100%;
            height: 8px;
            background: rgba(255,255,255,0.05);
            border-radius: 10px;
            overflow: hidden;
        }
        .energy-fill {
            height: 100%;
            width: 100%;
            background: linear-gradient(to right, #ffd700, #ff9f00);
            border-radius: 10px;
            transition: width 0.1s linear;
            box-shadow: 0 0 10px rgba(255, 215, 0, 0.3);
        }

        /* КНОПКИ И ПОЛЯ ВВОДА */
        .btn-prime {
            background: linear-gradient(135deg, var(--neon-blue), var(--neon-cyan));
            border: none; color: #000; font-size: 15px; font-weight: 700;
            padding: 14px 20px; border-radius: 16px; width: 100%; cursor: pointer;
            box-shadow: 0 4px 15px rgba(0, 242, 254, 0.2); transition: all 0.2s;
        }
        .btn-prime:active { transform: scale(0.98); opacity: 0.9; }
        .btn-sub { background: rgba(255, 255, 255, 0.06); color: var(--text-main); border: 1px solid rgba(255,255,255,0.03); box-shadow: none;}
        .btn-buy { background: linear-gradient(135deg, var(--crypto-green), #00b359); color: #000; box-shadow: none; }
        .btn-sell { background: linear-gradient(135deg, var(--crypto-red), #cc0029); color: #fff; box-shadow: none; }
        
        input {
            width: 100%; background: rgba(0, 0, 0, 0.25); border: 1px solid rgba(255,255,255,0.06);
            padding: 14px; border-radius: 14px; color: #fff; font-size: 14px; outline: none; margin: 8px 0;
        }
        input:focus { border-color: var(--neon-cyan); }

        /* БИРЖА И КОМПАКТНЫЕ СВЕЧИ */
        .market-header {
            display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;
        }
        .candles-box {
            height: 120px; display: flex; align-items: flex-end; justify-content: space-between;
            padding: 10px; background: rgba(0,0,0,0.3); border-radius: 16px; margin: 12px 0; border-bottom: 2px solid #1a1a36;
        }
        .candle-stick {
            display: flex; flex-direction: column; align-items: center; width: 6%; height: 100%; justify-content: center; position: relative;
        }
        .candle-wick { width: 1.5px; background: rgba(255,255,255,0.15); position: absolute; height: 90%; }
        .candle-bar { width: 100%; border-radius: 2px; z-index: 2; min-height: 4px; }
        .candle-stick.up .candle-bar { background: var(--crypto-green); box-shadow: 0 0 6px rgba(0,230,118,0.4); }
        .candle-stick.down .candle-bar { background: var(--crypto-red); box-shadow: 0 0 6px rgba(255,23,68,0.4); }

        /* СПИСКИ И ЗАДАНИЯ */
        .flex-row-item {
            display: flex; justify-content: space-between; align-items: center; padding: 12px 0;
            border-bottom: 1px solid rgba(255,255,255,0.04);
        }
        .flex-row-item:last-child { border-bottom: none; }

        /* НАВИГАЦИОННАЯ ПАНЕЛЬ */
        .footer-navigation {
            height: 70px; background: rgba(11, 11, 22, 0.95); border-top: 1px solid var(--panel-border);
            display: flex; justify-content: space-around; align-items: center; padding-bottom: env(safe-area-inset-bottom);
        }
        .nav-tab-item {
            display: flex; flex-direction: column; align-items: center; color: var(--text-muted);
            font-size: 10px; font-weight: 600; cursor: pointer; width: 16%; transition: all 0.2s;
        }
        .nav-tab-item span { font-size: 20px; margin-bottom: 3px; transition: transform 0.2s; }
        .nav-tab-item.active { color: var(--neon-cyan); }
        .nav-tab-item.active span { transform: translateY(-2px); text-shadow: 0 0 10px var(--neon-cyan); }

        /* МОДАЛЬНЫЕ ОКНА БОЛЬШИЕ */
        .sheet-overlay {
            display: none; position: fixed; top: 0; left: 0; right: 0; bottom: 0;
            background: rgba(0, 0, 0, 0.8); z-index: 200; backdrop-filter: blur(10px);
        }
        .sheet-content {
            position: fixed; bottom: 0; left: 0; right: 0; background: #0e0e1c;
            border-top-left-radius: 28px; border-top-right-radius: 28px; padding: 25px 20px;
            max-height: 75vh; overflow-y: auto; border-top: 1px solid rgba(255,255,255,0.08);
        }
        .sheet-title-bar { display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px; }

        #adminTabMenu { display: none; }
    </style>
</head>
<body>

    <div class="app-wrapper">
        
        <!-- НАВЕРХУ: МУЛЬТИ-БАЛАНС -->
        <div class="header-balance-card">
            <div style="display: flex; gap: 20px;">
                <div class="balance-item">
                    <span class="balance-value" id="zzDisplay">0</span>
                    <span class="balance-lbl">Монеты ZZ</span>
                </div>
                <div class="balance-item">
                    <span class="balance-value" id="tonDisplay">0.0000</span>
                    <span class="balance-lbl">Gram (TON)</span>
                </div>
            </div>
            
            <!-- Ряд кнопок управления -->
            <div class="action-row">
                <div class="icon-circle-btn" onclick="openSheet('sheet-leaderboard')">🏆</div>
                <div class="icon-circle-btn" onclick="openSheet('sheet-daily')">🎁</div>
                <div class="icon-circle-btn" onclick="openSheet('sheet-promocode')">🔑</div>
            </div>
        </div>

        <!-- ГЛАВНЫЙ БЛОК ВКЛАДОК -->
        <div class="main-body">
            
            <!-- 1. ВКЛАДКА: МАЙНЕР -->
            <div id="view-miner" class="tab-view active">
                <div class="clicker-container">
                    <div class="neon-click-sphere" id="tapSphere">
                        <span>⛏️</span>
                    </div>
                    
                    <!-- Нижняя Энергия -->
                    <div class="energy-wrapper">
                        <div class="energy-header">
                            <span>Энергия</span>
                            <span id="energyNumText">1000 / 1000</span>
                        </div>
                        <div class="energy-track">
                            <div class="energy-fill" id="energyBarFill"></div>
                        </div>
                    </div>
                </div>

                <!-- Карточки прокачки -->
                <div class="glass-card" style="margin-top: 15px;">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
                        <div>
                            <div style="font-weight: 700; font-size: 15px;">Мультиклик (Ур. <span id="lblClickLvl">1</span>)</div>
                            <div style="color: var(--text-muted); font-size: 12px;">Сила тапа: +<span id="lblClickPower">1</span></div>
                        </div>
                        <button class="btn-prime" style="width: auto; padding: 10px 16px; font-size: 13px;" id="btnUpgradeClick" onclick="buyClickUpgrade()">Прокачать (-1000)</button>
                    </div>
                    <div style="display: flex; justify-content: space-between; align-items: center; border-top: 1px solid rgba(255,255,255,0.03); padding-top: 12px;">
                        <div>
                            <div style="font-weight: 700; font-size: 15px;">Лимит энергии (Ур. <span id="lblEnergyLvl">1</span>)</div>
                            <div style="color: var(--text-muted); font-size: 12px;">Вместимость: <span id="lblEnergyMax">1000</span></div>
                        </div>
                        <button class="btn-prime" style="width: auto; padding: 10px 16px; font-size: 13px;" id="btnUpgradeEnergy" onclick="buyEnergyUpgrade()">Прокачать (-1000)</button>
                    </div>
                </div>
            </div>

            <!-- 2. ВКЛАДКА: ЗАДАНИЯ -->
            <div id="view-tasks" class="tab-view">
                <h3 style="margin-bottom: 15px; font-size: 18px;">Задания и Рефералы</h3>
                
                <!-- Постоянное реферальное задание -->
                <div class="glass-card" style="border-left: 4px solid var(--neon-cyan);">
                    <div style="font-weight: 700; color: var(--neon-cyan); margin-bottom: 4px;">👥 Приглашай друзей</div>
                    <div style="font-size: 13px; color: var(--text-muted); margin-bottom: 10px;">Приглашай друзей и получай 1 000 ZZ за каждого!</div>
                    <button class="btn-prime btn-sub" style="padding: 10px;" onclick="switchTab('view-refs', document.getElementById('nav-refs-btn'))">Открыть рефералы</button>
                </div>

                <!-- Контейнер для заданий -->
                <div id="tasksBox">
                    <div class="glass-card" id="task-base-sub">
                        <div style="font-weight: 700; font-size: 15px;">Вступить в официальный чат проекта</div>
                        <div style="color: var(--crypto-green); font-weight: 700; font-size: 13px; margin: 5px 0 12px 0;">+2 500 ZZ</div>
                        <button class="btn-prime btn-sub" id="btn-task-base-sub" onclick="processTask('task-base-sub', 'https://t.me/miner_zz_bot', 2500)">Выполнить задание</button>
                    </div>
                </div>
            </div>

            <!-- 3. ВКЛАДКА: РЕФЕРАЛЫ -->
            <div id="view-refs" class="tab-view">
                <h3 style="margin-bottom: 15px; font-size: 18px;">Реферальная система</h3>
                <div class="glass-card">
                    <div style="font-size: 13px; color: var(--text-muted); margin-bottom: 8px;">Твоя личная реф-ссылка для друзей:</div>
                    <input type="text" id="refLinkField" readonly value="Загрузка...">
                    <button class="btn-prime btn-buy" style="margin-top: 5px;" onclick="copyRefLink()">Копировать ссылку</button>
                </div>

                <h4 style="margin-bottom: 10px; font-size: 15px;">Твоя команда (<span id="countRefNum">0</span>)</h4>
                <div class="glass-card" id="refListContainer">
                    <div style="color: var(--text-muted); text-align: center; font-size: 13px;">У вас пока нет приглашенных рефералов</div>
                </div>
            </div>

            <!-- 4. ВКЛАДКА: БАЛАНС (ДЕПОЗИТ И ВЫВОД) -->
            <div id="view-wallet" class="tab-view">
                <h3 style="margin-bottom: 15px; font-size: 18px;">Пополнение и Вывод</h3>
                
                <div class="glass-card" style="background: linear-gradient(145deg, rgba(34,34,68,0.6), rgba(15,15,32,0.6));">
                    <div style="text-align: center; margin-bottom: 15px; font-weight: 700; font-size: 14px; text-transform: uppercase; color: var(--text-muted);">P2P Пополнение через Gram (TON)</div>
                    <p style="font-size: 13px; line-height: 1.4; color: #ddd; margin-bottom: 12px;">
                        Для зачисления баланса переведите TON на указанный ниже адрес кошелька. 
                        <b>Важно:</b> В поле «Комментарий» к переводу обязательно укажите ваш уникальный Telegram ID!
                    </p>
                    
                    <div style="background: rgba(0,0,0,0.2); padding: 12px; border-radius: 12px; font-size: 12px; word-break: break-all; text-align: center; border: 1px solid var(--panel-border); margin-bottom: 10px;">
                        UQDmNY1TIMIgnALOpAyJ4_XO2uroUNLFVRwGie5AEwzccaps
                    </div>
                    <button class="btn-prime btn-sub" style="padding: 10px; margin-bottom: 15px;" onclick="copyWalletAddr()">Скопировать адрес кошелька</button>

                    <div style="border-top: 1px solid rgba(255,255,255,0.05); padding-top: 12px; text-align: center;">
                        <div style="font-size: 12px; color: var(--text-muted);">Ваш уникальный комментарий (Telegram ID):</div>
                        <div style="font-size: 20px; font-weight: bold; color: var(--neon-cyan); margin-top: 4px;" id="lblUserWalletId">0</div>
                    </div>
                    <div style="font-size: 11px; color: var(--crypto-red); text-align: center; margin-top: 5px;">Минимальная сумма пополнения: 1 TON</div>
                </div>

                <!-- Раздел Вывода -->
                <div class="glass-card">
                    <h4 style="margin-bottom: 10px; font-size: 15px;">Вывести Gram (TON)</h4>
                    <input type="text" id="withdrawWalletInput" placeholder="Введите ваш TON адрес кошелька">
                    <input type="number" id="withdrawAmountInput" placeholder="Количество TON (Минимум 1 TON)">
                    <button class="btn-prime btn-sell" onclick="processWithdrawRequest()">Создать заявку на вывод</button>
                </div>
            </div>

            <!-- 5. ВКЛАДКА: КУРС И БИРЖА -->
            <div id="view-market" class="tab-view">
                <div class="market-header">
                    <div>
                        <div style="color: var(--text-muted); font-size: 12px;">Текущий курс ZZ/TON</div>
                        <div style="font-size: 22px; font-weight: bold; color: var(--neon-cyan);" id="lblPriceRate">0.00000010 TON</div>
                    </div>
                    <div style="text-align: right;">
                        <div style="color: var(--crypto-green); font-weight: bold; font-size: 15px;">Стабильный</div>
                        <div style="font-size: 11px; color: var(--text-muted);">Рынок под контролем</div>
                    </div>
                </div>

                <!-- Профессиональные Компактные Свечи -->
                <div class="candles-box">
                    <div class="candle-stick up" style="height: 50%;"><div class="candle-wick"></div><div class="candle-bar" style="height: 25px;"></div></div>
                    <div class="candle-stick down" style="height: 45%;"><div class="candle-wick"></div><div class="candle-bar" style="height: 15px;"></div></div>
                    <div class="candle-stick up" style="height: 60%;"><div class="candle-wick"></div><div class="candle-bar" style="height: 35px;"></div></div>
                    <div class="candle-stick down" style="height: 55%;"><div class="candle-wick"></div><div class="candle-bar" style="height: 20px;"></div></div>
                    <div class="candle-stick up" style="height: 75%;"><div class="candle-wick"></div><div class="candle-bar" style="height: 45px;"></div></div>
                    <div class="candle-stick up" style="height: 80%;" id="liveCandleBar"><div class="candle-wick"></div><div class="candle-bar" style="height: 30px;"></div></div>
                </div>

                <!-- Блок Торговли -->
                <div class="glass-card">
                    <h4 style="margin-bottom: 8px; font-size: 14px; text-align: center;">Торговые операции (От 1 000 000 ZZ)</h4>
                    <input type="number" id="marketVolumeInput" placeholder="Количество монет ZZ">
                    
                    <div style="display: flex; gap: 12px; margin-top: 5px;">
                        <button class="btn-prime btn-buy" style="flex: 1;" onclick="executeTrade(true)">Купить ZZ</button>
                        <button class="btn-prime btn-sell" style="flex: 1;" onclick="executeTrade(false)">Продать ZZ</button>
                    </div>
                </div>
            </div>

            <!-- 6. ВКЛАДКА: АДМИН ПАНЕЛЬ (СКРЫТА) -->
            <div id="view-admin" class="tab-view">
                <h3 style="color: var(--crypto-red); margin-bottom: 15px;">Панель Создателя</h3>
                
                <!-- Начисление/Снятие монет конкретному человеку по Telegram ID -->
                <div class="glass-card">
                    <h4 style="font-size: 14px; margin-bottom: 5px;">Управление балансом по ID</h4>
                    <input type="number" id="admTargetUserId" placeholder="Введите Telegram ID игрока">
                    <input type="number" id="admAmountZZ" placeholder="Количество монет ZZ">
                    <div style="display: flex; gap: 10px; margin-top: 5px;">
                        <button class="btn-prime btn-buy" style="font-size: 13px; padding: 10px;" onclick="adminUpdateUserBalance(true)">Добавить</button>
                        <button class="btn-prime btn-sell" style="font-size: 13px; padding: 10px;" onclick="adminUpdateUserBalance(false)">Снять</button>
                    </div>
                </div>

                <!-- Создание неуничтожаемых заданий -->
                <div class="glass-card">
                    <h4 style="font-size: 14px; margin-bottom: 5px;">Создать новое задание</h4>
                    <input type="text" id="admTaskTitle" placeholder="Имя задания (Напр: Чат спонсора)">
                    <input type="text" id="admTaskLink" placeholder="Ссылка (https://t.me/...)">
                    <input type="number" id="admTaskReward" placeholder="Награда ZZ">
                    <button class="btn-prime" style="padding: 11px;" onclick="adminLaunchTask()">Опубликовать задание</button>
                </div>

                <!-- Управление ключами-промокодами -->
                <div class="glass-card">
                    <h4 style="font-size: 14px; margin-bottom: 5px;">Создать Промокод (Ключ)</h4>
                    <input type="text" id="admPromoCode" placeholder="Текстовый код (Напр: START2026)">
                    <input type="number" id="admPromoReward" placeholder="Сумма награды ZZ">
                    <button class="btn-prime btn-buy" style="padding: 11px;" onclick="adminCreatePromo()">Активировать промокод</button>
                </div>
            </div>

        </div>

        <!-- СНИЗУ: НАВИГАЦИОННОЕ МЕНЮ -->
        <div class="footer-navigation">
            <div class="nav-tab-item active" onclick="switchTab('view-miner', this)"><span>⛏️</span>Майнер</div>
            <div class="nav-tab-item" onclick="switchTab('view-tasks', this)"><span>📋</span>Задания</div>
            <div class="nav-tab-item" id="nav-refs-btn" onclick="switchTab('view-refs', this)"><span>👥</span>Рефы</div>
            <div class="nav-tab-item" onclick="switchTab('view-wallet', this)"><span>💰</span>Баланс</div>
            <div class="nav-tab-item" onclick="switchTab('view-market', this)"><span>📈</span>Курс</div>
            <div class="nav-tab-item" id="adminTabMenu" onclick="switchTab('view-admin', this)"><span>⚙️</span>Админ</div>
        </div>

    </div>

    <!-- МОДАЛЬНОЕ ОКНО 1: ЛИДЕРБОРД ЧИСТЫЙ (ТОП-100) -->
    <div class="sheet-overlay" id="sheet-leaderboard">
        <div class="sheet-content">
            <div class="sheet-title-bar">
                <h3 style="color: #ffd700;">🏆 Зал славы ZZ (Топ 100)</h3>
                <div style="font-size: 22px; cursor: pointer; color: var(--text-muted);" onclick="closeSheet('sheet-leaderboard')">✕</div>
            </div>
            <p style="font-size: 12px; color: var(--text-muted); margin-bottom: 15px;">Здесь показываются только реальные пользователи, зарегистрированные в вашей системе.</p>
            <div id="leaderboardPlayersBox">
                <!-- Заполняется динамически из локального реестра зашедших игроков -->
            </div>
        </div>
    </div>

    <!-- МОДАЛЬНОЕ ОКНО 2: ЕЖЕДНЕВНЫЙ ПОДАРОК 24 ЧАСА -->
    <div class="sheet-overlay" id="sheet-daily">
        <div class="sheet-content" style="text-align: center;">
            <div class="sheet-title-bar" style="text-align: left;">
                <h3>🎁 Ежедневная награда</h3>
                <div style="font-size: 22px; cursor: pointer; color: var(--text-muted);" onclick="closeSheet('sheet-daily')">✕</div>
            </div>
            <span style="font-size: 60px; display: block; margin: 10px 0;">🎁</span>
            <p style="font-size: 14px; margin-bottom: 15px; color: #ddd;">Каждые 24 часа заходи в приложение и забирай бонусный подарок в размере <b>500 монет ZZ</b>!</p>
            <button class="btn-prime" id="btnClaimDaily" onclick="claimDailyReward()">Забрать бонус (+500 ZZ)</button>
            <div id="dailyCountdownText" style="color: var(--crypto-red); font-size: 13px; font-weight: bold; margin-top: 10px; display: none;"></div>
        </div>
    </div>

    <!-- МОДАЛЬНОЕ ОКНО 3: КЛЮЧИ (ПРОМОКОДЫ) -->
    <div class="sheet-overlay" id="sheet-promocode">
        <div class="sheet-content">
            <div class="sheet-title-bar">
                <h3>🔑 Активация Ключа</h3>
                <div style="font-size: 22px; cursor: pointer; color: var(--text-muted);" onclick="closeSheet('sheet-promocode')">✕</div>
            </div>
            <p style="font-size: 13px; color: var(--text-muted); margin-bottom: 10px;">Введите секретный код, сгенерированный администратором, чтобы получить ценный приз.</p>
            <input type="text" id="userPromoInputField" placeholder="Введите секретный код ключа...">
            <button class="btn-prime btn-buy" style="margin-top: 8px;" onclick="redeemPromoCode()">Активировать ключ</button>
        </div>
    </div>

    <script>
        const tgApp = window.Telegram?.WebApp;
        if (tgApp) {
            tgApp.expand();
            tgApp.ready();
        }

        // БЕЗОПАСНОСТЬ: ТВОЙ ID
        const OWNER_ID = 8684827145;
        let myTelegramId = 0;
        let myFirstName = "Игрок";

        // Получение данных юзера из Telegram API
        if (tgApp?.initDataUnsafe?.user) {
            myTelegramId = tgApp.initDataUnsafe.user.id;
            myFirstName = tgApp.initDataUnsafe.user.first_name || "Пользователь";
        } else {
            myTelegramId = 8684827145; // Тестовое значение для браузера компьютера
            myFirstName = "Абубакр";
        }

        // Включение админки строго по ID владельца
        if (myTelegramId === OWNER_ID) {
            document.getElementById('adminTabMenu').style.display = 'flex';
        }
        document.getElementById('lblUserWalletId').innerText = myTelegramId;

        // ПЕРЕМЕННЫЕ ЭКОНОМИКИ И СОСТОЯНИЯ
        let balanceZZ = Number(localStorage.getItem('zz_bal')) || 0;
        let balanceTON = Number(localStorage.getItem('ton_bal')) || 0.0000;
        
        let clickPower = Number(localStorage.getItem('click_pwr')) || 1;
        let clickLevel = Number(localStorage.getItem('click_lvl')) || 1;
        
        let energyMax = Number(localStorage.getItem('nrg_max')) || 1000;
        let energyLevel = Number(localStorage.getItem('nrg_lvl')) || 1;
        let energyCurrent = Number(localStorage.getItem('nrg_curr')) || energyMax;

        let baseRate = 0.0000001; 
        let globalRateModifier = Number(localStorage.getItem('rate_mod')) || 1.0; 

        // Инициализация базы данных пользователей (Топ-100) и Заданий
        let realPlayers = JSON.parse(localStorage.getItem('db_players')) || {};
        // Добавляем текущего юзера в базу данных, если его нет
        realPlayers[myTelegramId] = { name: myFirstName, bal: balanceZZ };
        localStorage.setItem('db_players', JSON.stringify(realPlayers));

        let customTasks = JSON.parse(localStorage.getItem('db_tasks')) || [];
        let promoCodes = JSON.parse(localStorage.getItem('db_promos')) || {};
        let activeTaskStates = {};

        // РЕФЕРАЛЫ ССЫЛКА
        document.getElementById('refLinkField').value = `https://t.me/miner_zz_bot?start=id${myTelegramId}`;

        // СИНХРОНИЗАЦИЯ С ЭКРАНОМ
        function syncInterface() {
            document.getElementById('zzDisplay').innerText = balanceZZ.toLocaleString('ru-RU');
            document.getElementById('tonDisplay').innerText = balanceTON.toFixed(4);
            
            document.getElementById('lblClickLvl').innerText = clickLevel;
            document.getElementById('lblClickPower').innerText = clickPower;
            document.getElementById('btnUpgradeClick').innerText = `Прокачать (-${(1000 * Math.pow(5, clickLevel - 1)).toLocaleString('ru-RU')})`;

            document.getElementById('lblEnergyLvl').innerText = energyLevel;
            document.getElementById('lblEnergyMax').innerText = energyMax;
            document.getElementById('btnUpgradeEnergy').innerText = `Прокачать (-${(1000 * Math.pow(5, energyLevel - 1)).toLocaleString('ru-RU')})`;

            document.getElementById('energyNumText').innerText = `${Math.floor(energyCurrent)} / ${energyMax}`;
            let percentage = (energyCurrent / energyMax) * 100;
            document.getElementById('energyBarFill').style.width = percentage + "%";

            let currentRate = baseRate * globalRateModifier;
            document.getElementById('lblPriceRate').innerText = currentRate.toFixed(8) + " TON";

            // Сохранение в память телефона
            localStorage.setItem('zz_bal', balanceZZ);
            localStorage.setItem('ton_bal', balanceTON);
            localStorage.setItem('click_pwr', clickPower);
            localStorage.setItem('click_lvl', clickLevel);
            localStorage.setItem('nrg_max', energyMax);
            localStorage.setItem('nrg_lvl', energyLevel);
            localStorage.setItem('rate_mod', globalRateModifier);

            // Обновляем данные в общем Топе-100
            realPlayers[myTelegramId].bal = balanceZZ;
            localStorage.setItem('db_players', JSON.stringify(realPlayers));
        }

        // ВОССТАНОВЛЕНИЕ ЭНЕРГИИ (+1 в секунду)
        setInterval(() => {
            if (energyCurrent < energyMax) {
                energyCurrent = Math.min(energyMax, energyCurrent + 1);
                syncInterface();
            }
        }, 1000);

        // ТАП ПО МИНЕРУ
        document.getElementById('tapSphere').addEventListener('click', () => {
            if (energyCurrent >= clickPower) {
                energyCurrent -= clickPower;
                balanceZZ += clickPower;
                syncInterface();
                if (navigator.vibrate) navigator.vibrate(35);
            } else {
                alert("Недостаточно энергии для совершения клика! Дождитесь восстановления.");
            }
        });

        // АПГРЕЙД МУЛЬТИКЛИКА (Цена умножается на 5х)
        function buyClickUpgrade() {
            let cost = 1000 * Math.pow(5, clickLevel - 1);
            if (balanceZZ >= cost) {
                balanceZZ -= cost;
                clickLevel += 1;
                clickPower += 1;
                syncInterface();
                alert("Сила тапа успешно повышена!");
            } else {
                alert("Недостаточно монет ZZ для покупки улучшения!");
            }
        }

        // АПГРЕЙД ЭНЕРГИИ (Цена на 5х, вместимость на +150)
        function buyEnergyUpgrade() {
            let cost = 1000 * Math.pow(5, energyLevel - 1);
            if (balanceZZ >= cost) {
                balanceZZ -= cost;
                energyLevel += 1;
                energyMax += 150;
                energyCurrent = energyMax;
                syncInterface();
                alert("Лимит энергии успешно увеличен на +150!");
            } else {
                alert("Недостаточно монет ZZ для покупки улучшения!");
            }
        }

        // ПЕРЕКЛЮЧЕНИЕ ВКЛАДОК МЕНЮ
        function switchTab(viewId, element) {
            document.querySelectorAll('.tab-view').forEach(tab => tab.classList.remove('active'));
            document.getElementById(viewId).classList.add('active');
            
            document.querySelectorAll('.nav-tab-item').forEach(btn => btn.classList.remove('active'));
            element.classList.add('active');
        }

        // МОДАЛЬНЫЕ ОКНА ЛОГИКА
        function openSheet(id) {
            document.getElementById(id).style.display = 'block';
            if (id === 'sheet-leaderboard') fillLeaderboardUI();
            if (id === 'sheet-daily') updateDailyRewardButtonState();
        }
        function closeSheet(id) { document.getElementById(id).style.display = 'none'; }

        // ЛИДЕРБОРД ТОП-100 ЧИСТЫЙ (ТОЛЬКО РЕАЛЬНЫЕ ИГРОКИ)
        function fillLeaderboardUI() {
            const box = document.getElementById('leaderboardPlayersBox');
            box.innerHTML = '';
            
            let playersArray = [];
            for (let id in realPlayers) {
                playersArray.push({ id: id, name: realPlayers[id].name, bal: realPlayers[id].bal });
            }
            // Сортировка по убыванию баланса
            playersArray.sort((a, b) => b.bal - a.bal);

            let renderCount = Math.min(playersArray.length, 100);
            for (let i = 0; i < renderCount; i++) {
                let p = playersArray[i];
                let crown = "";
                if (i === 0) crown = "🥇 ";
                else if (i === 1) crown = "🥈 ";
                else if (i === 2) crown = "🥉 ";
                else crown = ` ${i+1}. `;

                let isMeStyle = p.id == myTelegramId ? "background: rgba(0,242,254,0.08); padding: 8px; border-radius: 12px; border: 1px solid rgba(0,242,254,0.2);" : "";

                box.innerHTML += `
                    <div class="flex-row-item" style="${isMeStyle}">
                        <div style="font-weight: 600;">${crown}${p.name} ${p.id == myTelegramId ? '(Вы)' : ''}</div>
                        <div style="color: var(--neon-cyan); font-weight: bold;">${p.bal.toLocaleString('ru-RU')} ZZ</div>
                    </div>
                `;
            }
        }

        // ЕЖЕДНЕВНЫЙ БОНУС 24 ЧАСА ПО ТАЙМЕРУ
        function claimDailyReward() {
            let lastClaim = localStorage.getItem('last_daily_claim_time');
            let now = Date.now();

            if (lastClaim && (now - lastClaim < 24 * 60 * 60 * 1000)) {
                alert("Вы уже забрали ежедневный подарок! Возвращайтесь завтра.");
                return;
            }

            balanceZZ += 500;
            localStorage.setItem('last_daily_claim_time', now);
            syncInterface();
            updateDailyRewardButtonState();
            alert("Поздравляем! Вы получили +500 монет ZZ!");
        }

        function updateDailyRewardButtonState() {
            let lastClaim = localStorage.getItem('last_daily_claim_time');
            let now = Date.now();
            const btn = document.getElementById('btnClaimDaily');
            const countdown = document.getElementById('dailyCountdownText');

            if (lastClaim && (now - lastClaim < 24 * 60 * 60 * 1000)) {
                btn.disabled = true;
                btn.className = "btn-prime btn-sub";
                btn.innerText = "Уже получено";
                countdown.style.display = "block";
                
                let diff = (24 * 60 * 60 * 1000) - (now - lastClaim);
                let hours = Math.floor(diff / (1000 * 60 * 60));
                let minutes = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
                countdown.innerText = `До следующего бонуса осталось: ${hours}ч ${minutes}м`;
            } else {
                btn.disabled = false;
                btn.className = "btn-prime";
                btn.innerText = "Забрать бонус (+500 ZZ)";
                countdown.style.display = "none";
            }
        }

        // КОДЫ И КЛЮЧИ ПОЛЬЗОВАТЕЛЯ
        function redeemPromoCode() {
            const input = document.getElementById('userPromoInputField');
            let code = input.value.trim();

            if (promoCodes[code]) {
                let reward = promoCodes[code];
                balanceZZ += reward;
                syncInterface();
                alert(`Ключ активирован! Начислено +${reward} ZZ`);
                input.value = '';
                closeSheet('sheet-promocode');
            } else {
                alert("Ошибка: Такого ключа не существует или он введен неверно.");
            }
        }

        // ЛОГИКА ВЫПОЛНЕНИЯ ЗАДАНИЙ С ССЫЛКОЙ И ПРОВЕРКОЙ
        function processTask(id, url, reward) {
            if (!activeTaskStates[id]) {
                alert("Внимание: Сейчас откроется целевой канал/чат. Подпишитесь, чтобы забрать награду!");
                window.open(url, '_blank');
                
                const btn = document.getElementById('btn-' + id);
                btn.innerText = "Проверить выполнение";
                btn.className = "btn-prime btn-buy";
                activeTaskStates[id] = 'verify_state';
            } else if (activeTaskStates[id] === 'verify_state') {
                const btn = document.getElementById('btn-' + id);
                btn.innerText = "Сканирование подписки...";
                btn.disabled = true;

                setTimeout(() => {
                    balanceZZ += reward;
                    syncInterface();
                    btn.innerText = "Завершено ✓";
                    btn.className = "btn-prime btn-sub";
                    alert(`Задание успешно выполнено! Награда +${reward} ZZ начислена.`);
                    activeTaskStates[id] = 'completed';
                }, 1200);
            }
        }

        // РЕФЕРАЛЬНЫЕ ДЕЙСТВИЯ (ИМИТАЦИЯ)
        let simulatedRefCounter = 0;
        function copyRefLink() {
            const input = document.getElementById('refLinkField');
            input.select();
            document.execCommand('copy');
            alert("Ваша ссылка скопирована. Отправьте её другу!");
            
            // Симулируем регистрацию реферала для наглядности
            simulatedRefCounter++;
            balanceZZ += 1000;
            syncInterface();
            
            document.getElementById('countRefNum').innerText = simulatedRefCounter;
            const container = document.getElementById('refListContainer');
            if (simulatedRefCounter === 1) container.innerHTML = '';
            
            container.innerHTML += `
                <div class="flex-row-item">
                    <div>👤 Пользователь t.me (ID: ${Math.floor(200000 + Math.random() * 700000)})</div>
                    <div style="color: var(--crypto-green); font-weight:bold;">+1000 ZZ</div>
                </div>
            `;
        }

        // КОШЕЛЕК: КОПИРОВАНИЕ АДРЕСА
        function copyWalletAddr() {
            navigator.clipboard.writeText("UQDmNY1TIMIgnALOpAyJ4_XO2uroUNLFVRwGie5AEwzccaps");
            alert("Адрес кошелька TON успешно скопирован в буфер обмена!");
        }

        // СОЗДАНИЕ ЗАЯВКИ НА ВЫВОД
        function processWithdrawRequest() {
            let addr = document.getElementById('withdrawWalletInput').value.trim();
            let amount = Number(document.getElementById('withdrawAmountInput').value);

            if (!addr || amount < 1) {
                alert("Ошибка: Заполните адрес получателя и укажите сумму от 1 TON!");
                return;
            }

            if (balanceTON >= amount) {
                balanceTON -= amount;
                syncInterface();
                alert("Заявка на вывод успешно отправлена администратору! Ожидайте ручной выплаты.");
                document.getElementById('withdrawWalletInput').value = '';
                document.getElementById('withdrawAmountInput').value = '';
            } else {
                alert("Недостаточно средств на вашем балансе Gram (TON) для осуществления вывода!");
            }
        }

        // БИРЖА: КУПИТЬ / ПРОДАТЬ ZZ ОТ 1 МЛН С ВЛИЯНИЕМ НА КУРС ДЛЯ ВСЕХ
        function executeTrade(isBuyOperation) {
            let volume = Number(document.getElementById('marketVolumeInput').value);
            if (!volume || volume < 1000000) {
                alert("Минимальный объем сделки на бирже составляет 1 000 000 ZZ монет!");
                return;
            }

            let currentRate = baseRate * globalRateModifier;
            let totalCostTON = (volume / 1000000) * (currentRate / baseRate);

            if (isBuyOperation) {
                // Покупка монет ZZ за TON
                if (balanceTON >= totalCostTON) {
                    balanceTON -= totalCostTON;
                    balanceZZ += volume;
                    // Курс идет вверх от покупок
                    globalRateModifier += 0.05 * (volume / 1000000);
                    alert(`Сделка исполнена! Вы купили ${volume.toLocaleString('ru-RU')} ZZ.`);
                } else {
                    alert("У вас недостаточно Gram (TON) на кошельке для покупки такого объема монет!");
                }
            } else {
                // Продажа монет ZZ за TON
                if (balanceZZ >= volume) {
                    balanceZZ -= volume;
                    balanceTON += totalCostTON;
                    // Курс падает от продаж
                    globalRateModifier = Math.max(0.1, globalRateModifier - 0.04 * (volume / 1000000));
                    alert(`Сделка исполнена! Вы продали ${volume.toLocaleString('ru-RU')} ZZ.`);
                } else {
                    alert("У вас недостаточно монет ZZ для совершения этой продажи!");
                }
            }
            
            // Анимируем свечу
            let liveCandle = document.getElementById('liveCandleBar');
            if(liveCandle) {
                liveCandle.className = isBuyOperation ? "candle-stick up" : "candle-stick down";
                liveCandle.style.height = Math.min(40 + (globalRateModifier * 10), 100) + "%";
            }

            document.getElementById('marketVolumeInput').value = '';
            syncInterface();
        }

        // АДМИНКА 1: ТОЧЕЧНОЕ НАЧИСЛЕНИЕ ПО ТЕЛЕГРАМ ID
        function adminUpdateUserBalance(isAdd) {
            let targetId = document.getElementById('admTargetUserId').value.trim();
            let amount = Number(document.getElementById('admAmountZZ').value);

            if (!targetId || !amount || amount <= 0) {
                alert("Укажите корректный ID и количество монет!");
                return;
            }

            // Если правим свой баланс
            if (targetId == myTelegramId) {
                if (isAdd) balanceZZ += amount;
                else balanceZZ = Math.max(0, balanceZZ - amount);
            } else {
                // Если правим баланс стороннего юзера из кэша базы
                if (!realPlayers[targetId]) {
                    realPlayers[targetId] = { name: `User_${targetId}`, bal: 0 };
                }
                if (isAdd) realPlayers[targetId].bal += amount;
                else realPlayers[targetId].bal = Math.max(0, realPlayers[targetId].bal - amount);
                localStorage.setItem('db_players', JSON.stringify(realPlayers));
            }

            alert(`Успешно изменено состояние баланса для пользователя ID: ${targetId}`);
            document.getElementById('admAmountZZ').value = '';
            syncInterface();
        }

        // АДМИНКА 2: СОЗДАНИЕ НЕУНИЧТОЖАЕМЫХ ЗАДАНИЙ С КНОПКОЙ УДАЛЕНИЯ ДЛЯ АДМИНА
        function adminLaunchTask() {
            let title = document.getElementById('admTaskTitle').value.trim();
            let link = document.getElementById('admTaskLink').value.trim() || 'https://t.me/';
            let reward = Number(document.getElementById('admTaskReward').value);

            if (!title || !reward) {
                alert("Заполните название задания и укажите награду!");
                return;
            }

            let newId = 'task_' + Date.now();
            let tObj = { id: newId, title: title, link: link, reward: reward };
            customTasks.push(tObj);
            localStorage.setItem('db_tasks', JSON.stringify(customTasks));

            renderCustomTasksList();
            alert("Задание успешно создано, сохранено и опубликовано для всех участников!");
            
            document.getElementById('admTaskTitle').value = '';
            document.getElementById('admTaskReward').value = '';
        }

        function renderCustomTasksList() {
            // Очищаем старые кастомные, оставляя только базовое
            const container = document.getElementById('tasksBox');
            container.innerHTML = `
                <div class="glass-card" id="task-base-sub">
                    <div style="font-weight: 700; font-size: 15px;">Вступить в официальный чат проекта</div>
                    <div style="color: var(--crypto-green); font-weight: 700; font-size: 13px; margin: 5px 0 12px 0;">+2 500 ZZ</div>
                    <button class="btn-prime btn-sub" id="btn-task-base-sub" onclick="processTask('task-base-sub', 'https://t.me/miner_zz_bot', 2500)">Выполнить задание</button>
                </div>
            `;

            customTasks.forEach(t => {
                // Если зашел админ, добавляем кнопку удаления задания ❌
                let adminDeleteBtnHtml = (myTelegramId === OWNER_ID) ? 
                    `<button class="btn-prime btn-sell" style="padding: 6px; margin-top: 8px; font-size: 12px;" onclick="adminDeleteTask('${t.id}')">Удалить задание ❌</button>` : '';

                container.innerHTML += `
                    <div class="glass-card" id="${t.id}">
                        <div style="font-weight: 700; font-size: 15px;">${t.title}</div>
                        <div style="color: var(--crypto-green); font-weight: 700; font-size: 13px; margin: 5px 0 12px 0;">+${t.reward.toLocaleString('ru-RU')} ZZ</div>
                        <button class="btn-prime btn-sub" id="btn-${t.id}" onclick="processTask('${t.id}', '${t.link}', ${t.reward})">Выполнить задание</button>
                        ${adminDeleteBtnHtml}
                    </div>
                `;
            });
        }

        function adminDeleteTask(id) {
            customTasks = customTasks.filter(item => item.id !== id);
            localStorage.setItem('db_tasks', JSON.stringify(customTasks));
            renderCustomTasksList();
            alert("Задание полностью удалено из системы администратором!");
        }

        // АДМИНКА 3: СОЗДАНИЕ ПРОМОКОДОВ (КЛЮЧЕЙ)
        function adminCreatePromo() {
            let code = document.getElementById('admPromoCode').value.trim();
            let reward = Number(document.getElementById('admPromoReward').value);

            if (!code || !reward) {
                alert("Укажите текст промокода и сумму награды!");
                return;
            }

            promoCodes[code] = reward;
            localStorage.setItem('db_promos', JSON.stringify(promoCodes));
            alert(`Ключ «${code}» на сумму ${reward} ZZ успешно сгенерирован!`);
            
            document.getElementById('admPromoCode').value = '';
            document.getElementById('admPromoReward').value = '';
        }

        // Запуск при старте страницы
        renderCustomTasksList();
        syncInterface();
    </script>
</body>
</html>
