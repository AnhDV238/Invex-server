GET_REVENUE = """
    SELECT
        SUM(total_price)
    FROM
        "order"
    WHERE
        created_at BETWEEN %s and %s
"""

GET_INVENTORY_EXPIRY_DATE = """
    SELECT
        COUNT(expiry_date)
    FROM
        inventory
    WHERE
        expiry_date BETWEEN %s and %s
"""