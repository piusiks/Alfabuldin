from config import TG_TOKEN
import asyncio
from aiogram import Bot, Dispatcher, F 
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

bot = Bot(token= TG_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('данный бот создан исключительно в развлекательных целях без цели кого либо оскорбить, все команды и фото в боте шуточные! \n весь список команд: \n /start - старт бота и весь список команд \n /pizdi - отпиздить балдина \n /zoloto - дать поворовать \n /vOchko - дать в жопу балдину \n /raspisanie - скинуть расписание на завтра \n /info - информация о боте')

@dp.message(Command('pizdi'))
async def cmd_pizdi(message: Message):
    await message.answer('ты отпиздил балдина ')
    
@dp.message(Command('zoloto'))
async def cmd_zoloto(message: Message):
    await message.answer_photo(photo='AgACAgIAAxkBAAOoaCx0m64k2M6xE-tQPitbqjHm4NkAAqLyMRswPmFJo40urgldddABAAMCAAN4AAM2BA',
                                caption='балдин спиздил золото отпизди его')
    
@dp.message(Command('vOchko'))
async def cmd_vOchko(message: Message):
    await message.answer_photo(photo='AgACAgIAAxkBAAOiaCx0Q9OiVQZkDFWz1-YKWuvDRy4AAp7yMRswPmFJo7mdUSrGnFIBAAMCAAN4AAM2BA',
                               caption='балдина отъебли 3 негра громилы')
    
@dp.message(Command('raspisanie'))
async def cmd_raspisanie(message: Message):
    await message.answer_photo(photo='AgACAgIAAxkBAAOmaCx0WqePymBUofDH6P4tVra71VQAAqDyMRswPmFJR141xctHpLcBAAMCAAN4AAM2BA',
                               caption='в группе класса чекни даун')
    
@dp.message(Command('info'))
async def cmd_info(message: Message):
    await message.answer(f'версия бота на момент 20.05.25: 1.0.0 следующее обновление ожидается 21.05.25  \n!!!данный бот создан исключительно в развлекательных целях без цели кого либо оскорбить, все команды и фото в боте шуточные \n Саня сорян если чем то обидел')
    
    
    
@dp.message(F.photo)
async def get_photo(message : Message):
    await message.answer(f'ID фото: {message.photo[-1].file_id}')
    
async def main():
   await dp.start_polling(bot)
   
if __name__ == '__main__':
    asyncio.run(main())