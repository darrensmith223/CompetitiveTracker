import requests
import json


def GetAverageVolPerCampaign(apiKey, domain, qd=None):
    apiUrl = "http://api.edatasource.com/v4/competitive/intelligence/"+domain+"/averageVolumePerCampaign"
    parameters = {
        "Authorization": apiKey
    }
    apiResponse = MakeAPICall(apiUrl, parameters, qd=qd)

    return json.loads(apiResponse)


def GetCampaignByID(apiKey, campaignId, embed=None):
    apiUrl = "http://api.edatasource.com/v4/competitive/intelligence/campaign/"+campaignId
    parameters = {
        "Authorization": apiKey
    }
    apiResponse = MakeAPICall(apiUrl, parameters, embed=embed)

    return json.loads(apiResponse)


def GetCampaignsByDomain(apiKey, domain, qd, campaignLengthFilter=None, page=None, per_page=None, order=None, embed=None):
    apiUrl = "http://api.edatasource.com/v4/competitive/intelligence/"+domain+"/campaigns"
    parameters = {
        "Authorization": apiKey,
        "qd": qd
    }
    apiResponse = MakeAPICall(apiUrl, parameters, campaignLengthFilter=campaignLengthFilter, page=page, per_page=per_page, order=order, embed=embed)

    return json.loads(apiResponse)


def GetCampaignsPerWeekByDomain(apiKey, domain, startDate=None, weeksBack=None):
    apiUrl = "http://api.edatasource.com/v4/competitive/intelligence/"+domain+"/campaignsPerWeek"
    parameters = {
        "Authorization": apiKey
    }
    apiResponse = MakeAPICall(apiUrl, parameters, startDate=startDate, weeksBack=weeksBack)

    return json.loads(apiResponse)


def GetDeliverabilityByIP(apiKey, startingIpAddress, qd, lastBlock=None):
    apiUrl = "http://api.edatasource.com/v4/competitive/intelligence/ipdeliverability/range/"+startingIpAddress
    parameters = {
        "Authorization": apiKey,
        "qd": qd
    }
    apiResponse = MakeAPICall(apiUrl, parameters, lastBlock=lastBlock)

    return json.loads(apiResponse)


def GetDomainInfo(apiKey, domain):
    apiUrl = "http://api.edatasource.com/v4/competitive/domain_info"
    parameters = {
        "Authorization": apiKey,
        "domain": domain
    }
    apiResponse = MakeAPICall(apiUrl, parameters)

    return json.loads(apiResponse)


def GetDomainOverlap(apiKey, domain, minThreshold=None, maxResults=None, ignoreIndustry=None, excludeSameCompany=None, embed=None):
    apiUrl = "http://api.edatasource.com/v4/competitive/overlaps/"+domain
    parameters = {
        "Authorization": apiKey
    }
    apiResponse = MakeAPICall(apiUrl, parameters, minThreshold=minThreshold, maxResults=maxResults, ignoreIndustry=ignoreIndustry, excludeSameCompany=excludeSameCompany, embed=embed)

    return json.loads(apiResponse)


def GetDoWAverage(apiKey, domain, qd=None, embed=None):
    apiUrl = "http://api.edatasource.com/v4/competitive/intelligence/"+domain+"/dayOfWeekAverageVolume"
    parameters = {
        "Authorization": apiKey
    }
    apiResponse = MakeAPICall(apiUrl, parameters, qd=qd, embed=embed)

    return json.loads(apiResponse)


def GetIPDeliverabilityByIP(apiKey, sendingIPAddress, qd):
    apiUrl = "http://api.edatasource.com/v4/competitive/intelligence/ipdeliverability/"+sendingIPAddress
    parameters = {
        "Authorization": apiKey,
        "qd": qd
    }
    apiResponse = MakeAPICall(apiUrl, parameters)

    return json.loads(apiResponse)


def GetIspPlacementsByDomain(apiKey, domain, qd):
    apiUrl = "http://api.edatasource.com/v4/competitive/intelligence/"+domain+"/ispPlacements"
    parameters = {
        "Authorization": apiKey,
        "qd": qd
    }
    apiResponse = MakeAPICall(apiUrl, parameters)

    return json.loads(apiResponse)


def GetNarrowOverlap(apiKey, domain, overlapDomain):
    apiUrl = "http://api.edatasource.com/v4/competitive/overlaps/narrow/"+domain
    parameters = {
        "Authorization": apiKey,
        "overlapDomain": overlapDomain
    }
    apiResponse = MakeAPICall(apiUrl, parameters)

    return json.loads(apiResponse)


def GetPing(apiKey):
    apiUrl = "http://api.edatasource.com/v4/competitive/ping"
    parameters = {
        "Authorization": apiKey
    }
    apiResponse = MakeAPICall(apiUrl, parameters)

    return apiResponse


def GetSearch(apiKey):
    apiUrl = "http://api.edatasource.com/v4/competitive/search"
    parameters = {
        "Authorization": apiKey
    }
    apiResponse = MakeAPICall(apiUrl, parameters)

    return json.loads(apiResponse)


