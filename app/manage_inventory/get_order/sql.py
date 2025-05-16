GET_ALL_ORDER = """
    SELECT
        p.name,
        p.image,
        p.price,
        p.unit,
        SUM(oi.quantity) AS total_sold
    FROM
        order_item oi
    INNER JOIN
        product p ON oi.product_id = p.id
    GROUP BY
        p.id, p.name, p.image, p.price, p.unit
    ORDER BY
        total_sold,
        price DESC
    LIMIT %s
"""
