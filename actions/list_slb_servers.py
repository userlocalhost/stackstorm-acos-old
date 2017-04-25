import acos_client as acos

from acoslib.action import BaseAction


class ListSLBServers(BaseAction):
    def run(self, api_version):
        client = self.login(api_version)
        if client:
            try:
                return (True, client.slb.server.get(''))
            except acos.errors.AuthenticationFailure as e:
                return (False, 'An authentication error is occurr')
        else:
            return (False, 'Failed to initilaize Client object of acos_client')
