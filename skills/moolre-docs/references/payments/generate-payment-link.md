# Generate Payment Link API

Create a hosted payment page URL. The Payment link system is used to generate a URL that opens a Moolre Web POS page for collecting payments.

## Endpoint
`POST https://api.moolre.com/embed/link`

## Headers
| Name | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| X-API-USER | string | Yes | Your Moolre username. |
| X-API-PUBKEY | string | Yes | Your Public API Key. *(Not required in Sandbox)* |

## Request Parameters
| Name | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| type | integer | Yes | Must be 1. |
| amount | string | Yes | Amount to be paid. |
| email | string | Yes | Email of the business. |
| externalref | string | Yes | Unique ID to identify the payment. |
| callback | string | No | Callback URL for payment notifications. |
| redirect | string | No | Redirect URL after successful payment. |
| reusable | string | Yes | Determines if the link can be used for repeat payments. 0=No, 1=Yes. |
| expiration_time | integer | No | Link expiry time in minutes. Minimum 1 minute. |
| currency | string | Yes | Currency of your account/wallet. |
| accountnumber | string | Yes | Your Moolre Account Number. |
| metadata | object | No | Optional metadata to be returned in callbacks. |

## Responses
### 200 - Success
Link generated successfully.

```json
{
  "status": 1,
  "code": "POS09",
  "message": "POS payment link successfully generated.",
  "data": {
    "authorization_url": "https://pos.moolre.com/RZWs1yB6amGjNoiEQvlHPS5uqgp3Jc",
    "reference": "uuid-1234as2"
  }
}
```

### 400 - Duplicate Transaction
Transaction already exists with this reference.

```json
{
  "status": 0,
  "code": "INP02",
  "message": "Transaction already exits!",
  "data": []
}
```

