from .base import Resource

param_model = {
    'embed',
    'order',
    'page',
    'per_page',
    'q'
}


class Core:

    def __init__(self, base_uri, api_key):
        self.brands = Brands(base_uri, api_key)
        self.companies = Companies(base_uri, api_key)
        self.discover = Discover(base_uri, api_key)
        self.domains = Domains(base_uri, api_key)
        self.esps = Esps(base_uri, api_key)
        self.graph = Graph(base_uri, api_key)
        self.industries = Industries(base_uri, api_key)
        self.ping = Ping(base_uri, api_key)


class Industries(Resource):
    key = "industries"

    def get_all_industries(self, **kwargs):
        """
        Returns all of the industries ordered by name (paged).

        :param int page:  The page to query for in pagination
        :param int per_page:  The amount of records per page you wish to query for (max 100)
        :param str order:  The property to sort by ('property' for descending, '-property' for ascending)

            Accepts:  `name`, `-name`

        :return:  A ``list`` of object ``dict`` containing name and id of all industries
        """
        endpoint = ""
        apiUrl = self.uri + endpoint
        parameters = self.SetParameters(kwargs, param_model)
        apiResponse = self.request("GET", apiUrl, params=parameters)

        return apiResponse


class Esps(Resource):
    key = "esps"

    def get_all_esps(self, **kwargs):
        """
        Returns all of the email service providers ordered by name (paged).

        :param int page:  The page to query for in pagination
        :param int per_page:  The amount of records per page you wish to query for (max 100)
        :param str order:  The property to sort by ('property' for descending, '-property' for ascending)

            Accepts:  `name`, `-name`

        :return:  A ``list`` of object ``dict`` containing name and id of all esps
        """
        endpoint = ""
        apiUrl = self.uri + endpoint
        parameters = self.SetParameters(kwargs, param_model)
        apiResponse = self.request("GET", apiUrl, params=parameters)

        return apiResponse


class Discover(Resource):
    key = "discover"

    def search_industries(self, **kwargs):
        """
        Search in industries for a matching string (max 1000 results).

        :param str q:  Query parameter to match.  String to search for.

        :return:  A ``dict`` containing name and id of search results
        """
        endpoint = "/industry"
        apiUrl = self.uri + endpoint
        parameters = self.SetParameters(kwargs, param_model)
        apiResponse = self.request("GET", apiUrl, params=parameters)

        return apiResponse

    def search_esps(self, **kwargs):
        """
        Search ESPs for a matching string (max 1000 results).

        :param str q:  Query parameter to match.  String to search for.

        :return:  A ``dict`` containing name and id of search results
        """
        endpoint = "/esp"
        apiUrl = self.uri + endpoint
        parameters = self.SetParameters(kwargs, param_model)
        apiResponse = self.request("GET", apiUrl, params=parameters)

        return apiResponse

    def search_brands(self, **kwargs):
        """
        Search in brands for a matching string (max 1000 results).

        :param str q:  Query parameter to match.  String to search for.

        :return:  A ``dict`` containing name and id of search results
        """
        endpoint = "/brand"
        apiUrl = self.uri + endpoint
        parameters = self.SetParameters(kwargs, param_model)
        apiResponse = self.request("GET", apiUrl, params=parameters)

        return apiResponse

    def search_companies(self, **kwargs):
        """
        Search in companies for a matching string (max 1000 results).

        :param str q:  Query parameter to match.  String to search for.

        :return:  A ``dict`` containing name and id of search results
        """
        endpoint = "/company"
        apiUrl = self.uri + endpoint
        parameters = self.SetParameters(kwargs, param_model)
        apiResponse = self.request("GET", apiUrl, params=parameters)

        return apiResponse


class Brands(Resource):
    key = "brands"

    def get_all_brands(self, **kwargs):
        """
        Returns all of the brands (paged).

        :param int page:  The page to query for in pagination
        :param int per_page:  The amount of records per page you wish to query for (max 100)
        :param str order:  The property to sort by ('property' for descending, '-property' for ascending)

            Accepts:  `name`, `-name`

        :param str embed:  The objects within the return model you wish to embed in the form of
            'customer, customer.name, etc'

            Accepts:  ``address``, ``company``, ``industry``

        :return:  A ``list`` of object ``dict`` containing name and id of all brands
        """
        endpoint = ""
        apiUrl = self.uri + endpoint
        parameters = self.SetParameters(kwargs, param_model)
        apiResponse = self.request("GET", apiUrl, params=parameters)

        return apiResponse


class Companies(Resource):
    key = "companies"

    def get_all_companies(self, **kwargs):
        """
        Returns all of the companies (paged).

        :param int page:  The page to query for in pagination
        :param int per_page:  The amount of records per page you wish to query for (max 100)
        :param str order:  The property to sort by ('property' for descending, '-property' for ascending)

            Accepts:  `name`, `-name`

        :param str embed:  The objects within the return model you wish to embed in the form of
            'customer, customer.name, etc'

            Accepts:  ``address``, ``company``, ``industry``

        :return:  A ``list`` of object ``dict`` containing name and id of all companies
        """
        endpoint = ""
        apiUrl = self.uri + endpoint
        parameters = self.SetParameters(kwargs, param_model)
        apiResponse = self.request("GET", apiUrl, params=parameters)

        return apiResponse


class Domains(Resource):
    pass


class Graph(Resource):
    pass


class Ping(Resource):
    pass
