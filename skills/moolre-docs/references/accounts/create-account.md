# Create Account API

Create a new business wallet/account.

## Endpoint
`POST https://api.moolre.com/open/account/create`

## Headers
| Name | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| X-API-USER | string | Yes | Your Moolre username. |
| X-API-KEY | string | Yes | Your API Key. *(Not required in Sandbox)* |

## Request Parameters
| Name | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| type | integer | Yes | Must be 1. |
| accountname | string | Yes | Registered name of the business. |
| currency | string | Yes | Currency code (e.g., GHS). |
| api | boolean | No | Indicates if the account supports API transactions. |
| callback | string | No | Webhook URL for processing real-time transaction callbacks. |
| settlement | object | No | Optional settlement details (currency, frequency, channel, recipient, sublist). |

## Responses
### 200 - Success
Account created successfully.

```json
{
  "status": "1",
  "code": "WC02",
  "message": [
    "Wallet Created Successfully",
    "Your wallet will be reloaded shortly or Click close to refresh now."
  ],
  "data": {
    "status": 1,
    "accountnumber": "100000157291",
    "accountname": "My Business LTD",
    "paymentid": "0757291",
    "api": 0,
    "callback": "",
    "settlement": {},
    "secret": "cf2a797f-c8d8-470c-a736-6f5f78ae1d86"
  },
  "go": [
    "wallets",
    "1.57291"
  ]
}
```

