import telebot
from src.card import Card
from src.constants import *
from scr.one_user import OneUser


class Bot:
    def __init__(self):
        self.TOKEN = '6632832265:AAECpbpAxqwQUZ0aWOaqexyVGM4n6sKCoz4'
        self.bot = telebot.TeleBot(self.TOKEN)
        self.users = {}
        self.bot.message_handler(commands=['start'])(self.start)

    def start(self, message):
        self.bot.message_handler(func=lambda message: message.text in ["Правила"])(self.rools)
        self.bot.message_handler(func=lambda message: message.text in ["Начать"])(self.new_game)
        markup = telebot.types.ReplyKeyboardMarkup(row_width=2)
        btn1 = telebot.types.KeyboardButton('Правила')
        btn2 = telebot.types.KeyboardButton('Начать')
        markup.add(btn1, btn2)
        self.bot.send_message(chat_id=message.chat.id, text="Выберите действие:", reply_markup=markup)

    def rools(self, message):
        self.bot.send_message(chat_id=message.chat.id, text=Rules)
        self.bot.message_handler(func=lambda message: message.text in ["Вернуться назад"])(self.start)
        markup = telebot.types.ReplyKeyboardMarkup(row_width=1)
        btn1 = telebot.types.KeyboardButton("Вернуться назад")
        markup.add(btn1)
        self.bot.send_message(chat_id=message.chat.id, text="Выберите действие:", reply_markup=markup)

    def get_card(self, message):
        markup = telebot.types.ReplyKeyboardMarkup(row_width=4)
        self.bot.message_handler(func=lambda message: message.text in ["Вернуться назад"])(self.continue_the_game)

        btn1 = telebot.types.KeyboardButton("Вернуться назад")
        markup.add(btn1)
        self.bot.send_message(chat_id=message.chat.id, text="Введите карту в формате \"король крести\"/\"10 пики\"",
                              reply_markup=markup)

        @self.bot.message_handler(content_types=['text'])
        def get_text_messages(message):
            if message.text not in comands:
                card_name = message.text.split()
                if len(card_name) == 2 and card_name[0] in card_values and card_name[1] in suits:
                    self.users[message.chat.id].add_card(
                        Card(card_values.index(card_name[0]), suits.index(card_name[1])))
                elif len(card_name) == 4 and card_name[0] in card_values and card_name[1] in suits and card_name[
                    2] in card_values and card_name[3] in suits:
                    self.users[message.chat.id].add_personal_cards(
                        Card(card_values.index(card_name[0]), suits.index(card_name[1])),
                        Card(card_values.index(card_name[2]), suits.index(card_name[3])))
                else:
                    self.bot.send_message(chat_id=message.chat.id, text="Что-то НЕ то")

                self.continue_the_game(message)

    def add_a_shared_card(self, message):
        self.get_card(message)

    def get_cards(self, message):
        markup = telebot.types.ReplyKeyboardMarkup(row_width=4)
        self.bot.message_handler(func=lambda message: message.text in ["Вернуться назад"])(self.continue_the_game)
        btn1 = telebot.types.KeyboardButton("Вернуться назад")
        markup.add(btn1)
        self.bot.send_message(chat_id=message.chat.id,
                              text="Введите две ваши карты в формате \"король крести 10 пики\"",
                              reply_markup=markup)

        @self.bot.message_handler(content_types=['text'])
        def get_text_messages(message):
            if message.text not in comands:
                card_name = message.text.split()
                if len(card_name) == 2 and card_name[0] in card_values and card_name[1] in suits:
                    self.users[message.chat.id].add_card(
                        Card(card_values.index(card_name[0]), suits.index(card_name[1])))
                elif len(card_name) == 4 and card_name[0] in card_values and card_name[1] in suits and card_name[
                    2] in card_values and card_name[3] in suits:
                    self.users[message.chat.id].add_personal_cards(
                        Card(card_values.index(card_name[0]), suits.index(card_name[1])),
                        Card(card_values.index(card_name[2]), suits.index(card_name[3])))
                else:
                    self.bot.send_message(chat_id=message.chat.id, text="Что-то НЕ то")
                self.continue_the_game(message)

    def add_personal_cards(self, message):
        self.get_cards(message)

    def find_the_probability(self, message):
        self.bot.message_handler(func=lambda message: message.text in ["Вернуться назад"])(self.continue_the_game)
        self.bot.message_handler(func=lambda message: message.text in ["Начать новую игру"])(self.new_game)
        markup = telebot.types.ReplyKeyboardMarkup(row_width=1)
        btn1 = telebot.types.KeyboardButton("Вернуться назад")
        btn2 = telebot.types.KeyboardButton("Начать новую игру")
        markup.add(btn1, btn2)
        probability = self.users[message.chat.id].find_probability()
        self.bot.send_message(chat_id=message.chat.id,
                              text=f"Вероятность вашего выигрыша {int(probability * 1000) / 10}%", reply_markup=markup)

    def continue_the_game(self, message):
        self.bot.message_handler(func=lambda message: message.text in ["Ввести свои карты"])(self.add_personal_cards)
        self.bot.message_handler(func=lambda message: message.text in ["Добавить общую карту"])(self.add_a_shared_card)
        self.bot.message_handler(func=lambda message: message.text in ["Найти вероятность победы"])(
            self.find_the_probability)
        self.bot.message_handler(func=lambda message: message.text in ["Закончить игру"])(self.start)

        markup = telebot.types.ReplyKeyboardMarkup(row_width=3)
        btn1 = telebot.types.KeyboardButton("Ввести свои карты")
        btn2 = telebot.types.KeyboardButton("Добавить общую карту")
        btn3 = telebot.types.KeyboardButton("Найти вероятность победы")
        btn4 = telebot.types.KeyboardButton("Закончить игру")

        markup.add(btn1, btn2, btn3, btn4)
        self.bot.send_message(chat_id=message.chat.id, text="Выберите действие:", reply_markup=markup)

    def new_game(self, message):
        self.users[message.chat.id] = OneUser(3)
        self.continue_the_game(message)
