from competitivetracker import CompetitiveTracker

api_key = "API_KEY"
ct = CompetitiveTracker(api_key)
response = ct.core.industries.get_all_industries()
print(response)
