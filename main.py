from bs4 import BeautifulSoup
import requests
from aiogram import types, Dispatcher, executor, Bot
from config import TOKEN
bot = Bot(TOKEN)
dp = Dispatcher(bot)

LINK_ZL = "https://www.google.com/search?q=zloty+hryvnya&client=firefox-b-d&sxsrf=AB5stBg8Zqat_HfNRFudM8nlzZEHlZ9OnA%3A1688238933415&ei=VXugZNqBGeqRrgS3wKOQCA&ved=0ahUKEwiagLCPnO7_AhXqiIsKHTfgCIIQ4dUDCA4&uact=5&oq=zloty+hryvnya&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIMCAAQDRCABBBGEIICMggIABAFEB4QDTIICAAQCBAeEA06BwgjEOoCECc6DwgAEIoFEOoCELQCEEMYAToYCC4QigUQxwEQ0QMQyAMQ6gIQtAIQQxgCOggIABCABBCxAzoFCAAQgAQ6EQguEIAEELEDEIMBEMcBENEDOg4ILhDHARCxAxDRAxCABDoLCC4QgAQQxwEQ0QM6CwgAEIAEELEDEIMBOgcIABCKBRBDOgwIABCKBRBDEEYQggI6CwguEIAEEMcBEK8BOggIABCABBDLAToKCAAQgAQQRhCCAjoGCAAQFhAeOggIABAWEB4QCjoHCAAQDRCABEoECEEYAFCkEFiCNmDRN2gBcAF4AIABtwKIAaoNkgEIMS4xMS4wLjGYAQCgAQGwARPAAQHaAQYIARABGAHaAQYIAhABGAg&sclient=gws-wiz-serp"
LINK_BNB = "https://www.google.com/search?q=bnb+dolar&client=firefox-b-d&sxsrf=AB5stBgrwoWWKWGmGcCeQrHwHIq-9grDdA%3A1688238905073&ei=OXugZL_8A860rgSGhIKYDw&ved=0ahUKEwj__O2BnO7_AhVOmosKHQaCAPMQ4dUDCA4&uact=5&oq=bnb+dolar&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIHCAAQgAQQCjIICAAQgAQQywEyBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMggIABAWEB4QCjIGCAAQFhAeMgYIABAWEB46BwgjEOoCECc6BwgjEIoFECc6BwgAEIoFEEM6EwguEIoFELEDEIMBEMcBENEDEEM6CwgAEIAEELEDEIMBOgoIABCKBRCxAxBDOg4ILhDHARCxAxDRAxCABDoFCAAQgAQ6CwgAEIoFELEDEIMBOg0IABCKBRCxAxCDARBDOggIABCABBCxAzoKCAAQgAQQChDLAUoECEEYAFCPBljzG2CIH2gBcAF4AIABgQGIAfwHkgEDMC45mAEAoAEBsAEKwAEB&sclient=gws-wiz-serp"
LINK_ETH = "https://ru.investing.com/crypto/ethereum/eth-usd"
LINK_EU = "https://www.google.com/search?client=firefox-b-d&q=euro+grivna"
LINK_DOL = "https://www.google.com/search?client=firefox-b-d&q=dolar+grivna"
LINK_BIT = "https://ru.investing.com/crypto/bitcoin/btc-usd"
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0"}


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer("Hello! Welcome to CURRENCY ALERT BOT\nThis bot follow price of currency, and if price falls or rises, bot will send you sms, but be careful, if you already chose pair of currencies you cant change it before SMS is sent\n.To GET STARTED you need enter command for any pair of currency\nThere list of pair of currencies which bot can looking for:\n/BIT_USD\n/ETH_USD\n/USD_HRN\n/PLN_HRN\n/BNB_USD\n/EU_HRN")


@dp.message_handler(commands=["BIT_USD"])
async def get_price(message: types.Message):
    while True:
        currency = float(bit.bi_get_currency_price().replace(".", "").replace(",", "."))
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
    while True:
        currency = float(eth.et_get_currency_price().replace(".", "").replace(",", "."))
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


@dp.message_handler(commands=["USD_HRN"])
async def get_price(message: types.Message):
    while True:
        currency = float(dol.dol_get_currency_price().replace(",", "."))
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


@dp.message_handler(commands=["EU_HRN"])
async def get_price(message: types.Message):
    while True:
        currency = float(eu.eu_get_currency_price().replace(",", "."))
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


