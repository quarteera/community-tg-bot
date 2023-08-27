
from telegram import ReplyKeyboardRemove, Update
from telegram.ext import ConversationHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
  #context.bot.sendChatAction(chat_id = update.message.chat_id, action =        #telegram.ChatAction.TYPING)
  #sleep(random() * 2 + 3.)

  start_message = """\
    Привет! Я бот комьюнити-направления Quarteera. Что здесь можно сделать?
    1. Оставить отзыв.
    Для того чтобы оставить отзыв на работу одного из наших направлений, напишите /review.
    2. Оставить запрос.
    Если вы хотите оставить запрос или предложение о сотрудничестве, напишите /info.
    3. Узнать больше.
    Ответы на часто-задаваемые вопросы можно найти по команде /faq.
    4. Закончить разговор по команде /exit.
    """
  
  # Send the start message to the user
  await update.message.reply_text(start_message)
  return ConversationHandler.END


async def review(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
  review_message = "Как бы вы хотели оставить отзыв? Выберите ниже."
  await update.message.reply_text(review_message)
  return ConversationHandler.END


async def info(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
  info_message = ""
  await update.message.reply_text(info_message)
  return ConversationHandler.END


async def faq(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:

  faq_message = """\
    Что такое Квартира?
    Quarteera e. V. — первое общегерманское объединение русскоязычных ЛГБТК+ мигрантов*ок, которое с 2011 года выступает за видимость русскоязычных ЛГБТК+ в Германии, в особенности среди русскоязычного населения, а также за повышение информированности о ЛГБТК+ среди русскоязычных людей. Quarteera видит свою задачу в противодействии множественной дискриминации русскоязычных ЛГБТК+ (из-за их происхождения и сексуальной ориентации/гендерной идентичности).
    Какие есть направления помощи?
    [перечисление направлений помощи]
    Мы в социальных сетях и в телеграме
    [ссылки на все страницы в соц сетях, открытые чаты и каналы в телеграме]
    Какие есть результаты работы квартиры?
    [результаты работы квартиры (общая информация): чем квартира занимается краткая сводка публичные отчетности]
    """
                
  await update.message.reply_text(faq_message)
  return ConversationHandler.END


async def exit(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:

  await update.message.reply_text(
    "До свидания! Мы надеемся, что наш телеграм бот был полезен. Если Вы не нашли на все вопросы решение, напишите нам в службу поддержки. Для начала разговора нажмите /start.", reply_markup = ReplyKeyboardRemove()
  )

  return ConversationHandler.END