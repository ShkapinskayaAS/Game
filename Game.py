# ================================================
# ИГРА «ЗАБРОШЕННАЯ КУЗНИЦА»
# Автор: Анастасия Шкапинская
# Дата: сентябрь 2026
#
# Пункт 4 - потрогать наковальню герой проверяет,
# тёплая ли она ещё.
# Пункт 5 - осмотреть полки, герой ищет полезные вещи.
# Пункт 6 - тренировка. герой бьёт старое чучело.
# Пункт 7 - спуститься глубже встреча со случайным
# врагом и бой раундами. Побеждённый враг уходит из списка,
# а раунды копятся в журнале log для урока 8.
#
# Этап 6 - полная защита:
#   настройка героя читает все четыре числа в одном try и при
#   любой ошибке перечитывает набор целиком, свои правила характеристик
#   поднимаются через raise, пункт меню проверяется числом через
#   int, а не кортежем строк главный цикл обёрнут в
#   try/except KeyboardInterrupt/finally, поэтому прощание
#   печатается при любом исходе.
# ================================================


import random


# --- Заголовок ------------------------------------
title = "ЗАБРОШЕННАЯ КУЗНИЦА"
frame = "=" * 22
print(frame)
print(f" {title} ")
print(frame)
print()


# --- Знакомство с героем --------------------------
print("Как зовут героя?")
hero_name = input()
print(f"Добро пожаловать, {hero_name}!")
print("Ты входишь в старую кузницу. Здесь пахнет железом и золой, "
      "а в углу тлеет уголёк.")
print()


# --- Настройка героя -------------------------------
print("Настройка героя.")
print("Здоровье, сила, ловкость, воля — по одному числу в строке:")
while True:
    try:
        health = int(input())
        strength = int(input())
        agility = int(input())
        will = int(input())
        if health <= 0:
            raise ValueError(f"Здоровье должно быть положительным, а введено {health}")
        if strength > 20:
            raise ValueError(f"Сила не может быть больше 20, а введено {strength}")
        if agility < 0 or will < 0:
            raise ValueError("Ловкость и воля не могут быть отрицательными")
        break
    except ValueError as e:
        if "invalid literal" in str(e):
            print("Ой: одна из строк не число. Введи все четыре числа снова.")
        else:
            print(f"{e}. Введи все четыре числа снова.")


# --- Расчёт урона ----------------------------------
base_attack = 10
damage = base_attack + strength * 1.5
crit_damage = damage * 2
stamina = (health + will) // 5
max_stamina = stamina


# --- Формуляр героя --------------------------------
print("Характеристики героя:")
print(f"Здоровье:   {health}")
print(f"Сила:       {strength}")
print(f"Ловкость:   {agility}")
print(f"Воля:       {will}")
print()
print(f"Урон героя:        {damage:.1f}")
print(f"Критический урон:  {crit_damage:.1f}")
print(f"Запас сил:         {stamina}")
print()


# --- Враги подземелья ------------------------------
enemies = ["упырь", "скелет", "паук", "голем"]
log = []


# --- Главный цикл игры ---------------------------
running = True
actions = 0
menu_last = 7


