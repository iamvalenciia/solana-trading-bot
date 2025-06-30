from core import SolanaTraderBot


def lambda_handler(event, context):
    bot = SolanaTraderBot()
    bot.run()
    return {"statusCode": 200, "body": "AccumulationBot executed successfully."}


if __name__ == "__main__":
    lambda_handler({}, {})
