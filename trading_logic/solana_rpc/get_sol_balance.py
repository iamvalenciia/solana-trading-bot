def get_sol_balance(client, wallet, logger):
    balance = client.get_balance(wallet.pubkey()).value / 1e9
    logger.info(f"SOL balance: {balance:.4f}")
    return balance
