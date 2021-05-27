from base.baseapi import BaseApi


class Api:
    def api(self, data_api):
        self.api = BaseApi()
        return self.api.http(data_api)
