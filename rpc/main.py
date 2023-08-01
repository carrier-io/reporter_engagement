from pylon.core.tools import log  # pylint: disable=E0611,E0401
from pylon.core.tools import web

from tools import rpc_tools, VaultClient


class RPC:
    integration_name = 'reporter_engagement'

    @web.rpc(f'dusty_config_{integration_name}')
    @rpc_tools.wrap_exceptions(RuntimeError)
    def make_dusty_config(self, context, test_params, scanner_params):
        """ Prepare dusty config for reporter """  
        vault_client = VaultClient.from_project(test_params['project_id'])
        result = {
            "engagement_id": scanner_params,
            "url": vault_client.unsecret("{{secret.galloper_url}}"),
            "token": vault_client.unsecret("{{secret.auth_token}}"),
            "project_id": test_params['project_id']
        }

        return 'engagement', result