def GetTargetCountryByCampaign(apiKey, campaignId):
    apiUrl = "http://api.edatasource.com/v4/competitive/intelligence/campaign/targetCountry/"+campaignId
    parameters = {
        "Authorization": apiKey
    }
    apiResponse = MakeAPICall(apiUrl, parameters)

    return json.loads(apiResponse)


def GetTopCompetingByDomain(apiKey, domain, minThreshold=None, maxResults=None, embed=None):
    apiUrl = "http://api.edatasource.com/v4/competitive/overlaps/"+domain+"/top_competing"
    parameters = {
        "Authorization": apiKey
    }
    apiResponse = MakeAPICall(apiUrl, parameters, minThreshold=minThreshold, maxResults=maxResults, embed=embed)

    return json.loads(apiResponse)


def GetTopDomainsByBrand(apiKey, brandId):
    apiUrl = "http://api.edatasource.com/v4/competitive/intelligence/brand/"+brandId+"/top_domains"
    parameters = {
        "Authorization": apiKey
    }
    apiResponse = MakeAPICall(apiUrl, parameters)

    return json.loads(apiResponse)


def GetTotalVolByIP(apiKey, startingIpAddress, qd, lastBlock=None, embed=None):
    apiUrl = "http://api.edatasource.com/v4/competitive/intelligence/ipdeliverability/range/"+startingIpAddress+"/totalVolume"
    parameters = {
        "Authorization": apiKey,
        "qd": qd
    }
    apiResponse = MakeAPICall(apiUrl, parameters, lastBlock=lastBlock, embed=embed)

    return json.loads(apiResponse)


def GetTotalVolumeByDomain(apiKey, domain, qd=None, embed=None):
    apiUrl = "http://api.edatasource.com/v4/competitive/intelligence/"+domain+"/totalVolume"
    parameters = {
        "Authorization": apiKey
    }
    apiResponse = MakeAPICall(apiUrl, parameters, qd=qd, embed=embed)

    return json.loads(apiResponse)


def GetVolumeForListDomains(apiKey, domain, endDate=None, precision=None, timePeriod=None, mustMatchTLD=None):
    apiUrl = "http://api.edatasource.com/v4/competitive/domain_info/brand_volume_average_and_esps"
    parameters = {
        "Authorization": apiKey,
        "domain": domain
    }
    apiResponse = MakeAPICall(apiUrl, parameters, endDate=endDate, precision=precision, timePeriod=timePeriod, mustMatchTLD=mustMatchTLD)

    return json.loads(apiResponse)


def GetVolumesByDomain(apiKey, domain, qd, embed=None):
    apiUrl = "http://api.edatasource.com/v4/competitive/intelligence/"+domain+"/volumes"
    parameters = {
        "Authorization": apiKey,
        "qd": qd
    }
    apiResponse = MakeAPICall(apiUrl, parameters, embed=embed)

    return json.loads(apiResponse)


def MakeAPICall(apiUrl, parameters, campaignLengthFilter = None, domain = None, embed = None, endDate = None,
                mustMatchTLD = None, order = None, page = None, per_page = None, precision = None, qd = None,
                startDate = None, timePeriod = None, weeksBack = None, sendingIpAddress = None,
                startingIpAddress = None, lastBlock = None, minThreshold = None, maxResults = None,
                ignoreIndustry = None, excludeSameCompany = None, overlapDomain = None):

    parameters = AddOptionalParameter(parameters, campaignLengthFilter, "campaignLengthFilter")
    parameters = AddOptionalParameter(parameters, domain, "domain")
    parameters = AddOptionalParameter(parameters, embed, "embed")
    parameters = AddOptionalParameter(parameters, endDate, "endDate")
    parameters = AddOptionalParameter(parameters, mustMatchTLD, "mustMatchTLD")
    parameters = AddOptionalParameter(parameters, order, "order")
    parameters = AddOptionalParameter(parameters, page, "page")
    parameters = AddOptionalParameter(parameters, per_page, "per_page")
    parameters = AddOptionalParameter(parameters, precision, "precision")
    parameters = AddOptionalParameter(parameters, qd, "qd")
    parameters = AddOptionalParameter(parameters, startDate, "startDate")
    parameters = AddOptionalParameter(parameters, timePeriod, "timePeriod")
    parameters = AddOptionalParameter(parameters, weeksBack, "weeksBack")
    parameters = AddOptionalParameter(parameters, sendingIpAddress, "sendingIpAddress")
    parameters = AddOptionalParameter(parameters, startingIpAddress, "startingIpAddress")
    parameters = AddOptionalParameter(parameters, lastBlock, "lastBlock")
    parameters = AddOptionalParameter(parameters, minThreshold, "minThreshold")
    parameters = AddOptionalParameter(parameters, maxResults, "maxResults")
    parameters = AddOptionalParameter(parameters, ignoreIndustry, "ignoreIndustry")
    parameters = AddOptionalParameter(parameters, excludeSameCompany, "excludeSameCompany")
    parameters = AddOptionalParameter(parameters, overlapDomain, "overlapDomain")

    response = requests.get(apiUrl, parameters)

    if response.status_code == 200:
        return response.text
    else:
        return "Problem Getting Data: " + response.reason


def AddOptionalParameter(paramDict, optionalParam, optParamName):

    if optionalParam is not None:
        paramDict[optParamName] = optionalParam

    return paramDict