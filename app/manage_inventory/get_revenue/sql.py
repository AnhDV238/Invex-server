GET_REVENUE = """
    SELECT
        SUM(total_price)
    FROM
        "order"
    WHERE
        created_at BETWEEN %s and %s
"""