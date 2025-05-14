GET_ALL_ORDER = """
    SELECT
        *
    FROM
        order_item
    ORDER BY
        price DESC
    LIMIT %s
"""
