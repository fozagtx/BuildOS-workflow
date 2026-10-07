# Update Account API

Update business wallet/account details and settlement settings.

## Endpoint
`POST https://api.moolre.com/open/account/update`

## Headers
| Name | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| X-API-USER | string | Yes | Your Moolre username. |
| X-API-KEY | string | Yes | Your API Key. *(Not required in Sandbox)* |

## Request Parameters
| Name | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| type | integer | Yes | Must be 1. |
| accountnumber | string | Yes | The account number you want to update. |
| accountname | string | No | Updated business name. |
| api | boolean | No | Indicates if the account supports API transactions. |
| callback | string | No | Webhook URL for callbacks. |
| settlement | object | No | Settlement details object (currency, frequency, channel, recipient, sublist). |

## Responses
### 200 - Success
Account updated successfully.

```json
{
  "status": "1",
  "code": "WCU02",
  "message": "Account Updated Successfully",
  "data": {
    "status": 1,
    "accountnumber": "100000157257",
    "accountname": "My Business PLC",
    "paymentid": "0757257",
    "api": 0,
    "callback": "https://nocall.com/noend",
    "settlement": {
      "currency": "GHS",
      "frequency": "1",
      "channel": "1",
      "recipient": "0246798090",
      "sublist": "300303"
    },
    "secret": "bcec3865-bea1-4a99-8e70-c6a434cac757"
  },
  "go": null
}
```

