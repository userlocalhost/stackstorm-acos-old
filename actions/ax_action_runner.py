import acos_client as acos

from acoslib.action import BaseAction


class AXActionRunner(BaseAction):
    def run(self, api_version, action, object_path, **kwargs):
        client = self.login(api_version)
        if client:
            try:
                _target_obj = self.get_object(client, object_path)

                return (True, getattr(_target_obj, action)(**kwargs))
            except acos.errors.AuthenticationFailure:
                return (False, 'An authentication error is occurr')
            except acos.errors.NotFound as e:
                return (False, e)
            except AttributeError:
                return (False, 'The acos_client has no interfaces for %s' % (object_path))
        else:
            return (False, 'Failed to initilaize Client object of acos_client')
