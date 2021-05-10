from .base import Resource

param_model = {
        'qd'
    }


class Intelligence(Resource):
    key = "intelligence"

    class Brand(Resource):

        def get_top_domains(self, brandId, **kwargs):
            endpoint = "/%s/top_domains" % brandId
            apiUrl = self.uri + endpoint
            parameters = self.SetParameters(kwargs, param_model)
            apiResponse = self.request("GET", apiUrl, params=parameters)

            return apiResponse

    class Campaign(Resource):

        def get_target_country(self, campaignId, **kwargs):
            endpoint = "/targetCountry/%s" % campaignId
            apiUrl = self.uri + endpoint
            parameters = self.SetParameters(kwargs, param_model)
            apiResponse = self.request("GET", apiUrl, params=parameters)

            return apiResponse

        def get_campaign(self, campaignId, **kwargs):
            endpoint = "/campaign/%s" % campaignId
            apiUrl = self.uri + endpoint
            parameters = self.SetParameters(kwargs, param_model)
            apiResponse = self.request("GET", apiUrl, params=parameters)

            return apiResponse

    class IpDeliverability(Resource):

        def get_deliverability_stats(self, sendingIpAddress, **kwargs):
            endpoint = "/ipdeliverability/%s" % sendingIpAddress
            apiUrl = self.uri + endpoint
            parameters = self.SetParameters(kwargs, param_model)
            apiResponse = self.request("GET", apiUrl, params=parameters)

            return apiResponse

        def get_deliverability_stats_for_range(self, startingIpAddress, **kwargs):
            endpoint = "/ipdeliverability/range/%s" % startingIpAddress
            apiUrl = self.uri + endpoint
            parameters = self.SetParameters(kwargs, param_model)
            apiResponse = self.request("GET", apiUrl, params=parameters)

            return apiResponse

        def get_agg_stats_for_range(self, startingIpAddress, **kwargs):
            endpoint = "/ipdeliverability/range/%s/totalVolume" % startingIpAddress
            apiUrl = self.uri + endpoint
            parameters = self.SetParameters(kwargs, param_model)
            apiResponse = self.request("GET", apiUrl, params=parameters)

            return apiResponse

    class Domain(Resource):

        def get_campaigns(self, domain, **kwargs):
            endpoint = "/%s/campaigns" % domain
            apiUrl = self.uri + endpoint
            parameters = self.SetParameters(kwargs, param_model)
            apiResponse = self.request("GET", apiUrl, params=parameters)

            return apiResponse

        def get_campaigns_per_week(self, domain, **kwargs):
            endpoint = "/%s/campaignsPerWeek" % domain
            apiUrl = self.uri + endpoint
            parameters = self.SetParameters(kwargs, param_model)
            apiResponse = self.request("GET", apiUrl, params=parameters)

            return apiResponse

        def get_average_volume_per_campaign(self, domain, **kwargs):
            endpoint = "/%s/averageVolumePerCampaign" % domain
            apiUrl = self.uri + endpoint
            parameters = self.SetParameters(kwargs, param_model)
            apiResponse = self.request("GET", apiUrl, params=parameters)

            return apiResponse

        def get_volumes(self, domain, **kwargs):
            endpoint = "/%s/volumes" % domain
            apiUrl = self.uri + endpoint
            parameters = self.SetParameters(kwargs, param_model)
            apiResponse = self.request("GET", apiUrl, params=parameters)

            return apiResponse

        def get_isp_placements(self, domain, **kwargs):
            endpoint = "/%s/ispPlacements" % domain
            apiUrl = self.uri + endpoint
            parameters = self.SetParameters(kwargs, param_model)
            apiResponse = self.request("GET", apiUrl, params=parameters)

            return apiResponse

        def get_dow_avg_volume(self, domain, **kwargs):
            endpoint = "/%s/dayOfWeekAverageVolume" % domain
            apiUrl = self.uri + endpoint
            parameters = self.SetParameters(kwargs, param_model)
            apiResponse = self.request("GET", apiUrl, params=parameters)

            return apiResponse

        def get_total_volume(self, domain, **kwargs):
            endpoint = "/%s/totalVolume" % domain
            apiUrl = self.uri + endpoint
            parameters = self.SetParameters(kwargs, param_model)
            apiResponse = self.request("GET", apiUrl, params=parameters)

            return apiResponse




