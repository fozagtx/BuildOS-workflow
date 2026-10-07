# Message Status API

Track the delivery status of your WhatsApp messages using their unique references. Supports batch status checks.

## Endpoint
`POST https://api.moolre.com/open/whatsapp/status`

## Request Parameters
| Name | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| ref | array | Yes | An array of unique message references to check. |

## Responses
### 200 (Success) - Success
Status details for all requested references returned.

```json
{
  "status": 1,
  "code": "WAS200",
  "message": "success",
  "data": [
    {
      "ref": "879883HGUGF45583499HF2089001",
      "status": "read"
    },
    {
      "ref": "879883HGUGF45583499HF2089005",
      "status": "accepted"
    }
  ]
}
```

