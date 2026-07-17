from bot.client import client
from bot.logging_config import logger


def place_order(symbol, side, order_type, quantity, price=None):
    try:
        params = {
            "symbol": symbol.upper(),
            "side": side,
            "type": order_type,
            "quantity": quantity
        }

        if order_type == "LIMIT":
            params["price"] = price
            params["timeInForce"] = "GTC"

        logger.info(f"Order Request: {params}")

        response = client.futures_create_order(**params)

        logger.info(f"Order Response: {response}")

        return response

    except Exception as e:
        logger.error(f"Order Failed: {e}")
        raise


def get_order_status(symbol, order_id):
    try:
        response = client.futures_get_order(
            symbol=symbol.upper(),
            orderId=order_id
        )

        logger.info(f"Order Status: {response}")

        return response

    except Exception as e:
        logger.error(f"Status Check Failed: {e}")
        raise