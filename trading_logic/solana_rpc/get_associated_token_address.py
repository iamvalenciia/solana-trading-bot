from solana.rpc.commitment import Confirmed
from solana.rpc.types import TokenAccountOpts
from solders.pubkey import Pubkey


def get_associated_token_address(TOKEN_ADDRESS, client, wallet, logger):
    try:
        response = client.get_token_accounts_by_owner(
            wallet.pubkey(),
            TokenAccountOpts(mint=Pubkey.from_string(TOKEN_ADDRESS)),
            commitment=Confirmed,
        )
        logger.info(f"Associated token address: {response.value[0].pubkey}")
        return response.value[0].pubkey
    except Exception as e:
        logger.error(f"RPC MOBY associated token address fetch failed: {e}")
        return None
