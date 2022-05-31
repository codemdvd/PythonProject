import config
import telebot
from telebot import types
from main import Main

bot = telebot.TeleBot(config.token)
strength = Main.characters_strength
agility = Main.characters_agility
intelligence = Main.characters_intelligence
fav = []
statistics = []


@bot.message_handler(content_types=['text'])
def start(message):
    Main.get_strength()
    Main.get_agility()
    Main.get_intelligence()
    Main.parse_to_json()
    if message.text == '/start':
        bot.send_message(chat_id=message.chat.id,
                         text="Привет, {0.first_name}! "
                              "Здесь ты можешь узнать характеристики нужного "
                              "тебе героя и подобрать сборку."
                         .format(message.from_user)
                         )
    get_start(message)


@bot.message_handler(content_types=['text'])
def get_start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("💪 Сила")
    btn2 = types.KeyboardButton("￩ ￪ ￫ Ловкость")
    btn3 = types.KeyboardButton("☄ Интеллект")
    btn4 = types.KeyboardButton("📋 Список любимых персонажей")
    markup.add(btn1, btn2, btn3, btn4)
    bot.send_message(message.chat.id,
                     "Какой атрибут является основным у твоего героя?",
                     reply_markup=markup
                     )
    bot.register_next_step_handler(message, get_attribute)


def get_attribute(message):
    if message.text == "💪 Сила":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("📋 Список всех героев на силу")
        btn2 = types.KeyboardButton("✖ Назад")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, "Какого героя ты пикнул?",
                         reply_markup=markup)
        bot.register_next_step_handler(message, get_strength)
    elif message.text == "￩ ￪ ￫ Ловкость":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("📋 Список всех героев на ловкость")
        btn2 = types.KeyboardButton("✖ Назад")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, "Какого героя ты пикнул?",
                         reply_markup=markup)
        bot.register_next_step_handler(message, get_agility)
    elif message.text == "☄ Интеллект":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("📋 Список всех героев на интеллект")
        btn2 = types.KeyboardButton("✖ Назад")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, "Какого героя ты пикнул?",
                         reply_markup=markup)
        bot.register_next_step_handler(message, get_intelligence)
    elif message.text == "📋 Список любимых персонажей":
        show_fav(message)
    else:
        bot.send_message(message.chat.id, "Выбери атрибут")
        bot.register_next_step_handler(message, get_attribute)


def get_strength(message):
    flag = False
    hero = ''
    names = []
    for h in strength:
        names.append(h.name)
    names = (', '.join(names))
    names_str = repr(names)
    for ch in strength:
        if message.text == ch.name:
            bot.send_message(message.chat.id, ch)
            bot.send_photo(message.chat.id, ch.picture)
            hero = ch.name
            flag = True
            back(message, hero)
        elif message.text == "📋 Список всех героев на силу":
            bot.send_message(message.chat.id, names_str)
            bot.register_next_step_handler(message, get_strength)
            flag = True
            break
        elif message.text == "✖ Назад":
            flag = True
            again(message, hero)
            break
    if not flag:
        bot.send_message(message.chat.id,
                         "Введи имя героя из списка \"сила\"")
        bot.register_next_step_handler(message, get_strength)


def get_agility(message):
    flag = False
    hero = ''
    names = []
    for h in agility:
        names.append(h.name)
    names = (', '.join(names))
    names_str = repr(names)
    for ch in agility:
        if message.text == ch.name:
            bot.send_message(message.chat.id, ch)
            bot.send_photo(message.chat.id, ch.picture)
            hero = ch.name
            flag = True
            back(message, hero)
        elif message.text == "📋 Список всех героев на ловкость":
            bot.send_message(message.chat.id, names_str)
            bot.register_next_step_handler(message, get_agility)
            flag = True
            break
        elif message.text == "✖ Назад":
            flag = True
            again(message, hero)
            break
    if not flag:
        bot.send_message(message.chat.id,
                         "Введи имя героя из списка \"ловкость\"")
        bot.register_next_step_handler(message, get_agility)


