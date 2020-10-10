from main import bot, ourDispatcher
from aiogram.types import Message, ReplyKeyboardRemove
from config import adminID
from aiogram.dispatcher.filters import Command, Text
from keyboard.default import menu

async def startupMessage(ourDispatcher):
    await bot.send_message(chat_id=adminID, text="АХТУНГ! \n Бот перезапущён - небольшие технические шОкОлАдКи XD ")

@ourDispatcher.message_handler(Command("start"))
async def echo(message: Message):
    text = f"Приветики, я бот, у которого ты можешь узнать свое расписание.\n Я думаю это намного удобней, чем каждый раз заглядывать в дневник. \n Уверен, мы сработаемся с тобой :) \n Напиши комманду /menu что бы перейти к выбору дня."
    await message.answer(text=text)

@ourDispatcher.message_handler(Command("menu"))
async def showMenu(message: Message):
    await message.answer("Выбери из меню ниже: ", reply_markup=menu)

@ourDispatcher.message_handler(Text(equals=["Понедельник"]))
async def getMonday(message: Message):
    await message.answer("8:30 - 9:15\n"
                         "1. *отдых :з*\n"
                         "10 минут - перемена\n"
                         "9:25 - 10:10\n"
                         "2. Алгебра\n"
                         "10 минут - перемена\n"
                         "10:20 - 11:05\n"
                         "3. Фізкультура\n"
                         "20 минут - перемена\n"
                         "11:25 - 12:10\n"
                         "4. Англійська мова\n"
                         "20 минут - перемена\n"
                         "12:30 - 13:15\n"
                         "5. Громадянська освіта\n"
                         "10 минут - перемена\n"
                         "13:30 - 14:15\n"
                         "6. Фізика\n"
                         "10 минут - перемена\n"
                         "14:25 - 15:10\n"
                         "7. Зарубіжна література\n"
                         "10 минут - перемена\n"
                         "15:15 - 16:05\n"
                         "8. Українська мова\n"
                         "*РУССКИЕ ИДУТ ДОМОЙ!*\n")
replyMarkUpOnMonday = ReplyKeyboardRemove()

@ourDispatcher.message_handler(Text(equals=["Вторник"]))
async def getTuesday(message: Message):
    await message.answer("8:30 - 9:15\n"
                         "1. Історія України\n"
                         "10 минут - перемена\n"
                         "9:25 - 10:10\n"
                         "2. Українська мова\n"
                         "10 минут - перемена\n"
                         "10:20 - 11:05\n"
                         "3. Всесвітня Історія\n"
                         "20 минут - перемена\n"
                         "11:25 - 12:10\n"
                         "4. Інформатика\n"
                         "20 минут - перемена\n"
                         "12:30 - 13:15\n"
                         "5. Геометрія\n"
                         "10 минут - перемена\n"
                         "13:30 - 14:15\n"
                         "6. Геометрія\n"
                         "10 минут - перемена\n"
                         "14:25 - 15:10\n"
                         "7. *отдых :з*\n"
                         "10 минут - перемена\n"
                         "15:15 - 16:05\n"
                         "8. Географія\n"
                         "*РУССКИЕ ИДУТ ДОМОЙ!*\n")
replyMarkUpOnTuesday = ReplyKeyboardRemove()

@ourDispatcher.message_handler(Text(equals=["Среда"]))
async def getWednesday(message: Message):
    await message.answer("8:30 - 9:15\n"
                         "1. Англійська мова\n"
                         "10 минут - перемена\n"
                         "9:25 - 10:10\n"
                         "2. Фізика\n"
                         "10 минут - перемена\n"
                         "10:20 - 11:05\n"
                         "3. Історія України\n"
                         "20 минут - перемена\n"
                         "11:25 - 12:10\n"
                         "4. Українська мова\n"
                         "20 минут - перемена\n"
                         "12:30 - 13:15\n"
                         "5. Алегбра\n"
                         "10 минут - перемена\n"
                         "13:30 - 14:15\n"
                         "6. *отдых :з*\n"
                         "10 минут - перемена\n"
                         "14:25 - 15:10\n"
                         "7. Українська мова\n"
                         "10 минут - перемена\n"
                         "15:15 - 16:05\n"
                         "8. Трудове навчання\n"
                         "*РУССКИЕ ИДУТ ДОМОЙ!*\n")
replyMarkUpOnWednesday = ReplyKeyboardRemove()

@ourDispatcher.message_handler(Text(equals=["Четверг"]))
async def getThursday(message: Message):
    await message.answer("8:30 - 9:15\n"
                         "1. *отдых :з*\n"
                         "10 минут - перемена\n"
                         "9:25 - 10:10\n"
                         "2. Громадянська освіта\n"
                         "10 минут - перемена\n"
                         "10:20 - 11:05\n"
                         "3. Хімія\n"
                         "20 минут - перемена\n"
                         "11:25 - 12:10\n"
                         "4. Фізика\n"
                         "20 минут - перемена\n"
                         "12:30 - 13:15\n"
                         "5. Біологія\n"
                         "10 минут - перемена\n"
                         "13:30 - 14:15\n"
                         "6. Українська література\n"
                         "10 минут - перемена\n"
                         "14:25 - 15:10\n"
                         "7. Англійська мова\n"
                         "10 минут - перемена\n"
                         "15:15 - 16:05\n"
                         "8. Фізкультура\n"
                         "*РУССКИЕ ИДУТ ДОМОЙ!*\n")
replyMarkUpOnThursday = ReplyKeyboardRemove()

@ourDispatcher.message_handler(Text(equals=["Пятница"]))
async def getFriday(message: Message):
    await message.answer("8:30 - 9:15\n"
                         "1. *отдых :з*\n"
                         "10 минут - перемена\n"
                         "9:25 - 10:10\n"
                         "2. Захист Вітчизни\n"
                         "10 минут - перемена\n"
                         "10:20 - 11:05\n"
                         "3. Англійська мова\n"
                         "20 минут - перемена\n"
                         "11:25 - 12:10\n"
                         "4. Англійська Мова\n"
                         "20 минут - перемена\n"
                         "12:30 - 13:15\n"
                         "5. Українська література\n"
                         "10 минут - перемена\n"
                         "13:30 - 14:15\n"
                         "6. Біологія\n"
                         "10 минут - перемена\n"
                         "14:25 - 15:10\n"
                         "7. Фізкультура\n"
                         "10 минут - перемена\n"
                         "15:15 - 16:05\n"
                         "8. Хімія\n"
                         "*РУССКИЕ ИДУТ ДОМОЙ!*\n")

replyMarkUpOnFriday = ReplyKeyboardRemove()