# SMS Account Status API

Check your SMS credit balance. Note: This API requires X-API-VASKEY in the header for authentication.

## Endpoint
`POST https://api.moolre.com/open/sms/query`

## Request Parameters
| Name | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| type | integer | Yes | Must be 2. |

## Responses
### 200 - Success
Balance returned.

```json
{
  "status": 1,
  "code": "ASMQ03",
  "message": "Account Status",
  "data": {
    "balance": 857
  },
  "go": null
}
```

