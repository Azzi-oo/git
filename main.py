from aiogram import Bot, Dispatcher, executor, types

TOKEN = '6198687861:AAHXYEh4DacXEdslG_NFfVjan_fQHTs8HuE'

bot = Bot(TOKEN)
dp = Dispatcher(bot)

async def on_startup(_):
    print('Бот успешно был запущен')

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer('Привет, добро пожаловать в наш бот', parse_mode="HTML")

@dp.message_handler(commands=['give'])
async def start_command(message: types.Message):
    await bot.send_sticker(message.from_user.id, sticker="CAACAgIAAxkBAAEJDE9kac-NK7VIqPzKSn_KczvohaCJRwAC1xgAAm4m4UsFYy3CmOv8qy8E")
    await message.delete()

@dp.message_handler()
async def send_emoji(message: types.Message):
    await message.reply(message.text + '🤓')

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)