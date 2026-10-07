# Initiate Payment API

Send a USSD payment request to a payer's phone number for approval.

## Endpoint
`POST https://api.moolre.com/open/transact/payment`

## Headers
| Name | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| X-API-USER | string | Yes | Your Moolre username. |
| X-API-KEY | string | Yes | Your Private API Key. *(Not required in Sandbox)* |

## Request Parameters
| Name | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| type | integer | Yes | Must be 1. |
| channel | string | Yes | 13=MTN, 6=Telecel, 7=AT. |
| currency | string | Yes | Currency code (e.g., GHS). |
| payer | string | Yes | Customer's phone number. |
| amount | string | Yes | Amount to collect. |
| externalref | string | Yes | Unique reference for the payment. |
| otpcode | string | No | OTP code if required by the flow. |
| reference | string | No | Optional payment reference. |
| sessionid | string | No | USSD session ID if applicable. |
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

