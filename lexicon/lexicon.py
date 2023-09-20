# Dict for RU messages
LEXICON_MESSAGES_RU: dict[str, str] = {
    '/start': 'Привет! Привет!',
    '/help': 'Нет тут пока никакой помощи 🤓\n\n'
             'Я просто делаю вид, что "I`m your father" 💂‍♀️️',
    'say_what': 'Вот тут не понятно 😩\n\n'
                'Я ведь бот 🤖. Я не все команды понимаю.\n'
                'Попробуй напиши по-другому\n'
                'или посмотри список команд /help',
    'yes': 'Давай 😍',
    'no': 'Неееееет 😭',
    'yes_to_no': 'Да я всё равно пошучу 👹'
}

# Dict for sending stickers
LEXICON_STICKERS: dict[str, str] = {
    'say_what_sticker': 'CAACAgIAAxkBAAIPDmUKwWOANpC3iUQpEDVKAST1UwnAAAIurwEAAWOLRgxvZawu4Zn91TAE',
}

# Dict for jokes stickers
LEXICON_JOKES_STICKERS: dict[int, str] = {
    1: 'CAACAgIAAxkBAAIPEWULHOptr42wmLLlpMpxRkiRELtGAAK-DwAC9uTQSZ6MnpWN_CLyMAQ',
    2: 'CAACAgIAAxkBAAIPFGULN1FAshPtR6PD4kEcC34laSQFAALNDgACekFoSsNsPPK0sdbDMAQ',
    3: 'CAACAgIAAxkBAAIPF2ULN3hM1ni2Lch4hxa2Rc7rcen2AAK9DwACyPfZSYv4yxFiNtBYMAQ',
    4: 'CAACAgUAAxkBAAIPGmULN6jJN35lTHF-aTdgRQZHGwrwAAJxAwAC6QrIA_ARv0J3eWD8MAQ',
    5: 'CAACAgUAAxkBAAIPHWULN7-SSEaVXmzaI1K7Hkg3Qc9MAAJyAwAC6QrIA1t2hyVXP3HDMAQ',
    6: 'CAACAgUAAxkBAAIPIGULN8_ZZ4XxoXeut01mf6cR1fgyAAIqAgACCSNAV3OL1BfF6UE4MAQ',
    7: 'CAACAgUAAxkBAAIPI2ULN9yxWtm4Ibw-ZYloS2uQXaKMAAJ1AwAC6QrIA-Hzuc7shm0EMAQ',
    8: 'CAACAgUAAxkBAAIPJmULN_u71dxoWT3GD3TKGmXVk1s3AAJ2AwAC6QrIA_Bu__izxgxGMAQ',
    9: 'CAACAgUAAxkBAAIPKWULOAkYrkjCxc0WaVe6MtHFDhOGAAJ3AwAC6QrIA7UZgriAXTgnMAQ',
    10: 'CAACAgUAAxkBAAIPL2ULOC3Yk-9b0d_k04p70iWanhX1AAKDAwAC6QrIA3LDp_J9s7MAATAE',
    11: 'CAACAgUAAxkBAAIPNWULOEjhWfPaKCtqCgfrjvuq3KHqAAJ9AgACkbk4V_GoKPgszp6lMAQ',
    12: 'CAACAgUAAxkBAAIPO2ULOFsix1OQSNdxWBubmBSQTLVSAALrAQACfp5AVwpguYrrGxc_MAQ',
    13: 'CAACAgUAAxkBAAIPPmULOHLWv2lld06xLhxQHnuU4DTUAAJ_AwAC6QrIA4RCcQ9erC1cMAQ',
    14: 'CAACAgUAAxkBAAIPRGULOIfWPunEWJvklD1sC0Qiq60YAAKmAwAC6QrIA3mzkAhrhbH0MAQ',
    15: 'CAACAgUAAxkBAAIPSmULOJ7cazFy26uGhumxqwL7BsE_AAK7AwAC6QrIA-1pQNniqxPfMAQ',
    16: 'CAACAgUAAxkBAAIPTWULOLX-JhAH3QfQhhQMC_jXrs2mAALGAwAC6QrIA8HdjgpS79UTMAQ',
    17: 'CAACAgUAAxkBAAIPUGULOMGgR_VfI1vKYL3PTdS2yIcQAALHAwAC6QrIA1tzQyM4IJHmMAQ',
    18: 'CAACAgUAAxkBAAIPU2ULOM9zTgAB7UI59S0YcjoX2Rg9DgACyQMAAukKyANTCfgdLblqljAE',
    19: 'CAACAgIAAxkBAAIPWWULOVmKeemQ59JvYvRcJPegJN-QAALLFgAC2195SIUlKZQpDDcNMAQ',
    20: 'CAACAgIAAxkBAAIPXGULOXp3yEUxvDfcUFIjBwJHXyDbAAI4EQACe2KYScU9o5OriGzxMAQ',
    21: 'CAACAgIAAxkBAAIPZWULOe0pgZI2uFGVDOm1aLzVW7MqAAJMAwACRxVoCSY5TyFY9HRiMAQ',
    22: 'CAACAgIAAxkBAAIPa2ULOgxZIl9LoHBMQxUHBBdkOwXzAAKQAwACRxVoCXgrgKEWq1_7MAQ',
    23: 'CAACAgIAAxkBAAIPcWULOnKahoginhW-gdRFfn3PMWEaAAJFEwAC4iyoSy6-Zq-5UAb9MAQ',
    24: 'CAACAgIAAxkBAAIPd2ULOo5fUYEcmhIFD4g7SmtxfFq8AAJAAQACxKtoC5TbjupZJ7umMAQ',
    25: 'CAACAgIAAxkBAAIPfWULOucCX7Es3jjT-hWfqPYso3dbAAJbLwACvKGJSnltimhUhk3mMAQ',
    26: 'CAACAgIAAxkBAAIPgGULOwGqRURUMOKLgb_jk96zV1GeAAI9LgACZ9gYSIzpRDBXWCDlMAQ',
    27: 'CAACAgIAAxkBAAIPg2ULOzXcN-u3c65NNcmCCmQzmdv3AALoZAACVVLxSpOXbHw_q14pMAQ',
    28: 'CAACAgIAAxkBAAIPhmULO4M-sDzZu0A9kHusHllZRpOOAAL1OQACJcmJSjo3yvq1NwQsMAQ',
    29: 'CAACAgIAAxkBAAIPiWULO7B0GOykDgb5S2y69qxPA3x4AAJPNQACEkkYSyAOCfvokCDdMAQ',
    30: 'CAACAgIAAxkBAAIPjGULO91NuzINIjwy6VFE6ezUbhZGAAL_NgACPd05SQoP4ZJuuBDzMAQ',
    31: 'CAACAgIAAxkBAAIPj2ULPA-Wl90Js4ApRyzJBuM3tHdXAAJHAwACtXHaBjV7c9kAAYsdpDAE'

}

