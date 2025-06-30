import logging
import os
from decimal import Decimal

from dotenv import load_dotenv
from solana.rpc.api import Client
from solders.keypair import Keypair

from trading_logic.database.get_open_trades import get_open_trades
from trading_logic.jupiter_api.get_current_token_price import get_current_token_price
from trading_logic.solana_rpc.get_associated_token_address import (
    get_associated_token_address,
)
from trading_logic.solana_rpc.get_sol_balance import get_sol_balance
from trading_logic.solana_rpc.get_token_balance import get_token_balance
from trading_logic.trade_analysis.get_all_open_trades_performance import (
    get_all_open_trades_performance,
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()

PRIVATE_KEY = os.environ.get("PRIVATE_KEY")
MAINNET_RPC = os.environ.get("MAINNET_RPC")
TOKEN_ADDRESS = os.environ.get("TOKEN_ADDRESS")
TOKEN_NAME = os.environ.get("TOKEN_NAME")
SOL_ADDRESS = "So11111111111111111111111111111111111111112"


class SolanaTraderBot:
    def __init__(self):
        self.client = Client(MAINNET_RPC)

        self.wallet = Keypair.from_base58_string(PRIVATE_KEY)
        self.wallet_address = str(self.wallet.pubkey())

        self.sol_balance = get_sol_balance(self.client, self.wallet, logger)

        self.associated_token_address = get_associated_token_address(
            TOKEN_ADDRESS, self.client, self.wallet, logger
        )
        self.token_balance = get_token_balance(
            self.associated_token_address,
            TOKEN_NAME,
            self.client,
            logger,
        )

        self.open_trades = get_open_trades(logger)

        self.current_token_price = get_current_token_price(
            input_token_address=TOKEN_ADDRESS,
            output_token_address=SOL_ADDRESS,
            logger=logger,
            token_amount=1,
        )

        self.open_trades_performance = get_all_open_trades_performance(
            self.open_trades, self.current_token_price, logger
        )

        self.highest_bought_price = None
        self.lowest_bought_price = None
        # self.should_buy_more(
        #     self.current_token_price, self.open_trades_performance, logger
        # )

    def run(self):
        logger.info("bot started")

        if self.open_trades:
            self.highest_bought_price = max(
                trade["priceBought"] for trade in self.open_trades
            )
            self.lowest_bought_price = min(
                trade["priceBought"] for trade in self.open_trades
            )

            if self.current_token_price < self.lowest_bought_price * Decimal("0.95"):
                percentage_to_buy = (
                    (self.highest_bought_price - self.current_token_price)
                    / self.highest_bought_price
                ) * 100
                logger.info(f"Percentage difference: {percentage_to_buy:.2f}%")
                logger.info(
                    f"Current price {self.current_token_price} is lower than lowest bought price {self.lowest_bought_price}"
                )
                # implement buy_logic(sol_amount, percentage_to_buy, jupiter_api, logger)
                # create new record in the database

            # check current trades that are +10% to sell them logic
            # update the record in the database after the trade is done
        else:
            # buy 5% of sol balance
            # initial_purchase_strategy()
            logger.info(f"Highest bought price: {self.highest_bought_price:.8f} SOL")
        try:
            self.highest_bought_price = 0.0
        except Exception as e:
            logger.error(f"Error en el ciclo principal: {e}")
