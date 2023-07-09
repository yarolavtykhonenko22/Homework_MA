from bs4 import BeautifulSoup
import requests
from aiogram import types, Dispatcher, executor, Bot
from config import TOKEN
import json
bot = Bot(TOKEN)
dp = Dispatcher(bot)
LINK_ETH = "https://ru.investing.com/crypto/ethereum/eth-usd"
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0"}


def get_currency(have, want):
    api_url = f'https://api.api-ninjas.com/v1/convertcurrency?want={want}&have={have}&amount=1'
    response = requests.get(api_url, headers={'X-Api-Key': 'cpkY4VMRFV/EoGxTbCXVWg==n5UGKyteQ7A04nBi'})
    if response.status_code == requests.codes.ok:
        response_dict = json.loads(response.text)
        return response_dict["new_amount"]
    else:
        print("Error:", response.status_code, response.text)


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer("Hello! Welcome to CURRENCY ALERT BOT\nThis bot follow price of currency, and if price falls or rises, bot will send you sms, but be careful, if you already chose pair of currencies you cant change it before SMS is sent\nTo GET STARTED you need enter command for any pair of currency\nThere list of pair of currencies which bot can looking for:\n/BTC_USD\n/ETH_USD\n/USD_UAH\n/PLN_UAH\n/EU_UAH")


@dp.message_handler(commands=["BTC_USD"])
async def get_price(message: types.Message):
    count = 0
    while True:
        currency = float(bit.bi_get_currency_price())
        if 1 > count:
            await message.answer("Looking for Bitcoin price")
            count += 1
        if currency >= bit.bi_fix_price + bit.bi_difference:
            await message.answer(f"Bitcoin has increased in price and now it's costs {str(currency)} dollars")
            while True:
                if currency >= bit.bi_fix_price + bit.bi_big_difference:
                    await message.answer(f"Bitcoin has greatly increased in price and now it's costs {str(currency)} dollars")
                    break
                elif currency <= bit.bi_fix_price - bit.bi_big_difference:
                    await message.answer(f"Bitcoin has greatly fell in price and now it's costs {str(currency)} dollars")
                    break
                elif currency <= bit.bi_fix_price - bit.bi_difference:
                    await message.answer(f"Bitcoin has fell in price and now it's costs {str(currency)} dollars")
                    break
        elif currency <= bit.bi_fix_price - bit.bi_difference:
            await message.answer(f"Bitcoin has fell in price and now it's costs {str(currency)} dollars")
            while True:
                if currency >= bit.bi_fix_price + bit.bi_big_difference:
                    await message.answer(f"Bitcoin has greatly increased in price and now it's costs {str(currency)} dollars")
                    break
                elif currency <= bit.bi_fix_price - bit.bi_big_difference:
                    await message.answer(f"Bitcoin has greatly fell in price and now it's costs {str(currency)} dollars")
                    break
                elif currency >= bit.bi_fix_price + bit.bi_difference:
                    await message.answer(f"Bitcoin has increased in price and now it's costs {str(currency)} dollars")
                    break
        else:
            pass