outcome = "прерывание"
try:
    while running:
        print("Что делаешь?")
        print("1 - осмотреться")
        print("2 - идти вперёд")
        print("3 - отдохнуть")
        print("4 - потрогать наковальню")
        print("5 - осмотреть полки")
        print("6 - тренировка")
        print("7 - спуститься глубже")
        print("0 - выйти из кузницы")


        # --- Защита от неверного ввода ----------------
        while True:
            choice = input()
            try:
                menu_number = int(choice)
            except ValueError:
                print("Такого пункта нет. Введи номер пункта из меню.")
                continue
            if 0 <= menu_number <= menu_last:
                break
            print("Такого пункта нет. Введи номер пункта из меню.")


        if menu_number == 1:
            print("Вы внимательно осматриваетесь. В кузнице тихо, "
                  "только изредка потрескивает уголёк.")


        elif menu_number == 2:
            cost = 3
            if stamina >= cost:
                stamina -= cost
                print("Вы осторожно идёте вперёд. Пол скрипит под ногами.")
            else:
                health -= cost - stamina
                stamina = 0
                print("Сил больше нет — вы идёте на одном упорстве.")


        elif menu_number == 3:
            stamina += 1
            if stamina > max_stamina:
                stamina = max_stamina
            print("Вы присаживаетесь на край скамьи и переводите дух. "
                  "Силы понемногу возвращаются.")


        elif menu_number == 4:
            stamina -= 1
            print("Вы осторожно касаетесь наковальни. Металл ещё хранит "
                  "слабое тепло — кузница заброшена не так давно.")


        elif menu_number == 5:
            will += 1
            stamina -= 2
            print("На пыльной полке вы находите старую эмблему "
                  "кузнечного цеха. Что-то внутри вас крепнет.")


        elif menu_number == 6:
            # --- Тренировочный бой ----------------------
            strikes = 6
            total_damage = 0
            crit_count = 0


            print("Вы подходите к старому чучелу, сколоченному из брёвен "
                  "и обтянутому ржавыми листами железа.")
            print("Его оставил прошлый кузнец — тренировался, когда заказов "
                  "не было.")
            print()
            print(f"Наносите {strikes} ударов.")


            for i in range(1, strikes + 1):
                if i % 3 == 0:
                    hit_damage = crit_damage
                    crit_count += 1
                    print(f"Удар {i}: {hit_damage:.1f} — критический!")
                else:
                    hit_damage = damage
                    print(f"Удар {i}: {hit_damage:.1f}")


                total_damage += hit_damage


            print()
            print(f"Итог: {strikes} ударов, критических ударов: {crit_count}")
            print(f"Общий урон: {total_damage:.1f}")
            print(f"Средний урон: {total_damage / strikes:.1f}")


            stamina -= 4


        elif menu_number == 7:
            # --- Спуск и встреча с врагом ---------------
            if not enemies:
                print("Вы спускаетесь по ступеням, но подземелье пусто — "
                      "здесь больше некого встретить.")
            else:
                print("Вы спускаетесь по скрипучим ступеням вниз.")
                enemy = random.choice(enemies)
                enemy_hp = 45
                round_n = 0
                hero_hits = 0
                print(f"Из темноты навстречу выходит {enemy}!")


                # --- Бой раундами ------------------------
                while enemy_hp > 0 and health > 0:
                    round_n += 1
                    hero_hits += 1


                    if hero_hits % 3 == 0:
                        hit_damage = crit_damage
                    else:
                        hit_damage = damage


                    enemy_hp -= hit_damage


                    if enemy_hp <= 0:
                        print(f"Раунд {round_n}: вы наносите {hit_damage:.1f} урона "
                              f"— критический удар! Враг падает.")
                        log.append(f"раунд {round_n}: герой -{hit_damage:.1f}, {enemy} -0")
                        break


                    enemy_damage = random.randint(2, 6)
                    health -= enemy_damage
                    print(f"Раунд {round_n}: вы наносите {hit_damage:.1f} урона. "
                          f"Здоровье врага: {enemy_hp:.1f}. "
                          f"{enemy} наносит ответный удар: {enemy_damage}.")
                    log.append(f"раунд {round_n}: герой -{hit_damage:.1f}, "
                               f"{enemy} -{enemy_damage}")


                # --- Исход боя ---------------------------
                if enemy_hp <= 0:
                    enemies.remove(enemy)
                    print(f"{enemy} повержен! Осталось врагов в подземелье: {len(enemies)}.")


                print(f"Бой: {round_n} раундов.")
                print(f"Последняя запись журнала: {log[-1]}")


        elif menu_number == 0:
            print("Вы выходите из кузницы на свежий воздух. "
                  "Дверь со скрипом закрывается позади.")
            outcome = "выход"
            running = False


        # --- Счётчик и строка состояния ------------------
        if running:
            actions += 1
            print()
            print(f"Здоровье: {health:5d} Запас сил: {stamina:5d} "
                  f"Осталось врагов: {len(enemies)}")


            # --- Проверка гибели ------------------------
            if health <= 0:
                print(f"{hero_name} падает без сил. Кузница забирает ещё одного гостя.")
                outcome = "гибель"
                running = False


except KeyboardInterrupt:
    print()
    print("Игрок прервал сеанс.")


finally:
    print()
    print(frame)
    if outcome == "гибель":
        print(f"Ты не дошёл, {hero_name}. Действий совершено: {actions}.")
    elif outcome == "выход":
        print(f"Забег окончен, {hero_name}. Действий совершено: {actions}.")
    else:
        print(f"Сеанс прерван, {hero_name}. Действий совершено: {actions}.")
    print(frame)



