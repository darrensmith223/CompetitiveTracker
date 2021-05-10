from .intelligence import Intelligence, Domain
# from .deliverability import Deliverability
# from .domains import Domains
# from .intelliseeds import Intelliseeds
# from .ping import Ping
# from .regions import Regions
# from .seeds import Seeds


__version__ = '1.0.0'
competitive_tracker_uri = "api.edatasource.com"


class CompetitiveTracker(object):

    def __init__(self, api_key, base_uri=competitive_tracker_uri, version="4"):

        self.base_uri = 'http://' + base_uri + '/v' + version + '/competitive'
        self.api_key = api_key
        self.intelligence = Intelligence(self.base_uri, self.api_key)
        # self.deliverability = Deliverability(self.base_uri, self.api_key)
        # self.domains = Domains(self.base_uri, self.api_key)
        # self.intelliseeds = Intelliseeds(self.base_uri, self.api_key)
        # self.ping = Ping(self.base_uri, self.api_key)
        # self.regions = Regions(self.base_uri, self.api_key)
        # self.seeds = Seeds(self.base_uri, self.api_key)
