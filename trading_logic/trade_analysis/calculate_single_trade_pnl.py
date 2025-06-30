def calculate_single_trade_pnl(entry_price, current_token_price, quantity):
    """
    Calculate the profit and loss (PnL) for a single trade.

    Parameters:
    - entry_price (float): The price at which the asset was bought.
    - current_token_price (float): The current price of the asset.
    - quantity (float): The amount of the asset traded.
    - fees (float): The fees associated with the trade.

    Returns:
    - float: The PnL for the trade.
    """
    pnl = ((current_token_price) - entry_price) * quantity
    return pnl
