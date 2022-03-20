import tkinter as tk
import logging
from connectors.bitmex import get_contracts
from connectors.binance_future import BinanceFuturesClient
from decouple import config
logger = logging.getLogger()
logger.setLevel(logging.INFO)

stream_handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(levelname)s :: %(message)s')
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)

file_handler = logging.FileHandler('info.log')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)

if __name__ == '__main__':
    binance_id = config("testnet_bitmex_id", default='')
    binance_secret = config("testnet_bitmex_secret", default='')
    binance = BinanceFuturesClient(binance_id,
                                   binance_secret,
                                   True)
    root = tk.Tk()

    root.mainloop()
