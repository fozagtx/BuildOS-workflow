# Create Payment ID API

Generate a unique permanent payment ID for use in making payments. Customers can make payments by dialing *203*paymentid#.

## Endpoint
`POST https://api.moolre.com/open/account/create`

## Headers
| Name | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| X-API-USER | string | Yes | Your Moolre username. |
| X-API-PUBKEY | string | Yes | Your Public API Key. *(Not required in Sandbox)* |

## Request Parameters
| Name | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| type | integer | Yes | ID of the function. Must be 2. |
| phone | string | Yes | Phone number of the customer (e.g., +233267606822). |
| name | string | Yes | Name of the Customer or a Unique ID. |
| currency | string | Yes | Currency of your account/wallet. |
| externalref | string | No | Unique ID to identify the request. |
| accountnumber | string | Yes | Your Moolre Account Number. |

## Responses
### 200 - Success
Payment ID generated.

```json
{
  "status": 1,
  "code": "AD14",
  "message": "Terminal Creation Successful",
  "data": {
    "paymentid": "08160984",
    "name": "Kofi Adeniyi",
    "qrcode": null
  },
  "go": null
}
```

