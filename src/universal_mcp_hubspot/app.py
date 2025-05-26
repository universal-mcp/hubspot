from universal_mcp.applications import APIApplication
from universal_mcp.integrations import Integration
from universal_mcp_hubspot.api_segments.crm_api import CrmApi
from universal_mcp_hubspot.api_segments.marketing_api import MarketingApi

class HubspotApp(APIApplication):

    def __init__(self, integration: Integration=None, **kwargs) -> None:
        super().__init__(name='hubspot', integration=integration, **kwargs)
        self.base_url = 'https://api.hubapi.com'
        self.crm = CrmApi(self)
        self.marketing = MarketingApi(self)

    def list_tools(self):
        all_tools = []
        all_tools.extend(self.crm.list_tools())
        all_tools.extend(self.marketing.list_tools())
        return all_tools