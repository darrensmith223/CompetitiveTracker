from .base import Resource

param_model = {
        'qd'
    }

class Search(Resource):
    key = "search"

    def search(self, **kwargs):
        endpoint = ""
        apiUrl = self.uri + endpoint
        parameters = self.SetParameters(kwargs, param_model)
        apiResponse = self.request("GET", apiUrl, params=parameters)

        return apiResponse
