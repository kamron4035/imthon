from aiogram import types, executor
from aiogram import Bot, Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import BotCommand


class Form(StatesGroup):
    message1 = State()


BOT_TOKEN = '5822536726:AAE2V49_GGmsNQ_8iXPtnMheAVRMrSMwpqs'
bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot=bot, storage=MemoryStorage())


async def bot_command():
    await bot.set_my_commands([BotCommand('start',"Foydalanish ni Boshlash"), BotCommand('help', "Bu bot nima qila oladi")])


async def start(msg: types.Message):
    await bot_command()
    await msg.reply("Assalom Alekum")
    await Form.message1.set()


async def help(msg:types.Message):
    f = f"Assalomu alaykum <b>{msg.from_user.username}</b>\nMennga Xabar Jo'nating Agar Unli Harflar soni <b>5</b> tadan oshsa  xabarni o'chiraman "
    await bot_command()
    await msg.answer(f, parse_mode='html')
    await Form.message1.set()


async def del_msg(msg: types.Message):
    # i, e, a, o, u, oʻ
    await bot_command()
    s = msg.text
    count = 0
    for i in s:
        if i == 'a' or i == 'i' or i == 'e' or i == 'o' or i == 'u' or i == "o'":
            count+=1
    if count >= 5:
        s = f"<s>{msg.text}</s> ❌"
        await msg.answer(s,parse_mode='html')
        await msg.delete()
    else:
        await msg.reply(f"{msg.text}✅")


# ==================================== DP ================================================

#__COMMANDS__

dp.register_message_handler(start, commands='start', state='*')
dp.register_message_handler(help,commands='help', state='*')


#__STATES__

dp.register_message_handler(del_msg, state= Form.message1)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)