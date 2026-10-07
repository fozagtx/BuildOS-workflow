# Sender ID Status API

Check the approval status of a Sender ID. Note: This API requires X-API-VASKEY in the header for authentication.

## Endpoint
`POST https://api.moolre.com/open/sms/query`

## Request Parameters
| Name | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| type | integer | Yes | ID of the sender ID status function. Must be 1. |
| senderid | string | Yes | Sender ID to check. |

## Responses
### 200 - Success
Status returned.

```json
{
  "status": 1,
  "code": "ASMQ02",
  "message": "Sender ID is Approved",
  "data": "Moolre",
  "go": null
}
```