@dp.message_handler(commands=["ETH_USD"])
async def get_price(message: types.Message):
    count = 0
    while True:
        currency = float(eth.et_get_currency_price().replace(".", "").replace(",", "."))
        if 1 > count:
            await message.answer("looking for Ethereum price")
            count += 1
        if currency >= eth.et_fix_price + eth.et_difference:
            await message.answer(f"Ethereum has increased in price and now it's costs {str(currency)} dollars")
            while True:
                if currency >= eth.et_fix_price + eth.et_big_difference:
                    await message.answer(f"Ethereum has greatly increased in price and now it's costs {str(currency)} dollars")
                    break
                elif currency <= eth.et_fix_price - eth.et_big_difference:
                    await message.answer(f"Ethereum has greatly fell in price and now it's costs {str(currency)} dollars")
                    break
                elif currency <= eth.et_fix_price - eth.et_difference:
                    await message.answer(f"Ethereum has fell in price and now it's costs {str(currency)} dollars")
                    break
        elif currency <= eth.et_fix_price - eth.et_difference:
            await message.answer(f"Ethereum has fell in price and now it's costs {str(currency)} dollars")
            while True:
                if currency >= eth.et_fix_price + eth.et_big_difference:
                    await message.answer(f"Ethereum has greatly increased in price and now it's costs {str(currency)} dollars")
                    break
                elif currency <= eth.et_fix_price - eth.et_big_difference:
                    await message.answer(f"Ethereum has greatly fell in price and now it's costs {str(currency)} dollars")
                    break
                elif currency >= eth.et_fix_price + eth.et_difference:
                    await message.answer(f"Ethereum has increased in price and now it's costs {str(currency)} dollars")
                    break
        else:
            pass


@dp.message_handler(commands=["USD_UAH"])
async def get_price(message: types.Message):
    count = 0
    while True:
        currency = float(dol.dol_get_currency_price())
        if 1 > count:
            await message.answer("Looking for Dollar price")
            count += 1
        if currency >= dol.dol_fix_price + dol.dol_difference:
            await message.answer(f"Dollar has increased in price and now it's costs {str(currency)} hryvnias")
            while True:
                if currency >= dol.dol_fix_price + dol.dol_big_difference:
                    await message.answer(f"Dollar has greatly increased in price and now it's costs {str(currency)} hryvnias")
                    break
                elif currency <= dol.dol_fix_price - dol.dol_big_difference:
                    await message.answer(f"Dollar has greatly fell in price and now it's costs {str(currency)} hryvnias")
                    break
                elif currency <= dol.dol_fix_price - dol.dol_difference:
                    await message.answer(f"Dollar has fell in price and now it's costs {str(currency)} hryvnias")
                    break
        elif currency <= dol.dol_fix_price - dol.dol_difference:
            await message.answer(f"Dollar has fell in price and now it's costs {str(currency)} hryvnias")
            while True:
                if currency >= dol.dol_fix_price + dol.dol_big_difference:
                    await message.answer(f"Dollar has greatly increased in price and now it's costs {str(currency)} hryvnias")
                    break
                elif currency <= dol.dol_fix_price - dol.dol_big_difference:
                    await message.answer(f"Dollar has greatly fell in price and now it's costs {str(currency)} hryvnias")
                    break
                elif currency >= dol.dol_fix_price + dol.dol_big_difference:
                    await message.answer(f"Dollar has fell in price and now it's costs {str(currency)} hryvnias")
                    break
        else:
            pass


@dp.message_handler(commands=["EU_UAH"])
async def get_price(message: types.Message):
    count = 0
    while True:
        currency = float(eu.eu_get_currency_price())
        if 1 > count:
            await message.answer("Looking for Euro price")
            count += 1
        if currency >= eu.eu_fix_price + eu.eu_difference:
            await message.answer(f"Euro has increased in price and now it's costs {str(currency)} hryvnias")
            while True:
                if currency >= eu.eu_fix_price + eu.eu_big_difference:
                    await message.answer(f"Euro has greatly increased in price and now it's costs {str(currency)} hryvnias")
                    break
                elif currency <= eu.eu_fix_price - eu.eu_big_difference:
                    await message.answer(f"Euro has greatly fell in price and now it's costs {str(currency)} hryvnias")
                    break
                elif currency <= eu.eu_fix_price - eu.eu_difference:
                    await message.answer(f"Euro has fell in price and now it's costs {str(currency)} hryvnias")
                    break
        elif currency <= eu.eu_fix_price - eu.eu_difference:
            await message.answer(f"Euro has fell in price and now it's costs {str(currency)} hryvnias")
            while True:
                if currency >= eu.eu_fix_price + eu.eu_big_difference:
                    await message.answer(f"Euro has greatly increased in price and now it's costs {str(currency)} hryvnias")
                    break
                elif currency <= eu.eu_fix_price - eu.eu_big_difference:
                    await message.answer(f"Euro has greatly fell in price and now it's costs {str(currency)} hryvnias")
                    break
                elif currency >= eu.eu_fix_price + eu.eu_difference:
                    await message.answer(f"Euro has fell in price and now it's costs {str(currency)} hryvnias")
        else:
            pass


