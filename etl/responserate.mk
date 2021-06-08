# ETL pipeline for Decennial Census Self-Response Rates
# See https://www.census.gov/data/developers/data-sets/decennial-response-rates.2020.html

# Download self-response rate data from the API

$(DATA_DIR_PROCESSED)/responserate_2020_population_tracts.csv: | $(DATA_DIR_PROCESSED)
	pipenv run downloadresponseratetract  --data-dir $(DATA_DIR) --year 2020

$(DATA_DIR_PROCESSED)/responserate_2010_population_tracts.csv: | $(DATA_DIR_PROCESSED)
	pipenv run downloadresponseratetract  --data-dir $(DATA_DIR) --year 2010

# Download the crosswalk from self-response rate tracts for the 2020 census
# and current (presumably 2019 TIGER) tracts
$(DATA_DIR_SRC)/rr_tract_rel.zip: | $(DATA_DIR_PROCESSED)
	wget -O $@ https://www2.census.gov/geo/maps/DC2020/SR20/rr_tract_rel.zip