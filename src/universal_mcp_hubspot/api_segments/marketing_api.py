from typing import Any, Dict, Optional
from .api_segment_base import APISegmentBase

class MarketingApi(APISegmentBase):

    def __init__(self, main_app_client: Any):
        super().__init__(main_app_client)

    def get_marketing_v_campaigns(self, sort=None, after=None, limit=None, name=None, properties=None) -> dict[str, Any]:
        """

        Retrieves a list of marketing campaigns with optional filtering by name, sorting, and limiting results.

        Args:
            sort (string): Optional query parameter to specify sorting criteria for the returned campaigns, allowing sorting by one or more fields in ascending or descending order.
            after (string): Optional parameter to specify a string value for filtering campaigns that occur after a certain point in time.
            limit (integer): The maximum number of campaign records to return in the response.
            name (string): Optional string parameter to filter campaigns by name.
            properties (array): An optional array of campaign property names to include in the response for filtering or detailed retrieval.

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Search
        """
        url = f'{self.main_app_client.base_url}/marketing/v3/campaigns'
        query_params = {k: v for k, v in [('sort', sort), ('after', after), ('limit', limit), ('name', name), ('properties', properties)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if response.status_code == 204 or not response.content or (not response.text.strip()):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def post_marketing_v_campaigns(self, properties) -> dict[str, Any]:
        """

        Creates a new marketing campaign using the provided JSON data and returns a status message upon successful creation.

        Args:
            properties (object): properties

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Basic
        """
        request_body_data = None
        request_body_data = {'properties': properties}
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f'{self.main_app_client.base_url}/marketing/v3/campaigns'
        query_params = {}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        if response.status_code == 204 or not response.content or (not response.text.strip()):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def post_marketing_v_campaigns_batch_read(self, inputs, startDate=None, endDate=None, properties=None) -> dict[str, Any]:
        """

        Retrieves a batch of campaign data from the marketing API, filtering by optional start and end dates and specifying properties to include, using JSON-formatted request body.

        Args:
            inputs (array): inputs
            startDate (string): Optional string parameter to specify the start date for filtering campaigns in the batch read operation.
            endDate (string): Optional query parameter specifying the end date to filter campaigns up to that date in string format.
            properties (array): Optional array of properties to include in the response for the batch read operation.

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Batch
        """
        request_body_data = None
        request_body_data = {'inputs': inputs}
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f'{self.main_app_client.base_url}/marketing/v3/campaigns/batch/read'
        query_params = {k: v for k, v in [('startDate', startDate), ('endDate', endDate), ('properties', properties)] if v is not None}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        if response.status_code == 204 or not response.content or (not response.text.strip()):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def post_marketing_v_campaigns_batch_update(self, inputs) -> dict[str, Any]:
        """

        Updates multiple marketing campaigns in a batch using the POST method, requiring a JSON body and authentication via OAuth2 or private apps with "marketing.campaigns.read" permissions.

        Args:
            inputs (array): inputs

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Batch
        """
        request_body_data = None
        request_body_data = {'inputs': inputs}
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f'{self.main_app_client.base_url}/marketing/v3/campaigns/batch/update'
        query_params = {}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        if response.status_code == 204 or not response.content or (not response.text.strip()):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_marketing_v_campaigns_campaign_guid_reports_metrics(self, campaignGuid, startDate=None, endDate=None) -> dict[str, Any]:
        """

        Retrieves campaign metrics for a specified campaign GUID, optionally filtering by start and end dates.

        Args:
            campaignGuid (string): campaignGuid
            startDate (string): The optional startDate query parameter specifies the beginning date for retrieving campaign metrics in the report.
            endDate (string): Optional date parameter specifying the end date for fetching campaign metrics, formatted as a string.

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Reports
        """
        if campaignGuid is None:
            raise ValueError("Missing required parameter 'campaignGuid'.")
        url = f'{self.main_app_client.base_url}/marketing/v3/campaigns/{campaignGuid}/reports/metrics'
        query_params = {k: v for k, v in [('startDate', startDate), ('endDate', endDate)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if response.status_code == 204 or not response.content or (not response.text.strip()):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_marketing_v_campaigns_campaign_guid_assets_asset_type(self, campaignGuid, assetType, after=None, limit=None, startDate=None, endDate=None) -> dict[str, Any]:
        """

        Retrieves assets of a specified type for a given marketing campaign, supporting optional filtering by date range and pagination.

        Args:
            campaignGuid (string): campaignGuid
            assetType (string): assetType
            after (string): An optional string parameter used to specify a cursor for pagination, indicating the starting point for retrieving assets after a specific position.
            limit (string): Optional string parameter to specify the maximum number of items to return in the response.
            startDate (string): Optional start date filter for retrieving campaign assets, specified in string format.
            endDate (string): Optional date string to specify the end date for filtering campaign assets.

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Asset
        """
        if campaignGuid is None:
            raise ValueError("Missing required parameter 'campaignGuid'.")
        if assetType is None:
            raise ValueError("Missing required parameter 'assetType'.")
        url = f'{self.main_app_client.base_url}/marketing/v3/campaigns/{campaignGuid}/assets/{assetType}'
        query_params = {k: v for k, v in [('after', after), ('limit', limit), ('startDate', startDate), ('endDate', endDate)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if response.status_code == 204 or not response.content or (not response.text.strip()):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def post_marketing_v_campaigns_batch_archive(self, inputs) -> Any:
        """

        Archives a batch of marketing campaigns using the HubSpot API, requiring a JSON request body and returning a 204 status upon successful completion.

        Args:
            inputs (array): inputs

        Returns:
            Any: No content

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Batch
        """
        request_body_data = None
        request_body_data = {'inputs': inputs}
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f'{self.main_app_client.base_url}/marketing/v3/campaigns/batch/archive'
        query_params = {}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        if response.status_code == 204 or not response.content or (not response.text.strip()):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def put_marketing_v_campaigns_campaign_guid_assets_asset_type_asset_id(self, campaignGuid, assetType, assetId) -> Any:
        """

        Updates a specific asset of a given type within a marketing campaign identified by campaignGuid.

        Args:
            campaignGuid (string): campaignGuid
            assetType (string): assetType
            assetId (string): assetId

        Returns:
            Any: No content

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Asset
        """
        if campaignGuid is None:
            raise ValueError("Missing required parameter 'campaignGuid'.")
        if assetType is None:
            raise ValueError("Missing required parameter 'assetType'.")
        if assetId is None:
            raise ValueError("Missing required parameter 'assetId'.")
        request_body_data = None
        url = f'{self.main_app_client.base_url}/marketing/v3/campaigns/{campaignGuid}/assets/{assetType}/{assetId}'
        query_params = {}
        response = self._put(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        if response.status_code == 204 or not response.content or (not response.text.strip()):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def delete_marketing_v_campaigns_campaign_guid_assets_asset_type_asset_id(self, campaignGuid, assetType, assetId) -> Any:
        """

        Deletes a specific asset from a marketing campaign using the provided campaign GUID, asset type, and asset ID.

        Args:
            campaignGuid (string): campaignGuid
            assetType (string): assetType
            assetId (string): assetId

        Returns:
            Any: No content

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Asset
        """
        if campaignGuid is None:
            raise ValueError("Missing required parameter 'campaignGuid'.")
        if assetType is None:
            raise ValueError("Missing required parameter 'assetType'.")
        if assetId is None:
            raise ValueError("Missing required parameter 'assetId'.")
        url = f'{self.main_app_client.base_url}/marketing/v3/campaigns/{campaignGuid}/assets/{assetType}/{assetId}'
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        if response.status_code == 204 or not response.content or (not response.text.strip()):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_marketing_v_campaigns_campaign_guid_reports_revenue(self, campaignGuid, attributionModel=None, startDate=None, endDate=None) -> dict[str, Any]:
        """

        Retrieves revenue reports for a specific marketing campaign using the provided campaign GUID, with optional filtering by attribution model and date range.

        Args:
            campaignGuid (string): campaignGuid
            attributionModel (string): Specifies the attribution model to use for calculating revenue in the report, determining which marketing channels or touchpoints receive credit for conversions.
            startDate (string): The startDate query parameter specifies the optional beginning date to filter the revenue report data for the campaign.
            endDate (string): The endDate query parameter specifies the optional end date to filter the revenue report data for the campaign.

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Reports
        """
        if campaignGuid is None:
            raise ValueError("Missing required parameter 'campaignGuid'.")
        url = f'{self.main_app_client.base_url}/marketing/v3/campaigns/{campaignGuid}/reports/revenue'
        query_params = {k: v for k, v in [('attributionModel', attributionModel), ('startDate', startDate), ('endDate', endDate)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if response.status_code == 204 or not response.content or (not response.text.strip()):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def post_marketing_v_campaigns_batch_create(self, inputs) -> dict[str, Any]:
        """

        Creates multiple marketing campaigns in a single operation using the "POST" method, accepting a JSON body with campaign details and returning a status message upon successful creation.

        Args:
            inputs (array): inputs

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Batch
        """
        request_body_data = None
        request_body_data = {'inputs': inputs}
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f'{self.main_app_client.base_url}/marketing/v3/campaigns/batch/create'
        query_params = {}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        if response.status_code == 204 or not response.content or (not response.text.strip()):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_marketing_v_campaigns_campaign_guid_budget_totals(self, campaignGuid) -> dict[str, Any]:
        """

        Retrieves the total budget details for a marketing campaign using the campaign's GUID.

        Args:
            campaignGuid (string): campaignGuid

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Budget
        """
        if campaignGuid is None:
            raise ValueError("Missing required parameter 'campaignGuid'.")
        url = f'{self.main_app_client.base_url}/marketing/v3/campaigns/{campaignGuid}/budget/totals'
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if response.status_code == 204 or not response.content or (not response.text.strip()):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_marketing_v_campaigns_campaign_guid(self, campaignGuid, startDate=None, endDate=None, properties=None) -> dict[str, Any]:
        """

        Retrieves detailed information about a specific marketing campaign identified by its campaignGuid, optionally filtered by date range and selected properties.

        Args:
            campaignGuid (string): campaignGuid
            startDate (string): The optional startDate query parameter specifies the beginning date to filter campaign data for the GET /marketing/v3/campaigns/{campaignGuid} operation.
            endDate (string): Optional date parameter to filter campaigns by end date, specified in ISO 8601 format.
            properties (array): Optional array of properties to include in the response for the specified campaign.

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Basic
        """
        if campaignGuid is None:
            raise ValueError("Missing required parameter 'campaignGuid'.")
        url = f'{self.main_app_client.base_url}/marketing/v3/campaigns/{campaignGuid}'
        query_params = {k: v for k, v in [('startDate', startDate), ('endDate', endDate), ('properties', properties)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if response.status_code == 204 or not response.content or (not response.text.strip()):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def delete_marketing_v_campaigns_campaign_guid(self, campaignGuid) -> Any:
        """

        Deletes a marketing campaign using the provided campaign GUID and returns a 204 No Content response.

        Args:
            campaignGuid (string): campaignGuid

        Returns:
            Any: No content

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Basic
        """
        if campaignGuid is None:
            raise ValueError("Missing required parameter 'campaignGuid'.")
        url = f'{self.main_app_client.base_url}/marketing/v3/campaigns/{campaignGuid}'
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        if response.status_code == 204 or not response.content or (not response.text.strip()):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def patch_marketing_v_campaigns_campaign_guid(self, campaignGuid, properties) -> dict[str, Any]:
        """

        Updates specified properties of a marketing campaign identified by the campaignGuid using a JSON patch document.

        Args:
            campaignGuid (string): campaignGuid
            properties (object): properties

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Basic
        """
        if campaignGuid is None:
            raise ValueError("Missing required parameter 'campaignGuid'.")
        request_body_data = None
        request_body_data = {'properties': properties}
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f'{self.main_app_client.base_url}/marketing/v3/campaigns/{campaignGuid}'
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        response.raise_for_status()
        if response.status_code == 204 or not response.content or (not response.text.strip()):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_marketing_v_campaigns_campaign_guid_reports_contacts_contact_type(self, campaignGuid, contactType, startDate=None, endDate=None, limit=None, after=None) -> dict[str, Any]:
        """

        Retrieves a report of contacts of a specified type for a marketing campaign, allowing optional filtering by start and end dates and pagination.

        Args:
            campaignGuid (string): campaignGuid
            contactType (string): contactType
            startDate (string): Optional query parameter specifying the start date for filtering reports in the format of a string, allowing users to narrow down the data based on a specific date range.
            endDate (string): Optional query parameter to specify the end date for filtering the campaign contact report data.
            limit (integer): The "limit" parameter, an optional integer, specifies the maximum number of records to return in the response for the contacts report.
            after (string): Optional string parameter to specify a filter for retrieving contacts after a specific date or identifier.

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Reports
        """
        if campaignGuid is None:
            raise ValueError("Missing required parameter 'campaignGuid'.")
        if contactType is None:
            raise ValueError("Missing required parameter 'contactType'.")
        url = f'{self.main_app_client.base_url}/marketing/v3/campaigns/{campaignGuid}/reports/contacts/{contactType}'
        query_params = {k: v for k, v in [('startDate', startDate), ('endDate', endDate), ('limit', limit), ('after', after)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if response.status_code == 204 or not response.content or (not response.text.strip()):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_marketing_v_emails_statistics_list(self, startTimestamp=None, endTimestamp=None, emailIds=None, property=None) -> dict[str, Any]:
        """

        Retrieves email statistics for a specified time range and optional email IDs and properties using the GET method.

        Args:
            startTimestamp (string): Optional query parameter to specify the start timestamp for filtering email statistics.
            endTimestamp (string): Optional end timestamp in string format to filter email statistics up to a specific point in time.
            emailIds (array): Optional array of email IDs to filter statistics; allows retrieving specific email campaign statistics.
            property (string): An optional string parameter used in the query to specify additional properties for filtering or customizing the email statistics list.

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Statistics
        """
        url = f'{self.main_app_client.base_url}/marketing/v3/emails/statistics/list'
        query_params = {k: v for k, v in [('startTimestamp', startTimestamp), ('endTimestamp', endTimestamp), ('emailIds', emailIds), ('property', property)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if response.status_code == 204 or not response.content or (not response.text.strip()):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def post_marketing_v_emails_ab_test_create_variation(self, variationName, contentId) -> dict[str, Any]:
        """

        Creates a variation for an A/B test email using the POST method and returns a successful creation status.

        Args:
            variationName (string): variationName
            contentId (string): ID of the object to test.

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Public_VNext_Emails
        """
        request_body_data = None
        request_body_data = {'variationName': variationName, 'contentId': contentId}
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f'{self.main_app_client.base_url}/marketing/v3/emails/ab-test/create-variation'
        query_params = {}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        if response.status_code == 204 or not response.content or (not response.text.strip()):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_marketing_v_emails_statistics_histogram(self, interval=None, startTimestamp=None, endTimestamp=None, emailIds=None) -> dict[str, Any]:
        """

        Retrieves histogram statistics for marketing emails filtered by optional parameters such as interval, time range, and specific email IDs.

        Args:
            interval (string): The "interval" parameter specifies the time interval for dividing email statistics into buckets, with options including YEAR, QUARTER, MONTH, WEEK, DAY, HOUR, QUARTER_HOUR, MINUTE, and SECOND.
            startTimestamp (string): The optional query parameter specifying the start timestamp to filter email statistics in the histogram data.
            endTimestamp (string): Optional end timestamp for the histogram data, specified as a string.
            emailIds (array): Optional query parameter to specify one or more email IDs for which to retrieve histogram statistics.

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Statistics
        """
        url = f'{self.main_app_client.base_url}/marketing/v3/emails/statistics/histogram'
        query_params = {k: v for k, v in [('interval', interval), ('startTimestamp', startTimestamp), ('endTimestamp', endTimestamp), ('emailIds', emailIds)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if response.status_code == 204 or not response.content or (not response.text.strip()):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_marketing_v_emails_email_id_ab_test_get_variation(self, emailId) -> dict[str, Any]:
        """

        Retrieves the variation for an A/B test associated with a specific email by its ID using the GET method.

        Args:
            emailId (string): emailId

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Marketing Emails
        """
        if emailId is None:
            raise ValueError("Missing required parameter 'emailId'.")
        url = f'{self.main_app_client.base_url}/marketing/v3/emails/{emailId}/ab-test/get-variation'
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if response.status_code == 204 or not response.content or (not response.text.strip()):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def post_marketing_v_emails_email_id_draft_reset(self, emailId) -> Any:
        """

        Resets the draft status of an email using the specified email ID.

        Args:
            emailId (string): emailId

        Returns:
            Any: No content

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Marketing Emails
        """
        if emailId is None:
            raise ValueError("Missing required parameter 'emailId'.")
        request_body_data = None
        url = f'{self.main_app_client.base_url}/marketing/v3/emails/{emailId}/draft/reset'
        query_params = {}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        if response.status_code == 204 or not response.content or (not response.text.strip()):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def post_marketing_v_emails_email_id_revisions_revision_id_restore_to_draft(self, emailId, revisionId) -> dict[str, Any]:
        """

        Restores a specified email revision to draft status by email ID and revision ID.

        Args:
            emailId (string): emailId
            revisionId (string): revisionId

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Marketing Emails
        """
        if emailId is None:
            raise ValueError("Missing required parameter 'emailId'.")
        if revisionId is None:
            raise ValueError("Missing required parameter 'revisionId'.")
        request_body_data = None
        url = f'{self.main_app_client.base_url}/marketing/v3/emails/{emailId}/revisions/{revisionId}/restore-to-draft'
        query_params = {}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        if response.status_code == 204 or not response.content or (not response.text.strip()):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_marketing_v_emails_email_id_draft(self, emailId) -> dict[str, Any]:
        """

        Retrieves the draft of an email with the specified `{emailId}` using the marketing API.

        Args:
            emailId (string): emailId

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Marketing Emails
        """
        if emailId is None:
            raise ValueError("Missing required parameter 'emailId'.")
        url = f'{self.main_app_client.base_url}/marketing/v3/emails/{emailId}/draft'
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if response.status_code == 204 or not response.content or (not response.text.strip()):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def patch_marketing_v_emails_email_id_draft(self, emailId, rssData=None, subject=None, testing=None, publishDate=None, language=None, businessUnitId=None, content=None, webversion=None, archived=None, subscriptionDetails=None, activeDomain=None, name=None, campaign=None, from_=None, state=None, to=None, subcategory=None, sendOnPublish=None) -> dict[str, Any]:
        """

        Updates a draft email identified by the specified emailId using the provided JSON data.

        Args:
            emailId (string): emailId
            rssData (object): RSS related data if it is a blog or rss email.
            subject (string): The subject of the email.
            testing (object): AB testing related data. This property is only returned for AB type emails.
            publishDate (string): The date and time the email is scheduled for, in ISO8601 representation. This is only used in local time or scheduled emails.
            language (string): language
            businessUnitId (string): businessUnitId
            content (object): Data structure representing the content of the email.
            webversion (object): webversion
            archived (boolean): Determines if the email is archived or not.
            subscriptionDetails (object): Data structure representing the subscription fields of the email.
            activeDomain (string): The active domain of the email.
            name (string): The name of the email, as displayed on the email dashboard.
            campaign (string): The ID of the campaign this email is associated to.
            from_ (object): Data structure representing the from fields on the email.
            state (string): The email state.
            to (object): Data structure representing the to fields of the email.
            subcategory (string): The email subcategory.
            sendOnPublish (boolean): Determines whether the email will be sent immediately on publish.

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Marketing Emails
        """
        if emailId is None:
            raise ValueError("Missing required parameter 'emailId'.")
        request_body_data = None
        request_body_data = {'rssData': rssData, 'subject': subject, 'testing': testing, 'publishDate': publishDate, 'language': language, 'businessUnitId': businessUnitId, 'content': content, 'webversion': webversion, 'archived': archived, 'subscriptionDetails': subscriptionDetails, 'activeDomain': activeDomain, 'name': name, 'campaign': campaign, 'from': from_, 'state': state, 'to': to, 'subcategory': subcategory, 'sendOnPublish': sendOnPublish}
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f'{self.main_app_client.base_url}/marketing/v3/emails/{emailId}/draft'
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        response.raise_for_status()
        if response.status_code == 204 or not response.content or (not response.text.strip()):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_marketing_v_emails_email_id_revisions(self, emailId, after=None, before=None, limit=None) -> dict[str, Any]:
        """

        Get a list of revisions for a specified marketing email, optionally filtered by date range and limited in number.

        Args:
            emailId (string): emailId
            after (string): The "after" query parameter specifies a cursor or token to retrieve email revisions created after a certain point, enabling pagination of results.
            before (string): Filter the email revisions to include only those created before the specified timestamp or identifier.
            limit (integer): The "limit" parameter specifies the maximum number of revisions to return in the response when retrieving revisions for a specific email.

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Marketing Emails
        """
        if emailId is None:
            raise ValueError("Missing required parameter 'emailId'.")
        url = f'{self.main_app_client.base_url}/marketing/v3/emails/{emailId}/revisions'
        query_params = {k: v for k, v in [('after', after), ('before', before), ('limit', limit)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if response.status_code == 204 or not response.content or (not response.text.strip()):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_marketing_v_emails_email_id_revisions_revision_id(self, emailId, revisionId) -> dict[str, Any]:
        """

        Retrieves a specific revision of an email identified by the provided email ID and revision ID using the GET method.

        Args:
            emailId (string): emailId
            revisionId (string): revisionId

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Marketing Emails
        """
        if emailId is None:
            raise ValueError("Missing required parameter 'emailId'.")
        if revisionId is None:
            raise ValueError("Missing required parameter 'revisionId'.")
        url = f'{self.main_app_client.base_url}/marketing/v3/emails/{emailId}/revisions/{revisionId}'
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if response.status_code == 204 or not response.content or (not response.text.strip()):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def post_marketing_v_emails_clone(self, id, cloneName=None) -> dict[str, Any]:
        """

        Clones a marketing email using the POST method at the "/marketing/v3/emails/clone" endpoint, creating a duplicate email with the same properties as the original but with a unique ID.

        Args:
            id (string): ID of the email to be cloned.
            cloneName (string): Name of the cloned email.

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Public_VNext_Emails
        """
        request_body_data = None
        request_body_data = {'cloneName': cloneName, 'id': id}
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f'{self.main_app_client.base_url}/marketing/v3/emails/clone'
        query_params = {}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        if response.status_code == 204 or not response.content or (not response.text.strip()):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_marketing_v_emails(self, createdAt=None, createdAfter=None, createdBefore=None, updatedAt=None, updatedAfter=None, updatedBefore=None, sort=None, after=None, limit=None, includeStats=None, type=None, isPublished=None, includedProperties=None, archived=None) -> dict[str, Any]:
        """

        Retrieves a list of marketing emails with optional filtering, sorting, pagination, and inclusion of statistics.

        Args:
            createdAt (string): Optional query parameter specifying the creation date of emails to filter results, formatted as a string.
            createdAfter (string): Filter emails created after a specific date and time, specified in ISO 8601 format.
            createdBefore (string): Filter results to include only emails created before the specified date and time.
            updatedAt (string): Filter emails to include only those updated at or after the specified date and time.
            updatedAfter (string): Filter emails to include only those updated after the specified date and time.
            updatedBefore (string): Optional query parameter to filter emails updated before a specified date and time.
            sort (array): Specifies an array of fields to sort the email results by, allowing clients to customize the order of returned data.
            after (string): Optional string parameter to filter emails by retrieving only those sent after the specified date or time.
            limit (integer): Specifies the maximum number of email records to return in the response.
            includeStats (boolean): Indicates whether to include email statistics in the response; defaults to false if not specified.
            type (string): Optional query parameter to filter emails by type, with possible values including various email categories such as AB_EMAIL, BATCH_EMAIL, and others.
            isPublished (boolean): Indicates whether to include only published emails in the response; accepts boolean values (true or false).
            includedProperties (array): Optional array parameter to specify additional properties to include in the response for the GET operation at "/marketing/v3/emails/".
            archived (boolean): Filter emails by their archived status; set to true to return only archived emails, or false to exclude archived emails.

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Marketing Emails
        """
        url = f'{self.main_app_client.base_url}/marketing/v3/emails/'
        query_params = {k: v for k, v in [('createdAt', createdAt), ('createdAfter', createdAfter), ('createdBefore', createdBefore), ('updatedAt', updatedAt), ('updatedAfter', updatedAfter), ('updatedBefore', updatedBefore), ('sort', sort), ('after', after), ('limit', limit), ('includeStats', includeStats), ('type', type), ('isPublished', isPublished), ('includedProperties', includedProperties), ('archived', archived)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if response.status_code == 204 or not response.content or (not response.text.strip()):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def post_marketing_v_emails(self, name, feedbackSurveyId=None, rssData=None, subject=None, testing=None, publishDate=None, language=None, businessUnitId=None, content=None, webversion=None, archived=None, subscriptionDetails=None, activeDomain=None, campaign=None, from_=None, state=None, to=None, subcategory=None, sendOnPublish=None) -> dict[str, Any]:
        """

        Creates a new email resource in the marketing system using the provided JSON data and returns a success response upon creation.

        Args:
            name (string): The name of the email, as displayed on the email dashboard.
            feedbackSurveyId (string): The ID of the feedback survey linked to the email.
            rssData (object): RSS related data if it is a blog or rss email.
            subject (string): The subject of the email.
            testing (object): AB testing related data. This property is only returned for AB type emails.
            publishDate (string): The date and time the email is scheduled for, in ISO8601 representation. This is only used in local time or scheduled emails.
            language (string): language
            businessUnitId (string): businessUnitId
            content (object): Data structure representing the content of the email.
            webversion (object): webversion
            archived (boolean): Determines if the email is archived or not.
            subscriptionDetails (object): Data structure representing the subscription fields of the email.
            activeDomain (string): The active domain of the email.
            campaign (string): The ID of the campaign this email is associated to.
            from_ (object): Data structure representing the from fields on the email.
            state (string): The email state.
            to (object): Data structure representing the to fields of the email.
            subcategory (string): The email subcategory.
            sendOnPublish (boolean): Determines whether the email will be sent immediately on publish.

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Marketing Emails
        """
        request_body_data = None
        request_body_data = {'feedbackSurveyId': feedbackSurveyId, 'rssData': rssData, 'subject': subject, 'testing': testing, 'publishDate': publishDate, 'language': language, 'businessUnitId': businessUnitId, 'content': content, 'webversion': webversion, 'archived': archived, 'subscriptionDetails': subscriptionDetails, 'activeDomain': activeDomain, 'name': name, 'campaign': campaign, 'from': from_, 'state': state, 'to': to, 'subcategory': subcategory, 'sendOnPublish': sendOnPublish}
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f'{self.main_app_client.base_url}/marketing/v3/emails/'
        query_params = {}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        if response.status_code == 204 or not response.content or (not response.text.strip()):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def post_marketing_v_emails_email_id_revisions_revision_id_restore(self, emailId, revisionId) -> Any:
        """

        Restores a specific email revision using the provided email ID and revision ID via the POST method.

        Args:
            emailId (string): emailId
            revisionId (string): revisionId

        Returns:
            Any: No content

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Marketing Emails
        """
        if emailId is None:
            raise ValueError("Missing required parameter 'emailId'.")
        if revisionId is None:
            raise ValueError("Missing required parameter 'revisionId'.")
        request_body_data = None
        url = f'{self.main_app_client.base_url}/marketing/v3/emails/{emailId}/revisions/{revisionId}/restore'
        query_params = {}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        if response.status_code == 204 or not response.content or (not response.text.strip()):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def get_marketing_v_emails_email_id(self, emailId, includeStats=None, includedProperties=None, archived=None) -> dict[str, Any]:
        """

        Retrieves detailed information about a specific email by its ID, optionally including statistics, selected properties, and archived status.

        Args:
            emailId (string): emailId
            includeStats (boolean): Optionally includes email statistics in the response when set to true.
            includedProperties (array): An optional array parameter to specify which email properties should be included in the response, allowing customization of the returned data.
            archived (boolean): Optional boolean parameter to indicate whether to include archived emails in the response.

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Marketing Emails
        """
        if emailId is None:
            raise ValueError("Missing required parameter 'emailId'.")
        url = f'{self.main_app_client.base_url}/marketing/v3/emails/{emailId}'
        query_params = {k: v for k, v in [('includeStats', includeStats), ('includedProperties', includedProperties), ('archived', archived)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        if response.status_code == 204 or not response.content or (not response.text.strip()):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def delete_marketing_v_emails_email_id(self, emailId, archived=None) -> Any:
        """

        Deletes the specified marketing email by its emailId, optionally archiving it, and returns a 204 No Content status on success.

        Args:
            emailId (string): emailId
            archived (boolean): Optional boolean parameter to indicate whether archived emails should be considered during the deletion operation.

        Returns:
            Any: No content

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Marketing Emails
        """
        if emailId is None:
            raise ValueError("Missing required parameter 'emailId'.")
        url = f'{self.main_app_client.base_url}/marketing/v3/emails/{emailId}'
        query_params = {k: v for k, v in [('archived', archived)] if v is not None}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        if response.status_code == 204 or not response.content or (not response.text.strip()):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def patch_marketing_v_emails_email_id(self, emailId, archived=None, rssData=None, subject=None, testing=None, publishDate=None, language=None, businessUnitId=None, content=None, webversion=None, archived_body=None, subscriptionDetails=None, activeDomain=None, name=None, campaign=None, from_=None, state=None, to=None, subcategory=None, sendOnPublish=None) -> dict[str, Any]:
        """

        Updates an email resource identified by `{emailId}` with partial modifications using JSON in the request body and optionally sets its archived status.

        Args:
            emailId (string): emailId
            archived (boolean): Indicates whether the email should be marked as archived, with true meaning archived and false meaning not archived, during the PATCH operation.
            rssData (object): RSS related data if it is a blog or rss email.
            subject (string): The subject of the email.
            testing (object): AB testing related data. This property is only returned for AB type emails.
            publishDate (string): The date and time the email is scheduled for, in ISO8601 representation. This is only used in local time or scheduled emails.
            language (string): language
            businessUnitId (string): businessUnitId
            content (object): Data structure representing the content of the email.
            webversion (object): webversion
            archived_body (boolean): Determines if the email is archived or not.
            subscriptionDetails (object): Data structure representing the subscription fields of the email.
            activeDomain (string): The active domain of the email.
            name (string): The name of the email, as displayed on the email dashboard.
            campaign (string): The ID of the campaign this email is associated to.
            from_ (object): Data structure representing the from fields on the email.
            state (string): The email state.
            to (object): Data structure representing the to fields of the email.
            subcategory (string): The email subcategory.
            sendOnPublish (boolean): Determines whether the email will be sent immediately on publish.

        Returns:
            dict[str, Any]: successful operation

        Raises:
            HTTPError: Raised when the API request fails (e.g., non-2XX status code).
            JSONDecodeError: Raised if the response body cannot be parsed as JSON.

        Tags:
            Marketing Emails
        """
        if emailId is None:
            raise ValueError("Missing required parameter 'emailId'.")
        request_body_data = None
        request_body_data = {'rssData': rssData, 'subject': subject, 'testing': testing, 'publishDate': publishDate, 'language': language, 'businessUnitId': businessUnitId, 'content': content, 'webversion': webversion, 'archived': archived_body, 'subscriptionDetails': subscriptionDetails, 'activeDomain': activeDomain, 'name': name, 'campaign': campaign, 'from': from_, 'state': state, 'to': to, 'subcategory': subcategory, 'sendOnPublish': sendOnPublish}
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f'{self.main_app_client.base_url}/marketing/v3/emails/{emailId}'
        query_params = {k: v for k, v in [('archived', archived)] if v is not None}
        response = self._patch(url, data=request_body_data, params=query_params)
        response.raise_for_status()
        if response.status_code == 204 or not response.content or (not response.text.strip()):
            return None
        try:
            return response.json()
        except ValueError:
            return None

    def list_tools(self):
        return [self.get_marketing_v_campaigns, self.post_marketing_v_campaigns, self.post_marketing_v_campaigns_batch_read, self.post_marketing_v_campaigns_batch_update, self.get_marketing_v_campaigns_campaign_guid_reports_metrics, self.get_marketing_v_campaigns_campaign_guid_assets_asset_type, self.post_marketing_v_campaigns_batch_archive, self.put_marketing_v_campaigns_campaign_guid_assets_asset_type_asset_id, self.delete_marketing_v_campaigns_campaign_guid_assets_asset_type_asset_id, self.get_marketing_v_campaigns_campaign_guid_reports_revenue, self.post_marketing_v_campaigns_batch_create, self.get_marketing_v_campaigns_campaign_guid_budget_totals, self.get_marketing_v_campaigns_campaign_guid, self.delete_marketing_v_campaigns_campaign_guid, self.patch_marketing_v_campaigns_campaign_guid, self.get_marketing_v_campaigns_campaign_guid_reports_contacts_contact_type, self.get_marketing_v_emails_statistics_list, self.post_marketing_v_emails_ab_test_create_variation, self.get_marketing_v_emails_statistics_histogram, self.get_marketing_v_emails_email_id_ab_test_get_variation, self.post_marketing_v_emails_email_id_draft_reset, self.post_marketing_v_emails_email_id_revisions_revision_id_restore_to_draft, self.get_marketing_v_emails_email_id_draft, self.patch_marketing_v_emails_email_id_draft, self.get_marketing_v_emails_email_id_revisions, self.get_marketing_v_emails_email_id_revisions_revision_id, self.post_marketing_v_emails_clone, self.get_marketing_v_emails, self.post_marketing_v_emails, self.post_marketing_v_emails_email_id_revisions_revision_id_restore, self.get_marketing_v_emails_email_id, self.delete_marketing_v_emails_email_id, self.patch_marketing_v_emails_email_id]