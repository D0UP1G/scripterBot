import asyncio
import os
import subprocess
import webbrowser

from aiogram.types import BotCommand
from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.utils import executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

bot = Bot(token='6160259605:AAFR6z85JU8ZwAT-FH6ZovjDSWwnTb9A_4U')
dp = Dispatcher(bot, storage=storage)

def keyboard():
    markup = InlineKeyboardMarkup()
    for i in os.listdir('scripts'):
        markup.add(InlineKeyboardButton(text=i, callback_data=i ))

    return markup

class file(StatesGroup):
    filename = State()
    link = State()
def startup():
    if os.path.isdir('scripts'):
        pass
    else:
        os.mkdir('scripts')
@dp.message_handler(commands='link')
async def play(msg:types.Message):
    await msg.answer('Ссылка на видео:')
    await file.link.set()

@dp.message_handler(commands='launch')
async def launch(msg:types.Message):
    await msg.answer('launch', reply_markup=keyboard())

@dp.message_handler(commands='delete')
async def delete(msg:types.Message):
    await msg.answer("Введите название файла:")
    await file.filename.set()

@dp.message_handler(state=file.link)
async def link(msg:types.Message,state:FSMContext):
    await state.update_data(link=msg.text)
    webbrowser.open(msg.text)
    print(msg.from_user.id)

    if msg.from_user.id == 2011652576:
        await file.next()
@dp.message_handler(state=file.filename)
async def deleter(message: types.Message, state: FSMContext):
    await state.update_data(filename=message.text)
    path = f'scripts/{message.text}'
    if message.text in os.listdir('scripts'):
        os.remove(path)
        await message.answer("файл удалён")
    else:
        await message.answer('Файл не был найден, ' + path)
        for i in os.listdir('scripts'):
            await message.answer(i)

    await file.next()
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

@dp.message_handler(commands='list')
async def list(msg:types.Message):
    if ''.join(os.listdir('scripts')) == '':
        await msg.answer("Нету файлов")
    else:
        await msg.answer(''.join(os.listdir('scripts')))
@dp.message_handler(commands='start')
async def start(msg:types.Message):
    await msg.answer('Введи /link , и скинь ссылку на видео(желательно YT)')

if __name__ == '__main__':
    executor.start_polling(dp,on_startup=startup())
