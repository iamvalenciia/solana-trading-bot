def get_token_balance(associated_token_address, TOKEN_NAME, client, logger):
    try:
        token_balance = 0.0
        balance_response = client.get_token_account_balance(associated_token_address)
        ui_amount = balance_response.value.ui_amount
        token_balance += float(ui_amount)
        logger.info(f"💰 Total {TOKEN_NAME} balance: {token_balance}")
        return token_balance
    except Exception as account_error:
        logger.debug(f"Error checking token account: {account_error}")
