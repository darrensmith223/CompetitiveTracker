from .base import Resource

param_model = {
        'qd'
    }

class Domain_Info(Resource):
    key = "domain_info"

    def get_domain_info(self, **kwargs):
        endpoint = ""
        apiUrl = self.uri + endpoint
        parameters = self.SetParameters(kwargs, param_model)
        apiResponse = self.request("GET", apiUrl, params=parameters)

        return apiResponse

    def get_brand_volume_and_esps(self, **kwargs):
        endpoint = "/brand_volume_average_and_esps"
        apiUrl = self.uri + endpoint
        parameters = self.SetParameters(kwargs, param_model)
        apiResponse = self.request("GET", apiUrl, params=parameters)

        return apiResponse

    def get_brand_volume_and_esps_extended(self, **kwargs):
        endpoint = "/brand_volume_average_and_esps"
        apiUrl = self.uri + endpoint
        parameters = self.SetParameters(kwargs, param_model)
        apiResponse = self.request("POST", apiUrl, params=parameters)

        return apiResponse
