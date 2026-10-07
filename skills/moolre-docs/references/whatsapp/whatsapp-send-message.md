# Send Message API

Send batch WhatsApp messages using an approved template name. The unique reference (ref) is optional; however, without it, the message status cannot be tracked.

## Endpoint
`POST https://api.moolre.com/open/whatsapp/send`

## Request Parameters
| Name | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| template_name | string | Yes | The name of the approved WhatsApp template. |
| language | string | Yes | The language code for the template (English only). |
| messages | array | Yes | An array of message objects containing recipient, optional ref, and placeholders. Note: If ref is omitted, the status cannot be checked later. |

## Responses
### 200 (Success) - Success
All messages were sent successfully.

```json
{
  "status": 1,
  "code": "WAS200",
  "message": "suceess",
  "error": [],
  "data": []
}
```

### 200 (Duplicate Refs) - Warning
Some messages were not sent due to non-unique references.

```json
{
  "status": 1,
  "code": "WAS200",
  "error": "Some ref are not unique, corresponding messages will not be sent",
  "message": "",
  "data": [
    {
      "recipient": "233531419000",
      "ref": "879883HGU334553GF887799HF20004"
    },
    {
      "recipient": "233531419011",
      "ref": "879883HGU334553GF887799HF20006"
    }
  ]
}
```

### 401 (Insufficient Balance) - Insufficient Balance
The account has insufficient balance to send WhatsApp messages.

```json
{
  "status": 0,
  "code": "WAS401",
  "message": "Insufficient balance to send messages. Please top up your WhatsApp bundle."
}
```

