from decimal import Decimal

from .calculate_single_trade_pnl import calculate_single_trade_pnl


def get_all_open_trades_performance(open_trades, current_token_price, logger):
    open_trades_performance = []

    for trade in open_trades:
        entry_price = Decimal(trade["priceBought"])
        quantity = Decimal(trade["amount"])
        pnl = calculate_single_trade_pnl(entry_price, current_token_price, quantity)
        open_trades_performance.append({"trade": trade, "pnl": pnl})

    logger.info(f"Open trades performance: {open_trades_performance}")
    return open_trades_performance
