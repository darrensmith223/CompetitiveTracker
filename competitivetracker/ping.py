from .base import Resource

param_model = {

    }

class Ping(Resource):
    key = "ping"

    def ping_service(self):
        endpoint = ""
        apiUrl = self.uri + endpoint
        parameters = self.SetParameters({}, {})
        apiResponse = self.request("GET", apiUrl, params=parameters)

        return apiResponse
