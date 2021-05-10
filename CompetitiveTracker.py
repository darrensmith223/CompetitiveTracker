import requests
import json


def GetAverageVolPerCampaign(apiKey, domain, qd=None):
    """
    Get the average campaign volume for a domain
    :param apiKey:  API key for authentication
    :param domain:  The domain to query for  The domain to query for
    :param qd:  A date range query parameter.  Accepts "since:YYYYMMDD", "between:YYYYMMDDhhmmss,YYYYMMDDhhmmss",
                and "daysBack:N".
                Examples: 'since:20190601', 'between:20191001000000,20191002060000', 'daysBack:30'
    :return:  'float' object
    """
    apiUrl = "http://api.edatasource.com/v4/competitive/intelligence/"+domain+"/averageVolumePerCampaign"
    parameters = {
        "Authorization": apiKey
    }
    parameters = SetOptionalParams(parameters, qd=qd)
    apiResponse = MakeAPICall(apiUrl, parameters)

    return json.loads(apiResponse)


def GetCampaignByID(apiKey, campaignId, embed=None):
    """
    Get details for a specified campaign using the Campaign ID
    :param apiKey:  API key for authentication
    :param campaignId:  The campaign identifier value to search for.
    :param embed:  The objects within the return model you wish to embed.
                    Embed parameter accepts: sendingIps, rawEmail, ispPlacements, links, headers
    :return:  'dict' object
    """
    apiUrl = "http://api.edatasource.com/v4/competitive/intelligence/campaign/"+campaignId
    parameters = {
        "Authorization": apiKey
    }
    parameters = SetOptionalParams(parameters, embed=embed)
    apiResponse = MakeAPICall(apiUrl, parameters)

    return json.loads(apiResponse)


def GetCampaignsByDomain(apiKey, domain, qd, campaignLengthFilter=None, page=None, per_page=None, order=None
                         , embed=None):
    """
    Get campaign details for a domain within a specified time period
    :param apiKey:  API key for authentication
    :param domain:  The domain to query for
    :param qd:  A date range query parameter.  Accepts "since:YYYYMMDD", "between:YYYYMMDDhhmmss,YYYYMMDDhhmmss",
                and "daysBack:N".
                Examples: 'since:20190601', 'between:20191001000000,20191002060000', 'daysBack:30'
    :param campaignLengthFilter:  Length filter in days for the campaign (examples '>,2' '<,5' '=,1') 
    :param page:  The page to query for in pagination
    :param per_page:  The amount of records per page you wish to query for (max 100)
    :param order: The property to sort by ('property' for decending, '-property' for ascending)
                    Order options: firstSeen, -firstSeen, lastSeen, -lastSeen, inbox, -inbox, spam, -spam
    :param embed:  The objects within the return model you wish to embed.
                    Embed parameter accepts: sendingIps, rawEmail, ispPlacements, links, headers
    :return:  'list' object
    """
    apiUrl = "http://api.edatasource.com/v4/competitive/intelligence/"+domain+"/campaigns"
    parameters = {
        "Authorization": apiKey,
        "qd": qd
    }
    parameters = SetOptionalParams(parameters, campaignLengthFilter=campaignLengthFilter, page=page, per_page=per_page, order=order, embed=embed)
    apiResponse = MakeAPICall(apiUrl, parameters)

    return json.loads(apiResponse)


def GetCampaignsPerWeekByDomain(apiKey, domain, startDate=None, weeksBack=None):
    """
    Get the number of campaigns sent per week for a specified domain
    :param apiKey:  API key for authentication
    :param domain:  The domain to query for
    :param startDate:  Start date for the query
    :param weeksBack:  How many weeks to look back prior to startDate or now
    :return:  'float' object
    """
    apiUrl = "http://api.edatasource.com/v4/competitive/intelligence/"+domain+"/campaignsPerWeek"
    parameters = {
        "Authorization": apiKey
    }
    parameters = SetOptionalParams(parameters, startDate=startDate, weeksBack=weeksBack)
    apiResponse = MakeAPICall(apiUrl, parameters)

    return json.loads(apiResponse)


