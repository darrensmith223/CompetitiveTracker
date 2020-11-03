import requests
import json


def GetAverageVolPerCampaign(apiKey, domain, qd=None):
    apiUrl = "http://api.edatasource.com/v4/competitive/intelligence/"+domain+"/averageVolumePerCampaign"
    parameters = {
        "Authorization": apiKey
    }
    parameters = SetOptionalParams(parameters, qd=qd)
    apiResponse = MakeAPICall(apiUrl, parameters)

    return json.loads(apiResponse)


def GetCampaignByID(apiKey, campaignId, embed=None):
    apiUrl = "http://api.edatasource.com/v4/competitive/intelligence/campaign/"+campaignId
    parameters = {
        "Authorization": apiKey
    }
    parameters = SetOptionalParams(parameters, embed=embed)
    apiResponse = MakeAPICall(apiUrl, parameters)

    return json.loads(apiResponse)


def GetCampaignsByDomain(apiKey, domain, qd, campaignLengthFilter=None, page=None, per_page=None, order=None, embed=None):
    apiUrl = "http://api.edatasource.com/v4/competitive/intelligence/"+domain+"/campaigns"
    parameters = {
        "Authorization": apiKey,
        "qd": qd
    }
    parameters = SetOptionalParams(parameters, campaignLengthFilter=campaignLengthFilter, page=page, per_page=per_page, order=order, embed=embed)
    apiResponse = MakeAPICall(apiUrl, parameters)

    return json.loads(apiResponse)


def GetCampaignsPerWeekByDomain(apiKey, domain, startDate=None, weeksBack=None):
    apiUrl = "http://api.edatasource.com/v4/competitive/intelligence/"+domain+"/campaignsPerWeek"
    parameters = {
        "Authorization": apiKey
    }
    parameters = SetOptionalParams(parameters, startDate=startDate, weeksBack=weeksBack)
    apiResponse = MakeAPICall(apiUrl, parameters)

    return json.loads(apiResponse)


def GetDeliverabilityByIP(apiKey, startingIpAddress, qd, lastBlock=None):
    apiUrl = "http://api.edatasource.com/v4/competitive/intelligence/ipdeliverability/range/"+startingIpAddress
    parameters = {
        "Authorization": apiKey,
        "qd": qd
    }
    parameters = SetOptionalParams(parameters, lastBlock=lastBlock)
    apiResponse = MakeAPICall(apiUrl, parameters)

    return json.loads(apiResponse)


def GetDomainInfo(apiKey, domain):
    apiUrl = "http://api.edatasource.com/v4/competitive/domain_info"
    parameters = {
        "Authorization": apiKey,
        "domain": domain
    }
    parameters = SetOptionalParams(parameters)
    apiResponse = MakeAPICall(apiUrl, parameters)

    return json.loads(apiResponse)


def GetDomainOverlap(apiKey, domain, minThreshold=None, maxResults=None, ignoreIndustry=None, excludeSameCompany=None, embed=None):
    apiUrl = "http://api.edatasource.com/v4/competitive/overlaps/"+domain
    parameters = {
        "Authorization": apiKey
    }
    parameters = SetOptionalParams(parameters, minThreshold=minThreshold, maxResults=maxResults, ignoreIndustry=ignoreIndustry, excludeSameCompany=excludeSameCompany, embed=embed)
    apiResponse = MakeAPICall(apiUrl, parameters)

    return json.loads(apiResponse)


def GetDoWAverage(apiKey, domain, qd=None, embed=None):
    apiUrl = "http://api.edatasource.com/v4/competitive/intelligence/"+domain+"/dayOfWeekAverageVolume"
    parameters = {
        "Authorization": apiKey
    }
    parameters = SetOptionalParams(parameters, qd=qd, embed=embed)
    apiResponse = MakeAPICall(apiUrl, parameters)

    return json.loads(apiResponse)


def GetIPDeliverabilityByIP(apiKey, sendingIPAddress, qd):
    apiUrl = "http://api.edatasource.com/v4/competitive/intelligence/ipdeliverability/"+sendingIPAddress
    parameters = {
        "Authorization": apiKey,
        "qd": qd
    }
    parameters = SetOptionalParams(parameters)
    apiResponse = MakeAPICall(apiUrl, parameters)

    return json.loads(apiResponse)


def GetIspPlacementsByDomain(apiKey, domain, qd):
    apiUrl = "http://api.edatasource.com/v4/competitive/intelligence/"+domain+"/ispPlacements"
    parameters = {
        "Authorization": apiKey,
        "qd": qd
    }
    parameters = SetOptionalParams(parameters)
    apiResponse = MakeAPICall(apiUrl, parameters)

    return json.loads(apiResponse)


