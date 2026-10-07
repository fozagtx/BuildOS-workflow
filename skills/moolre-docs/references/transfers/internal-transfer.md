# Internal Transfer API

Initiate an internal transfer using your Moolre account.

## Endpoint
`POST https://api.moolre.com/open/transact/internal`

## Headers
| Name | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| X-API-USER | string | Yes | Your Moolre username. |
| X-API-KEY | string | Yes | Your Private API Key. *(Not required in Sandbox)* |

## Request Parameters
| Name | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| type | integer | Yes | Must be 1. |
| currency | string | Yes | Currency code (e.g., GHS). |
| amount | string | Yes | Amount to transfer. |
| receiver | string | Yes | Receiver account or wallet number. |
| externalref | string | Yes | Unique reference for the transfer. |
| reference | string | No | Optional narration or reference text. |
| accountnumber | string | Yes | Your Moolre Account Number. |

## Responses
### 200 (OTP Required) - OTP Required
Payment requires phone number verification.

```json
{
  "status": 1,
  "code": "TP14",
  "message": "Please complete the verification process sent to you via SMS and try again.",
  "data": "all",
  "go": null
}
```

### 200 (Payment Request) - Success
Payment request initiated successfully.

```json
{
  "status": 1,
  "code": "TR099",
  "message": null,
  "data": "f25fc80e-791b-495b-8799-dcf87660457d",
  "go": null
}
```

### 400 - Duplicate Reference
The external reference must be unique.

```json
{
  "status": "0",
  "code": "TP13",
  "message": "External Reference is required and must be unique.",
  "data": "externalref",
  "go": null
}
```