def GetDeliverabilityByIP(apiKey, startingIpAddress, qd, lastBlock=None):
    """
    Get deliverability information for a specified IP address, or IP range
    :param apiKey:  API key for authentication
    :param startingIpAddress:  The starting ip address to view results for
    :param qd:  A date range query parameter.  Accepts "since:YYYYMMDD", "between:YYYYMMDDhhmmss,YYYYMMDDhhmmss",
                and "daysBack:N".
                Examples: 'since:20190601', 'between:20191001000000,20191002060000', 'daysBack:30'
    :param lastBlock:  The last block of the range to request (last octet for IPv4 or last hextet in IPv6, max 256 return IPs)
    :return:  'list' object
    """
    apiUrl = "http://api.edatasource.com/v4/competitive/intelligence/ipdeliverability/range/"+startingIpAddress
    parameters = {
        "Authorization": apiKey,
        "qd": qd
    }
    parameters = SetOptionalParams(parameters, lastBlock=lastBlock)
    apiResponse = MakeAPICall(apiUrl, parameters)

    return json.loads(apiResponse)


def GetDomainInfo(apiKey, domain):
    """
    Get sending list size, and informational details for a specified domain
    :param apiKey:  API key for authentication
    :param domain:  (Array) The domain to query for
    :return:  'list' object
    """
    apiUrl = "http://api.edatasource.com/v4/competitive/domain_info"
    parameters = {
        "Authorization": apiKey,
        "domain": domain
    }
    parameters = SetOptionalParams(parameters)
    apiResponse = MakeAPICall(apiUrl, parameters)

    return json.loads(apiResponse)


def GetDomainOverlap(apiKey, domain, minThreshold=None, maxResults=None, ignoreIndustry=None, excludeSameCompany=None
                     , embed=None):
    """
    Get the overlap information of other brands for a specified domain
    :param apiKey:  API key for authentication
    :param domain:  The domain to query for
    :param minThreshold:  Minimum overlap percentage to use (default 10)
    :param maxResults:  Maximum Results to return (default 100)
    :param ignoreIndustry:  If you wish to ignore the industry filter and return all overlaps (default false)
    :param excludeSameCompany:  If you wish to exclude domains that are under the same company (default false)
    :param embed:  The objects within the return model you wish to embed.
                    Embed parameter accepts: readRatePercent, projectedReach
    :return:  'dict' object
    """
    apiUrl = "http://api.edatasource.com/v4/competitive/overlaps/"+domain
    parameters = {
        "Authorization": apiKey
    }
    parameters = SetOptionalParams(parameters, minThreshold=minThreshold, maxResults=maxResults, ignoreIndustry=ignoreIndustry, excludeSameCompany=excludeSameCompany, embed=embed)
    apiResponse = MakeAPICall(apiUrl, parameters)

    return json.loads(apiResponse)


def GetDoWAverage(apiKey, domain, qd=None, embed=None):
    """
    Get the average sending volume for a domain grouped by the day of the week
    :param apiKey:  API key for authentication
    :param domain:  The domain to query for
    :param qd:  A date range query parameter.  Accepts "since:YYYYMMDD", "between:YYYYMMDDhhmmss,YYYYMMDDhhmmss",
                and "daysBack:N".
                Examples: 'since:20190601', 'between:20191001000000,20191002060000', 'daysBack:30'
    :param embed:  The objects within the return model you wish to embed.
                    Embed parameter accepts: ispPlacements
    :return:  'list' object
    """
    apiUrl = "http://api.edatasource.com/v4/competitive/intelligence/"+domain+"/dayOfWeekAverageVolume"
    parameters = {
        "Authorization": apiKey
    }
    parameters = SetOptionalParams(parameters, qd=qd, embed=embed)
    apiResponse = MakeAPICall(apiUrl, parameters)

    return json.loads(apiResponse)


