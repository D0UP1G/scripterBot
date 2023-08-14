import os
import subprocess

from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
bot = Bot(token='6160259605:AAFR6z85JU8ZwAT-FH6ZovjDSWwnTb9A_4U')
dp = Dispatcher(bot)

def keyboard():
    markup = InlineKeyboardMarkup()
    for i in os.listdir('scripts'):
        markup.add(InlineKeyboardButton(text=i, callback_data=i ))

    return markup


def startup():
    if os.path.isdir('scripts'):
        pass
    else:
        os.mkdir('scripts')
    keyboard()

@dp.message_handler(commands='launch')
async def launch(msg:types.Message):
    await msg.answer('launch', reply_markup=keyboard())

@dp.callback_query_handler()
async def data(data: types.CallbackQuery):
    print(data.data)
    process = subprocess.Popen(['python3', 'scripts/'+data.data], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(process.communicate())

@dp.message_handler(content_types=types.ContentTypes.DOCUMENT)
async def process_document(message: types.Message):
    file_name = message.document.file_name
    file_info = await bot.get_file(message.document.file_id)
    file_path = file_info.file_path
    save_path = os.path.join('scripts', message.document.file_name)
    await bot.download_file(file_path, save_path)

if __name__ == '__main__':
    executor.start_polling(dp,on_startup=startup())