LEXICON_COMMANDS: dict[str, str] = {
    '/start': 'Запустить бот',
    '/help': 'Справка по работе бота',
    '/joke': 'Прислать великолепную шутку!'
}

# Dict for sending jokes
LEXICON_JOKES: dict[int, str] = {
    1: 'Митинг косоглазых состоялся на сорок метров левее здания городской администрации.',
    2: '- Что такое красное и вредно для зубов?\n'
       '- Кирпич',
    3: 'Девушка не вовремя сделала каменное лицо и утонула.',
    4: '— Скажите, Сергей, а как вы догадались, что в доме есть кто—то чужой?\n'
       '— Ну, у нас в семье как—то не принято внезапно бить меня сзади табуреткой по голове.',
    5: '— Неужели тебе сложно ответить? Что за игнор?\n'
       '— Молодой человек, отойдите от гроба.',
    6: 'Непринципиальный священник начал проповедь словами «Хотите — верьте, хотите — нет».',
    7: 'Когда перестает работать интернет, ты можешь погрузиться в свои мысли и серьезно поду...\n'
       'А нет, всё, заработал.',
    8: 'Молодой мясник не знал с чего начать и представился свинье.',
    9: 'У самой заботливой в мире девочки хомячок весит 22 килограмма.',
    10: 'Чтобы хоть как—то отвлечь внимание от дырки в носке, мальчик Петя ударил именинницу табуреткой.'
}