def GetIPDeliverabilityByIP(apiKey, sendingIPAddress, qd):
    """
    Get deliverability information for a specified IP address
    :param apiKey:  API key for authentication
    :param sendingIPAddress:
    :param qd:  A date range query parameter.  Accepts "since:YYYYMMDD", "between:YYYYMMDDhhmmss,YYYYMMDDhhmmss",
                and "daysBack:N".
                Examples: 'since:20190601', 'between:20191001000000,20191002060000', 'daysBack:30'
    :return:  'dict' object
    """
    apiUrl = "http://api.edatasource.com/v4/competitive/intelligence/ipdeliverability/"+sendingIPAddress
    parameters = {
        "Authorization": apiKey,
        "qd": qd
    }
    parameters = SetOptionalParams(parameters)
    apiResponse = MakeAPICall(apiUrl, parameters)

    return json.loads(apiResponse)


def GetIspPlacementsByDomain(apiKey, domain, qd):
    """
    Get ISP placement details for a specified domain
    :param apiKey:  API key for authentication
    :param domain:  The domain to query for
    :param qd:  A date range query parameter.  Accepts "since:YYYYMMDD", "between:YYYYMMDDhhmmss,YYYYMMDDhhmmss",
                and "daysBack:N".
                Examples: 'since:20190601', 'between:20191001000000,20191002060000', 'daysBack:30'
    :return:  'list' object
    """
    apiUrl = "http://api.edatasource.com/v4/competitive/intelligence/"+domain+"/ispPlacements"
    parameters = {
        "Authorization": apiKey,
        "qd": qd
    }
    parameters = SetOptionalParams(parameters)
    apiResponse = MakeAPICall(apiUrl, parameters)

    return json.loads(apiResponse)


def GetNarrowOverlap(apiKey, domain, overlapDomain):
    """
    Get the overlap information for a specified domain, restricted to a designated subset of overlap domains
    :param apiKey:  API key for authentication
    :param domain:  The domain to query for
    :param overlapDomain:  (Array) The other domains to analyze overlap with (multiple params accepted)
    :return:  'dict' object
    """
    apiUrl = "http://api.edatasource.com/v4/competitive/overlaps/narrow/"+domain
    parameters = {
        "Authorization": apiKey,
        "overlapDomain": overlapDomain
    }
    parameters = SetOptionalParams(parameters)
    apiResponse = MakeAPICall(apiUrl, parameters)

    return json.loads(apiResponse)


def GetPing(apiKey):
    """
    Ping the server to verify accessibility
    :param apiKey:  API key for authentication
    :return:  'str' object
    """
    apiUrl = "http://api.edatasource.com/v4/competitive/ping"
    parameters = {
        "Authorization": apiKey
    }
    parameters = SetOptionalParams(parameters)
    apiResponse = MakeAPICall(apiUrl, parameters)

    return apiResponse


