GET_PRODUCTS = """
    SELECT
        p.name,
        p.image,
        p.price,
        b.name as brand_name,
        p.inventory_quantity
    FROM
        product as p
    INNER JOIN
        brand as b ON b.id = p.brand_id
    LIMIT %s
"""