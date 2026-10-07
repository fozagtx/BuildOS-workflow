# Get Templates API

Fetch your approved WhatsApp message templates. Note: This API requires X-API-VASKEY in the header for authentication.

## Endpoint
`GET https://api.moolre.com/open/whatsapp/template`

## Responses
### 200 (Approved) - Success
Returns a list containing approved templates.

```json
{
  "status": 1,
  "code": "WAS200",
  "message": "Templates retrieved successfully",
  "data": [
    {
      "id": "1218877297066056",
      "name": "promotion",
      "language": "en",
      "status": "APPROVED",
      "message": "Hello {{1}},\n\nMelchizedek Technologies would like to share information about our {{2}} designed to support businesses like {{3}}.\n\nIf you would like to learn more or speak with our team, please reply to this message and we will be happy to assist.\n",
      "placeholders": [
        "1",
        "2",
        "3"
      ]
    }
  ]
}
```

### 200 (Rejected) - Success
Returns a list containing rejected templates.

```json
{
  "status": 1,
  "code": "WAS200",
  "message": "Templates retrieved successfully",
  "data": [
    {
      "id": "1470051854524583",
      "name": "whatsapp_test",
      "language": "en",
      "status": "REJECTED",
      "message": "Hello {{1}},\n\nYou are receiving this message from Melchizedek Technologies in response to your request with {{2}}.\n\nIf you need any assistance, please reply to this message and our support team will assist you.\n",
      "placeholders": [
        "1",
        "2"
      ]
    }
  ]
}
```

### 200 (Pending) - Success
Returns a list containing pending templates.

```json
{
  "status": 1,
  "code": "WAS200",
  "message": "Templates retrieved successfully",
  "data": [
    {
      "id": "1709192906730643",
      "name": "update",
      "language": "en",
      "status": "PENDING",
      "message": "Hello {{1}},\n\nThank you for contacting Melchizedek Technologies.\nYour request regarding {{2}} has been received and our team will assist you shortly.\n",
      "placeholders": [
        "1",
        "2"
      ]
    }
  ]
}
```

