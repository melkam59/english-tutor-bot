from aiogram.filters.callback_data import CallbackData


class CDBuyPremium(CallbackData, prefix="buy_premium"):
    months: int = 1