@dp.message_handler(commands=["BNB_USD"])
async def get_price(message: types.Message):
    while True:
        currency = float(bnb.bnb_get_currency_price().replace(",", "."))
        if currency >= bnb.bnb_fix_price + bnb.bnb_difference:
            await message.answer(f"Bnb has increased in price and now it's costs {str(currency)} dollars")
            while True:
                if currency >= bnb.bnb_fix_price + bnb.bnb_big_difference:
                    await message.answer(f"Bnb has greatly increased in price and now it's costs {str(currency)} dollars")
                    break
                elif currency <= bnb.bnb_fix_price - bnb.bnb_big_difference:
                    await message.answer(f"Bnb has greatly fell in price and now it's costs {str(currency)} dollars")
                    break
                elif currency <= bnb.bnb_fix_price - bnb.bnb_difference:
                    await message.answer(f"Bnb has fell in price and now it's costs {str(currency)} dollars")
                    break
        elif currency <= bnb.bnb_fix_price - bnb.bnb_difference:
            await message.answer(f"Bnb has fell in price and now it's costs {str(currency)} dollars")
            while True:
                if currency >= bnb.bnb_fix_price + bnb.bnb_big_difference:
                    await message.answer(f"Bnb has greatly increased in price and now it's costs {str(currency)} dollars")
                    break
                elif currency <= bnb.bnb_fix_price - bnb.bnb_big_difference:
                    await message.answer(f"Bnb has greatly fell in price and now it's costs {str(currency)} dollars")
                    break
                elif currency >= bnb.bnb_fix_price + bnb.bnb_difference:
                    await message.answer(f"Bnb has increased in price and now it's costs {str(currency)} dollars")
                    break
        else:
            pass


@dp.message_handler(commands=["PLN_HRN"])
async def get_price(message: types.Message):
    while True:
        currency = float(zl.zl_get_currency_price().replace(",", "."))
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


class Bitcoin:
    bi_difference = 400
    bi_big_difference = 1300

    def __init__(self):
        self.bi_fix_price = float(self.bi_get_currency_price().replace(".", "").replace(",", "."))

    def bi_get_currency_price(self):
        all_content = requests.get(LINK_BIT, headers=HEADERS)
        soup = BeautifulSoup(all_content.content, "html.parser")
        self.bi_price = soup.findAll("span", {"class": "text-2xl"})
        return self.bi_price[0].text


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


class Dollar:
    dol_difference = 1.5
    dol_big_difference = 5

    def __init__(self):
        self.dol_fix_price = float(self.dol_get_currency_price().replace(",", "."))

    def dol_get_currency_price(self):
        all_content = requests.get(LINK_DOL, headers=HEADERS)
        soup = BeautifulSoup(all_content.content, "html.parser")
        self.dol_price = soup.findAll("span", {"class": "DFlfde SwHCTb"})
        return self.dol_price[0].text


class Euro:
    eu_difference = 2
    eu_big_difference = 6

    def __init__(self):
        self.eu_fix_price = float(self.eu_get_currency_price().replace(",", "."))

    def eu_get_currency_price(self):
        all_content = requests.get(LINK_EU, headers=HEADERS)
        soup = BeautifulSoup(all_content.content, "html.parser")
        self.eu_price = soup.findAll("span", {"class": "DFlfde SwHCTb"})
        return self.eu_price[0].text


class Bnb:
    bnb_difference = 10
    bnb_big_difference = 50

    def __init__(self):
        self.bnb_fix_price = float(self.bnb_get_currency_price().replace(",", "."))

    def bnb_get_currency_price(self):
        all_content = requests.get(LINK_BNB, headers=HEADERS)
        soup = BeautifulSoup(all_content.content, "html.parser")
        self.bnb_price = soup.findAll("span", {"class": "pclqee"})
        return self.bnb_price[0].text


class Zloty:
    zl_difference = 0.5
    zl_big_difference = 2

    def __init__(self):
        self.zl_fix_price = float(self.zl_get_currency_price().replace(",", "."))

    def zl_get_currency_price(self):
        all_content = requests.get(LINK_ZL, headers=HEADERS)
        soup = BeautifulSoup(all_content.content, "html.parser")
        self.zl_price = soup.findAll("span", {"class": "DFlfde SwHCTb"})
        return self.zl_price[0].text


bit = Bitcoin()
bnb = Bnb()
dol = Dollar()
eu = Euro()
eth = Ethereum()
zl = Zloty()


executor.start_polling(dp)