@dp.message_handler(commands=["PLN_UAH"])
async def get_price(message: types.Message):
    count = 0
    while True:
        currency = float(zl.zl_get_currency_price())
        if 1 > count:
            await message.answer("Looking for Zloty price")
            count += 1
        if currency >= zl.zl_fix_price + zl.zl_difference:
            await message.answer(f"Zloty has increased in price and now it's costs {str(currency)} hryvnias")
            while True:
                if currency >= zl.zl_fix_price + zl.zl_big_difference:
                    await message.answer(f"Zloty has greatly increased in price and now it's costs {str(currency)} hryvnias")
                    break
                elif currency <= zl.zl_fix_price - zl.zl_big_difference:
                    await message.answer(f"Zloty has greatly fell in price and now it's costs {str(currency)} hryvnias")
                    break
                elif currency <= zl.zl_fix_price - zl.zl_difference:
                    await message.answer(f"Zloty has fell in price and now it's costs {str(currency)} hryvnias")
                    break
        elif currency <= zl.zl_fix_price - zl.zl_difference:
            await message.answer(f"Zloty has fell in price and now it's costs {str(currency)} hryvnias")
            while True:
                if currency >= zl.zl_fix_price + zl.zl_big_difference:
                    await message.answer(f"Zloty has greatly increased in price and now it's costs {str(currency)} hryvnias")
                    break
                elif currency <= zl.zl_fix_price - zl.zl_big_difference:
                    await message.answer(f"Zloty has greatly fell in price and now it's costs {str(currency)} hryvnias")
                    break
                elif currency >= zl.zl_fix_price + zl.zl_difference:
                    await message.answer(f"Zloty has fell in price and now it's costs {str(currency)} hryvnias")
                    break
        else:
            pass


class Euro:
    eu_difference = 2
    eu_big_difference = 6

    def __init__(self):
        self.eu_fix_price = float(self.eu_get_currency_price())

    def eu_get_currency_price(self):
        currency = get_currency("EUR", "UAH")
        return currency


class Bitcoin:
    bi_difference = 400
    bi_big_difference = 1300

    def __init__(self):
        self.bi_fix_price = float(self.bi_get_currency_price())

    def bi_get_currency_price(self):
        currency = get_currency("BTC", "USD")
        return currency


class Dollar:
    dol_difference = 1.5
    dol_big_difference = 5

    def __init__(self):
        self.dol_fix_price = float(self.dol_get_currency_price())

    def dol_get_currency_price(self):
        currency = get_currency("USD", "UAH")
        return currency


class Ethereum:
    et_difference = 67
    et_big_difference = 400

    def __init__(self):
        self.et_fix_price = float(self.et_get_currency_price().replace(".", "").replace(",", "."))

    def et_get_currency_price(self):
        all_content = requests.get(LINK_ETH, headers=HEADERS)
        soup = BeautifulSoup(all_content.content, "html.parser")
        self.et_price = soup.findAll("span", {"class": "text-2xl"})
        return self.et_price[0].text


class Zloty:
    zl_difference = 0.5
    zl_big_difference = 2

    def __init__(self):
        self.zl_fix_price = float(self.zl_get_currency_price())

    def zl_get_currency_price(self):
        currency = get_currency("PLN", "UAH")
        return currency


bit = Bitcoin()
eth = Ethereum()
zl = Zloty()
eu = Euro()
dol = Dollar()
executor.start_polling(dp)
