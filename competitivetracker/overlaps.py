from .base import Resource

param_model = {
        'qd'
    }

class Overlaps(Resource):
    key = "overlaps"

    def get_domain_overlaps(self, domain, **kwargs):
        endpoint = "/%s" % domain
        apiUrl = self.uri + endpoint
        parameters = self.SetParameters(kwargs, param_model)
        apiResponse = self.request("GET", apiUrl, params=parameters)

        return apiResponse

    def get_narrowed_overlap(self, domain, **kwargs):
        endpoint = "/narrow/%s" % domain
        apiUrl = self.uri + endpoint
        parameters = self.SetParameters(kwargs, param_model)
        apiResponse = self.request("GET", apiUrl, params=parameters)

        return apiResponse

    def get_top_competing(self, domain, **kwargs):
        endpoint = "/%s/top_competing" % domain
        apiUrl = self.uri + endpoint
        parameters = self.SetParameters(kwargs, param_model)
        apiResponse = self.request("GET", apiUrl, params=parameters)

        return apiResponse
