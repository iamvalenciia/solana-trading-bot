import boto3


def get_open_trades(logger):
    # - rewrite this function based on the field if isSold = false, so only get those trades,
    # - this feature should will be use where retrieve the items from the DynamoDB table
    dynamodb = boto3.resource("dynamodb", region_name="us-east-1")
    table = dynamodb.Table("BuyOrders")
    response = table.scan()
    items = response["Items"]
    logger.info(f"Open trades fetched: {items}")
    logger.info(f"Total open trades: {len(items)}")
    return items
