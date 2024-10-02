from telebot.types import ReplyKeyboardMarkup, KeyboardButton

def create_main_menu():
    markup = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    battle_button = KeyboardButton("Imperiyalar jangi")
    markup.add(battle_button)
    return markup

def create_battle_menu():
    markup = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    attack_button = KeyboardButton("Hujum qilish")
    defend_button = KeyboardButton("Himoya qilish")
    back_button = KeyboardButton("Orqaga")
    markup.add(attack_button, defend_button, back_button)
    return markup

def create_attack_menu(current_empire):
    markup = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    empires = ["Imperiya A", "Imperiya B", "Imperiya C", "Imperiya D"]  # Barcha imperiyalar ro'yxati
    for empire in empires:
        if empire != current_empire:  # Tanlangan imperiyadan boshqa imperiyalarni qo'shamiz
            markup.add(KeyboardButton(empire))
    back_button = KeyboardButton("Orqaga")
    markup.add(back_button)
    return markup
