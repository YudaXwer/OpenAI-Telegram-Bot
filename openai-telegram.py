# Telegram Bot OpenAI ChatGPT version Python by Wannazid
import openai
from aiogram import Bot, Dispatcher, types, executor

bot_tkn = '5999431093:AAEuVF0lCGXAGty1ohkh6oQ4m63b_FNJoPk'
openai.api_key = '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'


bot = Bot(token=bot_tkn)
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['start','help'])
async def user_come(pesan: types.Message):
	await pesan.answer('Selamat Datang, silahkan tanyakan apa saja yang ingin anda ketahui')
	
@dp.message_handler(lambda message: message.text)
async def ai_answer(message: types.Message):
	respon = openai.Completion.create(model='text-davinci-003', prompt=message.text, temperature=0, max_tokens=1000)
	parse = respon['choices'][0]['text']
	await message.reply(parse)
	
print('Bot berjalan !')	
executor.start_polling(dp)
