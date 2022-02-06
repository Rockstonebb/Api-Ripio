
CREATE TABLE IF NOT EXISTS ripio_app.`rate` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `pair` varchar(64) NOT NULL,
  `last_price` double(30,18) NOT NULL DEFAULT '0.000000000000000000',
  `low` double(30,18) NOT NULL DEFAULT '0.000000000000000000',
  `high` bigint NOT NULL DEFAULT '0',
  `variation` double(30,18) NOT NULL DEFAULT '0.000000000000000000',
  `volume` double(30,18) NOT NULL DEFAULT '0.000000000000000000',
  `base` varchar(64) NOT NULL,
  `base_name` varchar(128) NOT NULL,
  `quote` varchar(64) NOT NULL,
  `quote_name` varchar(128) NOT NULL,
  `bid` double(30,18) NOT NULL DEFAULT '0.000000000000000000',
  `ask` double(30,18) NOT NULL DEFAULT '0.000000000000000000',
  `avg` double(30,18) NOT NULL DEFAULT '0.000000000000000000',
  `ask_volume` double(30,18) NOT NULL DEFAULT '0.000000000000000000',
  `bid_volume` double(30,18) NOT NULL DEFAULT '0.000000000000000000',
  `created_at` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO ripio_app.`rate` (`id`, `pair`, `last_price`, `low`, `high`, `variation`, `volume`, `base`, `base_name`, `quote`, `quote_name`, `bid`, `ask`, `avg`, `ask_volume`, `bid_volume`, `created_at`) VALUES
	(3, 'USDC_ARS', 219.730000000000000000, 215.270000000000000000, 222, 0.110000000000000000, 21278.372400000000000000, 'USDC', 'USD Coin', 'ARS', 'Pesos', 219.470000000000000000, 220.000000000000000000, 219.220000000000000000, 2075.000000000000000000, 61.444600000000000000, '2022-01-23 15:01:32');
