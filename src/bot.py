
from telegram import ReplyKeyboardRemove, Update
from telegram.ext import ConversationHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
  cid = update.message.chat.id

  start_message = """\
    🤖 Привет! Я бот комьюнити-направления Quarteera. Что здесь можно сделать?

    📍 Оставить отзыв
    Для того чтобы оставить отзыв на работу одного из наших направлений, напишите /review.

    📍 Оставить запрос
    Если вы хотите оставить запрос или предложение о сотрудничестве, напишите /info.

    📍 Узнать больше
    Ответы на часто-задаваемые вопросы можно найти в /faq.

    📍 Закончить разговор с помощью /exit.
    """
  
  await update.message.reply_text(start_message, reply_markup = ReplyKeyboardRemove())

  return ConversationHandler.END


async def review(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
  review_message = "Как бы вы хотели оставить отзыв - персонально или анонимно?"
  await update.message.reply_text(review_message)

  processed: str = update.message.lower()
  if "персонально" in processed:
    update.message.reply_text("Требуется согласие на обработку персональных данных. Ознакомиться  можно здесь. (гиперссылка). Ответьте ниже согласны или нет.")
    
    if "согласен" & "согласна" in processed:
      update.message.reply_text("Укажите данные: ваше имя и электронную почту через запятую.")
    else:
      return review()
    
  else:
    await update.message.reply_text("Отзыв будет записываться в базу анонимно.")

  review_message = "Спасибо за ваш отзыв! Оставить еще один отзыв можно по команде /review." 
  await update.message.reply_text(review_message, reply_markup = ReplyKeyboardRemove())

  return ConversationHandler.END


async def info(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
  info_message = ""
  await update.message.reply_text(info_message, reply_markup = ReplyKeyboardRemove())

  return ConversationHandler.END


async def faq(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:

  faq_message = """\
    Что такое Квартира? 🏳️‍🌈

    Quarteera e. V. — первое общегерманское объединение русскоязычных ЛГБТК+ мигрантов*ок.
    С 2011 года выступает за видимость русскоязычных ЛГБТК+ в Германии, в особенности среди русскоязычного населения, а также за повышение информированности о ЛГБТК+ среди русскоязычных людей. 
    Quarteera видит свою задачу в противодействии множественной дискриминации русскоязычных ЛГБТК+ (из-за их происхождения и сексуальной ориентации/гендерной идентичности).

    🔸 Какие есть направления помощи?
    [перечисление направлений помощи]

    🔸 Мы в социальных сетях и в телеграме
    [ссылки на все страницы в соц сетях, открытые чаты и каналы в телеграме]

    🔸 Какие есть результаты работы квартиры?
    [результаты работы квартиры (общая информация): чем квартира занимается краткая сводка публичные отчетности]
    """

  await update.message.reply_text(faq_message, reply_markup = ReplyKeyboardRemove())

  return ConversationHandler.END


async def exit(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:

  await update.message.reply_text(
    """\
      До свидания! 👋 Мы надеемся, что наш телеграм бот был полезен. 
      
      Если Вы не нашли решение на все вопросы, напишите нам в службу поддержки. 
      
      Для начала разговора нажмите /start.
      
      """, reply_markup = ReplyKeyboardRemove()
  )

  return ConversationHandler.END


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:

  return ConversationHandler.END


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
  print(f'Update {update} caused the following error {context.error}.')

  return ConversationHandler.END