def GetSearch(apiKey, qd, subject=None, body=None, campaignLengthFilter=None, sendingDomain=None,
                            excludeSendingDomain=None, brandId=None, excludeBrandId=None, companyId=None,
                            excludeCompanyId=None, industryId=None, sentFrom=None, fromAddress=None, headerKey=None,
                            headerValue=None, receivedUsingMta=None, mobileReady=None, hasCreative=None,
                            onlyCommercial=None, emojiPresent=None, readPercentage=None, readDeletedPercentage=None,
                            deletedPercentage=None, inboxPercentage=None, spamPercentage=None,
                            projectedVolumeFilter=None, secondaryProjectedVolumeFilter=None,
                            droveTrafficToDomain=None, sendFromIp=None, espId=None, espStartIp=None, espEndIp=None,
                            espRedirectDomain=None, espRedirectString=None, campaignTargetCountry=None,
                            excludeCampaignTargetCountry=None, page=None, per_page=None, order=None, embed=None):
    """
    Search Competitive Tracker for campaign details fitting a specified set of criteria.
    :param apiKey:  API key for authentication
    :param qd:  A date range query parameter.  Accepts "since:YYYYMMDD", "between:YYYYMMDDhhmmss,YYYYMMDDhhmmss",
                and "daysBack:N".
                Examples: 'since:20190601', 'between:20191001000000,20191002060000', 'daysBack:30' 
    :param subject:  Subject search criteria
    :param body:  Body search criteriaSubject search criteria
    :param campaignLengthFilter:  Length filter in days for the campaign (examples '>,2' '<,5' '=,1')
    :param sendingDomain:  (Array) Filter search to specific sending domains (multiple allowed)
    :param excludeSendingDomain:  (Array) Filter out specific sending domains (multiple allowed)
    :param brandId:  (Array) Filter search to specific brands (multiple allowed)
    :param excludeBrandId:  (Array) Filter out specific brands (multiple allowed)
    :param companyId:  (Array) Filter search to specific companies (multiple allowed)
    :param excludeCompanyId:  (Array) Filter out specific companies (multiple allowed)
    :param industryId:  (Array) Filter search to specific industries (multiple allowed)
    :param sentFrom:  Campaigns with a matching sent from address
    :param fromAddress:  (Array) Campaigns with certain from addresses (multiple allowed)
    :param headerKey:  Campaigns that used a specific header key
    :param headerValue:  Campaigns that used a specific header value
    :param receivedUsingMta:  Campaigns were received using a matched MTA
    :param mobileReady:  Campaigns with/without mobile ready format
    :param hasCreative:  Campaigns with/without creatives
    :param onlyCommercial:  True for commercial campaigns, false for daily low-volume rollups, and leave unset (null) for both
    :param emojiPresent:  Campaigns with/without emojis in the subject
    :param readPercentage:  Read percentage filter (examples '>,20' '<,5' '=,2')
    :param readDeletedPercentage:  Read+Deleted percentage filter (examples '>,20' '<,5' '=,2')
    :param deletedPercentage:  Deleted percentage filter (examples '>,20' '<,5' '=,2')
    :param inboxPercentage:  Inbox percentage filter (examples '>,20' '<,5' '=,2')
    :param spamPercentage:  Spam percentage filter (examples '>,20' '<,5' '=,2')
    :param projectedVolumeFilter:  Projected Total Volume filter (examples '>,2000000' '<,50000' '=,324541')
    :param secondaryProjectedVolumeFilter:  Secondary Projected Total Volume filter (examples '>,2000000' '<,50000' '=,324541')
    :param droveTrafficToDomain:  (Array) Filter search to campaigns that drive traffic to certain domains (multiple allowed)
    :param sendFromIp:  (Array) Filter search to campaigns that were sent from certain ips (multiple allowed)
    :param espId:  Filter search to a specific ESP
    :param espStartIp:  The start IP of the sending ESP
    :param espEndIp:  The end IP of the sending ESP
    :param espRedirectDomain:  The redirect domain of the sending ESP
    :param espRedirectString:  The match the redirect string of the sending ESP
    :param campaignTargetCountry:  (Array) Filter search to campaigns with a specific target country code (multiple allowed)
    :param excludeCampaignTargetCountry:  (Array) Filter out campaigns with a specific target country code (multiple allowed)
    :param page:  The page to query for in pagination
    :param per_page:  The amount of records per page you wish to query for (max 100)
    ":param order:  The property to sort by ('property' for decending, '-property' for ascending)"
                    Order options: firstSeen, -firstSeen, lastSeen, -lastSeen, inbox, -inbox, spam, -spam
    :param embed:  The objects within the return model you wish to embed.
                    Embed parameter accepts: sendingIps, rawEmail, ispPlacements, links, headers
    :return: 'list' object
    """

    arguments = locals()

    apiUrl = "http://api.edatasource.com/v4/competitive/search"
    parameters = {
        "Authorization": apiKey,
        "qd": qd
    }

    for k, v in arguments.items():
        if v is not None and k not in("apiKey", "qd"):
            parameters[k] = v

    apiResponse = MakeAPICall(apiUrl, parameters)

    return json.loads(apiResponse)


