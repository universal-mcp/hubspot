from typing import Any
from universal_mcp.applications import APIApplication
from universal_mcp.integrations import Integration

class HubspotApp(APIApplication):
    def __init__(self, integration: Integration = None, **kwargs) -> None:
        super().__init__(name='hubspot', integration=integration, **kwargs)
        self.base_url = "https://api.hubapi.com"

    def post_crm_v_objects_emails_batch_read_read(self, propertiesWithHistory, inputs, properties, archived=None, idProperty=None) -> dict[str, Any]:
        """
        Retrieves a batch of emails from a CRM system using the "POST" method, allowing optional filtering by archived status, and returns the results in a multipart response.

        Args:
            propertiesWithHistory (array): propertiesWithHistory
            inputs (array): inputs
            properties (array): properties
            archived (boolean): Optional boolean query parameter to filter emails based on whether they are archived, defaulting to false if not specified.
            idProperty (string): idProperty

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Batch
        """
        request_body_data = None
        request_body_data = {
            'propertiesWithHistory': propertiesWithHistory,
            'idProperty': idProperty,
            'inputs': inputs,
            'properties': properties,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/objects/emails/batch/read"
        query_params = {k: v for k, v in [('archived', archived)] if v is not None}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

    def get_crm_v_objects_emails_email_id_get_by_id(self, emailId, properties=None, propertiesWithHistory=None, associations=None, archived=None, idProperty=None) -> dict[str, Any]:
        """
        Retrieves detailed information about a specific email object in a CRM system, allowing optional filtering by properties, associations, and archival status.

        Args:
            emailId (string): emailId
            properties (array): Optional array parameter to specify the properties of the email object to retrieve; allows customization of the response to include only the required properties.
            propertiesWithHistory (array): A comma-separated list of properties for which to include both current values and their historical changes in the response.
            associations (array): An optional array parameter specifying the associations to be included in the response for the email object, allowing for the retrieval of related records.
            archived (boolean): Whether to include archived emails in the response; defaults to false.
            idProperty (string): Optional string parameter that specifies the ID property to be used for filtering or identification purposes in the context of the GET operation for retrieving email objects.

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Basic
        """
        if emailId is None:
            raise ValueError("Missing required parameter 'emailId'.")
        url = f"{self.base_url}/crm/v3/objects/emails/{emailId}"
        query_params = {k: v for k, v in [('properties', properties), ('propertiesWithHistory', propertiesWithHistory), ('associations', associations), ('archived', archived), ('idProperty', idProperty)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_crm_v_objects_emails_email_id_archive(self, emailId) -> Any:
        """
        Deletes an email object identified by the specified emailId from a CRM system.

        Args:
            emailId (string): emailId

        Returns:
            Any: No content

        Tags:
            Basic
        """
        if emailId is None:
            raise ValueError("Missing required parameter 'emailId'.")
        url = f"{self.base_url}/crm/v3/objects/emails/{emailId}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def patch_crm_v_objects_emails_email_id_update(self, emailId, properties, idProperty=None) -> dict[str, Any]:
        """
        Updates specific properties of an existing email record in the CRM by its emailId using a PATCH request with JSON data.

        Args:
            emailId (string): emailId
            properties (object): No description provided. Example: "{'description': 'A new product description', 'name': '1 year implementation consultation', 'price': '6000.00', 'hs_cost_of_goods_sold': '700.00', 'property_date': '1572480000000', 'property_radio': 'option_1', 'property_number': '17', 'property_string': 'value', 'property_checkbox': 'false', 'property_dropdown': 'choice_b', 'property_multiple_checkboxes': 'chocolate;strawberry', 'quantity': '2', 'hs_product_id': '191902', 'recurringbillingfrequency': 'monthly', 'hs_recurring_billing_period': 'P24M'}".
            idProperty (string): Optional string parameter to specify the ID property for the email object, used in the PATCH operation to update specific email details.

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Basic
        """
        if emailId is None:
            raise ValueError("Missing required parameter 'emailId'.")
        request_body_data = None
        request_body_data = {
            'properties': properties,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/objects/emails/{emailId}"
        query_params = {k: v for k, v in [('idProperty', idProperty)] if v is not None}
        response = self._patch(url, data=request_body_data, params=query_params)
        response.raise_for_status()
        return response.json()

    def post_crm_v_objects_emails_merge_merge(self, objectIdToMerge, primaryObjectId) -> dict[str, Any]:
        """
        Merges email records using the provided JSON payload, utilizing OAuth2 or private app authentication to manage contact data in the CRM system.

        Args:
            objectIdToMerge (string): objectIdToMerge
            primaryObjectId (string): primaryObjectId

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Public_Object
        """
        request_body_data = None
        request_body_data = {
            'objectIdToMerge': objectIdToMerge,
            'primaryObjectId': primaryObjectId,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/objects/emails/merge"
        query_params = {}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

    def post_crm_v_objects_emails_batch_archive_archive(self, inputs) -> Any:
        """
        Archives a batch of emails by sending a POST request to the "/crm/v3/objects/emails/batch/archive" endpoint with a JSON payload containing the email IDs to be archived.

        Args:
            inputs (array): inputs

        Returns:
            Any: No content

        Tags:
            Batch
        """
        request_body_data = None
        request_body_data = {
            'inputs': inputs,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/objects/emails/batch/archive"
        query_params = {}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

    def post_crm_v_objects_emails_batch_create_create(self, inputs) -> dict[str, Any]:
        """
        Creates a batch of email objects in the CRM using the POST method, requiring JSON content and authorization through OAuth2 or private apps.

        Args:
            inputs (array): inputs

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Batch
        """
        request_body_data = None
        request_body_data = {
            'inputs': inputs,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/objects/emails/batch/create"
        query_params = {}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

    def post_crm_v_objects_emails_batch_update_update(self, inputs) -> dict[str, Any]:
        """
        Updates multiple email objects in a CRM system using a batch operation via the POST method, returning status messages for each update.

        Args:
            inputs (array): inputs

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Batch
        """
        request_body_data = None
        request_body_data = {
            'inputs': inputs,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/objects/emails/batch/update"
        query_params = {}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

    def post_crm_v_objects_emails_gdpr_delete_purge(self, objectId, idProperty=None) -> Any:
        """
        Deletes a contact and associated data from the CRM in compliance with GDPR guidelines using the provided JSON payload, requiring the "crm.objects.contacts.write" permission.

        Args:
            objectId (string): objectId
            idProperty (string): idProperty

        Returns:
            Any: No content

        Tags:
            GDPR
        """
        request_body_data = None
        request_body_data = {
            'idProperty': idProperty,
            'objectId': objectId,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/objects/emails/gdpr-delete"
        query_params = {}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

    def get_crm_v_objects_emails_get_page(self, limit=None, after=None, properties=None, propertiesWithHistory=None, associations=None, archived=None) -> dict[str, Any]:
        """
        Retrieves a paginated list of email objects with optional filtering by properties, associations, and archival status from the CRM email records.

        Args:
            limit (integer): The "limit" parameter specifies the maximum number of email objects to return in the response, with a default value of 10.
            after (string): An optional string parameter used for pagination, indicating the cursor position after which to retrieve results, allowing for retrieval of subsequent pages of data.
            properties (array): Optional array of properties to include in the response for the email object, allowing for customization of returned data.
            propertiesWithHistory (array): Specifies an array of properties for which both current and historical values should be returned in the email object response.
            associations (array): An optional array parameter that specifies the associations to retrieve for the email objects, allowing for filtering or inclusion of related records.
            archived (boolean): Filter emails by archived status, where true includes only archived emails, and false includes only non-archived emails.

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Basic, important
        """
        url = f"{self.base_url}/crm/v3/objects/emails"
        query_params = {k: v for k, v in [('limit', limit), ('after', after), ('properties', properties), ('propertiesWithHistory', propertiesWithHistory), ('associations', associations), ('archived', archived)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def post_crm_v_objects_emails_create(self, associations, properties) -> dict[str, Any]:
        """
        Creates an email object in the CRM using the POST method, allowing for the association of metadata with the email and requiring authentication via OAuth2 or private apps to access the necessary permissions.

        Args:
            associations (array): associations
            properties (object): No description provided. Example: "{'description': 'Onboarding service for data product', 'name': '1 year implementation consultation', 'price': '6000.00', 'hs_sku': '191902', 'hs_cost_of_goods_sold': '600.00', 'hs_recurring_billing_period': 'P24M', 'city': 'Cambridge', 'phone': '(877) 929-0687', 'state': 'Massachusetts', 'domain': 'biglytics.net', 'industry': 'Technology', 'amount': '1500.00', 'dealname': 'Custom data integrations', 'pipeline': 'default', 'closedate': '2019-12-07T16:50:06.678Z', 'dealstage': 'presentationscheduled', 'hubspot_owner_id': '910901', 'email': 'bcooper@biglytics.net', 'company': 'Biglytics', 'website': 'biglytics.net', 'lastname': 'Cooper', 'firstname': 'Bryan', 'subject': 'troubleshoot report', 'hs_pipeline': 'support_pipeline', 'hs_pipeline_stage': 'open', 'hs_ticket_priority': 'HIGH', 'quantity': '2', 'hs_product_id': '191902', 'recurringbillingfrequency': 'monthly'}".

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Basic
        """
        request_body_data = None
        request_body_data = {
            'associations': associations,
            'properties': properties,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/objects/emails"
        query_params = {}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

    def post_crm_v_objects_emails_search_do_search(self, limit, after, sorts, properties, filterGroups, query=None) -> dict[str, Any]:
        """
        Searches for email objects in a CRM system using specific criteria, returning relevant results.

        Args:
            limit (integer): limit
            after (string): after
            sorts (array): sorts
            properties (array): properties
            filterGroups (array): filterGroups
            query (string): query

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Search
        """
        request_body_data = None
        request_body_data = {
            'query': query,
            'limit': limit,
            'after': after,
            'sorts': sorts,
            'properties': properties,
            'filterGroups': filterGroups,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/objects/emails/search"
        query_params = {}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

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

        Tags:
            Search
        """
        url = f"{self.base_url}/marketing/v3/campaigns"
        query_params = {k: v for k, v in [('sort', sort), ('after', after), ('limit', limit), ('name', name), ('properties', properties)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def post_marketing_v_campaigns(self, properties) -> dict[str, Any]:
        """
        Creates a new marketing campaign using the provided JSON data and returns a status message upon successful creation.

        Args:
            properties (object): properties

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Basic
        """
        request_body_data = None
        request_body_data = {
            'properties': properties,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/marketing/v3/campaigns"
        query_params = {}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

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

        Tags:
            Batch
        """
        request_body_data = None
        request_body_data = {
            'inputs': inputs,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/marketing/v3/campaigns/batch/read"
        query_params = {k: v for k, v in [('startDate', startDate), ('endDate', endDate), ('properties', properties)] if v is not None}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

    def post_marketing_v_campaigns_batch_update(self, inputs) -> dict[str, Any]:
        """
        Updates multiple marketing campaigns in a batch using the POST method, requiring a JSON body and authentication via OAuth2 or private apps with "marketing.campaigns.read" permissions.

        Args:
            inputs (array): inputs

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Batch
        """
        request_body_data = None
        request_body_data = {
            'inputs': inputs,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/marketing/v3/campaigns/batch/update"
        query_params = {}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

    def get_marketing_v_campaigns_campaign_guid_reports_metrics(self, campaignGuid, startDate=None, endDate=None) -> dict[str, Any]:
        """
        Retrieves campaign metrics for a specified campaign GUID, optionally filtering by start and end dates.

        Args:
            campaignGuid (string): campaignGuid
            startDate (string): The optional startDate query parameter specifies the beginning date for retrieving campaign metrics in the report.
            endDate (string): Optional date parameter specifying the end date for fetching campaign metrics, formatted as a string.

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Reports
        """
        if campaignGuid is None:
            raise ValueError("Missing required parameter 'campaignGuid'.")
        url = f"{self.base_url}/marketing/v3/campaigns/{campaignGuid}/reports/metrics"
        query_params = {k: v for k, v in [('startDate', startDate), ('endDate', endDate)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

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

        Tags:
            Asset
        """
        if campaignGuid is None:
            raise ValueError("Missing required parameter 'campaignGuid'.")
        if assetType is None:
            raise ValueError("Missing required parameter 'assetType'.")
        url = f"{self.base_url}/marketing/v3/campaigns/{campaignGuid}/assets/{assetType}"
        query_params = {k: v for k, v in [('after', after), ('limit', limit), ('startDate', startDate), ('endDate', endDate)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def post_marketing_v_campaigns_batch_archive(self, inputs) -> Any:
        """
        Archives a batch of marketing campaigns using the HubSpot API, requiring a JSON request body and returning a 204 status upon successful completion.

        Args:
            inputs (array): inputs

        Returns:
            Any: No content

        Tags:
            Batch
        """
        request_body_data = None
        request_body_data = {
            'inputs': inputs,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/marketing/v3/campaigns/batch/archive"
        query_params = {}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

    def put_marketing_v_campaigns_campaign_guid_assets_asset_type_asset_id(self, campaignGuid, assetType, assetId) -> Any:
        """
        Updates a specific asset of a given type within a marketing campaign identified by campaignGuid.

        Args:
            campaignGuid (string): campaignGuid
            assetType (string): assetType
            assetId (string): assetId

        Returns:
            Any: No content

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
        url = f"{self.base_url}/marketing/v3/campaigns/{campaignGuid}/assets/{assetType}/{assetId}"
        query_params = {}
        response = self._put(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

    def delete_marketing_v_campaigns_campaign_guid_assets_asset_type_asset_id(self, campaignGuid, assetType, assetId) -> Any:
        """
        Deletes a specific asset from a marketing campaign using the provided campaign GUID, asset type, and asset ID.

        Args:
            campaignGuid (string): campaignGuid
            assetType (string): assetType
            assetId (string): assetId

        Returns:
            Any: No content

        Tags:
            Asset
        """
        if campaignGuid is None:
            raise ValueError("Missing required parameter 'campaignGuid'.")
        if assetType is None:
            raise ValueError("Missing required parameter 'assetType'.")
        if assetId is None:
            raise ValueError("Missing required parameter 'assetId'.")
        url = f"{self.base_url}/marketing/v3/campaigns/{campaignGuid}/assets/{assetType}/{assetId}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

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

        Tags:
            Reports
        """
        if campaignGuid is None:
            raise ValueError("Missing required parameter 'campaignGuid'.")
        url = f"{self.base_url}/marketing/v3/campaigns/{campaignGuid}/reports/revenue"
        query_params = {k: v for k, v in [('attributionModel', attributionModel), ('startDate', startDate), ('endDate', endDate)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def post_marketing_v_campaigns_batch_create(self, inputs) -> dict[str, Any]:
        """
        Creates multiple marketing campaigns in a single operation using the "POST" method, accepting a JSON body with campaign details and returning a status message upon successful creation.

        Args:
            inputs (array): inputs

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Batch
        """
        request_body_data = None
        request_body_data = {
            'inputs': inputs,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/marketing/v3/campaigns/batch/create"
        query_params = {}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

    def get_marketing_v_campaigns_campaign_guid_budget_totals(self, campaignGuid) -> dict[str, Any]:
        """
        Retrieves the total budget details for a marketing campaign using the campaign's GUID.

        Args:
            campaignGuid (string): campaignGuid

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Budget
        """
        if campaignGuid is None:
            raise ValueError("Missing required parameter 'campaignGuid'.")
        url = f"{self.base_url}/marketing/v3/campaigns/{campaignGuid}/budget/totals"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

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

        Tags:
            Basic
        """
        if campaignGuid is None:
            raise ValueError("Missing required parameter 'campaignGuid'.")
        url = f"{self.base_url}/marketing/v3/campaigns/{campaignGuid}"
        query_params = {k: v for k, v in [('startDate', startDate), ('endDate', endDate), ('properties', properties)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_marketing_v_campaigns_campaign_guid(self, campaignGuid) -> Any:
        """
        Deletes a marketing campaign using the provided campaign GUID and returns a 204 No Content response.

        Args:
            campaignGuid (string): campaignGuid

        Returns:
            Any: No content

        Tags:
            Basic
        """
        if campaignGuid is None:
            raise ValueError("Missing required parameter 'campaignGuid'.")
        url = f"{self.base_url}/marketing/v3/campaigns/{campaignGuid}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def patch_marketing_v_campaigns_campaign_guid(self, campaignGuid, properties) -> dict[str, Any]:
        """
        Updates specified properties of a marketing campaign identified by the campaignGuid using a JSON patch document.

        Args:
            campaignGuid (string): campaignGuid
            properties (object): properties

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Basic
        """
        if campaignGuid is None:
            raise ValueError("Missing required parameter 'campaignGuid'.")
        request_body_data = None
        request_body_data = {
            'properties': properties,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/marketing/v3/campaigns/{campaignGuid}"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        response.raise_for_status()
        return response.json()

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

        Tags:
            Reports
        """
        if campaignGuid is None:
            raise ValueError("Missing required parameter 'campaignGuid'.")
        if contactType is None:
            raise ValueError("Missing required parameter 'contactType'.")
        url = f"{self.base_url}/marketing/v3/campaigns/{campaignGuid}/reports/contacts/{contactType}"
        query_params = {k: v for k, v in [('startDate', startDate), ('endDate', endDate), ('limit', limit), ('after', after)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

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

        Tags:
            Statistics
        """
        url = f"{self.base_url}/marketing/v3/emails/statistics/list"
        query_params = {k: v for k, v in [('startTimestamp', startTimestamp), ('endTimestamp', endTimestamp), ('emailIds', emailIds), ('property', property)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def post_marketing_v_emails_ab_test_create_variation(self, variationName, contentId) -> dict[str, Any]:
        """
        Creates a variation for an A/B test email using the POST method and returns a successful creation status.

        Args:
            variationName (string): variationName
            contentId (string): ID of the object to test.

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Public_VNext_Emails
        """
        request_body_data = None
        request_body_data = {
            'variationName': variationName,
            'contentId': contentId,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/marketing/v3/emails/ab-test/create-variation"
        query_params = {}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

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

        Tags:
            Statistics
        """
        url = f"{self.base_url}/marketing/v3/emails/statistics/histogram"
        query_params = {k: v for k, v in [('interval', interval), ('startTimestamp', startTimestamp), ('endTimestamp', endTimestamp), ('emailIds', emailIds)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_marketing_v_emails_email_id_ab_test_get_variation(self, emailId) -> dict[str, Any]:
        """
        Retrieves the variation for an A/B test associated with a specific email by its ID using the GET method.

        Args:
            emailId (string): emailId

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Marketing Emails
        """
        if emailId is None:
            raise ValueError("Missing required parameter 'emailId'.")
        url = f"{self.base_url}/marketing/v3/emails/{emailId}/ab-test/get-variation"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def post_marketing_v_emails_email_id_draft_reset(self, emailId) -> Any:
        """
        Resets the draft status of an email using the specified email ID.

        Args:
            emailId (string): emailId

        Returns:
            Any: No content

        Tags:
            Marketing Emails
        """
        if emailId is None:
            raise ValueError("Missing required parameter 'emailId'.")
        request_body_data = None
        url = f"{self.base_url}/marketing/v3/emails/{emailId}/draft/reset"
        query_params = {}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

    def post_marketing_v_emails_email_id_revisions_revision_id_restore_to_draft(self, emailId, revisionId) -> dict[str, Any]:
        """
        Restores a specified email revision to draft status by email ID and revision ID.

        Args:
            emailId (string): emailId
            revisionId (string): revisionId

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Marketing Emails
        """
        if emailId is None:
            raise ValueError("Missing required parameter 'emailId'.")
        if revisionId is None:
            raise ValueError("Missing required parameter 'revisionId'.")
        request_body_data = None
        url = f"{self.base_url}/marketing/v3/emails/{emailId}/revisions/{revisionId}/restore-to-draft"
        query_params = {}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

    def get_marketing_v_emails_email_id_draft(self, emailId) -> dict[str, Any]:
        """
        Retrieves the draft of an email with the specified `{emailId}` using the marketing API.

        Args:
            emailId (string): emailId

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Marketing Emails
        """
        if emailId is None:
            raise ValueError("Missing required parameter 'emailId'.")
        url = f"{self.base_url}/marketing/v3/emails/{emailId}/draft"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

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

        Tags:
            Marketing Emails
        """
        if emailId is None:
            raise ValueError("Missing required parameter 'emailId'.")
        request_body_data = None
        request_body_data = {
            'rssData': rssData,
            'subject': subject,
            'testing': testing,
            'publishDate': publishDate,
            'language': language,
            'businessUnitId': businessUnitId,
            'content': content,
            'webversion': webversion,
            'archived': archived,
            'subscriptionDetails': subscriptionDetails,
            'activeDomain': activeDomain,
            'name': name,
            'campaign': campaign,
            'from': from_,
            'state': state,
            'to': to,
            'subcategory': subcategory,
            'sendOnPublish': sendOnPublish,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/marketing/v3/emails/{emailId}/draft"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        response.raise_for_status()
        return response.json()

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

        Tags:
            Marketing Emails
        """
        if emailId is None:
            raise ValueError("Missing required parameter 'emailId'.")
        url = f"{self.base_url}/marketing/v3/emails/{emailId}/revisions"
        query_params = {k: v for k, v in [('after', after), ('before', before), ('limit', limit)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_marketing_v_emails_email_id_revisions_revision_id(self, emailId, revisionId) -> dict[str, Any]:
        """
        Retrieves a specific revision of an email identified by the provided email ID and revision ID using the GET method.

        Args:
            emailId (string): emailId
            revisionId (string): revisionId

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Marketing Emails
        """
        if emailId is None:
            raise ValueError("Missing required parameter 'emailId'.")
        if revisionId is None:
            raise ValueError("Missing required parameter 'revisionId'.")
        url = f"{self.base_url}/marketing/v3/emails/{emailId}/revisions/{revisionId}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def post_marketing_v_emails_clone(self, id, cloneName=None) -> dict[str, Any]:
        """
        Clones a marketing email using the POST method at the "/marketing/v3/emails/clone" endpoint, creating a duplicate email with the same properties as the original but with a unique ID.

        Args:
            id (string): ID of the email to be cloned.
            cloneName (string): Name of the cloned email.

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Public_VNext_Emails
        """
        request_body_data = None
        request_body_data = {
            'cloneName': cloneName,
            'id': id,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/marketing/v3/emails/clone"
        query_params = {}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

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

        Tags:
            Marketing Emails
        """
        url = f"{self.base_url}/marketing/v3/emails/"
        query_params = {k: v for k, v in [('createdAt', createdAt), ('createdAfter', createdAfter), ('createdBefore', createdBefore), ('updatedAt', updatedAt), ('updatedAfter', updatedAfter), ('updatedBefore', updatedBefore), ('sort', sort), ('after', after), ('limit', limit), ('includeStats', includeStats), ('type', type), ('isPublished', isPublished), ('includedProperties', includedProperties), ('archived', archived)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

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

        Tags:
            Marketing Emails
        """
        request_body_data = None
        request_body_data = {
            'feedbackSurveyId': feedbackSurveyId,
            'rssData': rssData,
            'subject': subject,
            'testing': testing,
            'publishDate': publishDate,
            'language': language,
            'businessUnitId': businessUnitId,
            'content': content,
            'webversion': webversion,
            'archived': archived,
            'subscriptionDetails': subscriptionDetails,
            'activeDomain': activeDomain,
            'name': name,
            'campaign': campaign,
            'from': from_,
            'state': state,
            'to': to,
            'subcategory': subcategory,
            'sendOnPublish': sendOnPublish,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/marketing/v3/emails/"
        query_params = {}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

    def post_marketing_v_emails_email_id_revisions_revision_id_restore(self, emailId, revisionId) -> Any:
        """
        Restores a specific email revision using the provided email ID and revision ID via the POST method.

        Args:
            emailId (string): emailId
            revisionId (string): revisionId

        Returns:
            Any: No content

        Tags:
            Marketing Emails
        """
        if emailId is None:
            raise ValueError("Missing required parameter 'emailId'.")
        if revisionId is None:
            raise ValueError("Missing required parameter 'revisionId'.")
        request_body_data = None
        url = f"{self.base_url}/marketing/v3/emails/{emailId}/revisions/{revisionId}/restore"
        query_params = {}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

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

        Tags:
            Marketing Emails
        """
        if emailId is None:
            raise ValueError("Missing required parameter 'emailId'.")
        url = f"{self.base_url}/marketing/v3/emails/{emailId}"
        query_params = {k: v for k, v in [('includeStats', includeStats), ('includedProperties', includedProperties), ('archived', archived)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_marketing_v_emails_email_id(self, emailId, archived=None) -> Any:
        """
        Deletes the specified marketing email by its emailId, optionally archiving it, and returns a 204 No Content status on success.

        Args:
            emailId (string): emailId
            archived (boolean): Optional boolean parameter to indicate whether archived emails should be considered during the deletion operation.

        Returns:
            Any: No content

        Tags:
            Marketing Emails
        """
        if emailId is None:
            raise ValueError("Missing required parameter 'emailId'.")
        url = f"{self.base_url}/marketing/v3/emails/{emailId}"
        query_params = {k: v for k, v in [('archived', archived)] if v is not None}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

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

        Tags:
            Marketing Emails
        """
        if emailId is None:
            raise ValueError("Missing required parameter 'emailId'.")
        request_body_data = None
        request_body_data = {
            'rssData': rssData,
            'subject': subject,
            'testing': testing,
            'publishDate': publishDate,
            'language': language,
            'businessUnitId': businessUnitId,
            'content': content,
            'webversion': webversion,
            'archived': archived_body,
            'subscriptionDetails': subscriptionDetails,
            'activeDomain': activeDomain,
            'name': name,
            'campaign': campaign,
            'from': from_,
            'state': state,
            'to': to,
            'subcategory': subcategory,
            'sendOnPublish': sendOnPublish,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/marketing/v3/emails/{emailId}"
        query_params = {k: v for k, v in [('archived', archived)] if v is not None}
        response = self._patch(url, data=request_body_data, params=query_params)
        response.raise_for_status()
        return response.json()

    def batch_read_by_properties(self, propertiesWithHistory, inputs, properties, archived=None, idProperty=None) -> dict[str, Any]:
        """
        Retrieves a batch of product records from the CRM using the POST method, optionally filtering by archived status, and returns the results in a multi-status response.

        Args:
            propertiesWithHistory (array): propertiesWithHistory
            inputs (array): inputs
            properties (array): properties
            archived (boolean): Indicates whether to include archived products in the batch read operation; defaults to false.
            idProperty (string): idProperty

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Batch
        """
        request_body_data = None
        request_body_data = {
            'propertiesWithHistory': propertiesWithHistory,
            'idProperty': idProperty,
            'inputs': inputs,
            'properties': properties,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/objects/products/batch/read"
        query_params = {k: v for k, v in [('archived', archived)] if v is not None}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

    def basic_read_product_by_id(self, productId, properties=None, propertiesWithHistory=None, associations=None, archived=None, idProperty=None) -> dict[str, Any]:
        """
        Retrieves detailed information about a specific product by its ID, allowing optional filtering by properties, properties with history, associations, and archived status.

        Args:
            productId (string): productId
            properties (array): Specifies an array of property names to include in the response, allowing you to request only the specific product properties you need.
            propertiesWithHistory (array): An optional array parameter that specifies which properties to include with their historical data in the response.
            associations (array): An optional array parameter to specify which associations to include in the response, such as related contacts or companies associated with the product.
            archived (boolean): Filter results to include archived products by setting this boolean parameter to true; defaults to false if not specified.
            idProperty (string): Optional string parameter to specify the property used for identifying products.

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Basic
        """
        if productId is None:
            raise ValueError("Missing required parameter 'productId'.")
        url = f"{self.base_url}/crm/v3/objects/products/{productId}"
        query_params = {k: v for k, v in [('properties', properties), ('propertiesWithHistory', propertiesWithHistory), ('associations', associations), ('archived', archived), ('idProperty', idProperty)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def basic_archive_product(self, productId) -> Any:
        """
        Deletes a product from the CRM using its product ID.

        Args:
            productId (string): productId

        Returns:
            Any: No content

        Tags:
            Basic
        """
        if productId is None:
            raise ValueError("Missing required parameter 'productId'.")
        url = f"{self.base_url}/crm/v3/objects/products/{productId}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def basic_update_product(self, productId, properties, idProperty=None) -> dict[str, Any]:
        """
        Updates specified properties of a product identified by productId using a JSON PATCH request.

        Args:
            productId (string): productId
            properties (object): No description provided. Example: "{'description': 'A new product description', 'name': '1 year implementation consultation', 'price': '6000.00', 'hs_cost_of_goods_sold': '700.00', 'property_date': '1572480000000', 'property_radio': 'option_1', 'property_number': '17', 'property_string': 'value', 'property_checkbox': 'false', 'property_dropdown': 'choice_b', 'property_multiple_checkboxes': 'chocolate;strawberry', 'quantity': '2', 'hs_product_id': '191902', 'recurringbillingfrequency': 'monthly', 'hs_recurring_billing_period': 'P24M'}".
            idProperty (string): The idProperty query parameter specifies an optional custom property name to identify the product resource during the PATCH update operation.

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Basic
        """
        if productId is None:
            raise ValueError("Missing required parameter 'productId'.")
        request_body_data = None
        request_body_data = {
            'properties': properties,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/objects/products/{productId}"
        query_params = {k: v for k, v in [('idProperty', idProperty)] if v is not None}
        response = self._patch(url, data=request_body_data, params=query_params)
        response.raise_for_status()
        return response.json()

    def public_object_merge_products_same_type(self, objectIdToMerge, primaryObjectId) -> dict[str, Any]:
        """
        Merges two or more product records in a CRM system using the POST method, allowing for the consolidation of data into a single, unified record.

        Args:
            objectIdToMerge (string): objectIdToMerge
            primaryObjectId (string): primaryObjectId

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Public_Object
        """
        request_body_data = None
        request_body_data = {
            'objectIdToMerge': objectIdToMerge,
            'primaryObjectId': primaryObjectId,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/objects/products/merge"
        query_params = {}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

    def batch_archive_products_by_ids(self, inputs) -> Any:
        """
        Archives a batch of products by ID using the POST method, accepting JSON-formatted request bodies and returning a 204 status upon successful execution.

        Args:
            inputs (array): inputs

        Returns:
            Any: No content

        Tags:
            Batch
        """
        request_body_data = None
        request_body_data = {
            'inputs': inputs,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/objects/products/batch/archive"
        query_params = {}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

    def batch_create_products_batch(self, inputs) -> dict[str, Any]:
        """
        Creates multiple product records in a single batch request within the CRM system.

        Args:
            inputs (array): inputs

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Batch
        """
        request_body_data = None
        request_body_data = {
            'inputs': inputs,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/objects/products/batch/create"
        query_params = {}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

    def batch_update_products_batch(self, inputs) -> dict[str, Any]:
        """
        Updates multiple product records in a batch using the HubSpot CRM v3 API and returns a status response indicating success or partial failure.

        Args:
            inputs (array): inputs

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Batch
        """
        request_body_data = None
        request_body_data = {
            'inputs': inputs,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/objects/products/batch/update"
        query_params = {}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

    def gdpr_delete_contact(self, objectId, idProperty=None) -> Any:
        """
        Performs a GDPR-compliant deletion of product records in the CRM using the POST method, requiring a JSON request body and authentication.

        Args:
            objectId (string): objectId
            idProperty (string): idProperty

        Returns:
            Any: No content

        Tags:
            GDPR
        """
        request_body_data = None
        request_body_data = {
            'idProperty': idProperty,
            'objectId': objectId,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/objects/products/gdpr-delete"
        query_params = {}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

    def basic_list_products_page(self, limit=None, after=None, properties=None, propertiesWithHistory=None, associations=None, archived=None) -> dict[str, Any]:
        """
        Retrieves a list of products from a CRM system using the "GET" method, allowing for optional filtering and customization of the returned data based on parameters such as limit, after, properties, properties with history, associations, and archived status.

        Args:
            limit (integer): The "limit" parameter specifies the maximum number of product objects to return in the response, with a default value of 10.
            after (string): Specifies a cursor for pagination, allowing retrieval of the next page of product results after the specified item.
            properties (array): Optional query parameter to specify the properties of the product object to be returned in the response; it is an array of property names.
            propertiesWithHistory (array): Optional array parameter that specifies the properties for which both current and historical values should be returned in the response.
            associations (array): Optional array parameter to specify associations to be retrieved for the products.
            archived (boolean): Filter products by their archived status; when true, only archived products are returned, otherwise only active products are listed (default is false).

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Basic, important
        """
        url = f"{self.base_url}/crm/v3/objects/products"
        query_params = {k: v for k, v in [('limit', limit), ('after', after), ('properties', properties), ('propertiesWithHistory', propertiesWithHistory), ('associations', associations), ('archived', archived)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def basic_create_product_object(self, associations, properties) -> dict[str, Any]:
        """
        Creates a new product in the CRM product library to manage the collection of goods and services offered by the company.

        Args:
            associations (array): associations
            properties (object): No description provided. Example: "{'description': 'Onboarding service for data product', 'name': '1 year implementation consultation', 'price': '6000.00', 'hs_sku': '191902', 'hs_cost_of_goods_sold': '600.00', 'hs_recurring_billing_period': 'P24M', 'city': 'Cambridge', 'phone': '(877) 929-0687', 'state': 'Massachusetts', 'domain': 'biglytics.net', 'industry': 'Technology', 'amount': '1500.00', 'dealname': 'Custom data integrations', 'pipeline': 'default', 'closedate': '2019-12-07T16:50:06.678Z', 'dealstage': 'presentationscheduled', 'hubspot_owner_id': '910901', 'email': 'bcooper@biglytics.net', 'company': 'Biglytics', 'website': 'biglytics.net', 'lastname': 'Cooper', 'firstname': 'Bryan', 'subject': 'troubleshoot report', 'hs_pipeline': 'support_pipeline', 'hs_pipeline_stage': 'open', 'hs_ticket_priority': 'HIGH', 'quantity': '2', 'hs_product_id': '191902', 'recurringbillingfrequency': 'monthly'}".

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Basic
        """
        request_body_data = None
        request_body_data = {
            'associations': associations,
            'properties': properties,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/objects/products"
        query_params = {}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

    def search_products_by_criteria(self, limit, after, sorts, properties, filterGroups, query=None) -> dict[str, Any]:
        """
        Searches for products in a CRM using a POST request to the "/crm/v3/objects/products/search" endpoint, allowing for filtering and retrieval of product data in a JSON format.

        Args:
            limit (integer): limit
            after (string): after
            sorts (array): sorts
            properties (array): properties
            filterGroups (array): filterGroups
            query (string): query

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Search
        """
        request_body_data = None
        request_body_data = {
            'query': query,
            'limit': limit,
            'after': after,
            'sorts': sorts,
            'properties': properties,
            'filterGroups': filterGroups,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/objects/products/search"
        query_params = {}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

    def pipelines_get_by_id(self, objectType, pipelineId) -> dict[str, Any]:
        """
        Retrieves details about a specific CRM pipeline by its ID and object type, providing information about the stages and records within that pipeline.

        Args:
            objectType (string): objectType
            pipelineId (string): pipelineId

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Pipelines
        """
        if objectType is None:
            raise ValueError("Missing required parameter 'objectType'.")
        if pipelineId is None:
            raise ValueError("Missing required parameter 'pipelineId'.")
        url = f"{self.base_url}/crm/v3/pipelines/{objectType}/{pipelineId}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def pipelines_replace_pipeline_object(self, objectType, pipelineId, displayOrder, stages, label, validateReferencesBeforeDelete=None, validateDealStageUsagesBeforeDelete=None) -> dict[str, Any]:
        """
        Updates the details of a specified pipeline for a given CRM object type by replacing its properties using the provided JSON payload.

        Args:
            objectType (string): objectType
            pipelineId (string): pipelineId
            displayOrder (integer): The order for displaying this pipeline. If two pipelines have a matching `displayOrder`, they will be sorted alphabetically by label. Example: '0'.
            stages (array): Pipeline stage inputs used to create the new or replacement pipeline. Example: "[{'label': 'In Progress', 'metadata': {'ticketState': 'OPEN'}, 'displayOrder': 0}, {'label': 'Done', 'metadata': {'ticketState': 'CLOSED'}, 'displayOrder': 1}]".
            label (string): A unique label used to organize pipelines in HubSpot's UI Example: 'My replaced pipeline'.
            validateReferencesBeforeDelete (boolean): If set to true, validates whether references exist before deleting the pipeline; defaults to false.
            validateDealStageUsagesBeforeDelete (boolean): Indicates whether to validate deal stage usages before deleting, preventing deletion if stages are in use.

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Pipelines
        """
        if objectType is None:
            raise ValueError("Missing required parameter 'objectType'.")
        if pipelineId is None:
            raise ValueError("Missing required parameter 'pipelineId'.")
        request_body_data = None
        request_body_data = {
            'displayOrder': displayOrder,
            'stages': stages,
            'label': label,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/pipelines/{objectType}/{pipelineId}"
        query_params = {k: v for k, v in [('validateReferencesBeforeDelete', validateReferencesBeforeDelete), ('validateDealStageUsagesBeforeDelete', validateDealStageUsagesBeforeDelete)] if v is not None}
        response = self._put(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

    def pipelines_remove_by_id(self, objectType, pipelineId, validateReferencesBeforeDelete=None, validateDealStageUsagesBeforeDelete=None) -> Any:
        """
        Deletes a pipeline by its ID and object type in the CRM system using the specified security permissions, optionally validating references and deal stage usages before deletion.

        Args:
            objectType (string): objectType
            pipelineId (string): pipelineId
            validateReferencesBeforeDelete (boolean): Determines whether to validate references before deleting the specified pipeline, defaulting to false if not provided.
            validateDealStageUsagesBeforeDelete (boolean): Determines whether to validate deal stage usages before deleting a pipeline, defaults to false.

        Returns:
            Any: No content

        Tags:
            Pipelines
        """
        if objectType is None:
            raise ValueError("Missing required parameter 'objectType'.")
        if pipelineId is None:
            raise ValueError("Missing required parameter 'pipelineId'.")
        url = f"{self.base_url}/crm/v3/pipelines/{objectType}/{pipelineId}"
        query_params = {k: v for k, v in [('validateReferencesBeforeDelete', validateReferencesBeforeDelete), ('validateDealStageUsagesBeforeDelete', validateDealStageUsagesBeforeDelete)] if v is not None}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def pipelines_update_pipeline_by_id(self, objectType, pipelineId, validateReferencesBeforeDelete=None, validateDealStageUsagesBeforeDelete=None, archived=None, displayOrder=None, label=None) -> dict[str, Any]:
        """
        Updates a CRM pipeline by specifying the object type and pipeline ID, allowing modifications to its configuration with optional validation checks for references and deal stage usage before deletion.

        Args:
            objectType (string): objectType
            pipelineId (string): pipelineId
            validateReferencesBeforeDelete (boolean): Determines whether to validate references before deleting, defaults to false if not provided.
            validateDealStageUsagesBeforeDelete (boolean): Whether to validate deal stage usages before deleting a pipeline, defaults to false.
            archived (boolean): Whether the pipeline is archived. This property should only be provided when restoring an archived pipeline. If it's provided in any other call, the request will fail and a `400 Bad Request` will be returned.
            displayOrder (integer): The order for displaying this pipeline. If two pipelines have a matching `displayOrder`, they will be sorted alphabetically by label. Example: '0'.
            label (string): A unique label used to organize pipelines in HubSpot's UI Example: 'My updated pipeline'.

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Pipelines
        """
        if objectType is None:
            raise ValueError("Missing required parameter 'objectType'.")
        if pipelineId is None:
            raise ValueError("Missing required parameter 'pipelineId'.")
        request_body_data = None
        request_body_data = {
            'archived': archived,
            'displayOrder': displayOrder,
            'label': label,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/pipelines/{objectType}/{pipelineId}"
        query_params = {k: v for k, v in [('validateReferencesBeforeDelete', validateReferencesBeforeDelete), ('validateDealStageUsagesBeforeDelete', validateDealStageUsagesBeforeDelete)] if v is not None}
        response = self._patch(url, data=request_body_data, params=query_params)
        response.raise_for_status()
        return response.json()

    def pipeline_audits_get_by_pipeline_id(self, objectType, pipelineId) -> dict[str, Any]:
        """
        Retrieves an audit of all changes to a specific pipeline in HubSpot CRM, based on the provided object type and pipeline ID.

        Args:
            objectType (string): objectType
            pipelineId (string): pipelineId

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Pipeline Audits
        """
        if objectType is None:
            raise ValueError("Missing required parameter 'objectType'.")
        if pipelineId is None:
            raise ValueError("Missing required parameter 'pipelineId'.")
        url = f"{self.base_url}/crm/v3/pipelines/{objectType}/{pipelineId}/audit"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def pipeline_stages_get_all(self, objectType, pipelineId) -> dict[str, Any]:
        """
        Retrieves the list of stages within a specified pipeline for a given object type in the CRM system.

        Args:
            objectType (string): objectType
            pipelineId (string): pipelineId

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Pipeline Stages
        """
        if objectType is None:
            raise ValueError("Missing required parameter 'objectType'.")
        if pipelineId is None:
            raise ValueError("Missing required parameter 'pipelineId'.")
        url = f"{self.base_url}/crm/v3/pipelines/{objectType}/{pipelineId}/stages"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def pipeline_stages_create_stage_object(self, objectType, pipelineId, metadata, displayOrder, label) -> dict[str, Any]:
        """
        Creates a new stage in a specified CRM pipeline using the POST method, requiring the object type and pipeline ID, and a JSON-formatted request body.

        Args:
            objectType (string): objectType
            pipelineId (string): pipelineId
            metadata (object): A JSON object containing properties that are not present on all object pipelines.

        For `deals` pipelines, the `probability` field is required (`{ "probability": 0.5 }`), and represents the likelihood a deal will close. Possible values are between 0.0 and 1.0 in increments of 0.1.

        For `tickets` pipelines, the `ticketState` field is optional (`{ "ticketState": "OPEN" }`), and represents whether the ticket remains open or has been closed by a member of your Support team. Possible values are `OPEN` or `CLOSED`. Example: "{'ticketState': 'CLOSED'}".
            displayOrder (integer): The order for displaying this pipeline stage. If two pipeline stages have a matching `displayOrder`, they will be sorted alphabetically by label. Example: '1'.
            label (string): A label used to organize pipeline stages in HubSpot's UI. Each pipeline stage's label must be unique within that pipeline. Example: 'Done'.

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Pipeline Stages
        """
        if objectType is None:
            raise ValueError("Missing required parameter 'objectType'.")
        if pipelineId is None:
            raise ValueError("Missing required parameter 'pipelineId'.")
        request_body_data = None
        request_body_data = {
            'metadata': metadata,
            'displayOrder': displayOrder,
            'label': label,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/pipelines/{objectType}/{pipelineId}/stages"
        query_params = {}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

    def pipelines_get_all(self, objectType) -> dict[str, Any]:
        """
        Retrieves a list of pipelines for a specified object type in the CRM, allowing for the management and inspection of pipelines relevant to that object type.

        Args:
            objectType (string): objectType

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Pipelines
        """
        if objectType is None:
            raise ValueError("Missing required parameter 'objectType'.")
        url = f"{self.base_url}/crm/v3/pipelines/{objectType}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def pipelines_create_new_pipeline_object(self, objectType, displayOrder, stages, label) -> dict[str, Any]:
        """
        Creates a new pipeline for the specified CRM object type with the provided pipeline details.

        Args:
            objectType (string): objectType
            displayOrder (integer): The order for displaying this pipeline. If two pipelines have a matching `displayOrder`, they will be sorted alphabetically by label. Example: '0'.
            stages (array): Pipeline stage inputs used to create the new or replacement pipeline. Example: "[{'label': 'In Progress', 'metadata': {'ticketState': 'OPEN'}, 'displayOrder': 0}, {'label': 'Done', 'metadata': {'ticketState': 'CLOSED'}, 'displayOrder': 1}]".
            label (string): A unique label used to organize pipelines in HubSpot's UI Example: 'My replaced pipeline'.

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Pipelines
        """
        if objectType is None:
            raise ValueError("Missing required parameter 'objectType'.")
        request_body_data = None
        request_body_data = {
            'displayOrder': displayOrder,
            'stages': stages,
            'label': label,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/pipelines/{objectType}"
        query_params = {}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

    def pipeline_stages_get_by_id(self, objectType, pipelineId, stageId) -> dict[str, Any]:
        """
        Retrieves detailed information about a specific stage within a given pipeline and object type in the CRM system.

        Args:
            objectType (string): objectType
            pipelineId (string): pipelineId
            stageId (string): stageId

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Pipeline Stages
        """
        if objectType is None:
            raise ValueError("Missing required parameter 'objectType'.")
        if pipelineId is None:
            raise ValueError("Missing required parameter 'pipelineId'.")
        if stageId is None:
            raise ValueError("Missing required parameter 'stageId'.")
        url = f"{self.base_url}/crm/v3/pipelines/{objectType}/{pipelineId}/stages/{stageId}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def pipeline_stages_replace_stage_object(self, objectType, pipelineId, stageId, metadata, displayOrder, label) -> dict[str, Any]:
        """
        Updates a specific stage in a CRM pipeline using the provided JSON data and returns a status message.

        Args:
            objectType (string): objectType
            pipelineId (string): pipelineId
            stageId (string): stageId
            metadata (object): A JSON object containing properties that are not present on all object pipelines.

        For `deals` pipelines, the `probability` field is required (`{ "probability": 0.5 }`), and represents the likelihood a deal will close. Possible values are between 0.0 and 1.0 in increments of 0.1.

        For `tickets` pipelines, the `ticketState` field is optional (`{ "ticketState": "OPEN" }`), and represents whether the ticket remains open or has been closed by a member of your Support team. Possible values are `OPEN` or `CLOSED`. Example: "{'ticketState': 'CLOSED'}".
            displayOrder (integer): The order for displaying this pipeline stage. If two pipeline stages have a matching `displayOrder`, they will be sorted alphabetically by label. Example: '1'.
            label (string): A label used to organize pipeline stages in HubSpot's UI. Each pipeline stage's label must be unique within that pipeline. Example: 'Done'.

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Pipeline Stages
        """
        if objectType is None:
            raise ValueError("Missing required parameter 'objectType'.")
        if pipelineId is None:
            raise ValueError("Missing required parameter 'pipelineId'.")
        if stageId is None:
            raise ValueError("Missing required parameter 'stageId'.")
        request_body_data = None
        request_body_data = {
            'metadata': metadata,
            'displayOrder': displayOrder,
            'label': label,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/pipelines/{objectType}/{pipelineId}/stages/{stageId}"
        query_params = {}
        response = self._put(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

    def pipeline_stages_delete_stage(self, objectType, pipelineId, stageId) -> Any:
        """
        Deletes a specific stage from a pipeline for the given object type in the CRM system.

        Args:
            objectType (string): objectType
            pipelineId (string): pipelineId
            stageId (string): stageId

        Returns:
            Any: No content

        Tags:
            Pipeline Stages
        """
        if objectType is None:
            raise ValueError("Missing required parameter 'objectType'.")
        if pipelineId is None:
            raise ValueError("Missing required parameter 'pipelineId'.")
        if stageId is None:
            raise ValueError("Missing required parameter 'stageId'.")
        url = f"{self.base_url}/crm/v3/pipelines/{objectType}/{pipelineId}/stages/{stageId}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def pipeline_stages_update_stage_by_id(self, objectType, pipelineId, stageId, metadata, archived=None, displayOrder=None, label=None) -> dict[str, Any]:
        """
        Updates a specific stage in a CRM pipeline using a PATCH request to the "/crm/v3/pipelines/{objectType}/{pipelineId}/stages/{stageId}" endpoint, requiring a JSON body with the necessary updates.

        Args:
            objectType (string): objectType
            pipelineId (string): pipelineId
            stageId (string): stageId
            metadata (object): A JSON object containing properties that are not present on all object pipelines.

        For `deals` pipelines, the `probability` field is required (`{ "probability": 0.5 }`), and represents the likelihood a deal will close. Possible values are between 0.0 and 1.0 in increments of 0.1.

        For `tickets` pipelines, the `ticketState` field is optional (`{ "ticketState": "OPEN" }`), and represents whether the ticket remains open or has been closed by a member of your Support team. Possible values are `OPEN` or `CLOSED`. Example: "{'ticketState': 'CLOSED'}".
            archived (boolean): Whether the pipeline is archived.
            displayOrder (integer): The order for displaying this pipeline stage. If two pipeline stages have a matching `displayOrder`, they will be sorted alphabetically by label. Example: '1'.
            label (string): A label used to organize pipeline stages in HubSpot's UI. Each pipeline stage's label must be unique within that pipeline. Example: 'Done'.

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Pipeline Stages
        """
        if objectType is None:
            raise ValueError("Missing required parameter 'objectType'.")
        if pipelineId is None:
            raise ValueError("Missing required parameter 'pipelineId'.")
        if stageId is None:
            raise ValueError("Missing required parameter 'stageId'.")
        request_body_data = None
        request_body_data = {
            'archived': archived,
            'metadata': metadata,
            'displayOrder': displayOrder,
            'label': label,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/pipelines/{objectType}/{pipelineId}/stages/{stageId}"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        response.raise_for_status()
        return response.json()

    def batch_read_companies_by_properties(self, propertiesWithHistory, inputs, properties, archived=None, idProperty=None) -> dict[str, Any]:
        """
        Reads a batch of companies by internal ID or unique property values using the HubSpot CRM API and returns the results in a JSON format.

        Args:
            propertiesWithHistory (array): propertiesWithHistory
            inputs (array): inputs
            properties (array): properties
            archived (boolean): A boolean flag indicating whether to include archived companies in the batch read operation.
            idProperty (string): idProperty

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Batch
        """
        request_body_data = None
        request_body_data = {
            'propertiesWithHistory': propertiesWithHistory,
            'idProperty': idProperty,
            'inputs': inputs,
            'properties': properties,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/objects/companies/batch/read"
        query_params = {k: v for k, v in [('archived', archived)] if v is not None}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

    def basic_read_company_object(self, companyId, properties=None, propertiesWithHistory=None, associations=None, archived=None, idProperty=None) -> dict[str, Any]:
        """
        Retrieves a specific company record by ID from the CRM system, optionally including additional properties, associations, and historical data, depending on the query parameters provided.

        Args:
            companyId (string): companyId
            properties (array): Optional array parameter to specify the properties of the company object to be returned in the response, allowing for customization of the retrieved data.
            propertiesWithHistory (array): Specifies a comma-separated list of property names for which both the current and historical values should be returned in the response; if a company does not have a value for a property, it will not appear in the response[2].
            associations (array): An optional array parameter specifying the types of associations to include in the response for a company object.
            archived (boolean): When set to true, the archived parameter includes archived company records in the response; defaults to false if omitted.
            idProperty (string): Optional string parameter specifying the property to use as the ID for the companies object.

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Basic
        """
        if companyId is None:
            raise ValueError("Missing required parameter 'companyId'.")
        url = f"{self.base_url}/crm/v3/objects/companies/{companyId}"
        query_params = {k: v for k, v in [('properties', properties), ('propertiesWithHistory', propertiesWithHistory), ('associations', associations), ('archived', archived), ('idProperty', idProperty)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def basic_archive_company(self, companyId) -> Any:
        """
        Deletes a company by its ID using the DELETE method, requiring the company ID as a path parameter and authorization through OAuth2 or private apps with the "crm.objects.companies.write" permission.

        Args:
            companyId (string): companyId

        Returns:
            Any: No content

        Tags:
            Basic
        """
        if companyId is None:
            raise ValueError("Missing required parameter 'companyId'.")
        url = f"{self.base_url}/crm/v3/objects/companies/{companyId}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

  

    def public_object_merge_companies_same_type(self, objectIdToMerge, primaryObjectId) -> dict[str, Any]:
        """
        Merges two or more company records into a single unified record using the CRM API, requiring a JSON payload and appropriate write permissions.

        Args:
            objectIdToMerge (string): objectIdToMerge
            primaryObjectId (string): primaryObjectId

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Public_Object
        """
        request_body_data = None
        request_body_data = {
            'objectIdToMerge': objectIdToMerge,
            'primaryObjectId': primaryObjectId,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/objects/companies/merge"
        query_params = {}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

    def batch_archive_companies_by_id_batch(self, inputs) -> Any:
        """
        Archives a batch of companies using the HubSpot CRM API, requiring a JSON body and returning a 204 status on successful operation.

        Args:
            inputs (array): inputs

        Returns:
            Any: No content

        Tags:
            Batch
        """
        request_body_data = None
        request_body_data = {
            'inputs': inputs,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/objects/companies/batch/archive"
        query_params = {}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

    def batch_create_companies_batch(self, inputs) -> dict[str, Any]:
        """
        Creates multiple company records in batch using the HubSpot CRM API and returns a status message, requiring authorization via OAuth2 or private apps.

        Args:
            inputs (array): inputs

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Batch
        """
        request_body_data = None
        request_body_data = {
            'inputs': inputs,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/objects/companies/batch/create"
        query_params = {}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

    def batch_update_companies_batch(self, inputs) -> dict[str, Any]:
        """
        Updates multiple company records in a single request using the HubSpot CRM API.

        Args:
            inputs (array): inputs

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Batch
        """
        request_body_data = None
        request_body_data = {
            'inputs': inputs,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/objects/companies/batch/update"
        query_params = {}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

    def gdpr_permanently_delete_contact_company(self, objectId, idProperty=None) -> Any:
        """
        Performs a GDPR-compliant deletion of a company record in the CRM, permanently removing the associated personal data.

        Args:
            objectId (string): objectId
            idProperty (string): idProperty

        Returns:
            Any: No content

        Tags:
            GDPR
        """
        request_body_data = None
        request_body_data = {
            'idProperty': idProperty,
            'objectId': objectId,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/objects/companies/gdpr-delete"
        query_params = {}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

    def basic_list_companies_page(self, limit=None, after=None, properties=None, propertiesWithHistory=None, associations=None, archived=None) -> dict[str, Any]:
        """
        Retrieves a list of company records from a CRM system, allowing for filtering by properties, associations, and archived status.

        Args:
            limit (integer): The maximum number of company records to return in the response, defaulting to 1 if not specified.
            after (string): The "after" query parameter is an optional string used for pagination to retrieve the next set of results after a specific cursor or record ID in the list of companies.
            properties (array): This optional query parameter allows you to specify an array of properties to be included in the response for companies retrieved via the GET operation.
            propertiesWithHistory (array): Specifies an array of company properties to include both current and historical data in the response.
            associations (array): An optional array parameter specifying the associations to include when retrieving company objects, allowing for the retrieval of related records.
            archived (boolean): Indicates whether to include archived companies in the response.

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Basic, important
        """
        url = f"{self.base_url}/crm/v3/objects/companies"
        query_params = {k: v for k, v in [('limit', limit), ('after', after), ('properties', properties), ('propertiesWithHistory', propertiesWithHistory), ('associations', associations), ('archived', archived)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def basic_create_company_object(self, associations, properties) -> dict[str, Any]:
        """
        Creates a new company record in the CRM system using the provided JSON data and returns a 201 status code upon successful creation.

        Args:
            associations (array): associations
            properties (object): No description provided. Example: "{'description': 'Onboarding service for data product', 'name': '1 year implementation consultation', 'price': '6000.00', 'hs_sku': '191902', 'hs_cost_of_goods_sold': '600.00', 'hs_recurring_billing_period': 'P24M', 'city': 'Cambridge', 'phone': '(877) 929-0687', 'state': 'Massachusetts', 'domain': 'biglytics.net', 'industry': 'Technology', 'amount': '1500.00', 'dealname': 'Custom data integrations', 'pipeline': 'default', 'closedate': '2019-12-07T16:50:06.678Z', 'dealstage': 'presentationscheduled', 'hubspot_owner_id': '910901', 'email': 'bcooper@biglytics.net', 'company': 'Biglytics', 'website': 'biglytics.net', 'lastname': 'Cooper', 'firstname': 'Bryan', 'subject': 'troubleshoot report', 'hs_pipeline': 'support_pipeline', 'hs_pipeline_stage': 'open', 'hs_ticket_priority': 'HIGH', 'quantity': '2', 'hs_product_id': '191902', 'recurringbillingfrequency': 'monthly'}".

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Basic
        """
        request_body_data = None
        request_body_data = {
            'associations': associations,
            'properties': properties,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/objects/companies"
        query_params = {}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

    def search_company_objects(self, limit, after, sorts, properties, filterGroups, query=None) -> dict[str, Any]:
        """
        Searches for and retrieves company records and their associated properties in the CRM based on specified criteria.

        Args:
            limit (integer): limit
            after (string): after
            sorts (array): sorts
            properties (array): properties
            filterGroups (array): filterGroups
            query (string): query

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Search
        """
        request_body_data = None
        request_body_data = {
            'query': query,
            'limit': limit,
            'after': after,
            'sorts': sorts,
            'properties': properties,
            'filterGroups': filterGroups,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/objects/companies/search"
        query_params = {}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

    def settings_get_calling_config(self, appId) -> dict[str, Any]:
        """
        Retrieves the calling settings for a specified application in HubSpot CRM using the provided app ID.

        Args:
            appId (string): appId

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Settings
        """
        if appId is None:
            raise ValueError("Missing required parameter 'appId'.")
        url = f"{self.base_url}/crm/v3/extensions/calling/{appId}/settings"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def settings_configure_calling_extension(self, appId, name, url, supportsCustomObjects=None, isReady=None, width=None, height=None) -> dict[str, Any]:
        """
        Configures calling settings for a specified application ID in the CRM using a POST request with a JSON body.

        Args:
            appId (string): appId
            name (string): The name of your calling service to display to users. Example: 'HubPhone'.
            url (string): The URL to your phone/calling UI, built with the [Calling SDK](#). Example: 'https://www.example.com/hubspot/iframe'.
            supportsCustomObjects (boolean): When true, you are indicating that your service is compatible with engagement v2 service and can be used with custom objects. Example: 'True'.
            isReady (boolean): When true, your service will appear as an option under the *Call* action in contact records of connected accounts. Example: 'True'.
            width (integer): The target width of the iframe that will contain your phone/calling UI. Example: '200'.
            height (integer): The target height of the iframe that will contain your phone/calling UI. Example: '350'.

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Settings
        """
        if appId is None:
            raise ValueError("Missing required parameter 'appId'.")
        request_body_data = None
        request_body_data = {
            'supportsCustomObjects': supportsCustomObjects,
            'isReady': isReady,
            'name': name,
            'width': width,
            'url': url,
            'height': height,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/extensions/calling/{appId}/settings"
        query_params = {}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

    def settings_delete_calling_extension(self, appId) -> Any:
        """
        Deletes the settings for a specified CRM application identified by `{appId}`, returning a successful response with no content if the operation is completed.

        Args:
            appId (string): appId

        Returns:
            Any: No content

        Tags:
            Settings
        """
        if appId is None:
            raise ValueError("Missing required parameter 'appId'.")
        url = f"{self.base_url}/crm/v3/extensions/calling/{appId}/settings"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def settings_update_calling_extension(self, appId, supportsCustomObjects=None, isReady=None, name=None, width=None, url=None, height=None) -> dict[str, Any]:
        """
        Updates specific settings for the calling extension of the specified application by applying partial modifications to its resource.

        Args:
            appId (string): appId
            supportsCustomObjects (boolean): When true, you are indicating that your service is compatible with engagement v2 service and can be used with custom objects.
            isReady (boolean): When true, your service will appear as an option under the *Call* action in contact records of connected accounts.
            name (string): The name of your calling service to display to users.
            width (integer): The target width of the iframe that will contain your phone/calling UI.
            url (string): The URL to your phone/calling UI, built with the [Calling SDK](#).
            height (integer): The target height of the iframe that will contain your phone/calling UI.

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Settings
        """
        if appId is None:
            raise ValueError("Missing required parameter 'appId'.")
        request_body_data = None
        request_body_data = {
            'supportsCustomObjects': supportsCustomObjects,
            'isReady': isReady,
            'name': name,
            'width': width,
            'url': url,
            'height': height,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/extensions/calling/{appId}/settings"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        response.raise_for_status()
        return response.json()

    def recording_settings_get_by_app_id(self, appId) -> dict[str, Any]:
        """
        Retrieves the recording settings for a calling extension with the specified `appId` in the HubSpot CRM.

        Args:
            appId (string): appId

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Recording_Settings
        """
        if appId is None:
            raise ValueError("Missing required parameter 'appId'.")
        url = f"{self.base_url}/crm/v3/extensions/calling/{appId}/settings/recording"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def recording_settings_set_call_recording(self, appId, urlToRetrieveAuthedRecording) -> dict[str, Any]:
        """
        Configures call recording settings for a specific application ID in the CRM using a POST request to update the recording settings.

        Args:
            appId (string): appId
            urlToRetrieveAuthedRecording (string): urlToRetrieveAuthedRecording

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Recording_Settings
        """
        if appId is None:
            raise ValueError("Missing required parameter 'appId'.")
        request_body_data = None
        request_body_data = {
            'urlToRetrieveAuthedRecording': urlToRetrieveAuthedRecording,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/extensions/calling/{appId}/settings/recording"
        query_params = {}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

    def recording_settings_update_calling_settings(self, appId, urlToRetrieveAuthedRecording=None) -> dict[str, Any]:
        """
        Modifies the recording settings for a specific CRM application using the provided JSON body.

        Args:
            appId (string): appId
            urlToRetrieveAuthedRecording (string): urlToRetrieveAuthedRecording

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Recording_Settings
        """
        if appId is None:
            raise ValueError("Missing required parameter 'appId'.")
        request_body_data = None
        request_body_data = {
            'urlToRetrieveAuthedRecording': urlToRetrieveAuthedRecording,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/extensions/calling/{appId}/settings/recording"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        response.raise_for_status()
        return response.json()

    def batch_read_quotes_by_property_values(self, propertiesWithHistory, inputs, properties, archived=None, idProperty=None) -> dict[str, Any]:
        """
        Reads a batch of quote objects by their internal IDs or unique property values, optionally including archived quotes, in a single POST request.

        Args:
            propertiesWithHistory (array): propertiesWithHistory
            inputs (array): inputs
            properties (array): properties
            archived (boolean): Indicates whether to include archived quotes in the batch read operation, defaults to false.
            idProperty (string): idProperty

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Batch
        """
        request_body_data = None
        request_body_data = {
            'propertiesWithHistory': propertiesWithHistory,
            'idProperty': idProperty,
            'inputs': inputs,
            'properties': properties,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/objects/quotes/batch/read"
        query_params = {k: v for k, v in [('archived', archived)] if v is not None}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

    def basic_read_quote_by_id(self, quoteId, properties=None, propertiesWithHistory=None, associations=None, archived=None, idProperty=None) -> dict[str, Any]:
        """
        Retrieves a specific sales quote by its ID, optionally including custom properties, property history, associations, and archived status, using the HubSpot CRM API.

        Args:
            quoteId (string): quoteId
            properties (array): Optional array of properties to include in the response when retrieving a quote object, allowing for customization of the data returned.
            propertiesWithHistory (array): A comma-separated list of properties for which to return both current values and their historical changes in the response.
            associations (array): The "associations" query parameter specifies an optional array of association types to include related objects linked to the quote in the response.
            archived (boolean): Indicates whether to include archived quotes in the response, with a default value of `false`.
            idProperty (string): Optional string parameter to specify the property used for identification in the quotes object.

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Basic
        """
        if quoteId is None:
            raise ValueError("Missing required parameter 'quoteId'.")
        url = f"{self.base_url}/crm/v3/objects/quotes/{quoteId}"
        query_params = {k: v for k, v in [('properties', properties), ('propertiesWithHistory', propertiesWithHistory), ('associations', associations), ('archived', archived), ('idProperty', idProperty)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def basic_archive_quote_object(self, quoteId) -> Any:
        """
        Deletes a sales quote with the specified ID using the HubSpot CRM API, requiring "crm.objects.quotes.write" permission.

        Args:
            quoteId (string): quoteId

        Returns:
            Any: No content

        Tags:
            Basic
        """
        if quoteId is None:
            raise ValueError("Missing required parameter 'quoteId'.")
        url = f"{self.base_url}/crm/v3/objects/quotes/{quoteId}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def basic_update_quote_object(self, quoteId, properties, idProperty=None) -> dict[str, Any]:
        """
        Updates a quote object with the specified ID in the CRM system using partial modifications, requiring a JSON body with the changes and returning a status message upon success.

        Args:
            quoteId (string): quoteId
            properties (object): No description provided. Example: "{'description': 'A new product description', 'name': '1 year implementation consultation', 'price': '6000.00', 'hs_cost_of_goods_sold': '700.00', 'property_date': '1572480000000', 'property_radio': 'option_1', 'property_number': '17', 'property_string': 'value', 'property_checkbox': 'false', 'property_dropdown': 'choice_b', 'property_multiple_checkboxes': 'chocolate;strawberry', 'quantity': '2', 'hs_product_id': '191902', 'recurringbillingfrequency': 'monthly', 'hs_recurring_billing_period': 'P24M'}".
            idProperty (string): The optional query parameter to specify a custom property name to use as the unique identifier for the quote object.

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Basic, important
        """
        if quoteId is None:
            raise ValueError("Missing required parameter 'quoteId'.")
        request_body_data = None
        request_body_data = {
            'properties': properties,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/objects/quotes/{quoteId}"
        query_params = {k: v for k, v in [('idProperty', idProperty)] if v is not None}
        response = self._patch(url, data=request_body_data, params=query_params)
        response.raise_for_status()
        return response.json()

    def public_object_merge_two_quotes_same_type(self, objectIdToMerge, primaryObjectId) -> dict[str, Any]:
        """
        Merges quote objects in a CRM system using the POST method, allowing for the integration of data from multiple quotes into a single unified quote.

        Args:
            objectIdToMerge (string): objectIdToMerge
            primaryObjectId (string): primaryObjectId

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Public_Object
        """
        request_body_data = None
        request_body_data = {
            'objectIdToMerge': objectIdToMerge,
            'primaryObjectId': primaryObjectId,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/objects/quotes/merge"
        query_params = {}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

    def batch_archive_quotes_by_id_batch(self, inputs) -> Any:
        """
        Archives a batch of quotes by sending a POST request to the "/crm/v3/objects/quotes/batch/archive" endpoint, requiring a JSON body and authentication via OAuth2 or private apps with the "crm.objects.quotes.write" permission.

        Args:
            inputs (array): inputs

        Returns:
            Any: No content

        Tags:
            Batch
        """
        request_body_data = None
        request_body_data = {
            'inputs': inputs,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/objects/quotes/batch/archive"
        query_params = {}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

    def batch_create_quotes_batch(self, inputs) -> dict[str, Any]:
        """
        Creates a batch of sales quotes using the HubSpot CRM API, requiring a JSON body and returning a status message upon successful creation.

        Args:
            inputs (array): inputs

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Batch
        """
        request_body_data = None
        request_body_data = {
            'inputs': inputs,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/objects/quotes/batch/create"
        query_params = {}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

    def batch_update_quotes_batch(self, inputs) -> dict[str, Any]:
        """
        Updates a batch of quote objects in the CRM system using a single POST request, returning a status code indicating success or partial failure.

        Args:
            inputs (array): inputs

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Batch
        """
        request_body_data = None
        request_body_data = {
            'inputs': inputs,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/objects/quotes/batch/update"
        query_params = {}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

    def gdpr_permanently_delete_contact_quotes(self, objectId, idProperty=None) -> Any:
        """
        Performs a GDPR-compliant deletion of a quote object in the CRM system, permanently removing the associated personal data.

        Args:
            objectId (string): objectId
            idProperty (string): idProperty

        Returns:
            Any: No content

        Tags:
            GDPR
        """
        request_body_data = None
        request_body_data = {
            'idProperty': idProperty,
            'objectId': objectId,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/objects/quotes/gdpr-delete"
        query_params = {}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

    def basic_list_quotes_page(self, limit=None, after=None, properties=None, propertiesWithHistory=None, associations=None, archived=None) -> dict[str, Any]:
        """
        Retrieves a list of quotes from the CRM, allowing for optional filtering by limit, after, properties, properties with history, associations, and archived status.

        Args:
            limit (integer): Specifies the maximum number of quote objects to return in the response, with a default value of 10.
            after (string): Cursor for pagination; the string value to retrieve results after a specific record in the result set.
            properties (array): Optional array parameter to specify which properties of the quote object to include in the response.
            propertiesWithHistory (array): A comma-separated list of properties to include historical data in the response for the quote object.
            associations (array): An array of associations to include in the response, specifying the related CRM objects or activities to retrieve alongside the quotes.
            archived (boolean): Indicates whether to include archived quotes in the response, defaults to false.

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Basic
        """
        url = f"{self.base_url}/crm/v3/objects/quotes"
        query_params = {k: v for k, v in [('limit', limit), ('after', after), ('properties', properties), ('propertiesWithHistory', propertiesWithHistory), ('associations', associations), ('archived', archived)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def basic_create_quote_object(self, associations, properties) -> dict[str, Any]:
        """
        Creates a new quote in HubSpot using the CRM API and returns a status message upon successful creation.

        Args:
            associations (array): associations
            properties (object): No description provided. Example: "{'description': 'Onboarding service for data product', 'name': '1 year implementation consultation', 'price': '6000.00', 'hs_sku': '191902', 'hs_cost_of_goods_sold': '600.00', 'hs_recurring_billing_period': 'P24M', 'city': 'Cambridge', 'phone': '(877) 929-0687', 'state': 'Massachusetts', 'domain': 'biglytics.net', 'industry': 'Technology', 'amount': '1500.00', 'dealname': 'Custom data integrations', 'pipeline': 'default', 'closedate': '2019-12-07T16:50:06.678Z', 'dealstage': 'presentationscheduled', 'hubspot_owner_id': '910901', 'email': 'bcooper@biglytics.net', 'company': 'Biglytics', 'website': 'biglytics.net', 'lastname': 'Cooper', 'firstname': 'Bryan', 'subject': 'troubleshoot report', 'hs_pipeline': 'support_pipeline', 'hs_pipeline_stage': 'open', 'hs_ticket_priority': 'HIGH', 'quantity': '2', 'hs_product_id': '191902', 'recurringbillingfrequency': 'monthly'}".

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Basic
        """
        request_body_data = None
        request_body_data = {
            'associations': associations,
            'properties': properties,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/objects/quotes"
        query_params = {}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

    def search_quotes_by_criteria(self, limit, after, sorts, properties, filterGroups, query=None) -> dict[str, Any]:
        """
        Searches for quotes in a CRM system using specified criteria and returns the results, requiring authentication via OAuth2 or private apps with read permissions for quotes.

        Args:
            limit (integer): limit
            after (string): after
            sorts (array): sorts
            properties (array): properties
            filterGroups (array): filterGroups
            query (string): query

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Search
        """
        request_body_data = None
        request_body_data = {
            'query': query,
            'limit': limit,
            'after': after,
            'sorts': sorts,
            'properties': properties,
            'filterGroups': filterGroups,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/objects/quotes/search"
        query_params = {}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

    def batch_read_deals_by_internal_id_or_property_values(self, propertiesWithHistory, inputs, properties, archived=None, idProperty=None) -> dict[str, Any]:
        """
        Reads a batch of deals from the CRM using the provided IDs and returns the specified properties, allowing for optional filtering by archived status.

        Args:
            propertiesWithHistory (array): propertiesWithHistory
            inputs (array): inputs
            properties (array): properties
            archived (boolean): Indicates whether to include archived deals in the batch read operation.
            idProperty (string): idProperty

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Batch
        """
        request_body_data = None
        request_body_data = {
            'propertiesWithHistory': propertiesWithHistory,
            'idProperty': idProperty,
            'inputs': inputs,
            'properties': properties,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/objects/deals/batch/read"
        query_params = {k: v for k, v in [('archived', archived)] if v is not None}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

    def basic_read_deal_by_id(self, dealId, properties=None, propertiesWithHistory=None, associations=None, archived=None, idProperty=None) -> dict[str, Any]:
        """
        Retrieves a deal by its ID and returns its details, supporting optional parameters for specifying properties, associations, and archived status.

        Args:
            dealId (string): dealId
            properties (array): Optional array of properties to include in the response for the specified deal.
            propertiesWithHistory (array): A comma-separated list of deal properties for which current and historical values should be returned in the response.
            associations (array): List of associations to include with the deal, such as contacts, companies, or products, allowing for retrieval of related objects.
            archived (boolean): Optional boolean parameter to indicate whether to include archived deals in the response.
            idProperty (string): Optional query parameter "idProperty" of type string, used to specify a custom property for filtering or retrieving specific data related to the deal.

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Basic
        """
        if dealId is None:
            raise ValueError("Missing required parameter 'dealId'.")
        url = f"{self.base_url}/crm/v3/objects/deals/{dealId}"
        query_params = {k: v for k, v in [('properties', properties), ('propertiesWithHistory', propertiesWithHistory), ('associations', associations), ('archived', archived), ('idProperty', idProperty)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def basic_archive_deal_object(self, dealId) -> Any:
        """
        Deletes a specific deal by its ID from the CRM system.

        Args:
            dealId (string): dealId

        Returns:
            Any: No content

        Tags:
            Basic
        """
        if dealId is None:
            raise ValueError("Missing required parameter 'dealId'.")
        url = f"{self.base_url}/crm/v3/objects/deals/{dealId}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def basic_update_deal_object(self, dealId, properties, idProperty=None) -> dict[str, Any]:
        """
        Updates an individual deal in the CRM by its record ID using the PATCH method.

        Args:
            dealId (string): dealId
            properties (object): No description provided. Example: "{'description': 'A new product description', 'name': '1 year implementation consultation', 'price': '6000.00', 'hs_cost_of_goods_sold': '700.00', 'property_date': '1572480000000', 'property_radio': 'option_1', 'property_number': '17', 'property_string': 'value', 'property_checkbox': 'false', 'property_dropdown': 'choice_b', 'property_multiple_checkboxes': 'chocolate;strawberry', 'quantity': '2', 'hs_product_id': '191902', 'recurringbillingfrequency': 'monthly', 'hs_recurring_billing_period': 'P24M'}".
            idProperty (string): Optional string parameter to specify the ID property for the deal object in the patch operation.

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Basic
        """
        if dealId is None:
            raise ValueError("Missing required parameter 'dealId'.")
        request_body_data = None
        request_body_data = {
            'properties': properties,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/objects/deals/{dealId}"
        query_params = {k: v for k, v in [('idProperty', idProperty)] if v is not None}
        response = self._patch(url, data=request_body_data, params=query_params)
        response.raise_for_status()
        return response.json()

    def public_object_merge_deals_same_type(self, objectIdToMerge, primaryObjectId) -> dict[str, Any]:
        """
        Merges two or more deal records into a single master deal record, consolidating data and deleting duplicates in the CRM system.

        Args:
            objectIdToMerge (string): objectIdToMerge
            primaryObjectId (string): primaryObjectId

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Public_Object
        """
        request_body_data = None
        request_body_data = {
            'objectIdToMerge': objectIdToMerge,
            'primaryObjectId': primaryObjectId,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/objects/deals/merge"
        query_params = {}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

    def batch_archive_deals_by_ids(self, inputs) -> Any:
        """
        Archives a batch of deal records in the CRM by their IDs using the POST method.

        Args:
            inputs (array): inputs

        Returns:
            Any: No content

        Tags:
            Batch
        """
        request_body_data = None
        request_body_data = {
            'inputs': inputs,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/objects/deals/batch/archive"
        query_params = {}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

    def batch_create_deals_object(self, inputs) -> dict[str, Any]:
        """
        Creates multiple deals in a CRM using a batch operation via the POST method, requiring a JSON body with deal data and appropriate permissions for writing deals.

        Args:
            inputs (array): inputs

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Batch
        """
        request_body_data = None
        request_body_data = {
            'inputs': inputs,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/objects/deals/batch/create"
        query_params = {}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

    def batch_update_deals_objects(self, inputs) -> dict[str, Any]:
        """
        Updates multiple deals in HubSpot CRM in a single operation using a POST request to "/crm/v3/objects/deals/batch/update", requiring a JSON body with deal identifiers and updates, and supports OAuth2 and private app authentication for the "crm.objects.deals.write" scope.

        Args:
            inputs (array): inputs

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Batch
        """
        request_body_data = None
        request_body_data = {
            'inputs': inputs,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/objects/deals/batch/update"
        query_params = {}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

    def gdpr_permanently_delete_deal(self, objectId, idProperty=None) -> Any:
        """
        Deletes a deal record in compliance with GDPR requirements using the provided JSON payload, requiring a valid OAuth2 or private app authentication with the necessary write permissions.

        Args:
            objectId (string): objectId
            idProperty (string): idProperty

        Returns:
            Any: No content

        Tags:
            GDPR
        """
        request_body_data = None
        request_body_data = {
            'idProperty': idProperty,
            'objectId': objectId,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/objects/deals/gdpr-delete"
        query_params = {}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

    def basic_get_deals_page(self, limit=None, after=None, properties=None, propertiesWithHistory=None, associations=None, archived=None) -> dict[str, Any]:
        """
        Retrieves a list of CRM deal objects from HubSpot using the GET method, allowing optional filtering by parameters such as limit, after, properties, propertiesWithHistory, associations, and archived status.

        Args:
            limit (integer): Specifies the maximum number of deals to return in the response, defaulting to 10.
            after (string): Cursor for pagination to retrieve results after a specific identifier in the list of deals.
            properties (array): Optional array of properties to include in the response for each deal, allowing for customization of the data retrieved.
            propertiesWithHistory (array): Optional array parameter specifying the deal properties for which historical values should be returned, reducing the maximum number of objects that can be read in a single request.
            associations (array): Optional array parameter that specifies the associations to include in the response for the retrieved deals.
            archived (boolean): Indicates whether to retrieve only archived deals, with true returning archived deals and false returning non-archived deals.

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Basic
        """
        url = f"{self.base_url}/crm/v3/objects/deals"
        query_params = {k: v for k, v in [('limit', limit), ('after', after), ('properties', properties), ('propertiesWithHistory', propertiesWithHistory), ('associations', associations), ('archived', archived)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def basic_create_deal_object(self, associations, properties) -> dict[str, Any]:
        """
        Creates a new deal object in the CRM using the HubSpot API, requiring a JSON payload and returning a status code indicating success.

        Args:
            associations (array): associations
            properties (object): No description provided. Example: "{'description': 'Onboarding service for data product', 'name': '1 year implementation consultation', 'price': '6000.00', 'hs_sku': '191902', 'hs_cost_of_goods_sold': '600.00', 'hs_recurring_billing_period': 'P24M', 'city': 'Cambridge', 'phone': '(877) 929-0687', 'state': 'Massachusetts', 'domain': 'biglytics.net', 'industry': 'Technology', 'amount': '1500.00', 'dealname': 'Custom data integrations', 'pipeline': 'default', 'closedate': '2019-12-07T16:50:06.678Z', 'dealstage': 'presentationscheduled', 'hubspot_owner_id': '910901', 'email': 'bcooper@biglytics.net', 'company': 'Biglytics', 'website': 'biglytics.net', 'lastname': 'Cooper', 'firstname': 'Bryan', 'subject': 'troubleshoot report', 'hs_pipeline': 'support_pipeline', 'hs_pipeline_stage': 'open', 'hs_ticket_priority': 'HIGH', 'quantity': '2', 'hs_product_id': '191902', 'recurringbillingfrequency': 'monthly'}".

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Basic
        """
        request_body_data = None
        request_body_data = {
            'associations': associations,
            'properties': properties,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/objects/deals"
        query_params = {}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

    def search_deals_by_criteria(self, limit, after, sorts, properties, filterGroups, query=None) -> dict[str, Any]:
        """
        Searches and retrieves deal records in the CRM using filters and criteria provided in the request body.

        Args:
            limit (integer): limit
            after (string): after
            sorts (array): sorts
            properties (array): properties
            filterGroups (array): filterGroups
            query (string): query

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Search
        """
        request_body_data = None
        request_body_data = {
            'query': query,
            'limit': limit,
            'after': after,
            'sorts': sorts,
            'properties': properties,
            'filterGroups': filterGroups,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/objects/deals/search"
        query_params = {}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

    def core_cancel_import(self, importId) -> dict[str, Any]:
        """
        Cancels an active import operation in a CRM system using the provided import ID.

        Args:
            importId (string): importId

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Core
        """
        if importId is None:
            raise ValueError("Missing required parameter 'importId'.")
        request_body_data = None
        url = f"{self.base_url}/crm/v3/imports/{importId}/cancel"
        query_params = {}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

    def core_get_import_record(self, importId) -> dict[str, Any]:
        """
        Retrieves the status and details of a specific CRM import operation identified by the import ID.

        Args:
            importId (string): importId

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Core
        """
        if importId is None:
            raise ValueError("Missing required parameter 'importId'.")
        url = f"{self.base_url}/crm/v3/imports/{importId}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def public_imports_get_error_details(self, importId, after=None, limit=None) -> dict[str, Any]:
        """
        Retrieves a list of errors associated with a specific CRM import operation, using the import ID, and allows filtering by optional parameters such as "after" and "limit".

        Args:
            importId (string): importId
            after (string): Used to specify a cursor for pagination, indicating the position after which to retrieve the next set of error records.
            limit (integer): The "limit" parameter specifies the maximum number of error records to return in the response for the specified import ID.

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Public_Imports
        """
        if importId is None:
            raise ValueError("Missing required parameter 'importId'.")
        url = f"{self.base_url}/crm/v3/imports/{importId}/errors"
        query_params = {k: v for k, v in [('after', after), ('limit', limit)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def core_get_existing_schema(self, objectType) -> dict[str, Any]:
        """
        Retrieves the schema definition for a specified CRM object type, including its properties and metadata.

        Args:
            objectType (string): objectType

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Core
        """
        if objectType is None:
            raise ValueError("Missing required parameter 'objectType'.")
        url = f"{self.base_url}/crm/v3/schemas/{objectType}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def core_delete_schema(self, objectType, archived=None) -> Any:
        """
        Deletes the specified CRM object schema by its type, optionally including archived versions, to remove its definition from the system.

        Args:
            objectType (string): objectType
            archived (boolean): A boolean query parameter indicating whether to operate on archived schemas, defaulting to false if not specified.

        Returns:
            Any: No content

        Tags:
            Core
        """
        if objectType is None:
            raise ValueError("Missing required parameter 'objectType'.")
        url = f"{self.base_url}/crm/v3/schemas/{objectType}"
        query_params = {k: v for k, v in [('archived', archived)] if v is not None}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def core_update_schema_object(self, objectType, description=None, secondaryDisplayProperties=None, requiredProperties=None, searchableProperties=None, primaryDisplayProperty=None, restorable=None, labels=None) -> dict[str, Any]:
        """
        Updates a custom CRM object schema in HubSpot using the PATCH method, allowing for partial modifications to the schema of a specified object type.

        Args:
            objectType (string): objectType
            description (string): description
            secondaryDisplayProperties (array): The names of secondary properties for this object. These will be displayed as secondary on the HubSpot record page for this object type.
            requiredProperties (array): The names of properties that should be **required** when creating an object of this type. Example: "['my_object_property']".
            searchableProperties (array): Names of properties that will be indexed for this object type in by HubSpot's product search. Example: "['my_object_property']".
            primaryDisplayProperty (string): The name of the primary property for this object. This will be displayed as primary on the HubSpot record page for this object type. Example: 'my_object_property'.
            restorable (boolean): restorable
            labels (object): Singular and plural labels for the object. Used in CRM display. Example: "{'singular': 'My object', 'plural': 'My objects'}".

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Core
        """
        if objectType is None:
            raise ValueError("Missing required parameter 'objectType'.")
        request_body_data = None
        request_body_data = {
            'description': description,
            'secondaryDisplayProperties': secondaryDisplayProperties,
            'requiredProperties': requiredProperties,
            'searchableProperties': searchableProperties,
            'primaryDisplayProperty': primaryDisplayProperty,
            'restorable': restorable,
            'labels': labels,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/schemas/{objectType}"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        response.raise_for_status()
        return response.json()

    def core_create_association(self, objectType, fromObjectTypeId, toObjectTypeId, name=None) -> dict[str, Any]:
        """
        Creates a new association definition for the specified CRM object type to define relationships between that object and others.

        Args:
            objectType (string): objectType
            fromObjectTypeId (string): ID of the primary object type to link from. Example: '2-123456'.
            toObjectTypeId (string): ID of the target object type ID to link to. Example: 'contact'.
            name (string): A unique name for this association. Example: 'my_object_to_contact'.

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Core
        """
        if objectType is None:
            raise ValueError("Missing required parameter 'objectType'.")
        request_body_data = None
        request_body_data = {
            'fromObjectTypeId': fromObjectTypeId,
            'name': name,
            'toObjectTypeId': toObjectTypeId,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/schemas/{objectType}/associations"
        query_params = {}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

    def public_object_schemas_purge_object_schema(self, objectType) -> Any:
        """
        Purges a schema for a specific object type in the CRM system using the DELETE method, requiring the objectType as a path parameter and a custom write permission.

        Args:
            objectType (string): objectType

        Returns:
            Any: No content

        Tags:
            Public_Object_Schemas
        """
        if objectType is None:
            raise ValueError("Missing required parameter 'objectType'.")
        url = f"{self.base_url}/crm/v3/schemas/{objectType}/purge"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def core_remove_association(self, objectType, associationIdentifier) -> Any:
        """
        Removes an association identified by the associationIdentifier from a CRM object schema of the specified objectType using the HubSpot API.

        Args:
            objectType (string): objectType
            associationIdentifier (string): associationIdentifier

        Returns:
            Any: No content

        Tags:
            Core
        """
        if objectType is None:
            raise ValueError("Missing required parameter 'objectType'.")
        if associationIdentifier is None:
            raise ValueError("Missing required parameter 'associationIdentifier'.")
        url = f"{self.base_url}/crm/v3/schemas/{objectType}/associations/{associationIdentifier}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def core_get_all_schemas(self, archived=None) -> dict[str, Any]:
        """
        Retrieves a list of custom object schemas in the CRM, optionally filtering by archived status, using either legacy private apps or OAuth2 credentials for authentication.

        Args:
            archived (boolean): Filter results by their archival status; when set to true, only archived schemas are returned, otherwise only active schemas (default is false).

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Core
        """
        url = f"{self.base_url}/crm/v3/schemas"
        query_params = {k: v for k, v in [('archived', archived)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def core_define_object_schema(self, requiredProperties, name, associatedObjects, properties, labels, description=None, secondaryDisplayProperties=None, searchableProperties=None, primaryDisplayProperty=None) -> dict[str, Any]:
        """
        Creates a new custom object schema in the CRM to define a new type of CRM record.

        Args:
            requiredProperties (array): The names of properties that should be **required** when creating an object of this type. Example: "['my_object_property']".
            name (string): A unique name for this object. For internal use only. Example: 'my_object'.
            associatedObjects (array): Associations defined for this object type. Example: "['CONTACT']".
            properties (array): Properties defined for this object type. Example: "[{'name': 'my_object_property', 'label': 'My object property', 'isPrimaryDisplayLabel': True}]".
            labels (object): Singular and plural labels for the object. Used in CRM display. Example: "{'singular': 'My object', 'plural': 'My objects'}".
            description (string): description
            secondaryDisplayProperties (array): The names of secondary properties for this object. These will be displayed as secondary on the HubSpot record page for this object type.
            searchableProperties (array): Names of properties that will be indexed for this object type in by HubSpot's product search.
            primaryDisplayProperty (string): The name of the primary property for this object. This will be displayed as primary on the HubSpot record page for this object type. Example: 'my_object_property'.

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Core
        """
        request_body_data = None
        request_body_data = {
            'description': description,
            'secondaryDisplayProperties': secondaryDisplayProperties,
            'requiredProperties': requiredProperties,
            'searchableProperties': searchableProperties,
            'primaryDisplayProperty': primaryDisplayProperty,
            'name': name,
            'associatedObjects': associatedObjects,
            'properties': properties,
            'labels': labels,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/schemas"
        query_params = {}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

    def batch_archive_properties(self, objectType, inputs) -> Any:
        """
        Archives a batch of properties for a specified object type in CRM using a POST request.

        Args:
            objectType (string): objectType
            inputs (array): inputs

        Returns:
            Any: No content

        Tags:
            Batch
        """
        if objectType is None:
            raise ValueError("Missing required parameter 'objectType'.")
        request_body_data = None
        request_body_data = {
            'inputs': inputs,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/properties/{objectType}/batch/archive"
        query_params = {}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

    def groups_read_property_group(self, objectType, groupName) -> dict[str, Any]:
        """
        Retrieves details of a specified property group for a given CRM object type.

        Args:
            objectType (string): objectType
            groupName (string): groupName

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Groups
        """
        if objectType is None:
            raise ValueError("Missing required parameter 'objectType'.")
        if groupName is None:
            raise ValueError("Missing required parameter 'groupName'.")
        url = f"{self.base_url}/crm/v3/properties/{objectType}/groups/{groupName}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def groups_archive_property_group(self, objectType, groupName) -> Any:
        """
        Deletes a property group identified by the given object type and group name from the CRM schema.

        Args:
            objectType (string): objectType
            groupName (string): groupName

        Returns:
            Any: No content

        Tags:
            Groups
        """
        if objectType is None:
            raise ValueError("Missing required parameter 'objectType'.")
        if groupName is None:
            raise ValueError("Missing required parameter 'groupName'.")
        url = f"{self.base_url}/crm/v3/properties/{objectType}/groups/{groupName}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def groups_update_property_group(self, objectType, groupName, displayOrder=None, label=None) -> dict[str, Any]:
        """
        Modifies the properties of a specified group in a CRM object type using the PATCH method, requiring authentication and a JSON request body to update the group's properties.

        Args:
            objectType (string): objectType
            groupName (string): groupName
            displayOrder (integer): Property groups are displayed in order starting with the lowest positive integer value. Values of -1 will cause the property group to be displayed after any positive values. Example: '-1'.
            label (string): A human-readable label that will be shown in HubSpot. Example: 'My Property Group'.

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Groups
        """
        if objectType is None:
            raise ValueError("Missing required parameter 'objectType'.")
        if groupName is None:
            raise ValueError("Missing required parameter 'groupName'.")
        request_body_data = None
        request_body_data = {
            'displayOrder': displayOrder,
            'label': label,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/properties/{objectType}/groups/{groupName}"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        response.raise_for_status()
        return response.json()

    def core_read_property(self, objectType, propertyName, archived=None, properties=None) -> dict[str, Any]:
        """
        Retrieves the details of a specific property for a given CRM object type, optionally including archived properties and additional specified fields.

        Args:
            objectType (string): objectType
            propertyName (string): propertyName
            archived (boolean): Optional boolean query parameter to filter results by archived status.
            properties (string): The "properties" query parameter specifies a comma-separated list of property names to include in the response for the given object type and property name, allowing you to customize which property details are returned.

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Core
        """
        if objectType is None:
            raise ValueError("Missing required parameter 'objectType'.")
        if propertyName is None:
            raise ValueError("Missing required parameter 'propertyName'.")
        url = f"{self.base_url}/crm/v3/properties/{objectType}/{propertyName}"
        query_params = {k: v for k, v in [('archived', archived), ('properties', properties)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def core_archive_property(self, objectType, propertyName) -> Any:
        """
        Deletes a specified property of a given object type in the CRM system.

        Args:
            objectType (string): objectType
            propertyName (string): propertyName

        Returns:
            Any: No content

        Tags:
            Core
        """
        if objectType is None:
            raise ValueError("Missing required parameter 'objectType'.")
        if propertyName is None:
            raise ValueError("Missing required parameter 'propertyName'.")
        url = f"{self.base_url}/crm/v3/properties/{objectType}/{propertyName}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def core_update_property_by_id(self, objectType, propertyName, description=None, groupName=None, hidden=None, options=None, displayOrder=None, calculationFormula=None, label=None, type=None, fieldType=None, formField=None) -> dict[str, Any]:
        """
        Updates the specified property of a given CRM object type by applying partial modifications using a JSON Patch request.

        Args:
            objectType (string): objectType
            propertyName (string): propertyName
            description (string): A description of the property that will be shown as help text in HubSpot.
            groupName (string): The name of the property group the property belongs to. Example: 'contactinformation'.
            hidden (boolean): If true, the property won't be visible and can't be used in HubSpot. Example: 'False'.
            options (array): A list of valid options for the property. Example: "[{'description': 'Choice number one', 'label': 'Option A', 'value': 'A', 'hidden': False, 'displayOrder': 1}, {'description': 'Choice number two', 'label': 'Option B', 'value': 'B', 'hidden': False, 'displayOrder': 2}]".
            displayOrder (integer): Properties are displayed in order starting with the lowest positive integer value. Values of -1 will cause the Property to be displayed after any positive values. Example: '2'.
            calculationFormula (string): Represents a formula that is used to compute a calculated property.
            label (string): A human-readable property label that will be shown in HubSpot. Example: 'My Contact Property'.
            type (string): The data type of the property. Example: 'enumeration'.
            fieldType (string): Controls how the property appears in HubSpot. Example: 'select'.
            formField (boolean): Whether or not the property can be used in a HubSpot form. Example: 'True'.

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Core
        """
        if objectType is None:
            raise ValueError("Missing required parameter 'objectType'.")
        if propertyName is None:
            raise ValueError("Missing required parameter 'propertyName'.")
        request_body_data = None
        request_body_data = {
            'description': description,
            'groupName': groupName,
            'hidden': hidden,
            'options': options,
            'displayOrder': displayOrder,
            'calculationFormula': calculationFormula,
            'label': label,
            'type': type,
            'fieldType': fieldType,
            'formField': formField,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/properties/{objectType}/{propertyName}"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        response.raise_for_status()
        return response.json()

    def batch_read_properties(self, objectType, archived, inputs) -> dict[str, Any]:
        """
        Performs a batch read operation on CRM properties for a specified object type using a POST request, returning the results in a batch format.

        Args:
            objectType (string): objectType
            archived (boolean): archived
            inputs (array): inputs

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Batch
        """
        if objectType is None:
            raise ValueError("Missing required parameter 'objectType'.")
        request_body_data = None
        request_body_data = {
            'archived': archived,
            'inputs': inputs,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/properties/{objectType}/batch/read"
        query_params = {}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

    def batch_properties_create_batch(self, objectType, inputs) -> dict[str, Any]:
        """
        Creates multiple properties in batches for a specified object type in the CRM using a POST request to the "/crm/v3/properties/{objectType}/batch/create" endpoint.

        Args:
            objectType (string): objectType
            inputs (array): inputs

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Batch
        """
        if objectType is None:
            raise ValueError("Missing required parameter 'objectType'.")
        request_body_data = None
        request_body_data = {
            'inputs': inputs,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/properties/{objectType}/batch/create"
        query_params = {}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

    def core_get_all_properties(self, objectType, archived=None, properties=None) -> dict[str, Any]:
        """
        Retrieves a list of properties for a specified CRM object type using the HubSpot API, allowing for optional filtering by archived status and specific properties.

        Args:
            objectType (string): objectType
            archived (boolean): A boolean query parameter indicating whether to include archived properties in the response.
            properties (string): Specifies a comma-separated list of property names to include in the response, allowing you to retrieve only certain properties for the object instead of all defaults.

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Core
        """
        if objectType is None:
            raise ValueError("Missing required parameter 'objectType'.")
        url = f"{self.base_url}/crm/v3/properties/{objectType}"
        query_params = {k: v for k, v in [('archived', archived), ('properties', properties)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def core_create_property(self, objectType, label, type, groupName, name, fieldType, description=None, hidden=None, displayOrder=None, formField=None, referencedObjectType=None, options=None, calculationFormula=None, hasUniqueValue=None, externalOptions=None) -> dict[str, Any]:
        """
        Creates a new custom property for a specified CRM object type.

        Args:
            objectType (string): objectType
            label (string): A human-readable property label that will be shown in HubSpot. Example: 'My Contact Property'.
            type (string): The data type of the property. Example: 'enumeration'.
            groupName (string): The name of the property group the property belongs to. Example: 'contactinformation'.
            name (string): The internal property name, which must be used when referencing the property via the API.
            fieldType (string): Controls how the property appears in HubSpot. Example: 'select'.
            description (string): A description of the property that will be shown as help text in HubSpot.
            hidden (boolean): If true, the property won't be visible and can't be used in HubSpot. Example: 'False'.
            displayOrder (integer): Properties are displayed in order starting with the lowest positive integer value. Values of -1 will cause the property to be displayed after any positive values. Example: '2'.
            formField (boolean): Whether or not the property can be used in a HubSpot form. Example: 'True'.
            referencedObjectType (string): Should be set to 'OWNER' when 'externalOptions' is true, which causes the property to dynamically pull option values from the current HubSpot users.
            options (array): A list of valid options for the property. This field is required for enumerated properties. Example: "[{'description': 'Choice number one', 'label': 'Option A', 'value': 'A', 'hidden': False, 'displayOrder': 1}, {'description': 'Choice number two', 'label': 'Option B', 'value': 'B', 'hidden': False, 'displayOrder': 2}]".
            calculationFormula (string): Represents a formula that is used to compute a calculated property.
            hasUniqueValue (boolean): Whether or not the property's value must be unique. Once set, this can't be changed. Example: 'False'.
            externalOptions (boolean): Applicable only for 'enumeration' type properties.  Should be set to true in conjunction with a 'referencedObjectType' of 'OWNER'.  Otherwise false.

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Core
        """
        if objectType is None:
            raise ValueError("Missing required parameter 'objectType'.")
        request_body_data = None
        request_body_data = {
            'description': description,
            'hidden': hidden,
            'displayOrder': displayOrder,
            'label': label,
            'type': type,
            'formField': formField,
            'groupName': groupName,
            'referencedObjectType': referencedObjectType,
            'name': name,
            'options': options,
            'calculationFormula': calculationFormula,
            'hasUniqueValue': hasUniqueValue,
            'fieldType': fieldType,
            'externalOptions': externalOptions,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/properties/{objectType}"
        query_params = {}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

    def groups_read_all_property(self, objectType) -> dict[str, Any]:
        """
        Retrieves a list of groups for a specified object type in the CRM using the "GET" method at the path "/crm/v3/properties/{objectType}/groups".

        Args:
            objectType (string): objectType

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Groups
        """
        if objectType is None:
            raise ValueError("Missing required parameter 'objectType'.")
        url = f"{self.base_url}/crm/v3/properties/{objectType}/groups"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def groups_create_copy(self, objectType, name, label, displayOrder=None) -> dict[str, Any]:
        """
        Creates a new property group for the specified CRM object type to organize related properties within HubSpot records.

        Args:
            objectType (string): objectType
            name (string): The internal property group name, which must be used when referencing the property group via the API. Example: 'mypropertygroup'.
            label (string): A human-readable label that will be shown in HubSpot. Example: 'My Property Group'.
            displayOrder (integer): Property groups are displayed in order starting with the lowest positive integer value. Values of -1 will cause the property group to be displayed after any positive values. Example: '-1'.

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Groups
        """
        if objectType is None:
            raise ValueError("Missing required parameter 'objectType'.")
        request_body_data = None
        request_body_data = {
            'name': name,
            'displayOrder': displayOrder,
            'label': label,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/properties/{objectType}/groups"
        query_params = {}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

    def owners_get_by_id(self, ownerId, idProperty=None, archived=None) -> dict[str, Any]:
        """
        Retrieves detailed information about a specific CRM owner by their ID using the HubSpot API.

        Args:
            ownerId (string): ownerId
            idProperty (string): Specifies the property to use for identifying owners, accepting values 'id' or 'userId', with 'id' as the default.
            archived (boolean): Whether to include archived owners in the response; defaults to false.

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Owners
        """
        if ownerId is None:
            raise ValueError("Missing required parameter 'ownerId'.")
        url = f"{self.base_url}/crm/v3/owners/{ownerId}"
        query_params = {k: v for k, v in [('idProperty', idProperty), ('archived', archived)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def events_create_multiple_batch(self, inputs) -> dict[str, Any]:
        """
        Creates multiple timeline events in a batch using the provided event templates and returns a response with the created events.

        Args:
            inputs (array): A collection of timeline events we want to create. Example: '[{\'email\': \'art3mis-pup@petspot.com\', \'tokens\': {\'petAge\': 3, \'petName\': \'Art3mis\', \'petColor\': \'black\'}, \'extraData\': {\'questions\': [{\'answer\': \'Bark!\', \'question\': "Who\'s a good girl?"}, {\'answer\': \'Woof!\', \'question\': \'Do you wanna go on a walk?\'}]}, \'timelineIFrame\': {\'url\': \'https://my.petspot.com/pets/Art3mis\', \'width\': 600, \'height\': 400, \'linkLabel\': \'View Art3mis\', \'headerLabel\': \'Art3mis dog\'}, \'eventTemplateId\': \'1001298\'}, {\'email\': \'pocket-tiger@petspot.com\', \'tokens\': {\'petAge\': 3, \'petName\': \'Pocket\', \'petColor\': \'yellow\'}, \'extraData\': {\'questions\': [{\'answer\': \'Purr...\', \'question\': "Who\'s a good kitty?"}, {\'answer\': \'Meow!\', \'question\': \'Will you stop playing with that?\'}]}, \'timelineIFrame\': {\'url\': \'https://my.petspot.com/pets/Pocket\', \'width\': 600, \'height\': 400, \'linkLabel\': \'View Pocket\', \'headerLabel\': \'Pocket Tiger\'}, \'eventTemplateId\': \'1001298\'}]'.

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Events
        """
        request_body_data = None
        request_body_data = {
            'inputs': inputs,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/timeline/events/batch/create"
        query_params = {}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

    def templates_get_specific_event_template(self, appId, eventTemplateId) -> dict[str, Any]:
        """
        Retrieves a specific event template by its ID for an application in HubSpot CRM, using the provided app ID and event template ID.

        Args:
            appId (string): appId
            eventTemplateId (string): eventTemplateId

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Templates
        """
        if appId is None:
            raise ValueError("Missing required parameter 'appId'.")
        if eventTemplateId is None:
            raise ValueError("Missing required parameter 'eventTemplateId'.")
        url = f"{self.base_url}/crm/v3/timeline/{appId}/event-templates/{eventTemplateId}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def templates_update_event_template(self, appId, eventTemplateId, name, tokens, id, detailTemplate=None, headerTemplate=None) -> dict[str, Any]:
        """
        Updates an existing event template in the HubSpot CRM timeline for a specific app, using the provided event template ID and app ID, and returns a status message.

        Args:
            appId (string): appId
            eventTemplateId (string): eventTemplateId
            name (string): The template name. Example: 'PetSpot Registration'.
            tokens (array): A collection of tokens that can be used as custom properties on the event and to create fully fledged CRM objects. Example: "[{'name': 'petName', 'type': 'string', 'label': 'Pet Name', 'objectPropertyName': 'firstname'}, {'name': 'petAge', 'type': 'number', 'label': 'Pet Age'}, {'name': 'petColor', 'type': 'enumeration', 'label': 'Pet Color', 'options': [{'label': 'White', 'value': 'white'}, {'label': 'Black', 'value': 'black'}, {'label': 'Brown', 'value': 'brown'}, {'label': 'Yellow', 'value': 'yellow'}, {'label': 'Other', 'value': 'other'}]}]".
            id (string): The template ID. Example: '1001298'.
            detailTemplate (string): This uses Markdown syntax with Handlebars and event-specific data to render HTML on a timeline when you expand the details. Example: 'Registration occurred at {{#formatDate timestamp}}{{/formatDate}}\n\n#### Questions\n{{#each extraData.questions}}\n  **{{question}}**: {{answer}}\n{{/each}}\n\nEDIT'.
            headerTemplate (string): This uses Markdown syntax with Handlebars and event-specific data to render HTML on a timeline as a header. Example: 'Registered for [{{petName}}](https://my.petspot.com/pets/{{petName}})'.

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Templates
        """
        if appId is None:
            raise ValueError("Missing required parameter 'appId'.")
        if eventTemplateId is None:
            raise ValueError("Missing required parameter 'eventTemplateId'.")
        request_body_data = None
        request_body_data = {
            'detailTemplate': detailTemplate,
            'name': name,
            'tokens': tokens,
            'id': id,
            'headerTemplate': headerTemplate,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/timeline/{appId}/event-templates/{eventTemplateId}"
        query_params = {}
        response = self._put(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

    def templates_delete_event_template(self, appId, eventTemplateId) -> Any:
        """
        Deletes an event template with the specified `eventTemplateId` associated with the application identified by `appId` in a CRM system, returning a successful response with no content upon completion.

        Args:
            appId (string): appId
            eventTemplateId (string): eventTemplateId

        Returns:
            Any: No content

        Tags:
            Templates
        """
        if appId is None:
            raise ValueError("Missing required parameter 'appId'.")
        if eventTemplateId is None:
            raise ValueError("Missing required parameter 'eventTemplateId'.")
        url = f"{self.base_url}/crm/v3/timeline/{appId}/event-templates/{eventTemplateId}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def events_create_single_event(self, eventTemplateId, tokens, extraData=None, timelineIFrame=None, domain=None, id=None, utk=None, email=None, objectId=None, timestamp=None) -> dict[str, Any]:
        """
        Creates a new timeline event in a CRM record based on an event template, adding custom event information to the timeline of a contact, company, or deal.

        Args:
            eventTemplateId (string): The event template ID. Example: '1001298'.
            tokens (object): A collection of token keys and values associated with the template tokens. Example: "{'petAge': 3, 'petName': 'Art3mis', 'petColor': 'black'}".
            extraData (object): Additional event-specific data that can be interpreted by the template's markdown. Example: '{\'questions\': [{\'answer\': \'Bark!\', \'question\': "Who\'s a good girl?"}, {\'answer\': \'Woof!\', \'question\': \'Do you wanna go on a walk?\'}]}'.
            timelineIFrame (object): timelineIFrame Example: "{'linkLabel': 'View Art3mis', 'headerLabel': 'Art3mis dog', 'url': 'https://my.petspot.com/pets/Art3mis', 'width': 600, 'height': 400}".
            domain (string): The event domain (often paired with utk).
            id (string): Identifier for the event. This is optional, and we recommend you do not pass this in. We will create one for you if you omit this. You can also use `{{uuid}}` anywhere in the ID to generate a unique string, guaranteeing uniqueness.
            utk (string): Use the `utk` parameter to associate an event with a contact by `usertoken`. This is recommended if you don't know a user's email, but have an identifying user token in your cookie.
            email (string): The email address used for contact-specific events. This can be used to identify existing contacts, create new ones, or change the email for an existing contact (if paired with the `objectId`). Example: 'art3mis-pup@petspot.com'.
            objectId (string): The CRM object identifier. This is required for every event other than contacts (where utk or email can be used).
            timestamp (string): The time the event occurred. If not passed in, the curren time will be assumed. This is used to determine where an event is shown on a CRM object's timeline.

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Events
        """
        request_body_data = None
        request_body_data = {
            'eventTemplateId': eventTemplateId,
            'extraData': extraData,
            'timelineIFrame': timelineIFrame,
            'domain': domain,
            'tokens': tokens,
            'id': id,
            'utk': utk,
            'email': email,
            'objectId': objectId,
            'timestamp': timestamp,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/timeline/events"
        query_params = {}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

    def tokens_add_to_event_template(self, appId, eventTemplateId, name, label, type, createdAt=None, options=None, objectPropertyName=None, updatedAt=None) -> dict[str, Any]:
        """
        Creates a new token for an event template in the HubSpot CRM timeline using the provided JSON data.

        Args:
            appId (string): appId
            eventTemplateId (string): eventTemplateId
            name (string): The name of the token referenced in the templates. This must be unique for the specific template. It may only contain alphanumeric characters, periods, dashes, or underscores (. - _). Example: 'petType'.
            label (string): Used for list segmentation and reporting. Example: 'Pet Type'.
            type (string): The data type of the token. You can currently choose from [string, number, date, enumeration]. Example: 'enumeration'.
            createdAt (string): The date and time that the Event Template Token was created, as an ISO 8601 timestamp. Will be null if the template was created before Feb 18th, 2020.
            options (array): If type is `enumeration`, we should have a list of options to choose from. Example: "[{'label': 'Dog', 'value': 'dog'}, {'label': 'Cat', 'value': 'cat'}]".
            objectPropertyName (string): The name of the CRM object property. This will populate the CRM object property associated with the event. With enough of these, you can fully build CRM objects via the Timeline API. Example: 'customPropertyPetType'.
            updatedAt (string): The date and time that the Event Template Token was last updated, as an ISO 8601 timestamp. Will be null if the template was created before Feb 18th, 2020.

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Tokens
        """
        if appId is None:
            raise ValueError("Missing required parameter 'appId'.")
        if eventTemplateId is None:
            raise ValueError("Missing required parameter 'eventTemplateId'.")
        request_body_data = None
        request_body_data = {
            'createdAt': createdAt,
            'options': options,
            'name': name,
            'label': label,
            'objectPropertyName': objectPropertyName,
            'type': type,
            'updatedAt': updatedAt,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/timeline/{appId}/event-templates/{eventTemplateId}/tokens"
        query_params = {}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

    def tokens_update_existing_token_on_event_template(self, appId, eventTemplateId, tokenName, label, options=None, objectPropertyName=None) -> dict[str, Any]:
        """
        Updates a specific token in an event template within a CRM timeline using the provided JSON data.

        Args:
            appId (string): appId
            eventTemplateId (string): eventTemplateId
            tokenName (string): tokenName
            label (string): Used for list segmentation and reporting. Example: 'petType edit'.
            options (array): If type is `enumeration`, we should have a list of options to choose from. Example: "[{'label': 'Dog', 'value': 'dog'}, {'label': 'Cat', 'value': 'cat'}, {'label': 'Bird', 'value': 'bird'}]".
            objectPropertyName (string): The name of the CRM object property. This will populate the CRM object property associated with the event. With enough of these, you can fully build CRM objects via the Timeline API.

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Tokens
        """
        if appId is None:
            raise ValueError("Missing required parameter 'appId'.")
        if eventTemplateId is None:
            raise ValueError("Missing required parameter 'eventTemplateId'.")
        if tokenName is None:
            raise ValueError("Missing required parameter 'tokenName'.")
        request_body_data = None
        request_body_data = {
            'options': options,
            'label': label,
            'objectPropertyName': objectPropertyName,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/timeline/{appId}/event-templates/{eventTemplateId}/tokens/{tokenName}"
        query_params = {}
        response = self._put(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

    def tokens_remove_from_template(self, appId, eventTemplateId, tokenName) -> Any:
        """
        Deletes a token by the specified name from an event template in the CRM timeline for a given application ID.

        Args:
            appId (string): appId
            eventTemplateId (string): eventTemplateId
            tokenName (string): tokenName

        Returns:
            Any: No content

        Tags:
            Tokens
        """
        if appId is None:
            raise ValueError("Missing required parameter 'appId'.")
        if eventTemplateId is None:
            raise ValueError("Missing required parameter 'eventTemplateId'.")
        if tokenName is None:
            raise ValueError("Missing required parameter 'tokenName'.")
        url = f"{self.base_url}/crm/v3/timeline/{appId}/event-templates/{eventTemplateId}/tokens/{tokenName}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def events_render_detail_template(self, eventTemplateId, eventId) -> dict[str, Any]:
        """
        Retrieves detailed information for a specific timeline event identified by its event template ID and event ID in the CRM.

        Args:
            eventTemplateId (string): eventTemplateId
            eventId (string): eventId

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Events
        """
        if eventTemplateId is None:
            raise ValueError("Missing required parameter 'eventTemplateId'.")
        if eventId is None:
            raise ValueError("Missing required parameter 'eventId'.")
        url = f"{self.base_url}/crm/v3/timeline/events/{eventTemplateId}/{eventId}/detail"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def events_get_event_by_id(self, eventTemplateId, eventId) -> dict[str, Any]:
        """
        Retrieves a specific timeline event by its event template ID and event ID, returning detailed information about that event in the CRM.

        Args:
            eventTemplateId (string): eventTemplateId
            eventId (string): eventId

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Events
        """
        if eventTemplateId is None:
            raise ValueError("Missing required parameter 'eventTemplateId'.")
        if eventId is None:
            raise ValueError("Missing required parameter 'eventId'.")
        url = f"{self.base_url}/crm/v3/timeline/events/{eventTemplateId}/{eventId}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def templates_list_event_templates(self, appId) -> dict[str, Any]:
        """
        Retrieves a list of event templates for a specified app ID in the HubSpot CRM API.

        Args:
            appId (string): appId

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Templates
        """
        if appId is None:
            raise ValueError("Missing required parameter 'appId'.")
        url = f"{self.base_url}/crm/v3/timeline/{appId}/event-templates"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def templates_create_event_template_for_app(self, appId, name, tokens, objectType, detailTemplate=None, headerTemplate=None) -> dict[str, Any]:
        """
        Creates a new event template for a specified application ID in HubSpot's CRM timeline using the provided JSON payload.

        Args:
            appId (string): appId
            name (string): The template name. Example: 'PetSpot Registration'.
            tokens (array): A collection of tokens that can be used as custom properties on the event and to create fully fledged CRM objects. Example: "[{'name': 'petName', 'type': 'string', 'label': 'Pet Name'}, {'name': 'petAge', 'type': 'number', 'label': 'Pet Age'}, {'name': 'petColor', 'type': 'enumeration', 'label': 'Pet Color', 'options': [{'label': 'White', 'value': 'white'}, {'label': 'Black', 'value': 'black'}, {'label': 'Brown', 'value': 'brown'}, {'label': 'Other', 'value': 'other'}]}]".
            objectType (string): The type of CRM object this template is for. [Contacts, companies, tickets, and deals] are supported. Example: 'contacts'.
            detailTemplate (string): This uses Markdown syntax with Handlebars and event-specific data to render HTML on a timeline when you expand the details. Example: 'Registration occurred at {{#formatDate timestamp}}{{/formatDate}}\n\n#### Questions\n{{#each extraData.questions}}\n  **{{question}}**: {{answer}}\n{{/each}}'.
            headerTemplate (string): This uses Markdown syntax with Handlebars and event-specific data to render HTML on a timeline as a header. Example: 'Registered for [{{petName}}](https://my.petspot.com/pets/{{petName}})'.

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Templates
        """
        if appId is None:
            raise ValueError("Missing required parameter 'appId'.")
        request_body_data = None
        request_body_data = {
            'detailTemplate': detailTemplate,
            'name': name,
            'tokens': tokens,
            'headerTemplate': headerTemplate,
            'objectType': objectType,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/timeline/{appId}/event-templates"
        query_params = {}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

    def events_rendering_html(self, eventTemplateId, eventId, detail=None) -> Any:
        """
        Retrieves and renders a specific timeline event from a CRM object using an event template and event ID, allowing for optional detailed rendering.

        Args:
            eventTemplateId (string): eventTemplateId
            eventId (string): eventId
            detail (boolean): Specifies whether the response should include additional detailed information for the timeline event.

        Returns:
            Any: successful operation

        Tags:
            Events
        """
        if eventTemplateId is None:
            raise ValueError("Missing required parameter 'eventTemplateId'.")
        if eventId is None:
            raise ValueError("Missing required parameter 'eventId'.")
        url = f"{self.base_url}/crm/v3/timeline/events/{eventTemplateId}/{eventId}/render"
        query_params = {k: v for k, v in [('detail', detail)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def batch_read_contacts_by_properties(self, propertiesWithHistory, inputs, properties, archived=None, idProperty=None) -> dict[str, Any]:
        """
        Retrieves a batch of contacts from the CRM using the provided identifiers and properties, supporting optional filtering by archived status.

        Args:
            propertiesWithHistory (array): propertiesWithHistory
            inputs (array): inputs
            properties (array): properties
            archived (boolean): A boolean query parameter indicating whether to include archived contacts in the batch read operation, defaulting to false.
            idProperty (string): idProperty

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Batch
        """
        request_body_data = None
        request_body_data = {
            'propertiesWithHistory': propertiesWithHistory,
            'idProperty': idProperty,
            'inputs': inputs,
            'properties': properties,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/objects/contacts/batch/read"
        query_params = {k: v for k, v in [('archived', archived)] if v is not None}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

    def basic_read_contact_by_id(self, contactId, properties=None, propertiesWithHistory=None, associations=None, archived=None) -> dict[str, Any]:
        """
        Retrieves a contact by ID from the CRM, allowing for optional filtering by properties, properties with history, associations, and archived status.

        Args:
            contactId (string): contactId
            properties (array): Array of contact property names to include in the response, allowing customization of which contact fields are returned.
            propertiesWithHistory (array): A comma-separated list of contact properties for which to return both current values and their full change history in the response.
            associations (array): Array of association types to include related object associations in the response.
            archived (boolean): Optional boolean parameter to include or exclude archived contacts; defaults to false.

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Basic
        """
        if contactId is None:
            raise ValueError("Missing required parameter 'contactId'.")
        url = f"{self.base_url}/crm/v3/objects/contacts/{contactId}"
        query_params = {k: v for k, v in [('properties', properties), ('propertiesWithHistory', propertiesWithHistory), ('associations', associations), ('archived', archived)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def basic_archive_contact(self, contactId) -> Any:
        """
        Deletes a contact by its ID from the CRM system, permanently removing all associated content in compliance with GDPR, and requires the "crm.objects.contacts.write" permission.

        Args:
            contactId (string): contactId

        Returns:
            Any: No content

        Tags:
            Basic
        """
        if contactId is None:
            raise ValueError("Missing required parameter 'contactId'.")
        url = f"{self.base_url}/crm/v3/objects/contacts/{contactId}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def basic_update_contact_object(self, contactId, properties) -> dict[str, Any]:
        """
        Updates an individual contact by its record ID using a PATCH request to the "/crm/v3/objects/contacts/{contactId}" endpoint, requiring a JSON body with the fields to be updated.

        Args:
            contactId (string): contactId
            properties (object): No description provided. Example: "{'description': 'A new product description', 'name': '1 year implementation consultation', 'price': '6000.00', 'hs_cost_of_goods_sold': '700.00', 'property_date': '1572480000000', 'property_radio': 'option_1', 'property_number': '17', 'property_string': 'value', 'property_checkbox': 'false', 'property_dropdown': 'choice_b', 'property_multiple_checkboxes': 'chocolate;strawberry', 'quantity': '2', 'hs_product_id': '191902', 'recurringbillingfrequency': 'monthly', 'hs_recurring_billing_period': 'P24M'}".

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Basic
        """
        if contactId is None:
            raise ValueError("Missing required parameter 'contactId'.")
        request_body_data = None
        request_body_data = {
            'properties': properties,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/objects/contacts/{contactId}"
        query_params = {}
        response = self._patch(url, data=request_body_data, params=query_params)
        response.raise_for_status()
        return response.json()

    def public_object_merge_contacts_same_type(self, objectIdToMerge, primaryObjectId) -> dict[str, Any]:
        """
        Merges two or more duplicate contact records into a single record in the CRM system, retaining the most relevant data while discarding redundant information.

        Args:
            objectIdToMerge (string): objectIdToMerge
            primaryObjectId (string): primaryObjectId

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Public_Object
        """
        request_body_data = None
        request_body_data = {
            'objectIdToMerge': objectIdToMerge,
            'primaryObjectId': primaryObjectId,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/objects/contacts/merge"
        query_params = {}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

    def batch_archive_contacts_by_id_batch(self, inputs) -> Any:
        """
        Archives a batch of contacts by ID using the HubSpot CRM API, returning a "204 No Content" response upon success.

        Args:
            inputs (array): inputs

        Returns:
            Any: No content

        Tags:
            Batch
        """
        request_body_data = None
        request_body_data = {
            'inputs': inputs,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/objects/contacts/batch/archive"
        query_params = {}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

    def batch_create_contacts(self, inputs) -> dict[str, Any]:
        """
        Creates a batch of contacts in HubSpot using the CRM API, requiring a JSON payload and OAuth2 or private app authentication.

        Args:
            inputs (array): inputs

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Batch
        """
        request_body_data = None
        request_body_data = {
            'inputs': inputs,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/objects/contacts/batch/create"
        query_params = {}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

    def batch_update_contacts_batch(self, inputs) -> dict[str, Any]:
        """
        Updates multiple contact records in a single request by providing their IDs or unique property values, overwriting specified properties in batch.

        Args:
            inputs (array): inputs

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Batch
        """
        request_body_data = None
        request_body_data = {
            'inputs': inputs,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/objects/contacts/batch/update"
        query_params = {}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

    def gdpr_permanently_delete_contacts(self, objectId, idProperty=None) -> Any:
        """
        Permanently deletes a contact and all associated data from the CRM to comply with GDPR requirements.

        Args:
            objectId (string): objectId
            idProperty (string): idProperty

        Returns:
            Any: No content

        Tags:
            GDPR
        """
        request_body_data = None
        request_body_data = {
            'idProperty': idProperty,
            'objectId': objectId,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/objects/contacts/gdpr-delete"
        query_params = {}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

    def basic_list_contacts_page(self, limit=None, after=None, properties=None, propertiesWithHistory=None, associations=None, archived=None) -> dict[str, Any]:
        """
        Retrieves a list of contacts from a CRM system, allowing for optional filtering by limit, pagination, specific properties, property history, associations, and archived status.

        Args:
            limit (integer): Specifies the maximum number of contact records to return in the response, with a default value of 5.
            after (string): An optional string parameter used for pagination, specifying the cursor or identifier to retrieve results after a specific point, enabling the retrieval of subsequent pages of data in a large dataset.
            properties (array): Optional array parameter specifying the properties to include in the response for the contacts object.
            propertiesWithHistory (array): Optional array parameter to specify contact properties for which both current and historical values should be returned in the response.
            associations (array): An optional array of associations to retrieve for the contact object, allowing you to fetch related records or activities.
            archived (boolean): Include this boolean query parameter to specify whether to return only archived contacts; defaults to false.

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Basic
        """
        url = f"{self.base_url}/crm/v3/objects/contacts"
        query_params = {k: v for k, v in [('limit', limit), ('after', after), ('properties', properties), ('propertiesWithHistory', propertiesWithHistory), ('associations', associations), ('archived', archived)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def basic_create_contact_object(self, associations, properties) -> dict[str, Any]:
        """
        Creates a new contact in the CRM system using the provided JSON data and returns a successful creation response.

        Args:
            associations (array): associations
            properties (object): No description provided. Example: "{'description': 'Onboarding service for data product', 'name': '1 year implementation consultation', 'price': '6000.00', 'hs_sku': '191902', 'hs_cost_of_goods_sold': '600.00', 'hs_recurring_billing_period': 'P24M', 'city': 'Cambridge', 'phone': '(877) 929-0687', 'state': 'Massachusetts', 'domain': 'biglytics.net', 'industry': 'Technology', 'amount': '1500.00', 'dealname': 'Custom data integrations', 'pipeline': 'default', 'closedate': '2019-12-07T16:50:06.678Z', 'dealstage': 'presentationscheduled', 'hubspot_owner_id': '910901', 'email': 'bcooper@biglytics.net', 'company': 'Biglytics', 'website': 'biglytics.net', 'lastname': 'Cooper', 'firstname': 'Bryan', 'subject': 'troubleshoot report', 'hs_pipeline': 'support_pipeline', 'hs_pipeline_stage': 'open', 'hs_ticket_priority': 'HIGH', 'quantity': '2', 'hs_product_id': '191902', 'recurringbillingfrequency': 'monthly'}".

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Basic
        """
        request_body_data = None
        request_body_data = {
            'associations': associations,
            'properties': properties,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/objects/contacts"
        query_params = {}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

    def search_contacts_by_criteria(self, limit, after, sorts, properties, filterGroups, query=None) -> dict[str, Any]:
        """
        Searches for contact records in the CRM system based on specified criteria and returns matching contacts.

        Args:
            limit (integer): limit
            after (string): after
            sorts (array): sorts
            properties (array): properties
            filterGroups (array): filterGroups
            query (string): query

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Search
        """
        request_body_data = None
        request_body_data = {
            'query': query,
            'limit': limit,
            'after': after,
            'sorts': sorts,
            'properties': properties,
            'filterGroups': filterGroups,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/objects/contacts/search"
        query_params = {}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

    def batch_read_feedback_submissions(self, propertiesWithHistory, inputs, properties, archived=None, idProperty=None) -> dict[str, Any]:
        """
        Reads a batch of feedback submissions by sending a POST request, allowing for optional filtering by archived status, and returns the relevant data in JSON format.

        Args:
            propertiesWithHistory (array): propertiesWithHistory
            inputs (array): inputs
            properties (array): properties
            archived (boolean): Indicates whether to include archived feedback submissions in the batch read operation, with a default value of false.
            idProperty (string): idProperty

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Batch
        """
        request_body_data = None
        request_body_data = {
            'propertiesWithHistory': propertiesWithHistory,
            'idProperty': idProperty,
            'inputs': inputs,
            'properties': properties,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/objects/feedback_submissions/batch/read"
        query_params = {k: v for k, v in [('archived', archived)] if v is not None}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

    def basic_read_feedback_submission(self, feedbackSubmissionId, properties=None, propertiesWithHistory=None, associations=None, archived=None, idProperty=None) -> dict[str, Any]:
        """
        Retrieves detailed information about a specific feedback submission using its ID, with optional parameters to include properties, history, associations, and archived status.

        Args:
            feedbackSubmissionId (string): feedbackSubmissionId
            properties (array): Specifies an array of properties to include in the response for the feedback submission, allowing selective retrieval of specific details.
            propertiesWithHistory (array): A comma-separated list of property names for which to return both current values and full historical changes in the response.
            associations (array): Optional array of associated object types to include with the feedback submission in the response.
            archived (boolean): Include this query parameter to specify whether to retrieve the archived version of the feedback submission; defaults to false if omitted.
            idProperty (string): Optional query parameter to specify the ID property for the feedback submission.

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Basic
        """
        if feedbackSubmissionId is None:
            raise ValueError("Missing required parameter 'feedbackSubmissionId'.")
        url = f"{self.base_url}/crm/v3/objects/feedback_submissions/{feedbackSubmissionId}"
        query_params = {k: v for k, v in [('properties', properties), ('propertiesWithHistory', propertiesWithHistory), ('associations', associations), ('archived', archived), ('idProperty', idProperty)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def basic_archive_feedback_submission(self, feedbackSubmissionId) -> Any:
        """
        Deletes a specific feedback submission identified by the provided `feedbackSubmissionId` from the CRM system.

        Args:
            feedbackSubmissionId (string): feedbackSubmissionId

        Returns:
            Any: No content

        Tags:
            Basic
        """
        if feedbackSubmissionId is None:
            raise ValueError("Missing required parameter 'feedbackSubmissionId'.")
        url = f"{self.base_url}/crm/v3/objects/feedback_submissions/{feedbackSubmissionId}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def basic_update_feedback_submission(self, feedbackSubmissionId, properties, idProperty=None) -> dict[str, Any]:
        """
        Updates specific fields of a feedback submission by ID using partial modifications with a JSON request body.

        Args:
            feedbackSubmissionId (string): feedbackSubmissionId
            properties (object): No description provided. Example: "{'description': 'A new product description', 'name': '1 year implementation consultation', 'price': '6000.00', 'hs_cost_of_goods_sold': '700.00', 'property_date': '1572480000000', 'property_radio': 'option_1', 'property_number': '17', 'property_string': 'value', 'property_checkbox': 'false', 'property_dropdown': 'choice_b', 'property_multiple_checkboxes': 'chocolate;strawberry', 'quantity': '2', 'hs_product_id': '191902', 'recurringbillingfrequency': 'monthly', 'hs_recurring_billing_period': 'P24M'}".
            idProperty (string): The "idProperty" query parameter specifies the property name used to identify the feedback submission object for partial updates.

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Basic
        """
        if feedbackSubmissionId is None:
            raise ValueError("Missing required parameter 'feedbackSubmissionId'.")
        request_body_data = None
        request_body_data = {
            'properties': properties,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/objects/feedback_submissions/{feedbackSubmissionId}"
        query_params = {k: v for k, v in [('idProperty', idProperty)] if v is not None}
        response = self._patch(url, data=request_body_data, params=query_params)
        response.raise_for_status()
        return response.json()

    def public_object_merge_feedback_submissions(self, objectIdToMerge, primaryObjectId) -> dict[str, Any]:
        """
        Merges feedback submission records using the POST method, requiring a JSON body and supporting OAuth2 and private apps for authentication.

        Args:
            objectIdToMerge (string): objectIdToMerge
            primaryObjectId (string): primaryObjectId

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Public_Object
        """
        request_body_data = None
        request_body_data = {
            'objectIdToMerge': objectIdToMerge,
            'primaryObjectId': primaryObjectId,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/objects/feedback_submissions/merge"
        query_params = {}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

    def batch_archive_feedback_submissions_by_id(self, inputs) -> Any:
        """
        Archives a batch of feedback submissions by ID using the HubSpot API and returns a status response with a 204 status code upon successful completion.

        Args:
            inputs (array): inputs

        Returns:
            Any: No content

        Tags:
            Batch
        """
        request_body_data = None
        request_body_data = {
            'inputs': inputs,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/objects/feedback_submissions/batch/archive"
        query_params = {}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

    def batch_create_feedback_submissions(self, inputs) -> dict[str, Any]:
        """
        Creates a batch of feedback submissions using the HubSpot API, allowing for the simultaneous creation of multiple feedback submissions.

        Args:
            inputs (array): inputs

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Batch
        """
        request_body_data = None
        request_body_data = {
            'inputs': inputs,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/objects/feedback_submissions/batch/create"
        query_params = {}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

    def batch_update_feedback_submissions(self, inputs) -> dict[str, Any]:
        """
        Updates multiple feedback submissions in batches using the HubSpot CRM API.

        Args:
            inputs (array): inputs

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Batch
        """
        request_body_data = None
        request_body_data = {
            'inputs': inputs,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/objects/feedback_submissions/batch/update"
        query_params = {}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

    def gdpr_permanently_delete_contact_feedback_submission(self, objectId, idProperty=None) -> Any:
        """
        Permanently deletes feedback submissions and associated data to comply with GDPR regulations using the provided JSON body.

        Args:
            objectId (string): objectId
            idProperty (string): idProperty

        Returns:
            Any: No content

        Tags:
            GDPR
        """
        request_body_data = None
        request_body_data = {
            'idProperty': idProperty,
            'objectId': objectId,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/objects/feedback_submissions/gdpr-delete"
        query_params = {}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

    def basic_list_feedback_submissions_page(self, limit=None, after=None, properties=None, propertiesWithHistory=None, associations=None, archived=None) -> dict[str, Any]:
        """
        Retrieves a list of feedback submissions from HubSpot CRM, allowing for optional filtering by limit, pagination, specific properties, property history, associations, and archived status.

        Args:
            limit (integer): Maximum number of feedback submission records to return in the response, defaulting to 10 if not specified.
            after (string): The "after" query parameter is an optional string used as a paging cursor token to retrieve the next page of feedback submissions after a specified record in the GET /crm/v3/objects/feedback_submissions endpoint.
            properties (array): Optional array of properties to include in the response, allowing you to specify which fields of the feedback submissions to retrieve.
            propertiesWithHistory (array): A comma-separated list of properties for which to return both current values and their historical changes in the response.
            associations (array): Associations parameter specifies an array of association names to include in the response for the GET operation at the "/crm/v3/objects/feedback_submissions" path, allowing retrieval of related records.
            archived (boolean): Indicates whether to include archived feedback submissions in the response, defaulting to false.

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Basic
        """
        url = f"{self.base_url}/crm/v3/objects/feedback_submissions"
        query_params = {k: v for k, v in [('limit', limit), ('after', after), ('properties', properties), ('propertiesWithHistory', propertiesWithHistory), ('associations', associations), ('archived', archived)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def basic_create_feedback_submission(self, associations, properties) -> dict[str, Any]:
        """
        Searches for feedback submissions using the HubSpot CRM API and returns relevant results.

        Args:
            associations (array): associations
            properties (object): No description provided. Example: "{'description': 'Onboarding service for data product', 'name': '1 year implementation consultation', 'price': '6000.00', 'hs_sku': '191902', 'hs_cost_of_goods_sold': '600.00', 'hs_recurring_billing_period': 'P24M', 'city': 'Cambridge', 'phone': '(877) 929-0687', 'state': 'Massachusetts', 'domain': 'biglytics.net', 'industry': 'Technology', 'amount': '1500.00', 'dealname': 'Custom data integrations', 'pipeline': 'default', 'closedate': '2019-12-07T16:50:06.678Z', 'dealstage': 'presentationscheduled', 'hubspot_owner_id': '910901', 'email': 'bcooper@biglytics.net', 'company': 'Biglytics', 'website': 'biglytics.net', 'lastname': 'Cooper', 'firstname': 'Bryan', 'subject': 'troubleshoot report', 'hs_pipeline': 'support_pipeline', 'hs_pipeline_stage': 'open', 'hs_ticket_priority': 'HIGH', 'quantity': '2', 'hs_product_id': '191902', 'recurringbillingfrequency': 'monthly'}".

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Basic
        """
        request_body_data = None
        request_body_data = {
            'associations': associations,
            'properties': properties,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/objects/feedback_submissions"
        query_params = {}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

    def search_feedback_submissions(self, limit, after, sorts, properties, filterGroups, query=None) -> dict[str, Any]:
        """
        Searches for feedback submissions in HubSpot CRM using the POST method, allowing developers to filter and retrieve specific feedback data.

        Args:
            limit (integer): limit
            after (string): after
            sorts (array): sorts
            properties (array): properties
            filterGroups (array): filterGroups
            query (string): query

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Search
        """
        request_body_data = None
        request_body_data = {
            'query': query,
            'limit': limit,
            'after': after,
            'sorts': sorts,
            'properties': properties,
            'filterGroups': filterGroups,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/objects/feedback_submissions/search"
        query_params = {}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

    def batch_read_objects_by_internal_id_or_property_values(self, objectType, propertiesWithHistory, inputs, properties, archived=None, idProperty=None) -> dict[str, Any]:
        """
        Performs a batch read operation on CRM objects of the specified type, allowing for the retrieval of multiple records in a single request, with optional filtering by archived status.

        Args:
            objectType (string): objectType
            propertiesWithHistory (array): propertiesWithHistory
            inputs (array): inputs
            properties (array): properties
            archived (boolean): Indicates whether to include archived objects in the batch read operation; defaults to false.
            idProperty (string): idProperty

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Batch
        """
        if objectType is None:
            raise ValueError("Missing required parameter 'objectType'.")
        request_body_data = None
        request_body_data = {
            'propertiesWithHistory': propertiesWithHistory,
            'idProperty': idProperty,
            'inputs': inputs,
            'properties': properties,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/objects/{objectType}/batch/read"
        query_params = {k: v for k, v in [('archived', archived)] if v is not None}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

    def basic_read_object_by_id(self, objectType, objectId, properties=None, propertiesWithHistory=None, associations=None, archived=None, idProperty=None) -> dict[str, Any]:
        """
        Retrieves a specific CRM object record by its object type and ID, allowing for optional specification of properties, associations, and other query parameters.

        Args:
            objectType (string): objectType
            objectId (string): objectId
            properties (array): An optional array parameter that specifies the properties to include in the response for the specified CRM object.
            propertiesWithHistory (array): An optional array parameter specifying the properties for which both current and historical values should be returned in the response.
            associations (array): Optional array parameter to filter results by including or excluding specific associations related to the object.
            archived (boolean): Optional boolean query parameter indicating whether to include archived objects in the response.
            idProperty (string): The optional query parameter to specify a custom property name to use as the unique identifier instead of the default object ID.

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Basic
        """
        if objectType is None:
            raise ValueError("Missing required parameter 'objectType'.")
        if objectId is None:
            raise ValueError("Missing required parameter 'objectId'.")
        url = f"{self.base_url}/crm/v3/objects/{objectType}/{objectId}"
        query_params = {k: v for k, v in [('properties', properties), ('propertiesWithHistory', propertiesWithHistory), ('associations', associations), ('archived', archived), ('idProperty', idProperty)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def basic_archive_object(self, objectType, objectId) -> Any:
        """
        Deletes a specified CRM object of the given type and ID using the DELETE method.

        Args:
            objectType (string): objectType
            objectId (string): objectId

        Returns:
            Any: No content

        Tags:
            Basic
        """
        if objectType is None:
            raise ValueError("Missing required parameter 'objectType'.")
        if objectId is None:
            raise ValueError("Missing required parameter 'objectId'.")
        url = f"{self.base_url}/crm/v3/objects/{objectType}/{objectId}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def basic_update_object(self, objectType, objectId, properties, idProperty=None) -> dict[str, Any]:
        """
        Updates a specific CRM object using the PATCH method by modifying its properties based on the provided JSON body.

        Args:
            objectType (string): objectType
            objectId (string): objectId
            properties (object): No description provided. Example: "{'description': 'A new product description', 'name': '1 year implementation consultation', 'price': '6000.00', 'hs_cost_of_goods_sold': '700.00', 'property_date': '1572480000000', 'property_radio': 'option_1', 'property_number': '17', 'property_string': 'value', 'property_checkbox': 'false', 'property_dropdown': 'choice_b', 'property_multiple_checkboxes': 'chocolate;strawberry', 'quantity': '2', 'hs_product_id': '191902', 'recurringbillingfrequency': 'monthly', 'hs_recurring_billing_period': 'P24M'}".
            idProperty (string): Optional query parameter to specify a custom property name to use as the object identifier instead of the default ID.

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Basic
        """
        if objectType is None:
            raise ValueError("Missing required parameter 'objectType'.")
        if objectId is None:
            raise ValueError("Missing required parameter 'objectId'.")
        request_body_data = None
        request_body_data = {
            'properties': properties,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/objects/{objectType}/{objectId}"
        query_params = {k: v for k, v in [('idProperty', idProperty)] if v is not None}
        response = self._patch(url, data=request_body_data, params=query_params)
        response.raise_for_status()
        return response.json()

    def public_object_merge_objects_with_type(self, objectType, objectIdToMerge, primaryObjectId) -> dict[str, Any]:
        """
        Merges duplicate records of a specified object type into a single record using the provided JSON body.

        Args:
            objectType (string): objectType
            objectIdToMerge (string): objectIdToMerge
            primaryObjectId (string): primaryObjectId

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Public_Object
        """
        if objectType is None:
            raise ValueError("Missing required parameter 'objectType'.")
        request_body_data = None
        request_body_data = {
            'objectIdToMerge': objectIdToMerge,
            'primaryObjectId': primaryObjectId,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/objects/{objectType}/merge"
        query_params = {}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

    def batch_archive_objects_by_id(self, objectType, inputs) -> Any:
        """
        Archives a batch of objects of a specified type in CRM using the POST method, requiring a JSON body and returning a 204 status code upon successful archiving.

        Args:
            objectType (string): objectType
            inputs (array): inputs

        Returns:
            Any: No content

        Tags:
            Batch
        """
        if objectType is None:
            raise ValueError("Missing required parameter 'objectType'.")
        request_body_data = None
        request_body_data = {
            'inputs': inputs,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/objects/{objectType}/batch/archive"
        query_params = {}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

    def batch_create_objects(self, objectType, inputs) -> dict[str, Any]:
        """
        Creates multiple records of a specified object type in a CRM system using a single POST request, supporting batch creation and returning a status message based on the outcome.

        Args:
            objectType (string): objectType
            inputs (array): inputs

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Batch
        """
        if objectType is None:
            raise ValueError("Missing required parameter 'objectType'.")
        request_body_data = None
        request_body_data = {
            'inputs': inputs,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/objects/{objectType}/batch/create"
        query_params = {}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

    def batch_update_objects_by_internal_id_or_property_values(self, objectType, inputs) -> dict[str, Any]:
        """
        Updates multiple records of a specified object type in a CRM system using a batch operation via the POST method.

        Args:
            objectType (string): objectType
            inputs (array): inputs

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Batch
        """
        if objectType is None:
            raise ValueError("Missing required parameter 'objectType'.")
        request_body_data = None
        request_body_data = {
            'inputs': inputs,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/objects/{objectType}/batch/update"
        query_params = {}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

    def gdpr_permanently_delete_contact_object(self, objectType, objectId, idProperty=None) -> Any:
        """
        Permanently deletes an object of the specified type from the CRM, adhering to GDPR guidelines for data removal, using the "POST" method with the object type specified in the path and additional details in the request body.

        Args:
            objectType (string): objectType
            objectId (string): objectId
            idProperty (string): idProperty

        Returns:
            Any: No content

        Tags:
            GDPR
        """
        if objectType is None:
            raise ValueError("Missing required parameter 'objectType'.")
        request_body_data = None
        request_body_data = {
            'idProperty': idProperty,
            'objectId': objectId,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/objects/{objectType}/gdpr-delete"
        query_params = {}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

    def basic_list_objects_page(self, objectType, limit=None, after=None, properties=None, propertiesWithHistory=None, associations=None, archived=None) -> dict[str, Any]:
        """
        Retrieves a list of records for a specified CRM object type with optional filtering, pagination, property selection, association inclusion, and archived status.

        Args:
            objectType (string): objectType
            limit (integer): The "limit" parameter specifies the maximum number of objects to return in the response, with a default value of 10.
            after (string): The "after" query parameter is an optional string used for pagination to specify the cursor after which to return the next set of results.
            properties (array): Optional array parameter to specify which properties to include in the response for the GET operation at `/crm/v3/objects/{objectType}`.
            propertiesWithHistory (array): Optional array parameter to specify the properties for which both current and historical values should be returned in the response.
            associations (array): Filter to include specific association types when retrieving objects, provided as an optional array of association type identifiers in the query string.
            archived (boolean): Optional query parameter to filter results by archived status, defaulting to false.

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Basic
        """
        if objectType is None:
            raise ValueError("Missing required parameter 'objectType'.")
        url = f"{self.base_url}/crm/v3/objects/{objectType}"
        query_params = {k: v for k, v in [('limit', limit), ('after', after), ('properties', properties), ('propertiesWithHistory', propertiesWithHistory), ('associations', associations), ('archived', archived)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def basic_create_crmobject(self, objectType, associations, properties) -> dict[str, Any]:
        """
        Creates a new object of the specified type in a CRM system using the provided JSON data, returning a status message upon successful creation.

        Args:
            objectType (string): objectType
            associations (array): associations
            properties (object): No description provided. Example: "{'description': 'Onboarding service for data product', 'name': '1 year implementation consultation', 'price': '6000.00', 'hs_sku': '191902', 'hs_cost_of_goods_sold': '600.00', 'hs_recurring_billing_period': 'P24M', 'city': 'Cambridge', 'phone': '(877) 929-0687', 'state': 'Massachusetts', 'domain': 'biglytics.net', 'industry': 'Technology', 'amount': '1500.00', 'dealname': 'Custom data integrations', 'pipeline': 'default', 'closedate': '2019-12-07T16:50:06.678Z', 'dealstage': 'presentationscheduled', 'hubspot_owner_id': '910901', 'email': 'bcooper@biglytics.net', 'company': 'Biglytics', 'website': 'biglytics.net', 'lastname': 'Cooper', 'firstname': 'Bryan', 'subject': 'troubleshoot report', 'hs_pipeline': 'support_pipeline', 'hs_pipeline_stage': 'open', 'hs_ticket_priority': 'HIGH', 'quantity': '2', 'hs_product_id': '191902', 'recurringbillingfrequency': 'monthly'}".

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Basic
        """
        if objectType is None:
            raise ValueError("Missing required parameter 'objectType'.")
        request_body_data = None
        request_body_data = {
            'associations': associations,
            'properties': properties,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/objects/{objectType}"
        query_params = {}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

    def search_objects_by_criteria(self, objectType, limit, after, sorts, properties, filterGroups, query=None) -> dict[str, Any]:
        """
        Searches for objects of a specified type within a CRM using the provided JSON payload, filtering by various criteria to return a list of matching objects.

        Args:
            objectType (string): objectType
            limit (integer): limit
            after (string): after
            sorts (array): sorts
            properties (array): properties
            filterGroups (array): filterGroups
            query (string): query

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Search
        """
        if objectType is None:
            raise ValueError("Missing required parameter 'objectType'.")
        request_body_data = None
        request_body_data = {
            'query': query,
            'limit': limit,
            'after': after,
            'sorts': sorts,
            'properties': properties,
            'filterGroups': filterGroups,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/objects/{objectType}/search"
        query_params = {}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

    def settings_get_by_id(self, appId) -> dict[str, Any]:
        """
        Retrieves the video conferencing settings for a specific application identified by the provided appId using the HubSpot API.

        Args:
            appId (string): appId

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Settings
        """
        if appId is None:
            raise ValueError("Missing required parameter 'appId'.")
        url = f"{self.base_url}/crm/v3/extensions/videoconferencing/settings/{appId}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def settings_update_video_conferencing_app_settings(self, appId, createMeetingUrl, userVerifyUrl=None, fetchAccountsUri=None, updateMeetingUrl=None, deleteMeetingUrl=None) -> dict[str, Any]:
        """
        Updates video conferencing settings for a specific application identified by its `appId` using the provided JSON data.

        Args:
            appId (string): appId
            createMeetingUrl (string): The URL that HubSpot will send requests to create a new video conference. Example: 'https://example.com/create-meeting'.
            userVerifyUrl (string): The URL that HubSpot will use to verify that a user exists in the video conference application. Example: 'https://example.com/user-verify'.
            fetchAccountsUri (string): fetchAccountsUri
            updateMeetingUrl (string): The URL that HubSpot will send updates to existing meetings. Typically called when the user changes the topic or times of a meeting. Example: 'https://example.com/update-meeting'.
            deleteMeetingUrl (string): The URL that HubSpot will send notifications of meetings that have been deleted in HubSpot. Example: 'https://example.com/delete-meeting'.

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Settings
        """
        if appId is None:
            raise ValueError("Missing required parameter 'appId'.")
        request_body_data = None
        request_body_data = {
            'userVerifyUrl': userVerifyUrl,
            'fetchAccountsUri': fetchAccountsUri,
            'createMeetingUrl': createMeetingUrl,
            'updateMeetingUrl': updateMeetingUrl,
            'deleteMeetingUrl': deleteMeetingUrl,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/extensions/videoconferencing/settings/{appId}"
        query_params = {}
        response = self._put(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

    def settings_delete_video_conferencing_app_settings(self, appId) -> Any:
        """
        Deletes the video conferencing settings for the specified app identified by the appId.

        Args:
            appId (string): appId

        Returns:
            Any: No content

        Tags:
            Settings
        """
        if appId is None:
            raise ValueError("Missing required parameter 'appId'.")
        url = f"{self.base_url}/crm/v3/extensions/videoconferencing/settings/{appId}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def batch_read_tickets_by_properties(self, propertiesWithHistory, inputs, properties, archived=None, idProperty=None) -> dict[str, Any]:
        """
        Retrieves and formats a batch of tickets from HubSpot CRM using a POST request to the "/crm/v3/objects/tickets/batch/read" endpoint.

        Args:
            propertiesWithHistory (array): propertiesWithHistory
            inputs (array): inputs
            properties (array): properties
            archived (boolean): Indicates whether to include archived tickets in the batch read operation, defaulting to false.
            idProperty (string): idProperty

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Batch
        """
        request_body_data = None
        request_body_data = {
            'propertiesWithHistory': propertiesWithHistory,
            'idProperty': idProperty,
            'inputs': inputs,
            'properties': properties,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/objects/tickets/batch/read"
        query_params = {k: v for k, v in [('archived', archived)] if v is not None}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

    def basic_read_ticket_by_id(self, ticketId, properties=None, propertiesWithHistory=None, associations=None, archived=None, idProperty=None) -> dict[str, Any]:
        """
        Retrieves a specific ticket record by ID from the CRM, optionally including specified properties, property history, associations, and archived status.

        Args:
            ticketId (string): ticketId
            properties (array): An optional array parameter specifying the properties to include in the response for the ticket object.
            propertiesWithHistory (array): A query parameter that returns the specified properties of a ticket along with their version history.
            associations (array): An optional array parameter used to specify the types of associations to retrieve for the ticket, such as contacts or companies.
            archived (boolean): Indicates whether to include archived tickets in the response. Defaults to false.
            idProperty (string): Optional string parameter to specify the property that uniquely identifies a ticket in the CRM system.

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Basic
        """
        if ticketId is None:
            raise ValueError("Missing required parameter 'ticketId'.")
        url = f"{self.base_url}/crm/v3/objects/tickets/{ticketId}"
        query_params = {k: v for k, v in [('properties', properties), ('propertiesWithHistory', propertiesWithHistory), ('associations', associations), ('archived', archived), ('idProperty', idProperty)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def basic_archive_ticket(self, ticketId) -> Any:
        """
        Deletes a ticket by its ID using the CRM API.

        Args:
            ticketId (string): ticketId

        Returns:
            Any: No content

        Tags:
            Basic
        """
        if ticketId is None:
            raise ValueError("Missing required parameter 'ticketId'.")
        url = f"{self.base_url}/crm/v3/objects/tickets/{ticketId}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def basic_update_ticket_object(self, ticketId, properties, idProperty=None) -> dict[str, Any]:
        """
        Updates an individual ticket by its ID using the HubSpot CRM API, allowing modification of specific fields via a JSON payload.

        Args:
            ticketId (string): ticketId
            properties (object): No description provided. Example: "{'description': 'A new product description', 'name': '1 year implementation consultation', 'price': '6000.00', 'hs_cost_of_goods_sold': '700.00', 'property_date': '1572480000000', 'property_radio': 'option_1', 'property_number': '17', 'property_string': 'value', 'property_checkbox': 'false', 'property_dropdown': 'choice_b', 'property_multiple_checkboxes': 'chocolate;strawberry', 'quantity': '2', 'hs_product_id': '191902', 'recurringbillingfrequency': 'monthly', 'hs_recurring_billing_period': 'P24M'}".
            idProperty (string): The idProperty query parameter specifies the name of the property to use as the unique identifier in the ticket update request; it is optional and of type string.

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Basic
        """
        if ticketId is None:
            raise ValueError("Missing required parameter 'ticketId'.")
        request_body_data = None
        request_body_data = {
            'properties': properties,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/objects/tickets/{ticketId}"
        query_params = {k: v for k, v in [('idProperty', idProperty)] if v is not None}
        response = self._patch(url, data=request_body_data, params=query_params)
        response.raise_for_status()
        return response.json()

    def public_object_merge_tickets_same_type(self, objectIdToMerge, primaryObjectId) -> dict[str, Any]:
        """
        Merges two or more tickets into a single ticket in the CRM system using the POST method, allowing for the consolidation of related customer service requests.

        Args:
            objectIdToMerge (string): objectIdToMerge
            primaryObjectId (string): primaryObjectId

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Public_Object
        """
        request_body_data = None
        request_body_data = {
            'objectIdToMerge': objectIdToMerge,
            'primaryObjectId': primaryObjectId,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/objects/tickets/merge"
        query_params = {}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

    def batch_archive_tickets_by_id(self, inputs) -> Any:
        """
        Archives a batch of tickets by ID using the HubSpot API and returns a status message.

        Args:
            inputs (array): inputs

        Returns:
            Any: No content

        Tags:
            Batch
        """
        request_body_data = None
        request_body_data = {
            'inputs': inputs,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/objects/tickets/batch/archive"
        query_params = {}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

    def batch_ticket_creation_batch(self, inputs) -> dict[str, Any]:
        """
        Creates a batch of tickets in the CRM using the HubSpot API and returns a status message.

        Args:
            inputs (array): inputs

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Batch
        """
        request_body_data = None
        request_body_data = {
            'inputs': inputs,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/objects/tickets/batch/create"
        query_params = {}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

    def batch_update_tickets_batch(self, inputs) -> dict[str, Any]:
        """
        Updates multiple tickets in a single request using the HubSpot CRM API, returning a status message indicating the success or partial success of the operation.

        Args:
            inputs (array): inputs

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Batch
        """
        request_body_data = None
        request_body_data = {
            'inputs': inputs,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/objects/tickets/batch/update"
        query_params = {}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

    def gdpr_permanently_delete_contact(self, objectId, idProperty=None) -> Any:
        """
        Permanently deletes a ticket and associated data in compliance with GDPR guidelines using the POST method.

        Args:
            objectId (string): objectId
            idProperty (string): idProperty

        Returns:
            Any: No content

        Tags:
            GDPR
        """
        request_body_data = None
        request_body_data = {
            'idProperty': idProperty,
            'objectId': objectId,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/objects/tickets/gdpr-delete"
        query_params = {}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

    def basic_list_tickets_page(self, limit=None, after=None, properties=None, propertiesWithHistory=None, associations=None, archived=None) -> dict[str, Any]:
        """
        Retrieves a list of tickets from the CRM, allowing for filtering by limit, after cursor, specific properties, properties with history, associations, and archived status.

        Args:
            limit (integer): The "limit" parameter specifies the maximum number of tickets to return in the response, with a default value of 10.
            after (string): The "after" query parameter is an optional string used for pagination to specify the cursor or offset after which to return the next set of ticket results.
            properties (array): Optional query parameter to specify an array of properties to include in the response for the ticket objects, allowing for customization of the returned data.
            propertiesWithHistory (array): Optional array parameter to specify the properties for which both current and historical values should be returned in the response for the ticket object.
            associations (array): An optional array of association types to include related records linked to the ticket in the response.
            archived (boolean): Optional query parameter indicating whether to include archived tickets (true) or only non-archived tickets (false), defaulting to false.

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Basic
        """
        url = f"{self.base_url}/crm/v3/objects/tickets"
        query_params = {k: v for k, v in [('limit', limit), ('after', after), ('properties', properties), ('propertiesWithHistory', propertiesWithHistory), ('associations', associations), ('archived', archived)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def basic_create_ticket_object(self, associations, properties) -> dict[str, Any]:
        """
        Creates a new ticket object in the CRM using the HubSpot API, allowing for the management of customer service requests.

        Args:
            associations (array): associations
            properties (object): No description provided. Example: "{'description': 'Onboarding service for data product', 'name': '1 year implementation consultation', 'price': '6000.00', 'hs_sku': '191902', 'hs_cost_of_goods_sold': '600.00', 'hs_recurring_billing_period': 'P24M', 'city': 'Cambridge', 'phone': '(877) 929-0687', 'state': 'Massachusetts', 'domain': 'biglytics.net', 'industry': 'Technology', 'amount': '1500.00', 'dealname': 'Custom data integrations', 'pipeline': 'default', 'closedate': '2019-12-07T16:50:06.678Z', 'dealstage': 'presentationscheduled', 'hubspot_owner_id': '910901', 'email': 'bcooper@biglytics.net', 'company': 'Biglytics', 'website': 'biglytics.net', 'lastname': 'Cooper', 'firstname': 'Bryan', 'subject': 'troubleshoot report', 'hs_pipeline': 'support_pipeline', 'hs_pipeline_stage': 'open', 'hs_ticket_priority': 'HIGH', 'quantity': '2', 'hs_product_id': '191902', 'recurringbillingfrequency': 'monthly'}".

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Basic
        """
        request_body_data = None
        request_body_data = {
            'associations': associations,
            'properties': properties,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/objects/tickets"
        query_params = {}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

    def search_tickets_by_criteria(self, limit, after, sorts, properties, filterGroups, query=None) -> dict[str, Any]:
        """
        Searches and filters ticket records within the CRM system based on specified criteria, returning matching ticket results.

        Args:
            limit (integer): limit
            after (string): after
            sorts (array): sorts
            properties (array): properties
            filterGroups (array): filterGroups
            query (string): query

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Search
        """
        request_body_data = None
        request_body_data = {
            'query': query,
            'limit': limit,
            'after': after,
            'sorts': sorts,
            'properties': properties,
            'filterGroups': filterGroups,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/objects/tickets/search"
        query_params = {}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

    def batch_read_line_items(self, propertiesWithHistory, inputs, properties, archived=None, idProperty=None) -> dict[str, Any]:
        """
        Retrieves a batch of line items by internal ID or unique property values using the HubSpot CRM API.

        Args:
            propertiesWithHistory (array): propertiesWithHistory
            inputs (array): inputs
            properties (array): properties
            archived (boolean): A boolean flag indicating whether to include archived line items in the batch read operation, defaulting to false.
            idProperty (string): idProperty

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Batch
        """
        request_body_data = None
        request_body_data = {
            'propertiesWithHistory': propertiesWithHistory,
            'idProperty': idProperty,
            'inputs': inputs,
            'properties': properties,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/objects/line_items/batch/read"
        query_params = {k: v for k, v in [('archived', archived)] if v is not None}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

    def basic_read_line_item_by_id(self, lineItemId, properties=None, propertiesWithHistory=None, associations=None, archived=None, idProperty=None) -> dict[str, Any]:
        """
        Retrieves a specific line item by its ID from the CRM, optionally including additional properties, associations, and history, using the CRM API with appropriate permissions.

        Args:
            lineItemId (string): lineItemId
            properties (array): Optional array parameter to specify the properties of a line item to be returned in the response.
            propertiesWithHistory (array): A comma-separated list of property names to include their historical values in the response for the specified line item.
            associations (array): An optional query parameter specifying the associations to include in the response when retrieving a line item, represented as an array of association types.
            archived (boolean): Whether to include archived line items in the response; defaults to false when omitted.
            idProperty (string): Optional string parameter to specify the ID property for line items.

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Basic
        """
        if lineItemId is None:
            raise ValueError("Missing required parameter 'lineItemId'.")
        url = f"{self.base_url}/crm/v3/objects/line_items/{lineItemId}"
        query_params = {k: v for k, v in [('properties', properties), ('propertiesWithHistory', propertiesWithHistory), ('associations', associations), ('archived', archived), ('idProperty', idProperty)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def basic_archive_line_item(self, lineItemId) -> Any:
        """
        Deletes a line item from HubSpot CRM using its ID, requiring the "crm.objects.line_items.write" permission.

        Args:
            lineItemId (string): lineItemId

        Returns:
            Any: No content

        Tags:
            Basic
        """
        if lineItemId is None:
            raise ValueError("Missing required parameter 'lineItemId'.")
        url = f"{self.base_url}/crm/v3/objects/line_items/{lineItemId}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def basic_update_line_item_object(self, lineItemId, properties, idProperty=None) -> dict[str, Any]:
        """
        Updates properties of a specific line item in the CRM system using a partial JSON patch request.

        Args:
            lineItemId (string): lineItemId
            properties (object): No description provided. Example: "{'description': 'A new product description', 'name': '1 year implementation consultation', 'price': '6000.00', 'hs_cost_of_goods_sold': '700.00', 'property_date': '1572480000000', 'property_radio': 'option_1', 'property_number': '17', 'property_string': 'value', 'property_checkbox': 'false', 'property_dropdown': 'choice_b', 'property_multiple_checkboxes': 'chocolate;strawberry', 'quantity': '2', 'hs_product_id': '191902', 'recurringbillingfrequency': 'monthly', 'hs_recurring_billing_period': 'P24M'}".
            idProperty (string): Specifies which property uniquely identifies the line item for the PATCH operation; defaults to a standard ID if not provided.

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Basic
        """
        if lineItemId is None:
            raise ValueError("Missing required parameter 'lineItemId'.")
        request_body_data = None
        request_body_data = {
            'properties': properties,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/objects/line_items/{lineItemId}"
        query_params = {k: v for k, v in [('idProperty', idProperty)] if v is not None}
        response = self._patch(url, data=request_body_data, params=query_params)
        response.raise_for_status()
        return response.json()

    def public_object_merge_line_items_same_type(self, objectIdToMerge, primaryObjectId) -> dict[str, Any]:
        """
        Merges duplicate line items into a single instance using the specified parameters via the POST method.

        Args:
            objectIdToMerge (string): objectIdToMerge
            primaryObjectId (string): primaryObjectId

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Public_Object
        """
        request_body_data = None
        request_body_data = {
            'objectIdToMerge': objectIdToMerge,
            'primaryObjectId': primaryObjectId,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/objects/line_items/merge"
        query_params = {}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

    def batch_archive_line_items_by_ids(self, inputs) -> Any:
        """
        Archives a batch of line items by their IDs in the CRM using a POST request.

        Args:
            inputs (array): inputs

        Returns:
            Any: No content

        Tags:
            Batch
        """
        request_body_data = None
        request_body_data = {
            'inputs': inputs,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/objects/line_items/batch/archive"
        query_params = {}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

    def batch_line_items_create_batch(self, inputs) -> dict[str, Any]:
        """
        Creates a batch of line items using the HubSpot API and returns a status message upon successful creation.

        Args:
            inputs (array): inputs

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Batch
        """
        request_body_data = None
        request_body_data = {
            'inputs': inputs,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/objects/line_items/batch/create"
        query_params = {}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

    def batch_update_line_items(self, inputs) -> dict[str, Any]:
        """
        Updates a batch of line items using their internal IDs or unique property values via the POST method, requiring authentication with the "crm.objects.line_items.write" scope.

        Args:
            inputs (array): inputs

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Batch
        """
        request_body_data = None
        request_body_data = {
            'inputs': inputs,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/objects/line_items/batch/update"
        query_params = {}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

    def gdpr_delete_contact_content(self, objectId, idProperty=None) -> Any:
        """
        Deletes line item records from the CRM to comply with GDPR requirements, using the POST method with OAuth2 or private app authentication.

        Args:
            objectId (string): objectId
            idProperty (string): idProperty

        Returns:
            Any: No content

        Tags:
            GDPR
        """
        request_body_data = None
        request_body_data = {
            'idProperty': idProperty,
            'objectId': objectId,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/objects/line_items/gdpr-delete"
        query_params = {}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

    def basic_list_line_items_page(self, limit=None, after=None, properties=None, propertiesWithHistory=None, associations=None, archived=None) -> dict[str, Any]:
        """
        Retrieves a paginated list of line items with optional filters for properties, associations, and archival status in the CRM.

        Args:
            limit (integer): The "limit" parameter specifies the maximum number of line items to return in a response, with a default value of 10.
            after (string): The "after" query parameter is used for pagination to retrieve the next page of line items after the specified cursor or ID.
            properties (array): Optional array of properties to include in the response for line items; specify the properties you want to retrieve.
            propertiesWithHistory (array): Specifies an array of properties to include in the response with their historical values for line items.
            associations (array): A list of associations to include in the response for line items, allowing for retrieval of related objects.
            archived (boolean): Optional boolean parameter indicating whether to include archived line items in the response.

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Basic
        """
        url = f"{self.base_url}/crm/v3/objects/line_items"
        query_params = {k: v for k, v in [('limit', limit), ('after', after), ('properties', properties), ('propertiesWithHistory', propertiesWithHistory), ('associations', associations), ('archived', archived)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def basic_create_line_item_object(self, associations, properties) -> dict[str, Any]:
        """
        Creates a new line item in HubSpot CRM using the POST method, allowing you to add products or services to deals and quotes.

        Args:
            associations (array): associations
            properties (object): No description provided. Example: "{'description': 'Onboarding service for data product', 'name': '1 year implementation consultation', 'price': '6000.00', 'hs_sku': '191902', 'hs_cost_of_goods_sold': '600.00', 'hs_recurring_billing_period': 'P24M', 'city': 'Cambridge', 'phone': '(877) 929-0687', 'state': 'Massachusetts', 'domain': 'biglytics.net', 'industry': 'Technology', 'amount': '1500.00', 'dealname': 'Custom data integrations', 'pipeline': 'default', 'closedate': '2019-12-07T16:50:06.678Z', 'dealstage': 'presentationscheduled', 'hubspot_owner_id': '910901', 'email': 'bcooper@biglytics.net', 'company': 'Biglytics', 'website': 'biglytics.net', 'lastname': 'Cooper', 'firstname': 'Bryan', 'subject': 'troubleshoot report', 'hs_pipeline': 'support_pipeline', 'hs_pipeline_stage': 'open', 'hs_ticket_priority': 'HIGH', 'quantity': '2', 'hs_product_id': '191902', 'recurringbillingfrequency': 'monthly'}".

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Basic
        """
        request_body_data = None
        request_body_data = {
            'associations': associations,
            'properties': properties,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/objects/line_items"
        query_params = {}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

    def search_line_items_by_criteria(self, limit, after, sorts, properties, filterGroups, query=None) -> dict[str, Any]:
        """
        Searches and retrieves line items and their associated properties in the CRM based on specified filter criteria.

        Args:
            limit (integer): limit
            after (string): after
            sorts (array): sorts
            properties (array): properties
            filterGroups (array): filterGroups
            query (string): query

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Search
        """
        request_body_data = None
        request_body_data = {
            'query': query,
            'limit': limit,
            'after': after,
            'sorts': sorts,
            'properties': properties,
            'filterGroups': filterGroups,
        }
        request_body_data = {k: v for k, v in request_body_data.items() if v is not None}
        url = f"{self.base_url}/crm/v3/objects/line_items/search"
        query_params = {}
        response = self._post(url, data=request_body_data, params=query_params, content_type='application/json')
        response.raise_for_status()
        return response.json()

    def core_get_active_imports_page(self, after=None, before=None, limit=None) -> dict[str, Any]:
        """
        Retrieves a list of CRM import operations using the HubSpot API, allowing optional filtering by date and limit on the number of results returned.

        Args:
            after (string): Optional string parameter used to specify the cursor for pagination, allowing retrieval of the next page of results.
            before (string): The "before" query parameter specifies a cutoff point to filter and return only imports created before the given timestamp or identifier.
            limit (integer): Specifies the maximum number of items to return in the response for the import data.

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Core
        """
        url = f"{self.base_url}/crm/v3/imports"
        query_params = {k: v for k, v in [('after', after), ('before', before), ('limit', limit)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def core_start_import(self, files=None, importRequest=None) -> dict[str, Any]:
        """
        Imports data into a HubSpot CRM using a POST request with a multipart/form-data payload, allowing bulk creation or update of records via uploaded files such as CSV or Excel.

        Args:
            files (file (e.g., open('path/to/file', 'rb'))): A list of files containing the data to import
            importRequest (string): JSON formatted metadata about the import. This includes a name for the import and the column mappings for each file. See the overview tab for more on the required format.

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Core
        """
        request_body_data = None
        files_data = None
        request_body_data = {}
        files_data = {}
        if files is not None:
            files_data['files'] = files
        if importRequest is not None:
            request_body_data['importRequest'] = importRequest
        files_data = {k: v for k, v in files_data.items() if v is not None}
        if not files_data: files_data = None
        url = f"{self.base_url}/crm/v3/imports"
        query_params = {}
        response = self._post(url, data=request_body_data, files=files_data, params=query_params, content_type='multipart/form-data')
        response.raise_for_status()
        return response.json()

    def owners_get_page(self, email=None, after=None, limit=None, archived=None) -> dict[str, Any]:
        """
        Retrieves a list of CRM owners using the "GET" method, allowing optional filtering by email, pagination, and archived status, and returns a response with owner details.

        Args:
            email (string): An optional string parameter used to filter owners by their email address in the GET operation at the "/crm/v3/owners" path.
            after (string): **after**: Specifies a cursor for pagination, allowing retrieval of records that appear after the specified value in the result set.
            limit (integer): Specifies the maximum number of results to return in the response, with a default value of 100.
            archived (boolean): A boolean query parameter indicating whether to include archived owners in the response.

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Owners
        """
        url = f"{self.base_url}/crm/v3/owners"
        query_params = {k: v for k, v in [('email', email), ('after', after), ('limit', limit), ('archived', archived)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_crm_v_associations_from_object_type_to_object_type_types_get_all(self, fromObjectType, toObjectType) -> dict[str, Any]:
        """
        Retrieves the association types between two specified object types in HubSpot CRM using the "GET" method.

        Args:
            fromObjectType (string): fromObjectType
            toObjectType (string): toObjectType

        Returns:
            dict[str, Any]: successful operation

        Tags:
            Types
        """
        if fromObjectType is None:
            raise ValueError("Missing required parameter 'fromObjectType'.")
        if toObjectType is None:
            raise ValueError("Missing required parameter 'toObjectType'.")
        url = f"{self.base_url}/crm/v3/associations/{fromObjectType}/{toObjectType}/types"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_tools(self):
        return [
            self.post_crm_v_objects_emails_batch_read_read,
            self.get_crm_v_objects_emails_email_id_get_by_id,
            self.delete_crm_v_objects_emails_email_id_archive,
            self.patch_crm_v_objects_emails_email_id_update,
            self.post_crm_v_objects_emails_merge_merge,
            self.post_crm_v_objects_emails_batch_archive_archive,
            self.post_crm_v_objects_emails_batch_create_create,
            self.post_crm_v_objects_emails_batch_update_update,
            self.post_crm_v_objects_emails_gdpr_delete_purge,
            self.get_crm_v_objects_emails_get_page,
            self.post_crm_v_objects_emails_create,
            self.post_crm_v_objects_emails_search_do_search,
            self.get_marketing_v_campaigns,
            self.post_marketing_v_campaigns,
            self.post_marketing_v_campaigns_batch_read,
            self.post_marketing_v_campaigns_batch_update,
            self.get_marketing_v_campaigns_campaign_guid_reports_metrics,
            self.get_marketing_v_campaigns_campaign_guid_assets_asset_type,
            self.post_marketing_v_campaigns_batch_archive,
            self.put_marketing_v_campaigns_campaign_guid_assets_asset_type_asset_id,
            self.delete_marketing_v_campaigns_campaign_guid_assets_asset_type_asset_id,
            self.get_marketing_v_campaigns_campaign_guid_reports_revenue,
            self.post_marketing_v_campaigns_batch_create,
            self.get_marketing_v_campaigns_campaign_guid_budget_totals,
            self.get_marketing_v_campaigns_campaign_guid,
            self.delete_marketing_v_campaigns_campaign_guid,
            self.patch_marketing_v_campaigns_campaign_guid,
            self.get_marketing_v_campaigns_campaign_guid_reports_contacts_contact_type,
            self.get_marketing_v_emails_statistics_list,
            self.post_marketing_v_emails_ab_test_create_variation,
            self.get_marketing_v_emails_statistics_histogram,
            self.get_marketing_v_emails_email_id_ab_test_get_variation,
            self.post_marketing_v_emails_email_id_draft_reset,
            self.post_marketing_v_emails_email_id_revisions_revision_id_restore_to_draft,
            self.get_marketing_v_emails_email_id_draft,
            self.patch_marketing_v_emails_email_id_draft,
            self.get_marketing_v_emails_email_id_revisions,
            self.get_marketing_v_emails_email_id_revisions_revision_id,
            self.post_marketing_v_emails_clone,
            self.get_marketing_v_emails,
            self.post_marketing_v_emails,
            self.post_marketing_v_emails_email_id_revisions_revision_id_restore,
            self.get_marketing_v_emails_email_id,
            self.delete_marketing_v_emails_email_id,
            self.patch_marketing_v_emails_email_id,
            self.batch_read_by_properties,
            self.basic_read_product_by_id,
            self.basic_archive_product,
            self.basic_update_product,
            self.public_object_merge_products_same_type,
            self.batch_archive_products_by_ids,
            self.batch_create_products_batch,
            self.batch_update_products_batch,
            self.gdpr_delete_contact,
            self.basic_list_products_page,
            self.basic_create_product_object,
            self.search_products_by_criteria,
            self.pipelines_get_by_id,
            self.pipelines_replace_pipeline_object,
            self.pipelines_remove_by_id,
            self.pipelines_update_pipeline_by_id,
            self.pipeline_audits_get_by_pipeline_id,
            self.pipeline_stages_get_all,
            self.pipeline_stages_create_stage_object,
            self.pipelines_get_all,
            self.pipelines_create_new_pipeline_object,
            self.pipeline_stages_get_by_id,
            self.pipeline_stages_replace_stage_object,
            self.pipeline_stages_delete_stage,
            self.pipeline_stages_update_stage_by_id,
            self.batch_read_companies_by_properties,
            self.basic_read_company_object,
            self.basic_archive_company,
            self.basic_update_company_object,
            self.public_object_merge_companies_same_type,
            self.batch_archive_companies_by_id_batch,
            self.batch_create_companies_batch,
            self.batch_update_companies_batch,
            self.gdpr_permanently_delete_contact_company,
            self.basic_list_companies_page,
            self.basic_create_company_object,
            self.search_company_objects,
            self.settings_get_calling_config,
            self.settings_configure_calling_extension,
            self.settings_delete_calling_extension,
            self.settings_update_calling_extension,
            self.recording_settings_get_by_app_id,
            self.recording_settings_set_call_recording,
            self.recording_settings_update_calling_settings,
            self.batch_read_quotes_by_property_values,
            self.basic_read_quote_by_id,
            self.basic_archive_quote_object,
            self.basic_update_quote_object,
            self.public_object_merge_two_quotes_same_type,
            self.batch_archive_quotes_by_id_batch,
            self.batch_create_quotes_batch,
            self.batch_update_quotes_batch,
            self.gdpr_permanently_delete_contact_quotes,
            self.basic_list_quotes_page,
            self.basic_create_quote_object,
            self.search_quotes_by_criteria,
            self.batch_read_deals_by_internal_id_or_property_values,
            self.basic_read_deal_by_id,
            self.basic_archive_deal_object,
            self.basic_update_deal_object,
            self.public_object_merge_deals_same_type,
            self.batch_archive_deals_by_ids,
            self.batch_create_deals_object,
            self.batch_update_deals_objects,
            self.gdpr_permanently_delete_deal,
            self.basic_get_deals_page,
            self.basic_create_deal_object,
            self.search_deals_by_criteria,
            self.core_cancel_import,
            self.core_get_import_record,
            self.public_imports_get_error_details,
            self.core_get_existing_schema,
            self.core_delete_schema,
            self.core_update_schema_object,
            self.core_create_association,
            self.public_object_schemas_purge_object_schema,
            self.core_remove_association,
            self.core_get_all_schemas,
            self.core_define_object_schema,
            self.batch_archive_properties,
            self.groups_read_property_group,
            self.groups_archive_property_group,
            self.groups_update_property_group,
            self.core_read_property,
            self.core_archive_property,
            self.core_update_property_by_id,
            self.batch_read_properties,
            self.batch_properties_create_batch,
            self.core_get_all_properties,
            self.core_create_property,
            self.groups_read_all_property,
            self.groups_create_copy,
            self.owners_get_by_id,
            self.events_create_multiple_batch,
            self.templates_get_specific_event_template,
            self.templates_update_event_template,
            self.templates_delete_event_template,
            self.events_create_single_event,
            self.tokens_add_to_event_template,
            self.tokens_update_existing_token_on_event_template,
            self.tokens_remove_from_template,
            self.events_render_detail_template,
            self.events_get_event_by_id,
            self.templates_list_event_templates,
            self.templates_create_event_template_for_app,
            self.events_rendering_html,
            self.batch_read_contacts_by_properties,
            self.basic_read_contact_by_id,
            self.basic_archive_contact,
            self.basic_update_contact_object,
            self.public_object_merge_contacts_same_type,
            self.batch_archive_contacts_by_id_batch,
            self.batch_create_contacts,
            self.batch_update_contacts_batch,
            self.gdpr_permanently_delete_contacts,
            self.basic_list_contacts_page,
            self.basic_create_contact_object,
            self.search_contacts_by_criteria,
            self.batch_read_feedback_submissions,
            self.basic_read_feedback_submission,
            self.basic_archive_feedback_submission,
            self.basic_update_feedback_submission,
            self.public_object_merge_feedback_submissions,
            self.batch_archive_feedback_submissions_by_id,
            self.batch_create_feedback_submissions,
            self.batch_update_feedback_submissions,
            self.gdpr_permanently_delete_contact_feedback_submission,
            self.basic_list_feedback_submissions_page,
            self.basic_create_feedback_submission,
            self.search_feedback_submissions,
            self.batch_read_objects_by_internal_id_or_property_values,
            self.basic_read_object_by_id,
            self.basic_archive_object,
            self.basic_update_object,
            self.public_object_merge_objects_with_type,
            self.batch_archive_objects_by_id,
            self.batch_create_objects,
            self.batch_update_objects_by_internal_id_or_property_values,
            self.gdpr_permanently_delete_contact_object,
            self.basic_list_objects_page,
            self.basic_create_crmobject,
            self.search_objects_by_criteria,
            self.settings_get_by_id,
            self.settings_update_video_conferencing_app_settings,
            self.settings_delete_video_conferencing_app_settings,
            self.batch_read_tickets_by_properties,
            self.basic_read_ticket_by_id,
            self.basic_archive_ticket,
            self.basic_update_ticket_object,
            self.public_object_merge_tickets_same_type,
            self.batch_archive_tickets_by_id,
            self.batch_ticket_creation_batch,
            self.batch_update_tickets_batch,
            self.gdpr_permanently_delete_contact,
            self.basic_list_tickets_page,
            self.basic_create_ticket_object,
            self.search_tickets_by_criteria,
            self.batch_read_line_items,
            self.basic_read_line_item_by_id,
            self.basic_archive_line_item,
            self.basic_update_line_item_object,
            self.public_object_merge_line_items_same_type,
            self.batch_archive_line_items_by_ids,
            self.batch_line_items_create_batch,
            self.batch_update_line_items,
            self.gdpr_delete_contact_content,
            self.basic_list_line_items_page,
            self.basic_create_line_item_object,
            self.search_line_items_by_criteria,
            self.core_get_active_imports_page,
            self.core_start_import,
            self.owners_get_page,
            self.get_crm_v_associations_from_object_type_to_object_type_types_get_all
        ]
