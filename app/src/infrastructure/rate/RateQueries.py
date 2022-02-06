

AVERAGE_RATE = """
SELECT c.pair AS pair, AVG(c.last_price) AS lastPrice, AVG(c.variation) AS variation, AVG(c.created_at) AS createdAt
FROM rate c WHERE c.pair = %s;
"""

ALL_RATES_PAIR = """
SELECT c.pair AS pair, c.last_price AS lastPrice, c.variation AS variation, c.created_at AS createdAt
FROM rate c WHERE c.pair = %s ORDER BY c.created_at DESC ;
"""