def GetTargetCountryByCampaign(apiKey, campaignId):
    """
    Get the target country for a specified campaign
    :param apiKey:  API key for authentication
    :param campaignId:  The campaign identifier value to search for.
    :return:  'dict' object
    """
    apiUrl = "http://api.edatasource.com/v4/competitive/intelligence/campaign/targetCountry/"+campaignId
    parameters = {
        "Authorization": apiKey
    }
    parameters = SetOptionalParams(parameters)
    apiResponse = MakeAPICall(apiUrl, parameters)

    return json.loads(apiResponse)


def GetTopCompetingByDomain(apiKey, domain, minThreshold=None, maxResults=None, embed=None):
    """
    Get the top competing domains for a specified domain
    :param apiKey:  API key for authentication
    :param domain:  The domain to query for
    :param minThreshold:  Minimum overlap percentage to use (default 10)
    :param maxResults:  Maximum Results to return (default 100)
    :param embed:  The objects within the return model you wish to embed.
                    Embed parameter accepts: readRatePercent, projectedReach
    :return:  'dict' object
    """
    apiUrl = "http://api.edatasource.com/v4/competitive/overlaps/"+domain+"/top_competing"
    parameters = {
        "Authorization": apiKey
    }
    parameters = SetOptionalParams(parameters, minThreshold=minThreshold, maxResults=maxResults, embed=embed)
    apiResponse = MakeAPICall(apiUrl, parameters)

    return json.loads(apiResponse)


def GetTopDomainsByBrand(apiKey, brandId):
    """
    Get the top sending domains for a specified brand
    :param apiKey:  API key for authentication
    :param brandId:  The Brand ID to get top sending domains for
    :return:  'list' object
    """
    apiUrl = "http://api.edatasource.com/v4/competitive/intelligence/brand/"+brandId+"/top_domains"
    parameters = {
        "Authorization": apiKey
    }
    parameters = SetOptionalParams(parameters)
    apiResponse = MakeAPICall(apiUrl, parameters)

    return json.loads(apiResponse)


def GetTotalVolByIP(apiKey, startingIpAddress, qd, lastBlock=None, embed=None):
    """
    Get the total volume for a specified IP address, or IP range
    :param apiKey:  API key for authentication
    :param startingIpAddress:  The starting ip address to view results for
    :param qd:  A date range query parameter.  Accepts "since:YYYYMMDD", "between:YYYYMMDDhhmmss,YYYYMMDDhhmmss",
                and "daysBack:N".
                Examples: 'since:20190601', 'between:20191001000000,20191002060000', 'daysBack:30'
    :param lastBlock:  The last block of the range to request (last octet for IPv4 or last hextet in IPv6, max 256 return IPs)
    :param embed:  The objects within the return model you wish to embed.
                    Embed parameter accepts: ispPlacements
    :return:  'dict' object
    """
    apiUrl = "http://api.edatasource.com/v4/competitive/intelligence/ipdeliverability/range/"+startingIpAddress+"/totalVolume"
    parameters = {
        "Authorization": apiKey,
        "qd": qd
    }
    parameters = SetOptionalParams(parameters, lastBlock=lastBlock, embed=embed)
    apiResponse = MakeAPICall(apiUrl, parameters)

    return json.loads(apiResponse)


