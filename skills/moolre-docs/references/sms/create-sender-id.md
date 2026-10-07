# Create Sender ID API

Request a new Sender ID for your SMS campaigns. Note: This API requires X-API-VASKEY in the header for authentication.

## Endpoint
`POST https://api.moolre.com/open/sms/query`

## Request Parameters
| Name | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| type | integer | Yes | ID of the sender ID creation function. Must be 3. |
| senderids | array | Yes | An array of sender ID objects containing senderid (max 11 chars) and optional approve boolean. |

## Responses
### 200 - Success
Registration request submitted.

```json
{
  "status": 1,
  "code": "ASMQ12",
  "message": "Sender IDs Created Successfully.",
  "data": null,
  "go": null
}
```

### 400 - Permission Denied
You do not have permission to approve Sender IDs.

```json
{
  "status": 0,
  "code": "ASMQ09",
  "message": "You do not have permission to approve Sender IDs. Contact Customer Support.",
  "data": "senderid",
  "go": null
}
```