def GetNarrowOverlap(apiKey, domain, overlapDomain):
    apiUrl = "http://api.edatasource.com/v4/competitive/overlaps/narrow/"+domain
    parameters = {
        "Authorization": apiKey,
        "overlapDomain": overlapDomain
    }
    parameters = SetOptionalParams(parameters)
    apiResponse = MakeAPICall(apiUrl, parameters)

    return json.loads(apiResponse)


def GetPing(apiKey):
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
    apiUrl = "http://api.edatasource.com/v4/competitive/intelligence/campaign/targetCountry/"+campaignId
    parameters = {
        "Authorization": apiKey
    }
    parameters = SetOptionalParams(parameters)
    apiResponse = MakeAPICall(apiUrl, parameters)

    return json.loads(apiResponse)


def GetTopCompetingByDomain(apiKey, domain, minThreshold=None, maxResults=None, embed=None):
    apiUrl = "http://api.edatasource.com/v4/competitive/overlaps/"+domain+"/top_competing"
    parameters = {
        "Authorization": apiKey
    }
    parameters = SetOptionalParams(parameters, minThreshold=minThreshold, maxResults=maxResults, embed=embed)
    apiResponse = MakeAPICall(apiUrl, parameters)

    return json.loads(apiResponse)


def GetTopDomainsByBrand(apiKey, brandId):
    apiUrl = "http://api.edatasource.com/v4/competitive/intelligence/brand/"+brandId+"/top_domains"
    parameters = {
        "Authorization": apiKey
    }
    parameters = SetOptionalParams(parameters)
    apiResponse = MakeAPICall(apiUrl, parameters)

    return json.loads(apiResponse)


def GetTotalVolByIP(apiKey, startingIpAddress, qd, lastBlock=None, embed=None):
    apiUrl = "http://api.edatasource.com/v4/competitive/intelligence/ipdeliverability/range/"+startingIpAddress+"/totalVolume"
    parameters = {
        "Authorization": apiKey,
        "qd": qd
    }
    parameters = SetOptionalParams(parameters, lastBlock=lastBlock, embed=embed)
    apiResponse = MakeAPICall(apiUrl, parameters)

    return json.loads(apiResponse)


def GetTotalVolumeByDomain(apiKey, domain, qd=None, embed=None):
    apiUrl = "http://api.edatasource.com/v4/competitive/intelligence/"+domain+"/totalVolume"
    parameters = {
        "Authorization": apiKey
    }
    parameters = SetOptionalParams(parameters, qd=qd, embed=embed)
    apiResponse = MakeAPICall(apiUrl, parameters)

    return json.loads(apiResponse)


def GetVolumeForListDomains(apiKey, domain, endDate=None, precision=None, timePeriod=None, mustMatchTLD=None):
    apiUrl = "http://api.edatasource.com/v4/competitive/domain_info/brand_volume_average_and_esps"
    parameters = {
        "Authorization": apiKey,
        "domain": domain
    }
    parameters = SetOptionalParams(parameters, endDate=endDate, precision=precision, timePeriod=timePeriod, mustMatchTLD=mustMatchTLD)
    apiResponse = MakeAPICall(apiUrl, parameters)

    return json.loads(apiResponse)


def PostVolumeForListDomains(apiKey, domainArray, endDate=None, precision=None, timePeriod=None, mustMatchTLD=None):
    apiUrl = "http://api.edatasource.com/v4/competitive/domain_info/brand_volume_average_and_esps"
    parameters = {
        "Authorization": apiKey
    }
    body = domainArray

    parameters = SetOptionalParams(parameters, endDate=endDate, precision=precision, timePeriod=timePeriod, mustMatchTLD=mustMatchTLD)

    apiResponse = MakePostAPICall(apiUrl, parameters, body)

    return json.loads(apiResponse)


def GetVolumesByDomain(apiKey, domain, qd, embed=None):
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
    arguments = locals()

    for k, v in arguments.items():
        if v is not None and k != "parameters":
            parameters[k] = v

    return parameters


def MakeAPICall(apiUrl, parameters):

    response = requests.get(apiUrl, parameters)

    if response.status_code == 200:
        return response.text
    else:
        return "Problem Getting Data: " + response.reason


def MakePostAPICall(apiUrl, parameters, body):

    response = requests.post(apiUrl, params=parameters, json=body)

    if response.status_code == 200:
        return response.text
    else:
        return "Problem Getting Data: " + response.reason