def GetTotalVolumeByDomain(apiKey, domain, qd=None, embed=None):
    """
    Get total sending volume for a specified domain
    :param apiKey:  API key for authentication
    :param domain:  The domain to query for
    :param qd:  A date range query parameter.  Accepts "since:YYYYMMDD", "between:YYYYMMDDhhmmss,YYYYMMDDhhmmss",
                and "daysBack:N".
                Examples: 'since:20190601', 'between:20191001000000,20191002060000', 'daysBack:30'
    :param embed:  The objects within the return model you wish to embed.
                    Embed parameter accepts: ispPlacements
    :return:  'dict' object
    """
    apiUrl = "http://api.edatasource.com/v4/competitive/intelligence/"+domain+"/totalVolume"
    parameters = {
        "Authorization": apiKey
    }
    parameters = SetOptionalParams(parameters, qd=qd, embed=embed)
    apiResponse = MakeAPICall(apiUrl, parameters)

    return json.loads(apiResponse)


def GetVolumeForListDomains(apiKey, domain, endDate=None, precision=None, timePeriod=None, mustMatchTLD=None):
    """
    Get sending volume for a specified list of domains (max 300 domains)
    :param apiKey:  API key for authentication
    :param domain:  (Array) The domain to query for
    :param endDate:  Endpoint of the requested date range concerning volume data with a format of yyyy-mm-dd. Defaults to current date if no argument provided. This date is exclusive: data concerning the given date will not be included in volume average.
    :param precision:  Precision of the average (i.e. per month or per day). Possible values: 'days' or 'months'. Defaults to 'days' if argument is not supplied.
    :param timePeriod:  How many days or months back you would like sending volume data for. This is for a time period backwards. Defaults to 30 if argument is not supplied.
    :param mustMatchTLD:  Include only domains that match the top level domain (TLD) of any domain requested
    :return:  'dict' object
    """
    apiUrl = "http://api.edatasource.com/v4/competitive/domain_info/brand_volume_average_and_esps"
    parameters = {
        "Authorization": apiKey,
        "domain": domain
    }
    parameters = SetOptionalParams(parameters, endDate=endDate, precision=precision, timePeriod=timePeriod, mustMatchTLD=mustMatchTLD)
    apiResponse = MakeAPICall(apiUrl, parameters)

    return json.loads(apiResponse)


def PostVolumeForListDomains(apiKey, domainArray, endDate=None, precision=None, timePeriod=None, mustMatchTLD=None):
    """
    Get sending volume for an extended specified list of domains (max 1,000 domains)
    :param apiKey:  API key for authentication
    :param domainArray:  Array of domains to search for
    :param endDate:  Endpoint of the requested date range concerning volume data with a format of yyyy-mm-dd. Defaults to current date if no argument provided. This date is exclusive: data concerning the given date will not be included in volume average.
    :param precision:  Precision of the average (i.e. per month or per day). Possible values: 'days' or 'months'. Defaults to 'days' if argument is not supplied.
    :param timePeriod:  How many days or months back you would like sending volume data for. This is for a time period backwards. Defaults to 30 if argument is not supplied.
    :param mustMatchTLD:  Include only domains that match the top level domain (TLD) of any domain requested
    :return:  'dict' object
    """
    apiUrl = "http://api.edatasource.com/v4/competitive/domain_info/brand_volume_average_and_esps"
    parameters = {
        "Authorization": apiKey
    }
    body = domainArray

    parameters = SetOptionalParams(parameters, endDate=endDate, precision=precision, timePeriod=timePeriod, mustMatchTLD=mustMatchTLD)

    apiResponse = MakePostAPICall(apiUrl, parameters, body)

    return json.loads(apiResponse)


def GetVolumesByDomain(apiKey, domain, qd, embed=None):
    """
    Get sending volumes for a specified domain
    :param apiKey:  API key for authentication
    :param domain:  The domain to query for
    :param qd:  A date range query parameter.  Accepts "since:YYYYMMDD", "between:YYYYMMDDhhmmss,YYYYMMDDhhmmss",
                and "daysBack:N".
                Examples: 'since:20190601', 'between:20191001000000,20191002060000', 'daysBack:30'
    :param embed:  The objects within the return model you wish to embed.
                    Embed parameter accepts: ispPlacements
    :return:  'list' object
    """
    apiUrl = "http://api.edatasource.com/v4/competitive/intelligence/"+domain+"/volumes"
    parameters = {
        "Authorization": apiKey,
        "qd": qd
    }
    parameters = SetOptionalParams(parameters, embed=embed)
    apiResponse = MakeAPICall(apiUrl, parameters)

    return json.loads(apiResponse)


