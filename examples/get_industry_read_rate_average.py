from competitivetracker import CompetitiveTracker
import time

# Initialize Variables
api_key = "API_KEY"
industry_name = "Consumer Electronics & Accessories"
time_period = "daysBack:7"


ct = CompetitiveTracker(api_key)  # Instantiate Competitive Tracker
industryId = ct.core.discover.search_industries(q=industry_name)["industries"][0]["id"]  # Use core.discover to search for the brand and pull the industryId of the first result

#
rolling_sum = 0
rolling_count = 0
page = 1
running = True
while running:
    time.sleep(5)  # Sleep for 5 seconds due to rate limiting on the API
    results = ct.search.search(
        qd=time_period,
        industryId=industryId,
        page=page
    )  # Use the search function to query for all campaigns sent by an industry during the specified time window

    if len(results) == 0:  # check if results page is empty
        running = False
    else:
        page += 1

    # Check all campaign results for read rate
    for campaign in results:
        readRatePercent = campaign.get("readRatePercent")
        if readRatePercent is not None and readRatePercent != 0.0:
            rolling_sum += float(readRatePercent)
            rolling_count += 1

industry_avg = rolling_sum / rolling_count
print(industry_avg)


