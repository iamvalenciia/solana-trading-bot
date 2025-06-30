from decimal import Decimal

import requests


def get_current_token_price(
    input_token_address,
    output_token_address,
    logger,
    token_amount=1,
    input_decimals=6,
    slippage_tolerance=50,
    request_timeout=10,
):
    jupiter_quote_url = "https://quote-api.jup.ag/v6/quote"
    sol_decimals = 9

    request_params = {
        "inputMint": input_token_address,
        "outputMint": output_token_address,
        "amount": int(token_amount * (10**input_decimals)),
        "slippageBps": slippage_tolerance,
    }

    try:
        logger.info(f"Fetching price for {token_amount} tokens")

        response = requests.get(
            jupiter_quote_url, params=request_params, timeout=request_timeout
        )
        response.raise_for_status()

        quote_data = response.json()

        if "outAmount" not in quote_data:
            logger.warning("Missing 'outAmount' in API response")
            return None

        output_amount_raw = Decimal(quote_data["outAmount"])
        token_price_in_sol = output_amount_raw / (10**sol_decimals)

        logger.info(f"Token price: {token_price_in_sol:.8f} SOL")
        return token_price_in_sol

    except requests.exceptions.Timeout:
        logger.error("Request timeout while fetching token price")
        return None
    except requests.exceptions.RequestException as network_error:
        logger.error(f"Network error: {network_error}")
        return None
    except (KeyError, ValueError) as data_error:
        logger.error(f"Data parsing error: {data_error}")
        return None
    except Exception as unexpected_error:
        logger.error(f"Unexpected error: {unexpected_error}")
        return None
