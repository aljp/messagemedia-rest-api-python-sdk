# MessageMedia REST API Python SDK
Australia's Leading Messaging Solutions for Business and Enterprise.


- API version: 1.0.0
- Package version: 1.0.0
- Build date: 2017-02-19T22:32:25.655Z
For more information, please visit [https://www.messagemedia.com/contact-us](https://www.messagemedia.com/contact-us)

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/messagemedia/messagemedia-rest-api-python-sdk.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/messagemedia/messagemedia-rest-api-python-sdk.git`)

Then import the package:
```python
import messagemedia_rest_api 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import messagemedia_rest_api
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
import time
import messagemedia_rest_api
from messagemedia_rest_api.rest import ApiException
from pprint import pprint

# MessageMedia REST API Python SDK
messagemedia_rest_api.configuration.username = 'YOUR_USERNAME'
messagemedia_rest_api.configuration.password = 'YOUR_PASSWORD'
# MessageMedia REST API Python SDK
api_instance = messagemedia_rest_api.DeliveryReportsApi

try:
    # Check delivery reports
    api_response = api_instance.check_reports()
    pprint(api_response)
except ApiException as e:
    print "Exception when calling DeliveryReportsApi->check_reports: %s\n" % e

```

## Documentation for API Endpoints

All URIs are relative to *https://api.messagemedia.com/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DeliveryReportsApi* | [**check_reports**](docs/DeliveryReportsApi.md#check_reports) | **GET** /delivery_reports | Check delivery reports
*DeliveryReportsApi* | [**confirm_reports**](docs/DeliveryReportsApi.md#confirm_reports) | **POST** /delivery_reports/confirmed | Confirm delivery reports as received
*MessagingApi* | [**get_message_status**](docs/MessagingApi.md#get_message_status) | **GET** /messages/{messageId} | Get the status of a submitted message
*MessagingApi* | [**send_messages**](docs/MessagingApi.md#send_messages) | **POST** /messages | Send one or more messages
*MessagingApi* | [**update_message_status**](docs/MessagingApi.md#update_message_status) | **PUT** /messages/{messageId} | Cancel a scheduled message
*MessagingReportsApi* | [**get_async_report_by_id**](docs/MessagingReportsApi.md#get_async_report_by_id) | **GET** /reporting/async_reports/{report_id} | Lists an asynchronous report.
*MessagingReportsApi* | [**get_async_report_data_by_id**](docs/MessagingReportsApi.md#get_async_report_data_by_id) | **GET** /reporting/async_reports/{report_id}/data | Gets the data of an asynchronous report.
*MessagingReportsApi* | [**get_async_reports**](docs/MessagingReportsApi.md#get_async_reports) | **GET** /reporting/async_reports | Gets a single asynchronous report.
*MessagingReportsApi* | [**get_delivery_reports_detail**](docs/MessagingReportsApi.md#get_delivery_reports_detail) | **GET** /reporting/delivery_reports/detail | Returns a list of delivery reports
*MessagingReportsApi* | [**get_delivery_reports_summary**](docs/MessagingReportsApi.md#get_delivery_reports_summary) | **GET** /reporting/delivery_reports/summary | Returns a summarised report of delivery reports
*MessagingReportsApi* | [**get_metadata_keys**](docs/MessagingReportsApi.md#get_metadata_keys) | **GET** /reporting/{messageType}/metadata/keys | Returns a list of metadata keys
*MessagingReportsApi* | [**get_received_messages_detail**](docs/MessagingReportsApi.md#get_received_messages_detail) | **GET** /reporting/received_messages/detail | Returns a list message received
*MessagingReportsApi* | [**get_received_messages_summary**](docs/MessagingReportsApi.md#get_received_messages_summary) | **GET** /reporting/received_messages/summary | Returns a summarised report of messages received
*MessagingReportsApi* | [**get_sent_messages_detail**](docs/MessagingReportsApi.md#get_sent_messages_detail) | **GET** /reporting/sent_messages/detail | Returns a list of message sent
*MessagingReportsApi* | [**get_sent_messages_summary**](docs/MessagingReportsApi.md#get_sent_messages_summary) | **GET** /reporting/sent_messages/summary | Returns a summarised report of messages sent
*MessagingReportsApi* | [**submit_async_delivery_reports_detail**](docs/MessagingReportsApi.md#submit_async_delivery_reports_detail) | **POST** /reporting/delivery_reports/detail/async | Submits a request to generate an async detail report
*MessagingReportsApi* | [**submit_delivery_reports_summary**](docs/MessagingReportsApi.md#submit_delivery_reports_summary) | **POST** /reporting/delivery_reports/summary/async | Submits a summarised report of delivery reports
*MessagingReportsApi* | [**submit_received_messages_detail**](docs/MessagingReportsApi.md#submit_received_messages_detail) | **POST** /reporting/received_messages/detail/async | Submits a request to generate an async detail report
*MessagingReportsApi* | [**submit_received_messages_summary**](docs/MessagingReportsApi.md#submit_received_messages_summary) | **POST** /reporting/received_messages/summary/async | Submits a summarised report of received messages
*MessagingReportsApi* | [**submit_sent_messages_detail**](docs/MessagingReportsApi.md#submit_sent_messages_detail) | **POST** /reporting/sent_messages/detail/async | Submits a request to generate an async detail report
*MessagingReportsApi* | [**submit_sent_messages_summary**](docs/MessagingReportsApi.md#submit_sent_messages_summary) | **POST** /reporting/sent_messages/summary/async | Submits a summarised report of sent messages
*RepliesApi* | [**check_replies**](docs/RepliesApi.md#check_replies) | **GET** /replies | Check replies
*RepliesApi* | [**confirm_replies**](docs/RepliesApi.md#confirm_replies) | **POST** /replies/confirmed | Confirm replies as received


## Documentation For Models

 - [AccountsBody](docs/AccountsBody.md)
 - [ActionBody](docs/ActionBody.md)
 - [AsyncDeliveryReportDetailRequest](docs/AsyncDeliveryReportDetailRequest.md)
 - [AsyncDeliveryReportsSummaryRequest](docs/AsyncDeliveryReportsSummaryRequest.md)
 - [AsyncDeliverySentMessagesRequest](docs/AsyncDeliverySentMessagesRequest.md)
 - [AsyncReceivedMessagesDetailRequest](docs/AsyncReceivedMessagesDetailRequest.md)
 - [AsyncReceivedMessagesSummaryRequest](docs/AsyncReceivedMessagesSummaryRequest.md)
 - [AsyncReport](docs/AsyncReport.md)
 - [AsyncReportResponse](docs/AsyncReportResponse.md)
 - [AsyncSentMessagesDetailRequest](docs/AsyncSentMessagesDetailRequest.md)
 - [DeliveryReport](docs/DeliveryReport.md)
 - [DeliveryReportBody](docs/DeliveryReportBody.md)
 - [DeliveryReportId](docs/DeliveryReportId.md)
 - [DeliveryReports](docs/DeliveryReports.md)
 - [DestinationAddressBody](docs/DestinationAddressBody.md)
 - [DestinationAddressCountryBody](docs/DestinationAddressCountryBody.md)
 - [EndDateBody](docs/EndDateBody.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [InlineResponse400](docs/InlineResponse400.md)
 - [MessageFormatBody](docs/MessageFormatBody.md)
 - [MessageStatusCode](docs/MessageStatusCode.md)
 - [Messages](docs/Messages.md)
 - [MetadataKeyBody](docs/MetadataKeyBody.md)
 - [MetadataKeysResponse](docs/MetadataKeysResponse.md)
 - [MetadataKeysResponseProperties](docs/MetadataKeysResponseProperties.md)
 - [MetadataValueBody](docs/MetadataValueBody.md)
 - [NewMessage](docs/NewMessage.md)
 - [Pagination](docs/Pagination.md)
 - [ReceivedMessage](docs/ReceivedMessage.md)
 - [ReceivedMessages](docs/ReceivedMessages.md)
 - [Replies](docs/Replies.md)
 - [Reply](docs/Reply.md)
 - [ReplyId](docs/ReplyId.md)
 - [ReplyVendorAccountId](docs/ReplyVendorAccountId.md)
 - [Report](docs/Report.md)
 - [ReportingDetailProperties](docs/ReportingDetailProperties.md)
 - [ReportingDetailPropertiesFilters](docs/ReportingDetailPropertiesFilters.md)
 - [ReportingDetailPropertiesSorting](docs/ReportingDetailPropertiesSorting.md)
 - [Reports](docs/Reports.md)
 - [SentMessage](docs/SentMessage.md)
 - [SentMessages](docs/SentMessages.md)
 - [SortDirectionBody](docs/SortDirectionBody.md)
 - [SourceAddressBody](docs/SourceAddressBody.md)
 - [SourceAddressCountryBody](docs/SourceAddressCountryBody.md)
 - [StartDateBody](docs/StartDateBody.md)
 - [Status](docs/Status.md)
 - [StatusBody](docs/StatusBody.md)
 - [StatusCodeBody](docs/StatusCodeBody.md)
 - [SubmittedMessage](docs/SubmittedMessage.md)
 - [SubmittedMessages](docs/SubmittedMessages.md)
 - [SummaryByBody](docs/SummaryByBody.md)
 - [SummaryFieldBody](docs/SummaryFieldBody.md)
 - [SummaryReport](docs/SummaryReport.md)
 - [SummaryReportData](docs/SummaryReportData.md)
 - [SummaryReportProperties](docs/SummaryReportProperties.md)
 - [TimezoneBody](docs/TimezoneBody.md)


## Documentation For Authorization


## basic

- **Type**: HTTP basic authentication


## Author

support@messagemedia.com

