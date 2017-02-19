# messagemedia_rest_api.MessagingReportsApi

All URIs are relative to *https://api.messagemedia.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_async_report_by_id**](MessagingReportsApi.md#get_async_report_by_id) | **GET** /reporting/async_reports/{report_id} | Lists an asynchronous report.
[**get_async_report_data_by_id**](MessagingReportsApi.md#get_async_report_data_by_id) | **GET** /reporting/async_reports/{report_id}/data | Gets the data of an asynchronous report.
[**get_async_reports**](MessagingReportsApi.md#get_async_reports) | **GET** /reporting/async_reports | Gets a single asynchronous report.
[**get_delivery_reports_detail**](MessagingReportsApi.md#get_delivery_reports_detail) | **GET** /reporting/delivery_reports/detail | Returns a list of delivery reports
[**get_delivery_reports_summary**](MessagingReportsApi.md#get_delivery_reports_summary) | **GET** /reporting/delivery_reports/summary | Returns a summarised report of delivery reports
[**get_metadata_keys**](MessagingReportsApi.md#get_metadata_keys) | **GET** /reporting/{messageType}/metadata/keys | Returns a list of metadata keys
[**get_received_messages_detail**](MessagingReportsApi.md#get_received_messages_detail) | **GET** /reporting/received_messages/detail | Returns a list message received
[**get_received_messages_summary**](MessagingReportsApi.md#get_received_messages_summary) | **GET** /reporting/received_messages/summary | Returns a summarised report of messages received
[**get_sent_messages_detail**](MessagingReportsApi.md#get_sent_messages_detail) | **GET** /reporting/sent_messages/detail | Returns a list of message sent
[**get_sent_messages_summary**](MessagingReportsApi.md#get_sent_messages_summary) | **GET** /reporting/sent_messages/summary | Returns a summarised report of messages sent
[**submit_async_delivery_reports_detail**](MessagingReportsApi.md#submit_async_delivery_reports_detail) | **POST** /reporting/delivery_reports/detail/async | Submits a request to generate an async detail report
[**submit_delivery_reports_summary**](MessagingReportsApi.md#submit_delivery_reports_summary) | **POST** /reporting/delivery_reports/summary/async | Submits a summarised report of delivery reports
[**submit_received_messages_detail**](MessagingReportsApi.md#submit_received_messages_detail) | **POST** /reporting/received_messages/detail/async | Submits a request to generate an async detail report
[**submit_received_messages_summary**](MessagingReportsApi.md#submit_received_messages_summary) | **POST** /reporting/received_messages/summary/async | Submits a summarised report of received messages
[**submit_sent_messages_detail**](MessagingReportsApi.md#submit_sent_messages_detail) | **POST** /reporting/sent_messages/detail/async | Submits a request to generate an async detail report
[**submit_sent_messages_summary**](MessagingReportsApi.md#submit_sent_messages_summary) | **POST** /reporting/sent_messages/summary/async | Submits a summarised report of sent messages


# **get_async_report_by_id**
> AsyncReport get_async_report_by_id(report_id)

Lists an asynchronous report.

This endpoints lists metadata of a requested asynchronous report.

### Example 
```python
import time
import messagemedia_rest_api
from messagemedia_rest_api.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
messagemedia_rest_api.configuration.username = 'YOUR_USERNAME'
messagemedia_rest_api.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = messagemedia_rest_api.MessagingReportsApi()
report_id = 'report_id_example' # str | Unique ID of the async report

try: 
    # Lists an asynchronous report.
    api_response = api_instance.get_async_report_by_id(report_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling MessagingReportsApi->get_async_report_by_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_id** | **str**| Unique ID of the async report | 

### Return type

[**AsyncReport**](AsyncReport.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_async_report_data_by_id**
> file get_async_report_data_by_id(report_id)

Gets the data of an asynchronous report.

This endpoints gets the data of an asynchronous report as a download.

### Example 
```python
import time
import messagemedia_rest_api
from messagemedia_rest_api.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
messagemedia_rest_api.configuration.username = 'YOUR_USERNAME'
messagemedia_rest_api.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = messagemedia_rest_api.MessagingReportsApi()
report_id = 'report_id_example' # str | Unique ID of the async report

try: 
    # Gets the data of an asynchronous report.
    api_response = api_instance.get_async_report_data_by_id(report_id)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling MessagingReportsApi->get_async_report_data_by_id: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_id** | **str**| Unique ID of the async report | 

### Return type

[**file**](file.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_async_reports**
> InlineResponse200 get_async_reports()

Gets a single asynchronous report.

This endpoint lists metadata about requested async reports.

### Example 
```python
import time
import messagemedia_rest_api
from messagemedia_rest_api.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
messagemedia_rest_api.configuration.username = 'YOUR_USERNAME'
messagemedia_rest_api.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = messagemedia_rest_api.MessagingReportsApi()

try: 
    # Gets a single asynchronous report.
    api_response = api_instance.get_async_reports()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling MessagingReportsApi->get_async_reports: %s\n" % e
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_delivery_reports_detail**
> DeliveryReports get_delivery_reports_detail(end_date, start_date, accounts=accounts, destination_address_country=destination_address_country, destination_address=destination_address, message_format=message_format, metadata_key=metadata_key, metadata_value=metadata_value, status_code=status_code, status=status, page=page, page_size=page_size, sort_by=sort_by, sort_direction=sort_direction, source_address_country=source_address_country, source_address=source_address, timezone=timezone)

Returns a list of delivery reports

Returns a detailed list of all delivery reports received during the specified time

### Example 
```python
import time
import messagemedia_rest_api
from messagemedia_rest_api.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
messagemedia_rest_api.configuration.username = 'YOUR_USERNAME'
messagemedia_rest_api.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = messagemedia_rest_api.MessagingReportsApi()
end_date = 'end_date_example' # str | End date time for report window. By default, the timezone for this parameter will be taken from the account settings for the account associated with the credentials used to make the request, or the account included in the Account parameter. This can be overridden using the timezone parameter per request. The date must be in the format of \"yyyy-MM-dd'T'HH:mm:ss\", e.g. \"2017-02-10T13:30:00\".
start_date = 'start_date_example' # str | Start date time for report window. By default, the timezone for this parameter will be taken from the account settings for the account associated with the credentials used to make the request, or the account included in the Account parameter. This can be overridden using the timezone parameter per request. The date must be in the format of \"yyyy-MM-dd'T'HH:mm:ss\", e.g. \"2017-02-10T13:30:00\".
accounts = 'accounts_example' # str | Filter results by a specific account. By default results will be returned for the account associated with the authentication credentials and all sub accounts. (optional)
destination_address_country = 'destination_address_country_example' # str | Filter results by destination address country. (optional)
destination_address = 'destination_address_example' # str | Filter results by destination address. (optional)
message_format = 'message_format_example' # str | Filter results by message format. (optional)
metadata_key = 'metadata_key_example' # str | Filter results for messages that include a metadata key. (optional)
metadata_value = 'metadata_value_example' # str | Filter results for messages that include a metadata key containing this value. If this parameter is provided, the metadata_key parameter must also be provided. (optional)
status_code = 'status_code_example' # str | Filter results by message status code. (optional)
status = 'status_example' # str | Filter results by message status. (optional)
page = 56 # int | Page number for paging through paginated result sets. (optional)
page_size = 56 # int | Number of results to return in a page for paginated result sets. (optional)
sort_by = 'sort_by_example' # str | Field to sort results set by (optional)
sort_direction = 'sort_direction_example' # str | Order to sort results by. (optional)
source_address_country = 'source_address_country_example' # str | Filter results by source address country. (optional)
source_address = 'source_address_example' # str | Filter results by source address. (optional)
timezone = 'timezone_example' # str | The timezone to use for the context of the request. If provided this will be used as the timezone for the start date and end date parameters, and all datetime fields returns in the response. The timezone should be provided as a IANA (Internet Assigned Numbers Authority) time zone database zone name, i.e. 'Australia/Melbourne'. (optional)

try: 
    # Returns a list of delivery reports
    api_response = api_instance.get_delivery_reports_detail(end_date, start_date, accounts=accounts, destination_address_country=destination_address_country, destination_address=destination_address, message_format=message_format, metadata_key=metadata_key, metadata_value=metadata_value, status_code=status_code, status=status, page=page, page_size=page_size, sort_by=sort_by, sort_direction=sort_direction, source_address_country=source_address_country, source_address=source_address, timezone=timezone)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling MessagingReportsApi->get_delivery_reports_detail: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **end_date** | **str**| End date time for report window. By default, the timezone for this parameter will be taken from the account settings for the account associated with the credentials used to make the request, or the account included in the Account parameter. This can be overridden using the timezone parameter per request. The date must be in the format of \&quot;yyyy-MM-dd&#39;T&#39;HH:mm:ss\&quot;, e.g. \&quot;2017-02-10T13:30:00\&quot;. | 
 **start_date** | **str**| Start date time for report window. By default, the timezone for this parameter will be taken from the account settings for the account associated with the credentials used to make the request, or the account included in the Account parameter. This can be overridden using the timezone parameter per request. The date must be in the format of \&quot;yyyy-MM-dd&#39;T&#39;HH:mm:ss\&quot;, e.g. \&quot;2017-02-10T13:30:00\&quot;. | 
 **accounts** | **str**| Filter results by a specific account. By default results will be returned for the account associated with the authentication credentials and all sub accounts. | [optional] 
 **destination_address_country** | **str**| Filter results by destination address country. | [optional] 
 **destination_address** | **str**| Filter results by destination address. | [optional] 
 **message_format** | **str**| Filter results by message format. | [optional] 
 **metadata_key** | **str**| Filter results for messages that include a metadata key. | [optional] 
 **metadata_value** | **str**| Filter results for messages that include a metadata key containing this value. If this parameter is provided, the metadata_key parameter must also be provided. | [optional] 
 **status_code** | **str**| Filter results by message status code. | [optional] 
 **status** | **str**| Filter results by message status. | [optional] 
 **page** | **int**| Page number for paging through paginated result sets. | [optional] 
 **page_size** | **int**| Number of results to return in a page for paginated result sets. | [optional] 
 **sort_by** | **str**| Field to sort results set by | [optional] 
 **sort_direction** | **str**| Order to sort results by. | [optional] 
 **source_address_country** | **str**| Filter results by source address country. | [optional] 
 **source_address** | **str**| Filter results by source address. | [optional] 
 **timezone** | **str**| The timezone to use for the context of the request. If provided this will be used as the timezone for the start date and end date parameters, and all datetime fields returns in the response. The timezone should be provided as a IANA (Internet Assigned Numbers Authority) time zone database zone name, i.e. &#39;Australia/Melbourne&#39;. | [optional] 

### Return type

[**DeliveryReports**](DeliveryReports.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_delivery_reports_summary**
> SummaryReport get_delivery_reports_summary(end_date, group_by, start_date, accounts=accounts, destination_address_country=destination_address_country, destination_address=destination_address, message_format=message_format, metadata_key=metadata_key, metadata_value=metadata_value, status_code=status_code, status=status, summary_by=summary_by, summary_field=summary_field, source_address_country=source_address_country, source_address=source_address, timezone=timezone)

Returns a summarised report of delivery reports

Returns a summarised report of all delivery reports received during the specified time, grouped by by the specified grouping parameter

### Example 
```python
import time
import messagemedia_rest_api
from messagemedia_rest_api.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
messagemedia_rest_api.configuration.username = 'YOUR_USERNAME'
messagemedia_rest_api.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = messagemedia_rest_api.MessagingReportsApi()
end_date = 'end_date_example' # str | End date time for report window. By default, the timezone for this parameter will be taken from the account settings for the account associated with the credentials used to make the request, or the account included in the Account parameter. This can be overridden using the timezone parameter per request. The date must be in the format of \"yyyy-MM-dd'T'HH:mm:ss\", e.g. \"2017-02-10T13:30:00\".
group_by = 'group_by_example' # str | Field to group results set by
start_date = 'start_date_example' # str | Start date time for report window. By default, the timezone for this parameter will be taken from the account settings for the account associated with the credentials used to make the request, or the account included in the Account parameter. This can be overridden using the timezone parameter per request. The date must be in the format of \"yyyy-MM-dd'T'HH:mm:ss\", e.g. \"2017-02-10T13:30:00\".
accounts = 'accounts_example' # str | Filter results by a specific account. By default results will be returned for the account associated with the authentication credentials and all sub accounts. (optional)
destination_address_country = 'destination_address_country_example' # str | Filter results by destination address country. (optional)
destination_address = 'destination_address_example' # str | Filter results by destination address. (optional)
message_format = 'message_format_example' # str | Filter results by message format. (optional)
metadata_key = 'metadata_key_example' # str | Filter results for messages that include a metadata key. (optional)
metadata_value = 'metadata_value_example' # str | Filter results for messages that include a metadata key containing this value. If this parameter is provided, the metadata_key parameter must also be provided. (optional)
status_code = 'status_code_example' # str | Filter results by message status code. (optional)
status = 'status_example' # str | Filter results by message status. (optional)
summary_by = 'summary_by_example' # str | Function to apply when summarising results (optional)
summary_field = 'summary_field_example' # str | Field to summarise results by (optional)
source_address_country = 'source_address_country_example' # str | Filter results by source address country. (optional)
source_address = 'source_address_example' # str | Filter results by source address. (optional)
timezone = 'timezone_example' # str | The timezone to use for the context of the request. If provided this will be used as the timezone for the start date and end date parameters, and all datetime fields returns in the response. The timezone should be provided as a IANA (Internet Assigned Numbers Authority) time zone database zone name, i.e. 'Australia/Melbourne'. (optional)

try: 
    # Returns a summarised report of delivery reports
    api_response = api_instance.get_delivery_reports_summary(end_date, group_by, start_date, accounts=accounts, destination_address_country=destination_address_country, destination_address=destination_address, message_format=message_format, metadata_key=metadata_key, metadata_value=metadata_value, status_code=status_code, status=status, summary_by=summary_by, summary_field=summary_field, source_address_country=source_address_country, source_address=source_address, timezone=timezone)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling MessagingReportsApi->get_delivery_reports_summary: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **end_date** | **str**| End date time for report window. By default, the timezone for this parameter will be taken from the account settings for the account associated with the credentials used to make the request, or the account included in the Account parameter. This can be overridden using the timezone parameter per request. The date must be in the format of \&quot;yyyy-MM-dd&#39;T&#39;HH:mm:ss\&quot;, e.g. \&quot;2017-02-10T13:30:00\&quot;. | 
 **group_by** | **str**| Field to group results set by | 
 **start_date** | **str**| Start date time for report window. By default, the timezone for this parameter will be taken from the account settings for the account associated with the credentials used to make the request, or the account included in the Account parameter. This can be overridden using the timezone parameter per request. The date must be in the format of \&quot;yyyy-MM-dd&#39;T&#39;HH:mm:ss\&quot;, e.g. \&quot;2017-02-10T13:30:00\&quot;. | 
 **accounts** | **str**| Filter results by a specific account. By default results will be returned for the account associated with the authentication credentials and all sub accounts. | [optional] 
 **destination_address_country** | **str**| Filter results by destination address country. | [optional] 
 **destination_address** | **str**| Filter results by destination address. | [optional] 
 **message_format** | **str**| Filter results by message format. | [optional] 
 **metadata_key** | **str**| Filter results for messages that include a metadata key. | [optional] 
 **metadata_value** | **str**| Filter results for messages that include a metadata key containing this value. If this parameter is provided, the metadata_key parameter must also be provided. | [optional] 
 **status_code** | **str**| Filter results by message status code. | [optional] 
 **status** | **str**| Filter results by message status. | [optional] 
 **summary_by** | **str**| Function to apply when summarising results | [optional] 
 **summary_field** | **str**| Field to summarise results by | [optional] 
 **source_address_country** | **str**| Filter results by source address country. | [optional] 
 **source_address** | **str**| Filter results by source address. | [optional] 
 **timezone** | **str**| The timezone to use for the context of the request. If provided this will be used as the timezone for the start date and end date parameters, and all datetime fields returns in the response. The timezone should be provided as a IANA (Internet Assigned Numbers Authority) time zone database zone name, i.e. &#39;Australia/Melbourne&#39;. | [optional] 

### Return type

[**SummaryReport**](SummaryReport.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_metadata_keys**
> MetadataKeysResponse get_metadata_keys(message_type, start_date, end_date, accounts=accounts, timezone=timezone)

Returns a list of metadata keys

Returns a list of all metadata keys used for the specified message type during the specified time. Results are limited to 100 keys.

### Example 
```python
import time
import messagemedia_rest_api
from messagemedia_rest_api.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
messagemedia_rest_api.configuration.username = 'YOUR_USERNAME'
messagemedia_rest_api.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = messagemedia_rest_api.MessagingReportsApi()
message_type = 'message_type_example' # str | Message type. Possible values are sent messages, received messages and delivery receipts.
start_date = 'start_date_example' # str | Start date time for report window. By default, the timezone for this parameter will be taken from the account settings for the account associated with the credentials used to make the request, or the account included in the Account parameter. This can be overridden using the timezone parameter per request. The date must be in the format of \"yyyy-MM-dd'T'HH:mm:ss\", e.g. \"2017-02-10T13:30:00\".
end_date = 'end_date_example' # str | End date time for report window. By default, the timezone for this parameter will be taken from the account settings for the account associated with the credentials used to make the request, or the account included in the Account parameter. This can be overridden using the timezone parameter per request. The date must be in the format of \"yyyy-MM-dd'T'HH:mm:ss\", e.g. \"2017-02-10T13:30:00\".
accounts = 'accounts_example' # str | Filter results by a specific account. By default results will be returned for the account associated with the authentication credentials and all sub accounts. (optional)
timezone = 'timezone_example' # str | The timezone to use for the context of the request. If provided this will be used as the timezone for the start date and end date parameters, and all datetime fields returns in the response. The timezone should be provided as a IANA (Internet Assigned Numbers Authority) time zone database zone name, i.e. 'Australia/Melbourne'. (optional)

try: 
    # Returns a list of metadata keys
    api_response = api_instance.get_metadata_keys(message_type, start_date, end_date, accounts=accounts, timezone=timezone)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling MessagingReportsApi->get_metadata_keys: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message_type** | **str**| Message type. Possible values are sent messages, received messages and delivery receipts. | 
 **start_date** | **str**| Start date time for report window. By default, the timezone for this parameter will be taken from the account settings for the account associated with the credentials used to make the request, or the account included in the Account parameter. This can be overridden using the timezone parameter per request. The date must be in the format of \&quot;yyyy-MM-dd&#39;T&#39;HH:mm:ss\&quot;, e.g. \&quot;2017-02-10T13:30:00\&quot;. | 
 **end_date** | **str**| End date time for report window. By default, the timezone for this parameter will be taken from the account settings for the account associated with the credentials used to make the request, or the account included in the Account parameter. This can be overridden using the timezone parameter per request. The date must be in the format of \&quot;yyyy-MM-dd&#39;T&#39;HH:mm:ss\&quot;, e.g. \&quot;2017-02-10T13:30:00\&quot;. | 
 **accounts** | **str**| Filter results by a specific account. By default results will be returned for the account associated with the authentication credentials and all sub accounts. | [optional] 
 **timezone** | **str**| The timezone to use for the context of the request. If provided this will be used as the timezone for the start date and end date parameters, and all datetime fields returns in the response. The timezone should be provided as a IANA (Internet Assigned Numbers Authority) time zone database zone name, i.e. &#39;Australia/Melbourne&#39;. | [optional] 

### Return type

[**MetadataKeysResponse**](MetadataKeysResponse.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_received_messages_detail**
> ReceivedMessages get_received_messages_detail(end_date, start_date, accounts=accounts, action=action, destination_address_country=destination_address_country, destination_address=destination_address, message_format=message_format, metadata_key=metadata_key, metadata_value=metadata_value, page=page, page_size=page_size, sort_by=sort_by, sort_direction=sort_direction, source_address_country=source_address_country, source_address=source_address, timezone=timezone)

Returns a list message received

Returns a detailed list of all message received during the specified time

### Example 
```python
import time
import messagemedia_rest_api
from messagemedia_rest_api.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
messagemedia_rest_api.configuration.username = 'YOUR_USERNAME'
messagemedia_rest_api.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = messagemedia_rest_api.MessagingReportsApi()
end_date = 'end_date_example' # str | End date time for report window. By default, the timezone for this parameter will be taken from the account settings for the account associated with the credentials used to make the request, or the account included in the Account parameter. This can be overridden using the timezone parameter per request. The date must be in the format of \"yyyy-MM-dd'T'HH:mm:ss\", e.g. \"2017-02-10T13:30:00\".
start_date = 'start_date_example' # str | Start date time for report window. By default, the timezone for this parameter will be taken from the account settings for the account associated with the credentials used to make the request, or the account included in the Account parameter. This can be overridden using the timezone parameter per request. The date must be in the format of \"yyyy-MM-dd'T'HH:mm:ss\", e.g. \"2017-02-10T13:30:00\".
accounts = 'accounts_example' # str | Filter results by a specific account. By default results will be returned for the account associated with the authentication credentials and all sub accounts. (optional)
action = 'action_example' # str | Filter results by the action that was invoked for this message. (optional)
destination_address_country = 'destination_address_country_example' # str | Filter results by destination address country. (optional)
destination_address = 'destination_address_example' # str | Filter results by destination address. (optional)
message_format = 'message_format_example' # str | Filter results by message format. (optional)
metadata_key = 'metadata_key_example' # str | Filter results for messages that include a metadata key. (optional)
metadata_value = 'metadata_value_example' # str | Filter results for messages that include a metadata key containing this value. If this parameter is provided, the metadata_key parameter must also be provided. (optional)
page = 56 # int | Page number for paging through paginated result sets. (optional)
page_size = 56 # int | Number of results to return in a page for paginated result sets. (optional)
sort_by = 'sort_by_example' # str | Field to sort results set by (optional)
sort_direction = 'sort_direction_example' # str | Order to sort results by. (optional)
source_address_country = 'source_address_country_example' # str | Filter results by source address country. (optional)
source_address = 'source_address_example' # str | Filter results by source address. (optional)
timezone = 'timezone_example' # str | The timezone to use for the context of the request. If provided this will be used as the timezone for the start date and end date parameters, and all datetime fields returns in the response. The timezone should be provided as a IANA (Internet Assigned Numbers Authority) time zone database zone name, i.e. 'Australia/Melbourne'. (optional)

try: 
    # Returns a list message received
    api_response = api_instance.get_received_messages_detail(end_date, start_date, accounts=accounts, action=action, destination_address_country=destination_address_country, destination_address=destination_address, message_format=message_format, metadata_key=metadata_key, metadata_value=metadata_value, page=page, page_size=page_size, sort_by=sort_by, sort_direction=sort_direction, source_address_country=source_address_country, source_address=source_address, timezone=timezone)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling MessagingReportsApi->get_received_messages_detail: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **end_date** | **str**| End date time for report window. By default, the timezone for this parameter will be taken from the account settings for the account associated with the credentials used to make the request, or the account included in the Account parameter. This can be overridden using the timezone parameter per request. The date must be in the format of \&quot;yyyy-MM-dd&#39;T&#39;HH:mm:ss\&quot;, e.g. \&quot;2017-02-10T13:30:00\&quot;. | 
 **start_date** | **str**| Start date time for report window. By default, the timezone for this parameter will be taken from the account settings for the account associated with the credentials used to make the request, or the account included in the Account parameter. This can be overridden using the timezone parameter per request. The date must be in the format of \&quot;yyyy-MM-dd&#39;T&#39;HH:mm:ss\&quot;, e.g. \&quot;2017-02-10T13:30:00\&quot;. | 
 **accounts** | **str**| Filter results by a specific account. By default results will be returned for the account associated with the authentication credentials and all sub accounts. | [optional] 
 **action** | **str**| Filter results by the action that was invoked for this message. | [optional] 
 **destination_address_country** | **str**| Filter results by destination address country. | [optional] 
 **destination_address** | **str**| Filter results by destination address. | [optional] 
 **message_format** | **str**| Filter results by message format. | [optional] 
 **metadata_key** | **str**| Filter results for messages that include a metadata key. | [optional] 
 **metadata_value** | **str**| Filter results for messages that include a metadata key containing this value. If this parameter is provided, the metadata_key parameter must also be provided. | [optional] 
 **page** | **int**| Page number for paging through paginated result sets. | [optional] 
 **page_size** | **int**| Number of results to return in a page for paginated result sets. | [optional] 
 **sort_by** | **str**| Field to sort results set by | [optional] 
 **sort_direction** | **str**| Order to sort results by. | [optional] 
 **source_address_country** | **str**| Filter results by source address country. | [optional] 
 **source_address** | **str**| Filter results by source address. | [optional] 
 **timezone** | **str**| The timezone to use for the context of the request. If provided this will be used as the timezone for the start date and end date parameters, and all datetime fields returns in the response. The timezone should be provided as a IANA (Internet Assigned Numbers Authority) time zone database zone name, i.e. &#39;Australia/Melbourne&#39;. | [optional] 

### Return type

[**ReceivedMessages**](ReceivedMessages.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_received_messages_summary**
> SummaryReport get_received_messages_summary(end_date, group_by, start_date, accounts=accounts, destination_address_country=destination_address_country, destination_address=destination_address, message_format=message_format, metadata_key=metadata_key, metadata_value=metadata_value, summary_by=summary_by, summary_field=summary_field, source_address_country=source_address_country, source_address=source_address, timezone=timezone)

Returns a summarised report of messages received

Returns a summarised report of all messages received during the specified time, grouped by by the specified grouping parameter

### Example 
```python
import time
import messagemedia_rest_api
from messagemedia_rest_api.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
messagemedia_rest_api.configuration.username = 'YOUR_USERNAME'
messagemedia_rest_api.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = messagemedia_rest_api.MessagingReportsApi()
end_date = 'end_date_example' # str | End date time for report window. By default, the timezone for this parameter will be taken from the account settings for the account associated with the credentials used to make the request, or the account included in the Account parameter. This can be overridden using the timezone parameter per request. The date must be in the format of \"yyyy-MM-dd'T'HH:mm:ss\", e.g. \"2017-02-10T13:30:00\".
group_by = 'group_by_example' # str | Field to group results set by
start_date = 'start_date_example' # str | Start date time for report window. By default, the timezone for this parameter will be taken from the account settings for the account associated with the credentials used to make the request, or the account included in the Account parameter. This can be overridden using the timezone parameter per request. The date must be in the format of \"yyyy-MM-dd'T'HH:mm:ss\", e.g. \"2017-02-10T13:30:00\".
accounts = 'accounts_example' # str | Filter results by a specific account. By default results will be returned for the account associated with the authentication credentials and all sub accounts. (optional)
destination_address_country = 'destination_address_country_example' # str | Filter results by destination address country. (optional)
destination_address = 'destination_address_example' # str | Filter results by destination address. (optional)
message_format = 'message_format_example' # str | Filter results by message format. (optional)
metadata_key = 'metadata_key_example' # str | Filter results for messages that include a metadata key. (optional)
metadata_value = 'metadata_value_example' # str | Filter results for messages that include a metadata key containing this value. If this parameter is provided, the metadata_key parameter must also be provided. (optional)
summary_by = 'summary_by_example' # str | Function to apply when summarising results (optional)
summary_field = 'summary_field_example' # str | Field to summarise results by (optional)
source_address_country = 'source_address_country_example' # str | Filter results by source address country. (optional)
source_address = 'source_address_example' # str | Filter results by source address. (optional)
timezone = 'timezone_example' # str | The timezone to use for the context of the request. If provided this will be used as the timezone for the start date and end date parameters, and all datetime fields returns in the response. The timezone should be provided as a IANA (Internet Assigned Numbers Authority) time zone database zone name, i.e. 'Australia/Melbourne'. (optional)

try: 
    # Returns a summarised report of messages received
    api_response = api_instance.get_received_messages_summary(end_date, group_by, start_date, accounts=accounts, destination_address_country=destination_address_country, destination_address=destination_address, message_format=message_format, metadata_key=metadata_key, metadata_value=metadata_value, summary_by=summary_by, summary_field=summary_field, source_address_country=source_address_country, source_address=source_address, timezone=timezone)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling MessagingReportsApi->get_received_messages_summary: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **end_date** | **str**| End date time for report window. By default, the timezone for this parameter will be taken from the account settings for the account associated with the credentials used to make the request, or the account included in the Account parameter. This can be overridden using the timezone parameter per request. The date must be in the format of \&quot;yyyy-MM-dd&#39;T&#39;HH:mm:ss\&quot;, e.g. \&quot;2017-02-10T13:30:00\&quot;. | 
 **group_by** | **str**| Field to group results set by | 
 **start_date** | **str**| Start date time for report window. By default, the timezone for this parameter will be taken from the account settings for the account associated with the credentials used to make the request, or the account included in the Account parameter. This can be overridden using the timezone parameter per request. The date must be in the format of \&quot;yyyy-MM-dd&#39;T&#39;HH:mm:ss\&quot;, e.g. \&quot;2017-02-10T13:30:00\&quot;. | 
 **accounts** | **str**| Filter results by a specific account. By default results will be returned for the account associated with the authentication credentials and all sub accounts. | [optional] 
 **destination_address_country** | **str**| Filter results by destination address country. | [optional] 
 **destination_address** | **str**| Filter results by destination address. | [optional] 
 **message_format** | **str**| Filter results by message format. | [optional] 
 **metadata_key** | **str**| Filter results for messages that include a metadata key. | [optional] 
 **metadata_value** | **str**| Filter results for messages that include a metadata key containing this value. If this parameter is provided, the metadata_key parameter must also be provided. | [optional] 
 **summary_by** | **str**| Function to apply when summarising results | [optional] 
 **summary_field** | **str**| Field to summarise results by | [optional] 
 **source_address_country** | **str**| Filter results by source address country. | [optional] 
 **source_address** | **str**| Filter results by source address. | [optional] 
 **timezone** | **str**| The timezone to use for the context of the request. If provided this will be used as the timezone for the start date and end date parameters, and all datetime fields returns in the response. The timezone should be provided as a IANA (Internet Assigned Numbers Authority) time zone database zone name, i.e. &#39;Australia/Melbourne&#39;. | [optional] 

### Return type

[**SummaryReport**](SummaryReport.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sent_messages_detail**
> SentMessages get_sent_messages_detail(end_date, start_date, accounts=accounts, delivery_report=delivery_report, destination_address_country=destination_address_country, destination_address=destination_address, message_format=message_format, metadata_key=metadata_key, metadata_value=metadata_value, status_code=status_code, status=status, page=page, page_size=page_size, sort_by=sort_by, sort_direction=sort_direction, source_address_country=source_address_country, source_address=source_address, timezone=timezone)

Returns a list of message sent

Returns a detailed list of all message sent during the specified time

### Example 
```python
import time
import messagemedia_rest_api
from messagemedia_rest_api.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
messagemedia_rest_api.configuration.username = 'YOUR_USERNAME'
messagemedia_rest_api.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = messagemedia_rest_api.MessagingReportsApi()
end_date = 'end_date_example' # str | End date time for report window. By default, the timezone for this parameter will be taken from the account settings for the account associated with the credentials used to make the request, or the account included in the Account parameter. This can be overridden using the timezone parameter per request. The date must be in the format of \"yyyy-MM-dd'T'HH:mm:ss\", e.g. \"2017-02-10T13:30:00\".
start_date = 'start_date_example' # str | Start date time for report window. By default, the timezone for this parameter will be taken from the account settings for the account associated with the credentials used to make the request, or the account included in the Account parameter. This can be overridden using the timezone parameter per request. The date must be in the format of \"yyyy-MM-dd'T'HH:mm:ss\", e.g. \"2017-02-10T13:30:00\".
accounts = 'accounts_example' # str | Filter results by a specific account. By default results will be returned for the account associated with the authentication credentials and all sub accounts. (optional)
delivery_report = true # bool | Filter results by delivery report. (optional)
destination_address_country = 'destination_address_country_example' # str | Filter results by destination address country. (optional)
destination_address = 'destination_address_example' # str | Filter results by destination address. (optional)
message_format = 'message_format_example' # str | Filter results by message format. (optional)
metadata_key = 'metadata_key_example' # str | Filter results for messages that include a metadata key. (optional)
metadata_value = 'metadata_value_example' # str | Filter results for messages that include a metadata key containing this value. If this parameter is provided, the metadata_key parameter must also be provided. (optional)
status_code = 'status_code_example' # str | Filter results by message status code. (optional)
status = 'status_example' # str | Filter results by message status. (optional)
page = 56 # int | Page number for paging through paginated result sets. (optional)
page_size = 56 # int | Number of results to return in a page for paginated result sets. (optional)
sort_by = 'sort_by_example' # str | Field to sort results set by (optional)
sort_direction = 'sort_direction_example' # str | Order to sort results by. (optional)
source_address_country = 'source_address_country_example' # str | Filter results by source address country. (optional)
source_address = 'source_address_example' # str | Filter results by source address. (optional)
timezone = 'timezone_example' # str | The timezone to use for the context of the request. If provided this will be used as the timezone for the start date and end date parameters, and all datetime fields returns in the response. The timezone should be provided as a IANA (Internet Assigned Numbers Authority) time zone database zone name, i.e. 'Australia/Melbourne'. (optional)

try: 
    # Returns a list of message sent
    api_response = api_instance.get_sent_messages_detail(end_date, start_date, accounts=accounts, delivery_report=delivery_report, destination_address_country=destination_address_country, destination_address=destination_address, message_format=message_format, metadata_key=metadata_key, metadata_value=metadata_value, status_code=status_code, status=status, page=page, page_size=page_size, sort_by=sort_by, sort_direction=sort_direction, source_address_country=source_address_country, source_address=source_address, timezone=timezone)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling MessagingReportsApi->get_sent_messages_detail: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **end_date** | **str**| End date time for report window. By default, the timezone for this parameter will be taken from the account settings for the account associated with the credentials used to make the request, or the account included in the Account parameter. This can be overridden using the timezone parameter per request. The date must be in the format of \&quot;yyyy-MM-dd&#39;T&#39;HH:mm:ss\&quot;, e.g. \&quot;2017-02-10T13:30:00\&quot;. | 
 **start_date** | **str**| Start date time for report window. By default, the timezone for this parameter will be taken from the account settings for the account associated with the credentials used to make the request, or the account included in the Account parameter. This can be overridden using the timezone parameter per request. The date must be in the format of \&quot;yyyy-MM-dd&#39;T&#39;HH:mm:ss\&quot;, e.g. \&quot;2017-02-10T13:30:00\&quot;. | 
 **accounts** | **str**| Filter results by a specific account. By default results will be returned for the account associated with the authentication credentials and all sub accounts. | [optional] 
 **delivery_report** | **bool**| Filter results by delivery report. | [optional] 
 **destination_address_country** | **str**| Filter results by destination address country. | [optional] 
 **destination_address** | **str**| Filter results by destination address. | [optional] 
 **message_format** | **str**| Filter results by message format. | [optional] 
 **metadata_key** | **str**| Filter results for messages that include a metadata key. | [optional] 
 **metadata_value** | **str**| Filter results for messages that include a metadata key containing this value. If this parameter is provided, the metadata_key parameter must also be provided. | [optional] 
 **status_code** | **str**| Filter results by message status code. | [optional] 
 **status** | **str**| Filter results by message status. | [optional] 
 **page** | **int**| Page number for paging through paginated result sets. | [optional] 
 **page_size** | **int**| Number of results to return in a page for paginated result sets. | [optional] 
 **sort_by** | **str**| Field to sort results set by | [optional] 
 **sort_direction** | **str**| Order to sort results by. | [optional] 
 **source_address_country** | **str**| Filter results by source address country. | [optional] 
 **source_address** | **str**| Filter results by source address. | [optional] 
 **timezone** | **str**| The timezone to use for the context of the request. If provided this will be used as the timezone for the start date and end date parameters, and all datetime fields returns in the response. The timezone should be provided as a IANA (Internet Assigned Numbers Authority) time zone database zone name, i.e. &#39;Australia/Melbourne&#39;. | [optional] 

### Return type

[**SentMessages**](SentMessages.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sent_messages_summary**
> SummaryReport get_sent_messages_summary(end_date, group_by, start_date, accounts=accounts, delivery_report=delivery_report, destination_address_country=destination_address_country, destination_address=destination_address, summary_by=summary_by, summary_field=summary_field, message_format=message_format, metadata_key=metadata_key, metadata_value=metadata_value, status_code=status_code, source_address_country=source_address_country, source_address=source_address, timezone=timezone)

Returns a summarised report of messages sent

Returns a summarised report of all messages sent during the specified time, grouped by by the specified grouping parameter

### Example 
```python
import time
import messagemedia_rest_api
from messagemedia_rest_api.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
messagemedia_rest_api.configuration.username = 'YOUR_USERNAME'
messagemedia_rest_api.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = messagemedia_rest_api.MessagingReportsApi()
end_date = 'end_date_example' # str | End date time for report window. By default, the timezone for this parameter will be taken from the account settings for the account associated with the credentials used to make the request, or the account included in the Account parameter. This can be overridden using the timezone parameter per request. The date must be in the format of \"yyyy-MM-dd'T'HH:mm:ss\", e.g. \"2017-02-10T13:30:00\".
group_by = 'group_by_example' # str | Field to group results set by
start_date = 'start_date_example' # str | Start date time for report window. By default, the timezone for this parameter will be taken from the account settings for the account associated with the credentials used to make the request, or the account included in the Account parameter. This can be overridden using the timezone parameter per request. The date must be in the format of \"yyyy-MM-dd'T'HH:mm:ss\", e.g. \"2017-02-10T13:30:00\".
accounts = 'accounts_example' # str | Filter results by a specific account. By default results will be returned for the account associated with the authentication credentials and all sub accounts. (optional)
delivery_report = true # bool | Filter results by delivery report. (optional)
destination_address_country = 'destination_address_country_example' # str | Filter results by destination address country. (optional)
destination_address = 'destination_address_example' # str | Filter results by destination address. (optional)
summary_by = 'summary_by_example' # str | Function to apply when summarising results (optional)
summary_field = 'summary_field_example' # str | Field to summarise results by (optional)
message_format = 'message_format_example' # str | Filter results by message format. (optional)
metadata_key = 'metadata_key_example' # str | Filter results for messages that include a metadata key. (optional)
metadata_value = 'metadata_value_example' # str | Filter results for messages that include a metadata key containing this value. If this parameter is provided, the metadata_key parameter must also be provided. (optional)
status_code = 'status_code_example' # str | Filter results by message status code. (optional)
source_address_country = 'source_address_country_example' # str | Filter results by source address country. (optional)
source_address = 'source_address_example' # str | Filter results by source address. (optional)
timezone = 'timezone_example' # str | The timezone to use for the context of the request. If provided this will be used as the timezone for the start date and end date parameters, and all datetime fields returns in the response. The timezone should be provided as a IANA (Internet Assigned Numbers Authority) time zone database zone name, i.e. 'Australia/Melbourne'. (optional)

try: 
    # Returns a summarised report of messages sent
    api_response = api_instance.get_sent_messages_summary(end_date, group_by, start_date, accounts=accounts, delivery_report=delivery_report, destination_address_country=destination_address_country, destination_address=destination_address, summary_by=summary_by, summary_field=summary_field, message_format=message_format, metadata_key=metadata_key, metadata_value=metadata_value, status_code=status_code, source_address_country=source_address_country, source_address=source_address, timezone=timezone)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling MessagingReportsApi->get_sent_messages_summary: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **end_date** | **str**| End date time for report window. By default, the timezone for this parameter will be taken from the account settings for the account associated with the credentials used to make the request, or the account included in the Account parameter. This can be overridden using the timezone parameter per request. The date must be in the format of \&quot;yyyy-MM-dd&#39;T&#39;HH:mm:ss\&quot;, e.g. \&quot;2017-02-10T13:30:00\&quot;. | 
 **group_by** | **str**| Field to group results set by | 
 **start_date** | **str**| Start date time for report window. By default, the timezone for this parameter will be taken from the account settings for the account associated with the credentials used to make the request, or the account included in the Account parameter. This can be overridden using the timezone parameter per request. The date must be in the format of \&quot;yyyy-MM-dd&#39;T&#39;HH:mm:ss\&quot;, e.g. \&quot;2017-02-10T13:30:00\&quot;. | 
 **accounts** | **str**| Filter results by a specific account. By default results will be returned for the account associated with the authentication credentials and all sub accounts. | [optional] 
 **delivery_report** | **bool**| Filter results by delivery report. | [optional] 
 **destination_address_country** | **str**| Filter results by destination address country. | [optional] 
 **destination_address** | **str**| Filter results by destination address. | [optional] 
 **summary_by** | **str**| Function to apply when summarising results | [optional] 
 **summary_field** | **str**| Field to summarise results by | [optional] 
 **message_format** | **str**| Filter results by message format. | [optional] 
 **metadata_key** | **str**| Filter results for messages that include a metadata key. | [optional] 
 **metadata_value** | **str**| Filter results for messages that include a metadata key containing this value. If this parameter is provided, the metadata_key parameter must also be provided. | [optional] 
 **status_code** | **str**| Filter results by message status code. | [optional] 
 **source_address_country** | **str**| Filter results by source address country. | [optional] 
 **source_address** | **str**| Filter results by source address. | [optional] 
 **timezone** | **str**| The timezone to use for the context of the request. If provided this will be used as the timezone for the start date and end date parameters, and all datetime fields returns in the response. The timezone should be provided as a IANA (Internet Assigned Numbers Authority) time zone database zone name, i.e. &#39;Australia/Melbourne&#39;. | [optional] 

### Return type

[**SummaryReport**](SummaryReport.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_async_delivery_reports_detail**
> AsyncReportResponse submit_async_delivery_reports_detail(async_delivery_report_detail_request)

Submits a request to generate an async detail report

Submits a request to generate an async detail report of all delivery reports received during the specified time.

### Example 
```python
import time
import messagemedia_rest_api
from messagemedia_rest_api.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
messagemedia_rest_api.configuration.username = 'YOUR_USERNAME'
messagemedia_rest_api.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = messagemedia_rest_api.MessagingReportsApi()
async_delivery_report_detail_request = messagemedia_rest_api.AsyncDeliveryReportDetailRequest() # AsyncDeliveryReportDetailRequest | 

try: 
    # Submits a request to generate an async detail report
    api_response = api_instance.submit_async_delivery_reports_detail(async_delivery_report_detail_request)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling MessagingReportsApi->submit_async_delivery_reports_detail: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **async_delivery_report_detail_request** | [**AsyncDeliveryReportDetailRequest**](AsyncDeliveryReportDetailRequest.md)|  | 

### Return type

[**AsyncReportResponse**](AsyncReportResponse.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_delivery_reports_summary**
> AsyncReportResponse submit_delivery_reports_summary(async_delivery_reports_summary_request)

Submits a summarised report of delivery reports

Submits a request to generate an async summary report of all delivery reports during the specified time.

### Example 
```python
import time
import messagemedia_rest_api
from messagemedia_rest_api.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
messagemedia_rest_api.configuration.username = 'YOUR_USERNAME'
messagemedia_rest_api.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = messagemedia_rest_api.MessagingReportsApi()
async_delivery_reports_summary_request = messagemedia_rest_api.AsyncDeliveryReportsSummaryRequest() # AsyncDeliveryReportsSummaryRequest | 

try: 
    # Submits a summarised report of delivery reports
    api_response = api_instance.submit_delivery_reports_summary(async_delivery_reports_summary_request)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling MessagingReportsApi->submit_delivery_reports_summary: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **async_delivery_reports_summary_request** | [**AsyncDeliveryReportsSummaryRequest**](AsyncDeliveryReportsSummaryRequest.md)|  | 

### Return type

[**AsyncReportResponse**](AsyncReportResponse.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_received_messages_detail**
> AsyncReportResponse submit_received_messages_detail(async_received_messages_detail_request)

Submits a request to generate an async detail report

Submits a request to generate an async detail report of all received messages during the specified time.

### Example 
```python
import time
import messagemedia_rest_api
from messagemedia_rest_api.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
messagemedia_rest_api.configuration.username = 'YOUR_USERNAME'
messagemedia_rest_api.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = messagemedia_rest_api.MessagingReportsApi()
async_received_messages_detail_request = messagemedia_rest_api.AsyncReceivedMessagesDetailRequest() # AsyncReceivedMessagesDetailRequest | 

try: 
    # Submits a request to generate an async detail report
    api_response = api_instance.submit_received_messages_detail(async_received_messages_detail_request)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling MessagingReportsApi->submit_received_messages_detail: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **async_received_messages_detail_request** | [**AsyncReceivedMessagesDetailRequest**](AsyncReceivedMessagesDetailRequest.md)|  | 

### Return type

[**AsyncReportResponse**](AsyncReportResponse.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_received_messages_summary**
> AsyncReportResponse submit_received_messages_summary(async_received_messages_summary_request)

Submits a summarised report of received messages

Submits a request to generate an async summary report of all received messages during the specified time.

### Example 
```python
import time
import messagemedia_rest_api
from messagemedia_rest_api.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
messagemedia_rest_api.configuration.username = 'YOUR_USERNAME'
messagemedia_rest_api.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = messagemedia_rest_api.MessagingReportsApi()
async_received_messages_summary_request = messagemedia_rest_api.AsyncReceivedMessagesSummaryRequest() # AsyncReceivedMessagesSummaryRequest | 

try: 
    # Submits a summarised report of received messages
    api_response = api_instance.submit_received_messages_summary(async_received_messages_summary_request)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling MessagingReportsApi->submit_received_messages_summary: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **async_received_messages_summary_request** | [**AsyncReceivedMessagesSummaryRequest**](AsyncReceivedMessagesSummaryRequest.md)|  | 

### Return type

[**AsyncReportResponse**](AsyncReportResponse.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_sent_messages_detail**
> AsyncReportResponse submit_sent_messages_detail(async_sent_messages_detail_request)

Submits a request to generate an async detail report

Submits a request to generate an async detail report of all sent messages during the specified time.

### Example 
```python
import time
import messagemedia_rest_api
from messagemedia_rest_api.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
messagemedia_rest_api.configuration.username = 'YOUR_USERNAME'
messagemedia_rest_api.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = messagemedia_rest_api.MessagingReportsApi()
async_sent_messages_detail_request = messagemedia_rest_api.AsyncSentMessagesDetailRequest() # AsyncSentMessagesDetailRequest | 

try: 
    # Submits a request to generate an async detail report
    api_response = api_instance.submit_sent_messages_detail(async_sent_messages_detail_request)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling MessagingReportsApi->submit_sent_messages_detail: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **async_sent_messages_detail_request** | [**AsyncSentMessagesDetailRequest**](AsyncSentMessagesDetailRequest.md)|  | 

### Return type

[**AsyncReportResponse**](AsyncReportResponse.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_sent_messages_summary**
> AsyncReportResponse submit_sent_messages_summary(async_delivery_sent_messages_request)

Submits a summarised report of sent messages

Submits a request to generate an async summary report of all sent messages during the specified time.

### Example 
```python
import time
import messagemedia_rest_api
from messagemedia_rest_api.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basic
messagemedia_rest_api.configuration.username = 'YOUR_USERNAME'
messagemedia_rest_api.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = messagemedia_rest_api.MessagingReportsApi()
async_delivery_sent_messages_request = messagemedia_rest_api.AsyncDeliverySentMessagesRequest() # AsyncDeliverySentMessagesRequest | 

try: 
    # Submits a summarised report of sent messages
    api_response = api_instance.submit_sent_messages_summary(async_delivery_sent_messages_request)
    pprint(api_response)
except ApiException as e:
    print "Exception when calling MessagingReportsApi->submit_sent_messages_summary: %s\n" % e
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **async_delivery_sent_messages_request** | [**AsyncDeliverySentMessagesRequest**](AsyncDeliverySentMessagesRequest.md)|  | 

### Return type

[**AsyncReportResponse**](AsyncReportResponse.md)

### Authorization

[basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

