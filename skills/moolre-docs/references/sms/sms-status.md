# SMS Status API

Check the delivery status of sent SMS messages. Note: This API requires X-API-VASKEY in the header for authentication.

## Endpoint
`POST https://api.moolre.com/open/sms/query`

## Request Parameters
| Name | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| type | integer | Yes | Must be 5. |
| ref | array | Yes | Array of message references to check. |

## Responses
### 200 - Success
Status details returned.

```json
{
  "status": 1,
  "code": "ASMQ10",
  "message": "SMS Status",
  "data": [
    {
      "ref": "0338954001737166274",
      "status": 3
    },
    {
      "ref": "uuid--001",
      "status": 2
    }
  ],
  "go": null
}
```