def SetOptionalParams(parameters, campaignLengthFilter = None, domain = None, embed = None, endDate = None,
                mustMatchTLD = None, order = None, page = None, per_page = None, precision = None, qd = None,
                startDate = None, timePeriod = None, weeksBack = None, sendingIpAddress = None,
                startingIpAddress = None, lastBlock = None, minThreshold = None, maxResults = None,
                ignoreIndustry = None, excludeSameCompany = None, overlapDomain = None):
    """
    Sets the optional parameters for the api calls.
    :param parameters:  The parameters to use in the API call 
    :param campaignLengthFilter:  Length filter in days for the campaign (examples '>,2' '<,5' '=,1')  
    :param domain:  The domain to query for 
    :param embed: The objects within the return model you wish to embed.
    :param endDate:  Endpoint of the requested date range concerning volume data with a format of yyyy-mm-dd. Defaults to current date if no argument provided. This date is exclusive: data concerning the given date will not be included in volume average. 
    :param mustMatchTLD:  Include only domains that match the top level domain (TLD) of any domain requested 
    :param order: The property to sort by ('property' for decending, '-property' for ascending)
    :param page:  The page to query for in pagination 
    :param per_page:  The amount of records per page you wish to query for (max 100) 
    :param precision:  Precision of the average (i.e. per month or per day). Possible values: 'days' or 'months'. Defaults to 'days' if argument is not supplied. 
    :param qd:  A date range query parameter.  Accepts "since:YYYYMMDD", "between:YYYYMMDDhhmmss,YYYYMMDDhhmmss",
                and "daysBack:N".
                Examples: 'since:20190601', 'between:20191001000000,20191002060000', 'daysBack:30' 
    :param startDate:  Start date for the query 
    :param timePeriod:  How many days or months back you would like sending volume data for. This is for a time period backwards. Defaults to 30 if argument is not supplied. 
    :param weeksBack:  How many weeks to look back prior to startDate or now 
    :param sendingIpAddress:  The ip address to view results for
    :param startingIpAddress:  The starting ip address to view results for 
    :param lastBlock:  The last block of the range to request (last octet for IPv4 or last hextet in IPv6, max 256 return IPs) 
    :param minThreshold:  Minimum overlap percentage to use (default 10) 
    :param maxResults:  Maximum Results to return (default 100) 
    :param ignoreIndustry:  If you wish to ignore the industry filter and return all overlaps (default false) 
    :param excludeSameCompany:  If you wish to exclude domains that are under the same company (default false) 
    :param overlapDomain:  The other domains to analyze overlap with (multiple params accepted) 
    :return:  'dict' object
    """
    arguments = locals()

    for k, v in arguments.items():
        if v is not None and k != "parameters":
            parameters[k] = v

    return parameters


def MakeAPICall(apiUrl, parameters):
    """
    Makes a GET API call to the server
    :param apiUrl:  The API URL to use 
    :param parameters:  The parameters to use in the API call 
    :return:  'response' object
    """

    response = requests.get(apiUrl, parameters)

    if response.status_code == 200:
        return response.text
    else:
        return "Problem Getting Data: " + response.reason


def MakePostAPICall(apiUrl, parameters, body):
    """
    Makes a POST API call to the server
    :param apiUrl:  The API URL to use 
    :param parameters:  The parameters to use in the API call 
    :param body: The body of the API call to include
    :return:  'response' object
    """

    response = requests.post(apiUrl, params=parameters, json=body)

    if response.status_code == 200:
        return response.text
    else:
        return "Problem Getting Data: " + response.reason