def get_intelligence(message):
    flag = False
    hero = ''
    names = []
    for h in intelligence:
        names.append(h.name)
    names = (', '.join(names))
    names_str = repr(names)
    for ch in intelligence:
        if message.text == ch.name:
            bot.send_message(message.chat.id, ch)
            bot.send_photo(message.chat.id, ch.picture)
            hero = ch.name
            flag = True
            back(message, hero)
        elif message.text == "📋 Список всех героев на интеллект":
            bot.send_message(message.chat.id, names_str)
            bot.register_next_step_handler(message, get_intelligence)
            flag = True
            break
        elif message.text == "✖ Назад":
            flag = True
            again(message, hero)
            break
    if not flag:
        bot.send_message(message.chat.id,
                         "Введи имя героя из списка \"интеллект\"")
        bot.register_next_step_handler(message, get_intelligence)


def back(message, hero):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("✖ Назад")
    btn2 = types.KeyboardButton("⭐ Добавить героя в избранное")
    btn3 = types.KeyboardButton("☑ Роли")
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id, "Выбери действие",
                     reply_markup=markup)
    bot.register_next_step_handler(message, again, hero)


def again(message, hero):
    if message.text == "✖ Назад":
        get_start(message)
    elif message.text == "⭐ Добавить героя в избранное":
        favourite(message, hero)
    elif message.text == "☑ Роли":
        get_role(message, hero)
    else:
        back(message, hero)


def favourite(message, hero):
    for x in strength:
        statistics.append(x)
    for x in agility:
        statistics.append(x)
    for x in intelligence:
        statistics.append(x)
    for ch in statistics:
        if hero == ch.name:
            new_hero = ch
            if new_hero not in fav:
                fav.append(new_hero)
                bot.send_message(message.chat.id,
                                 "Герой добавлен")
                break
            else:
                bot.send_message(message.chat.id,
                                 "Ты уже добавил этого героя")
                break
    bot.register_next_step_handler(message, again, hero)


def show_fav(message):
    if not fav:
        bot.send_message(message.chat.id, "Список пуст")
        bot.register_next_step_handler(message, get_attribute)
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("↺ Удалить персонажа из списка")
        btn2 = types.KeyboardButton("✖ Назад")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, " Выберите действие",
                         reply_markup=markup)
        fav_str = repr(fav)
        bot.send_message(message.chat.id, ' '.join(fav_str))
        bot.register_next_step_handler(message, delete)


def delete(message):
    if message.text == "↺ Удалить персонажа из списка":
        if len(fav) > 1:
            bot.send_message(message.chat.id,
                             "Выбери героя")
            bot.register_next_step_handler(message, delete_end)
        else:
            delete_one(message)
    elif message.text == "✖ Назад":
        get_start(message)
    else:
        show_fav(message)


def delete_end(message):
    flag = True

    for ch in fav:
        if message.text == ch.name:
            fav.remove(ch)
            bot.send_message(message.chat.id,
                             "Герой удалён")
            get_start(message)
            flag = False
            break

    if flag:
        delete_ex(message)


def delete_ex(message):
    bot.send_message(message.chat.id,
                     "Герой не найден, проверьте список")
    get_start(message)


def delete_one(message):
    for ch in fav:
        fav.remove(ch)
        bot.send_message(message.chat.id,
                         "Герой удалён")
        get_start(message)


def get_role(message, hero):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("Carry",
                                      url='https://gosu.ai/blog/dota2/'
                                          'how-to-get-better-as-a-carry/')
    btn2 = types.InlineKeyboardButton("Support",
                                      url='https://dmarket.com/'
                                          'blog/'
                                          'how-to-be-a-good-support-in-dota2/')
    btn3 = types.InlineKeyboardButton("Jungle",
                                      url='https://dota2.fandom.com/'
                                          'wiki/Jungling')
    btn4 = types.InlineKeyboardButton("Mid",
                                      url='https://www.hotspawn.com/'
                                          'dota2/guides/'
                                          'flying-solo-how-to'
                                          '-play-mid-in-dota-2')
    btn5 = types.InlineKeyboardButton("Offlane",
                                      url='https://dota2freaks.com/'
                                          'offlane-guide/')
    markup.add(btn1, btn2, btn3, btn4, btn5)
    bot.send_message(message.chat.id,
                     "Нажми на кноку и получи нужную информацию",
                     reply_markup=markup)
    bot.register_next_step_handler(message, again, hero)


bot.polling(none_stop=True, interval=0)
