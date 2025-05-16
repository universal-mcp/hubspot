# HubspotApp MCP Server

An MCP Server for the HubspotApp API.

## 🛠️ Tool List

This is automatically generated from OpenAPI schema for the HubspotApp API.


| Tool | Description |
|------|-------------|
| `post_crm_v_objects_emails_batch_read_read` | Retrieves a batch of emails from a CRM system using the "POST" method, allowing optional filtering by archived status, and returns the results in a multipart response. |
| `get_crm_v_objects_emails_email_id_get_by_id` | Retrieves detailed information about a specific email object in a CRM system, allowing optional filtering by properties, associations, and archival status. |
| `delete_crm_v_objects_emails_email_id_archive` | Deletes an email object identified by the specified emailId from a CRM system. |
| `patch_crm_v_objects_emails_email_id_update` | Updates specific properties of an existing email record in the CRM by its emailId using a PATCH request with JSON data. |
| `post_crm_v_objects_emails_merge_merge` | Merges email records using the provided JSON payload, utilizing OAuth2 or private app authentication to manage contact data in the CRM system. |
| `post_crm_v_objects_emails_batch_archive_archive` | Archives a batch of emails by sending a POST request to the "/crm/v3/objects/emails/batch/archive" endpoint with a JSON payload containing the email IDs to be archived. |
| `post_crm_v_objects_emails_batch_create_create` | Creates a batch of email objects in the CRM using the POST method, requiring JSON content and authorization through OAuth2 or private apps. |
| `post_crm_v_objects_emails_batch_update_update` | Updates multiple email objects in a CRM system using a batch operation via the POST method, returning status messages for each update. |
| `post_crm_v_objects_emails_gdpr_delete_purge` | Deletes a contact and associated data from the CRM in compliance with GDPR guidelines using the provided JSON payload, requiring the "crm.objects.contacts.write" permission. |
| `get_crm_v_objects_emails_get_page` | Retrieves a paginated list of email objects with optional filtering by properties, associations, and archival status from the CRM email records. |
| `post_crm_v_objects_emails_create` | Creates an email object in the CRM using the POST method, allowing for the association of metadata with the email and requiring authentication via OAuth2 or private apps to access the necessary permissions. |
| `post_crm_v_objects_emails_search_do_search` | Searches for email objects in a CRM system using specific criteria, returning relevant results. |
| `get_marketing_v_campaigns` | Retrieves a list of marketing campaigns with optional filtering by name, sorting, and limiting results. |
| `post_marketing_v_campaigns` | Creates a new marketing campaign using the provided JSON data and returns a status message upon successful creation. |
| `post_marketing_v_campaigns_batch_read` | Retrieves a batch of campaign data from the marketing API, filtering by optional start and end dates and specifying properties to include, using JSON-formatted request body. |
| `post_marketing_v_campaigns_batch_update` | Updates multiple marketing campaigns in a batch using the POST method, requiring a JSON body and authentication via OAuth2 or private apps with "marketing.campaigns.read" permissions. |
| `get_marketing_v_campaigns_campaign_guid_reports_metrics` | Retrieves campaign metrics for a specified campaign GUID, optionally filtering by start and end dates. |
| `get_marketing_v_campaigns_campaign_guid_assets_asset_type` | Retrieves assets of a specified type for a given marketing campaign, supporting optional filtering by date range and pagination. |
| `post_marketing_v_campaigns_batch_archive` | Archives a batch of marketing campaigns using the HubSpot API, requiring a JSON request body and returning a 204 status upon successful completion. |
| `put_marketing_v_campaigns_campaign_guid_assets_asset_type_asset_id` | Updates a specific asset of a given type within a marketing campaign identified by campaignGuid. |
| `delete_marketing_v_campaigns_campaign_guid_assets_asset_type_asset_id` | Deletes a specific asset from a marketing campaign using the provided campaign GUID, asset type, and asset ID. |
| `get_marketing_v_campaigns_campaign_guid_reports_revenue` | Retrieves revenue reports for a specific marketing campaign using the provided campaign GUID, with optional filtering by attribution model and date range. |
| `post_marketing_v_campaigns_batch_create` | Creates multiple marketing campaigns in a single operation using the "POST" method, accepting a JSON body with campaign details and returning a status message upon successful creation. |
| `get_marketing_v_campaigns_campaign_guid_budget_totals` | Retrieves the total budget details for a marketing campaign using the campaign's GUID. |
| `get_marketing_v_campaigns_campaign_guid` | Retrieves detailed information about a specific marketing campaign identified by its campaignGuid, optionally filtered by date range and selected properties. |
| `delete_marketing_v_campaigns_campaign_guid` | Deletes a marketing campaign using the provided campaign GUID and returns a 204 No Content response. |
| `patch_marketing_v_campaigns_campaign_guid` | Updates specified properties of a marketing campaign identified by the campaignGuid using a JSON patch document. |
| `get_marketing_v_campaigns_campaign_guid_reports_contacts_contact_type` | Retrieves a report of contacts of a specified type for a marketing campaign, allowing optional filtering by start and end dates and pagination. |
| `get_marketing_v_emails_statistics_list` | Retrieves email statistics for a specified time range and optional email IDs and properties using the GET method. |
| `post_marketing_v_emails_ab_test_create_variation` | Creates a variation for an A/B test email using the POST method and returns a successful creation status. |
| `get_marketing_v_emails_statistics_histogram` | Retrieves histogram statistics for marketing emails filtered by optional parameters such as interval, time range, and specific email IDs. |
| `get_marketing_v_emails_email_id_ab_test_get_variation` | Retrieves the variation for an A/B test associated with a specific email by its ID using the GET method. |
| `post_marketing_v_emails_email_id_draft_reset` | Resets the draft status of an email using the specified email ID. |
| `post_marketing_v_emails_email_id_revisions_revision_id_restore_to_draft` | Restores a specified email revision to draft status by email ID and revision ID. |
| `get_marketing_v_emails_email_id_draft` | Retrieves the draft of an email with the specified `{emailId}` using the marketing API. |
| `patch_marketing_v_emails_email_id_draft` | Updates a draft email identified by the specified emailId using the provided JSON data. |
| `get_marketing_v_emails_email_id_revisions` | Get a list of revisions for a specified marketing email, optionally filtered by date range and limited in number. |
| `get_marketing_v_emails_email_id_revisions_revision_id` | Retrieves a specific revision of an email identified by the provided email ID and revision ID using the GET method. |
| `post_marketing_v_emails_clone` | Clones a marketing email using the POST method at the "/marketing/v3/emails/clone" endpoint, creating a duplicate email with the same properties as the original but with a unique ID. |
| `get_marketing_v_emails` | Retrieves a list of marketing emails with optional filtering, sorting, pagination, and inclusion of statistics. |
| `post_marketing_v_emails` | Creates a new email resource in the marketing system using the provided JSON data and returns a success response upon creation. |
| `post_marketing_v_emails_email_id_revisions_revision_id_restore` | Restores a specific email revision using the provided email ID and revision ID via the POST method. |
| `get_marketing_v_emails_email_id` | Retrieves detailed information about a specific email by its ID, optionally including statistics, selected properties, and archived status. |
| `delete_marketing_v_emails_email_id` | Deletes the specified marketing email by its emailId, optionally archiving it, and returns a 204 No Content status on success. |
| `patch_marketing_v_emails_email_id` | Updates an email resource identified by `{emailId}` with partial modifications using JSON in the request body and optionally sets its archived status. |
| `batch_read_by_properties` | Retrieves a batch of product records from the CRM using the POST method, optionally filtering by archived status, and returns the results in a multi-status response. |
| `basic_read_product_by_id` | Retrieves detailed information about a specific product by its ID, allowing optional filtering by properties, properties with history, associations, and archived status. |
| `basic_archive_product` | Deletes a product from the CRM using its product ID. |
| `basic_update_product` | Updates specified properties of a product identified by productId using a JSON PATCH request. |
| `public_object_merge_products_same_type` | Merges two or more product records in a CRM system using the POST method, allowing for the consolidation of data into a single, unified record. |
| `batch_archive_products_by_ids` | Archives a batch of products by ID using the POST method, accepting JSON-formatted request bodies and returning a 204 status upon successful execution. |
| `batch_create_products_batch` | Creates multiple product records in a single batch request within the CRM system. |
| `batch_update_products_batch` | Updates multiple product records in a batch using the HubSpot CRM v3 API and returns a status response indicating success or partial failure. |
| `gdpr_delete_contact` | Performs a GDPR-compliant deletion of product records in the CRM using the POST method, requiring a JSON request body and authentication. |
| `basic_list_products_page` | Retrieves a list of products from a CRM system using the "GET" method, allowing for optional filtering and customization of the returned data based on parameters such as limit, after, properties, properties with history, associations, and archived status. |
| `basic_create_product_object` | Creates a new product in the CRM product library to manage the collection of goods and services offered by the company. |
| `search_products_by_criteria` | Searches for products in a CRM using a POST request to the "/crm/v3/objects/products/search" endpoint, allowing for filtering and retrieval of product data in a JSON format. |
| `pipelines_get_by_id` | Retrieves details about a specific CRM pipeline by its ID and object type, providing information about the stages and records within that pipeline. |
| `pipelines_replace_pipeline_object` | Updates the details of a specified pipeline for a given CRM object type by replacing its properties using the provided JSON payload. |
| `pipelines_remove_by_id` | Deletes a pipeline by its ID and object type in the CRM system using the specified security permissions, optionally validating references and deal stage usages before deletion. |
| `pipelines_update_pipeline_by_id` | Updates a CRM pipeline by specifying the object type and pipeline ID, allowing modifications to its configuration with optional validation checks for references and deal stage usage before deletion. |
| `pipeline_audits_get_by_pipeline_id` | Retrieves an audit of all changes to a specific pipeline in HubSpot CRM, based on the provided object type and pipeline ID. |
| `pipeline_stages_get_all` | Retrieves the list of stages within a specified pipeline for a given object type in the CRM system. |
| `pipeline_stages_create_stage_object` | Creates a new stage in a specified CRM pipeline using the POST method, requiring the object type and pipeline ID, and a JSON-formatted request body. |
| `pipelines_get_all` | Retrieves a list of pipelines for a specified object type in the CRM, allowing for the management and inspection of pipelines relevant to that object type. |
| `pipelines_create_new_pipeline_object` | Creates a new pipeline for the specified CRM object type with the provided pipeline details. |
| `pipeline_stages_get_by_id` | Retrieves detailed information about a specific stage within a given pipeline and object type in the CRM system. |
| `pipeline_stages_replace_stage_object` | Updates a specific stage in a CRM pipeline using the provided JSON data and returns a status message. |
| `pipeline_stages_delete_stage` | Deletes a specific stage from a pipeline for the given object type in the CRM system. |
| `pipeline_stages_update_stage_by_id` | Updates a specific stage in a CRM pipeline using a PATCH request to the "/crm/v3/pipelines/{objectType}/{pipelineId}/stages/{stageId}" endpoint, requiring a JSON body with the necessary updates. |
| `batch_read_companies_by_properties` | Reads a batch of companies by internal ID or unique property values using the HubSpot CRM API and returns the results in a JSON format. |
| `basic_read_company_object` | Retrieves a specific company record by ID from the CRM system, optionally including additional properties, associations, and historical data, depending on the query parameters provided. |
| `basic_archive_company` | Deletes a company by its ID using the DELETE method, requiring the company ID as a path parameter and authorization through OAuth2 or private apps with the "crm.objects.companies.write" permission. |
| `basic_update_company_object` | Updates a company in the CRM using the PATCH method, allowing partial modifications to the company's properties. |
| `public_object_merge_companies_same_type` | Merges two or more company records into a single unified record using the CRM API, requiring a JSON payload and appropriate write permissions. |
| `batch_archive_companies_by_id_batch` | Archives a batch of companies using the HubSpot CRM API, requiring a JSON body and returning a 204 status on successful operation. |
| `batch_create_companies_batch` | Creates multiple company records in batch using the HubSpot CRM API and returns a status message, requiring authorization via OAuth2 or private apps. |
| `batch_update_companies_batch` | Updates multiple company records in a single request using the HubSpot CRM API. |
| `gdpr_permanently_delete_contact_company` | Performs a GDPR-compliant deletion of a company record in the CRM, permanently removing the associated personal data. |
| `basic_list_companies_page` | Retrieves a list of company records from a CRM system, allowing for filtering by properties, associations, and archived status. |
| `basic_create_company_object` | Creates a new company record in the CRM system using the provided JSON data and returns a 201 status code upon successful creation. |
| `search_company_objects` | Searches for and retrieves company records and their associated properties in the CRM based on specified criteria. |
| `settings_get_calling_config` | Retrieves the calling settings for a specified application in HubSpot CRM using the provided app ID. |
| `settings_configure_calling_extension` | Configures calling settings for a specified application ID in the CRM using a POST request with a JSON body. |
| `settings_delete_calling_extension` | Deletes the settings for a specified CRM application identified by `{appId}`, returning a successful response with no content if the operation is completed. |
| `settings_update_calling_extension` | Updates specific settings for the calling extension of the specified application by applying partial modifications to its resource. |
| `recording_settings_get_by_app_id` | Retrieves the recording settings for a calling extension with the specified `appId` in the HubSpot CRM. |
| `recording_settings_set_call_recording` | Configures call recording settings for a specific application ID in the CRM using a POST request to update the recording settings. |
| `recording_settings_update_calling_settings` | Modifies the recording settings for a specific CRM application using the provided JSON body. |
| `batch_read_quotes_by_property_values` | Reads a batch of quote objects by their internal IDs or unique property values, optionally including archived quotes, in a single POST request. |
| `basic_read_quote_by_id` | Retrieves a specific sales quote by its ID, optionally including custom properties, property history, associations, and archived status, using the HubSpot CRM API. |
| `basic_archive_quote_object` | Deletes a sales quote with the specified ID using the HubSpot CRM API, requiring "crm.objects.quotes.write" permission. |
| `basic_update_quote_object` | Updates a quote object with the specified ID in the CRM system using partial modifications, requiring a JSON body with the changes and returning a status message upon success. |
| `public_object_merge_two_quotes_same_type` | Merges quote objects in a CRM system using the POST method, allowing for the integration of data from multiple quotes into a single unified quote. |
| `batch_archive_quotes_by_id_batch` | Archives a batch of quotes by sending a POST request to the "/crm/v3/objects/quotes/batch/archive" endpoint, requiring a JSON body and authentication via OAuth2 or private apps with the "crm.objects.quotes.write" permission. |
| `batch_create_quotes_batch` | Creates a batch of sales quotes using the HubSpot CRM API, requiring a JSON body and returning a status message upon successful creation. |
| `batch_update_quotes_batch` | Updates a batch of quote objects in the CRM system using a single POST request, returning a status code indicating success or partial failure. |
| `gdpr_permanently_delete_contact_quotes` | Performs a GDPR-compliant deletion of a quote object in the CRM system, permanently removing the associated personal data. |
| `basic_list_quotes_page` | Retrieves a list of quotes from the CRM, allowing for optional filtering by limit, after, properties, properties with history, associations, and archived status. |
| `basic_create_quote_object` | Creates a new quote in HubSpot using the CRM API and returns a status message upon successful creation. |
| `search_quotes_by_criteria` | Searches for quotes in a CRM system using specified criteria and returns the results, requiring authentication via OAuth2 or private apps with read permissions for quotes. |
| `batch_read_deals_by_internal_id_or_property_values` | Reads a batch of deals from the CRM using the provided IDs and returns the specified properties, allowing for optional filtering by archived status. |
| `basic_read_deal_by_id` | Retrieves a deal by its ID and returns its details, supporting optional parameters for specifying properties, associations, and archived status. |
| `basic_archive_deal_object` | Deletes a specific deal by its ID from the CRM system. |
| `basic_update_deal_object` | Updates an individual deal in the CRM by its record ID using the PATCH method. |
| `public_object_merge_deals_same_type` | Merges two or more deal records into a single master deal record, consolidating data and deleting duplicates in the CRM system. |
| `batch_archive_deals_by_ids` | Archives a batch of deal records in the CRM by their IDs using the POST method. |
| `batch_create_deals_object` | Creates multiple deals in a CRM using a batch operation via the POST method, requiring a JSON body with deal data and appropriate permissions for writing deals. |
| `batch_update_deals_objects` | Updates multiple deals in HubSpot CRM in a single operation using a POST request to "/crm/v3/objects/deals/batch/update", requiring a JSON body with deal identifiers and updates, and supports OAuth2 and private app authentication for the "crm.objects.deals.write" scope. |
| `gdpr_permanently_delete_deal` | Deletes a deal record in compliance with GDPR requirements using the provided JSON payload, requiring a valid OAuth2 or private app authentication with the necessary write permissions. |
| `basic_get_deals_page` | Retrieves a list of CRM deal objects from HubSpot using the GET method, allowing optional filtering by parameters such as limit, after, properties, propertiesWithHistory, associations, and archived status. |
| `basic_create_deal_object` | Creates a new deal object in the CRM using the HubSpot API, requiring a JSON payload and returning a status code indicating success. |
| `search_deals_by_criteria` | Searches and retrieves deal records in the CRM using filters and criteria provided in the request body. |
| `core_cancel_import` | Cancels an active import operation in a CRM system using the provided import ID. |
| `core_get_import_record` | Retrieves the status and details of a specific CRM import operation identified by the import ID. |
| `public_imports_get_error_details` | Retrieves a list of errors associated with a specific CRM import operation, using the import ID, and allows filtering by optional parameters such as "after" and "limit". |
| `core_get_existing_schema` | Retrieves the schema definition for a specified CRM object type, including its properties and metadata. |
| `core_delete_schema` | Deletes the specified CRM object schema by its type, optionally including archived versions, to remove its definition from the system. |
| `core_update_schema_object` | Updates a custom CRM object schema in HubSpot using the PATCH method, allowing for partial modifications to the schema of a specified object type. |
| `core_create_association` | Creates a new association definition for the specified CRM object type to define relationships between that object and others. |
| `public_object_schemas_purge_object_schema` | Purges a schema for a specific object type in the CRM system using the DELETE method, requiring the objectType as a path parameter and a custom write permission. |
| `core_remove_association` | Removes an association identified by the associationIdentifier from a CRM object schema of the specified objectType using the HubSpot API. |
| `core_get_all_schemas` | Retrieves a list of custom object schemas in the CRM, optionally filtering by archived status, using either legacy private apps or OAuth2 credentials for authentication. |
| `core_define_object_schema` | Creates a new custom object schema in the CRM to define a new type of CRM record. |
| `batch_archive_properties` | Archives a batch of properties for a specified object type in CRM using a POST request. |
| `groups_read_property_group` | Retrieves details of a specified property group for a given CRM object type. |
| `groups_archive_property_group` | Deletes a property group identified by the given object type and group name from the CRM schema. |
| `groups_update_property_group` | Modifies the properties of a specified group in a CRM object type using the PATCH method, requiring authentication and a JSON request body to update the group's properties. |
| `core_read_property` | Retrieves the details of a specific property for a given CRM object type, optionally including archived properties and additional specified fields. |
| `core_archive_property` | Deletes a specified property of a given object type in the CRM system. |
| `core_update_property_by_id` | Updates the specified property of a given CRM object type by applying partial modifications using a JSON Patch request. |
| `batch_read_properties` | Performs a batch read operation on CRM properties for a specified object type using a POST request, returning the results in a batch format. |
| `batch_properties_create_batch` | Creates multiple properties in batches for a specified object type in the CRM using a POST request to the "/crm/v3/properties/{objectType}/batch/create" endpoint. |
| `core_get_all_properties` | Retrieves a list of properties for a specified CRM object type using the HubSpot API, allowing for optional filtering by archived status and specific properties. |
| `core_create_property` | Creates a new custom property for a specified CRM object type. |
| `groups_read_all_property` | Retrieves a list of groups for a specified object type in the CRM using the "GET" method at the path "/crm/v3/properties/{objectType}/groups". |
| `groups_create_copy` | Creates a new property group for the specified CRM object type to organize related properties within HubSpot records. |
| `owners_get_by_id` | Retrieves detailed information about a specific CRM owner by their ID using the HubSpot API. |
| `events_create_multiple_batch` | Creates multiple timeline events in a batch using the provided event templates and returns a response with the created events. |
| `templates_get_specific_event_template` | Retrieves a specific event template by its ID for an application in HubSpot CRM, using the provided app ID and event template ID. |
| `templates_update_event_template` | Updates an existing event template in the HubSpot CRM timeline for a specific app, using the provided event template ID and app ID, and returns a status message. |
| `templates_delete_event_template` | Deletes an event template with the specified `eventTemplateId` associated with the application identified by `appId` in a CRM system, returning a successful response with no content upon completion. |
| `events_create_single_event` | Creates a new timeline event in a CRM record based on an event template, adding custom event information to the timeline of a contact, company, or deal. |
| `tokens_add_to_event_template` | Creates a new token for an event template in the HubSpot CRM timeline using the provided JSON data. |
| `tokens_update_existing_token_on_event_template` | Updates a specific token in an event template within a CRM timeline using the provided JSON data. |
| `tokens_remove_from_template` | Deletes a token by the specified name from an event template in the CRM timeline for a given application ID. |
| `events_render_detail_template` | Retrieves detailed information for a specific timeline event identified by its event template ID and event ID in the CRM. |
| `events_get_event_by_id` | Retrieves a specific timeline event by its event template ID and event ID, returning detailed information about that event in the CRM. |
| `templates_list_event_templates` | Retrieves a list of event templates for a specified app ID in the HubSpot CRM API. |
| `templates_create_event_template_for_app` | Creates a new event template for a specified application ID in HubSpot's CRM timeline using the provided JSON payload. |
| `events_rendering_html` | Retrieves and renders a specific timeline event from a CRM object using an event template and event ID, allowing for optional detailed rendering. |
| `batch_read_contacts_by_properties` | Retrieves a batch of contacts from the CRM using the provided identifiers and properties, supporting optional filtering by archived status. |
| `basic_read_contact_by_id` | Retrieves a contact by ID from the CRM, allowing for optional filtering by properties, properties with history, associations, and archived status. |
| `basic_archive_contact` | Deletes a contact by its ID from the CRM system, permanently removing all associated content in compliance with GDPR, and requires the "crm.objects.contacts.write" permission. |
| `basic_update_contact_object` | Updates an individual contact by its record ID using a PATCH request to the "/crm/v3/objects/contacts/{contactId}" endpoint, requiring a JSON body with the fields to be updated. |
| `public_object_merge_contacts_same_type` | Merges two or more duplicate contact records into a single record in the CRM system, retaining the most relevant data while discarding redundant information. |
| `batch_archive_contacts_by_id_batch` | Archives a batch of contacts by ID using the HubSpot CRM API, returning a "204 No Content" response upon success. |
| `batch_create_contacts` | Creates a batch of contacts in HubSpot using the CRM API, requiring a JSON payload and OAuth2 or private app authentication. |
| `batch_update_contacts_batch` | Updates multiple contact records in a single request by providing their IDs or unique property values, overwriting specified properties in batch. |
| `gdpr_permanently_delete_contacts` | Permanently deletes a contact and all associated data from the CRM to comply with GDPR requirements. |
| `basic_list_contacts_page` | Retrieves a list of contacts from a CRM system, allowing for optional filtering by limit, pagination, specific properties, property history, associations, and archived status. |
| `basic_create_contact_object` | Creates a new contact in the CRM system using the provided JSON data and returns a successful creation response. |
| `search_contacts_by_criteria` | Searches for contact records in the CRM system based on specified criteria and returns matching contacts. |
| `batch_read_feedback_submissions` | Reads a batch of feedback submissions by sending a POST request, allowing for optional filtering by archived status, and returns the relevant data in JSON format. |
| `basic_read_feedback_submission` | Retrieves detailed information about a specific feedback submission using its ID, with optional parameters to include properties, history, associations, and archived status. |
| `basic_archive_feedback_submission` | Deletes a specific feedback submission identified by the provided `feedbackSubmissionId` from the CRM system. |
| `basic_update_feedback_submission` | Updates specific fields of a feedback submission by ID using partial modifications with a JSON request body. |
| `public_object_merge_feedback_submissions` | Merges feedback submission records using the POST method, requiring a JSON body and supporting OAuth2 and private apps for authentication. |
| `batch_archive_feedback_submissions_by_id` | Archives a batch of feedback submissions by ID using the HubSpot API and returns a status response with a 204 status code upon successful completion. |
| `batch_create_feedback_submissions` | Creates a batch of feedback submissions using the HubSpot API, allowing for the simultaneous creation of multiple feedback submissions. |
| `batch_update_feedback_submissions` | Updates multiple feedback submissions in batches using the HubSpot CRM API. |
| `gdpr_permanently_delete_contact_feedback_submission` | Permanently deletes feedback submissions and associated data to comply with GDPR regulations using the provided JSON body. |
| `basic_list_feedback_submissions_page` | Retrieves a list of feedback submissions from HubSpot CRM, allowing for optional filtering by limit, pagination, specific properties, property history, associations, and archived status. |
| `basic_create_feedback_submission` | Searches for feedback submissions using the HubSpot CRM API and returns relevant results. |
| `search_feedback_submissions` | Searches for feedback submissions in HubSpot CRM using the POST method, allowing developers to filter and retrieve specific feedback data. |
| `batch_read_objects_by_internal_id_or_property_values` | Performs a batch read operation on CRM objects of the specified type, allowing for the retrieval of multiple records in a single request, with optional filtering by archived status. |
| `basic_read_object_by_id` | Retrieves a specific CRM object record by its object type and ID, allowing for optional specification of properties, associations, and other query parameters. |
| `basic_archive_object` | Deletes a specified CRM object of the given type and ID using the DELETE method. |
| `basic_update_object` | Updates a specific CRM object using the PATCH method by modifying its properties based on the provided JSON body. |
| `public_object_merge_objects_with_type` | Merges duplicate records of a specified object type into a single record using the provided JSON body. |
| `batch_archive_objects_by_id` | Archives a batch of objects of a specified type in CRM using the POST method, requiring a JSON body and returning a 204 status code upon successful archiving. |
| `batch_create_objects` | Creates multiple records of a specified object type in a CRM system using a single POST request, supporting batch creation and returning a status message based on the outcome. |
| `batch_update_objects_by_internal_id_or_property_values` | Updates multiple records of a specified object type in a CRM system using a batch operation via the POST method. |
| `gdpr_permanently_delete_contact_object` | Permanently deletes an object of the specified type from the CRM, adhering to GDPR guidelines for data removal, using the "POST" method with the object type specified in the path and additional details in the request body. |
| `basic_list_objects_page` | Retrieves a list of records for a specified CRM object type with optional filtering, pagination, property selection, association inclusion, and archived status. |
| `basic_create_crmobject` | Creates a new object of the specified type in a CRM system using the provided JSON data, returning a status message upon successful creation. |
| `search_objects_by_criteria` | Searches for objects of a specified type within a CRM using the provided JSON payload, filtering by various criteria to return a list of matching objects. |
| `settings_get_by_id` | Retrieves the video conferencing settings for a specific application identified by the provided appId using the HubSpot API. |
| `settings_update_video_conferencing_app_settings` | Updates video conferencing settings for a specific application identified by its `appId` using the provided JSON data. |
| `settings_delete_video_conferencing_app_settings` | Deletes the video conferencing settings for the specified app identified by the appId. |
| `batch_read_tickets_by_properties` | Retrieves and formats a batch of tickets from HubSpot CRM using a POST request to the "/crm/v3/objects/tickets/batch/read" endpoint. |
| `basic_read_ticket_by_id` | Retrieves a specific ticket record by ID from the CRM, optionally including specified properties, property history, associations, and archived status. |
| `basic_archive_ticket` | Deletes a ticket by its ID using the CRM API. |
| `basic_update_ticket_object` | Updates an individual ticket by its ID using the HubSpot CRM API, allowing modification of specific fields via a JSON payload. |
| `public_object_merge_tickets_same_type` | Merges two or more tickets into a single ticket in the CRM system using the POST method, allowing for the consolidation of related customer service requests. |
| `batch_archive_tickets_by_id` | Archives a batch of tickets by ID using the HubSpot API and returns a status message. |
| `batch_ticket_creation_batch` | Creates a batch of tickets in the CRM using the HubSpot API and returns a status message. |
| `batch_update_tickets_batch` | Updates multiple tickets in a single request using the HubSpot CRM API, returning a status message indicating the success or partial success of the operation. |
| `gdpr_permanently_delete_contact` | Permanently deletes a ticket and associated data in compliance with GDPR guidelines using the POST method. |
| `basic_list_tickets_page` | Retrieves a list of tickets from the CRM, allowing for filtering by limit, after cursor, specific properties, properties with history, associations, and archived status. |
| `basic_create_ticket_object` | Creates a new ticket object in the CRM using the HubSpot API, allowing for the management of customer service requests. |
| `search_tickets_by_criteria` | Searches and filters ticket records within the CRM system based on specified criteria, returning matching ticket results. |
| `batch_read_line_items` | Retrieves a batch of line items by internal ID or unique property values using the HubSpot CRM API. |
| `basic_read_line_item_by_id` | Retrieves a specific line item by its ID from the CRM, optionally including additional properties, associations, and history, using the CRM API with appropriate permissions. |
| `basic_archive_line_item` | Deletes a line item from HubSpot CRM using its ID, requiring the "crm.objects.line_items.write" permission. |
| `basic_update_line_item_object` | Updates properties of a specific line item in the CRM system using a partial JSON patch request. |
| `public_object_merge_line_items_same_type` | Merges duplicate line items into a single instance using the specified parameters via the POST method. |
| `batch_archive_line_items_by_ids` | Archives a batch of line items by their IDs in the CRM using a POST request. |
| `batch_line_items_create_batch` | Creates a batch of line items using the HubSpot API and returns a status message upon successful creation. |
| `batch_update_line_items` | Updates a batch of line items using their internal IDs or unique property values via the POST method, requiring authentication with the "crm.objects.line_items.write" scope. |
| `gdpr_delete_contact_content` | Deletes line item records from the CRM to comply with GDPR requirements, using the POST method with OAuth2 or private app authentication. |
| `basic_list_line_items_page` | Retrieves a paginated list of line items with optional filters for properties, associations, and archival status in the CRM. |
| `basic_create_line_item_object` | Creates a new line item in HubSpot CRM using the POST method, allowing you to add products or services to deals and quotes. |
| `search_line_items_by_criteria` | Searches and retrieves line items and their associated properties in the CRM based on specified filter criteria. |
| `core_get_active_imports_page` | Retrieves a list of CRM import operations using the HubSpot API, allowing optional filtering by date and limit on the number of results returned. |
| `core_start_import` | Imports data into a HubSpot CRM using a POST request with a multipart/form-data payload, allowing bulk creation or update of records via uploaded files such as CSV or Excel. |
| `owners_get_page` | Retrieves a list of CRM owners using the "GET" method, allowing optional filtering by email, pagination, and archived status, and returns a response with owner details. |
| `get_crm_v_associations_from_object_type_to_object_type_types_get_all` | Retrieves the association types between two specified object types in HubSpot CRM using the "GET" method. |
