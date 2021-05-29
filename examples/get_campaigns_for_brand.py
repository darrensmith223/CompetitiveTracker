from competitivetracker import CompetitiveTracker
import time

api_key = "API_KEY"
brand_name = "example_brand"
time_period = "daysBack:3"

ct = CompetitiveTracker(api_key)  # Instantiate Competitive Tracker
brandId = ct.core.discover.search_brands(brand_name)["brands"][0]["id"]  # Use core.discover to search for the brand and pull the brandId of the first result
time.sleep(5)  # Sleep for 5 seconds due to default rate limiting on the API
results = ct.search.search(
    qd=time_period,
    brandId=brandId
)  # Use the search function to query for all campaigns sent by the brand during the specified time window
