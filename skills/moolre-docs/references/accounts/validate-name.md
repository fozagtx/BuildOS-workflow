# Validate Name API

Confirm the name of a Mobile Money or Bank Account holder before initiating a transfer.

## Endpoint
`POST https://api.moolre.com/open/transact/validate`

## Headers
| Name | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| X-API-USER | string | Yes | Your Moolre username. |
| X-API-KEY | string | Yes | Your API Key (accepts both Public Key and Private Key). *(Not required in Sandbox)* |

## Request Parameters
| Name | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| type | integer | Yes | Must be 1. |
| receiver | string | Yes | Phone number or bank account number. |
| channel | string | Yes | 1=MTN, 6=Telecel, 7=AT, 2=Instant Bank Transfer. |
| sublistid | string | No | Bank ID if channel is Bank Transfer. |
| currency | string | Yes | Currency code (e.g., GHS). |
| accountnumber | string | Yes | Your Moolre Account Number. |

## Responses
### 200 - Success
Name validated successfully.

```json
{
  "status": 1,
  "code": "AVD01",
  "message": "Successful",
  "data": "BRIGHT BUAME",
  "go": null
}
```

### 400 - Not Found
The phone number or account was not found.

```json
{
  "status": 0,
  "code": "AVD02",
  "message": "Phone No. not found",
  "data": "Phone No. not found",
  "go": null
}
```

