import telebot
from telebot import types
import conf
import shelve
import pandas as pd
import csv
import collections
from telebot import util
bot = telebot.TeleBot(conf.TOKEN)

bot = telebot.TeleBot(conf.TOKEN)
markup = types.ForceReply()
shelve_name = 'shelve.db'
csv_path = "community_db.csv" #Можно изменить название

fields = ['fb_id', 'user_id', 'if_anon', 'pers_email', 'fb_type', 'fb_text']

df = pd.DataFrame(columns=fields)

welcome_msg = """
Я бот комьюнити-направления Quarteera. Что здесь можно сделать?
*Оставить отзыв.*
  Для того чтобы оставить отзыв на работу одного из наших направлений, напишите /review.
*Оставить запрос.*
  (как сформулировать?) Если вы хотите оставить запрос или предложение о сотрудничестве, напишите /info. 
*Узнать больше.*
  Ответы на часто-задаваемые вопросы можно найти по команде /faq.
"""

if_anon_msg = """
Вы хотите оставить отзыв анонимно или персонально? Если вы хотите оставить свои контакты, требуется согласие на обработку персональных данных. Ознакомиться можно [здесь](http://quarteera.de)."""

faq_msg = """
*Что такое Квартира?*
Quarteera e. V. — первое общегерманское объединение русскоязычных ЛГБТК+ мигрантов  ок, которое с 2011 года выступает за видимость русскоязычных ЛГБТК+ в Германии, в особенности среди русскоязычного населения, а также за повышение информированности о ЛГБТК+ среди русскоязычных людей.
Quarteera видит свою задачу в противодействии множественной дискриминации русскоязычных ЛГБТК+ (из-за их происхождения и сексуальной ориентации/гендерной идентичности).
*Какие есть направления помощи?*
перечисление направлений помощи
*Мы в социальных сетях и в телеграме*
[ссылки на все страницы в соц сетях, открытые чаты и каналы в телеграме]
*Какие есть результаты работы квартиры?*
[результаты работы квартиры (общая информация): чем квартира занимается краткая сводка публичные отчетности]


"""

teams_dic = {
    "комьюнити-направление: работа организации": "team_gen",
    "комьюнити-направление: модерация чатов": "team_chat",
    "комьюнити-направление: проведение мероприятий": "team_event",
    "комьюнити - направление: предложение по контенту": "team_cont",
    "консультационная помощь (юридическая / психологическая)": "team_cons",
    "команда по помощи в релокации": "team_reloc",
    "другое": "other"}
teams = list(teams_dic.keys())

teams_dics =[
{"комьюнити-направление: работа организации": "team_gen"},
{"комьюнити-направление: модерация чатов": "team_chat"},
{"комьюнити-направление: проведение мероприятий": "team_event"},
{"комьюнити - направление: предложение по контенту": "team_cont"},
{"консультационная помощь (юридическая / психологическая)": "team_cons"},
{"команда по помощи в релокации": "team_reloc"},
{"другое": "other"}]


@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = message.from_user.id
    bot.send_message(message.chat.id, "Привет, " + message.from_user.first_name + welcome_msg, parse_mode= "Markdown")
@bot.message_handler(commands=['faq'])
def send_faq(message):
    bot.send_message(message.chat.id,
                     faq_msg,
                     reply_markup=markup, parse_mode="Markdown")

@bot.message_handler(commands=['review'])
def if_anon(message):
    keyboard = types.InlineKeyboardMarkup()
    butt_yes = types.InlineKeyboardButton(text="Даю согласие", callback_data="butt_yes")
    butt_no = types.InlineKeyboardButton(text="Оставить анонимно", callback_data="butt_no")
    keyboard.add(butt_yes)
    keyboard.add(butt_no)
    bot.send_message(message.chat.id,
                     if_anon_msg,
                     reply_markup=keyboard, parse_mode="Markdown")

@bot.message_handler(commands=['team_gen'])
def team_review(message):
    team_name = "комьюнити-направление: работа организации"
    bot.send_message(message.chat.id,
            "Чтобы оставить отклик на работу команды \"" + team_name + "\", просто отправь свой отзыв ответным сообщением. Оно будет переправлено этой команде напрямую.",
            reply_markup = keyboard, parse_mode = "Markdown")


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        if call.data == "butt_yes":
            pers_email = bot.send_message(call.message.chat.id, "Оставьте ваш email для обратной связи", reply_markup=markup)
            #check if the format is correct
            #save to db

            keyboard = types.InlineKeyboardMarkup()
            emo1 = types.InlineKeyboardButton(text="комьюнити-направление: работа организации", callback_data="emo1")
            emo2 = types.InlineKeyboardButton(text="комьюнити-направление: модерация чатов", callback_data="emo2")
            emo3 = types.InlineKeyboardButton(text='помощь в релокации', callback_data="emo3")

            keyboard.add(emo1)
            keyboard.add(emo2)
            keyboard.add(emo3)
            bot.send_message(call.message.chat.id, "На какое направление хотели бы оставить отзыв?", reply_markup=keyboard)

        if call.data == "butt_no":

            keyboard = types.InlineKeyboardMarkup()
            emo1 = types.InlineKeyboardButton(text="комьюнити-направление: работа организации", callback_data="team_gen")
            emo2 = types.InlineKeyboardButton(text="комьюнити-направление: модерация чатов", callback_data="team_chat")
            emo3 = types.InlineKeyboardButton(text='помощь в релокации', callback_data="team_reloc")

            keyboard.add(emo1)
            keyboard.add(emo2)
            keyboard.add(emo3)
            bot.send_message(call.message.chat.id, "На какое направление хотели бы оставить отзыв?", reply_markup=keyboard)
        if call.data in teams:
            team = call.data #переписать чтобы сохранялось название направления в базу


if __name__ == '__main__':
    bot.polling(none_stop=True)