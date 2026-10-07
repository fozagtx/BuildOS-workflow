# Send SMS (GET) API

The Send SMS (GET) API allows you to send SMS instantly using query parameters.

## Endpoint
`GET https://api.moolre.com/open/sms/send`

## Headers
| Name | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| X-API-VASKEY | string | Yes | Your unique SMS service VAS Key. |

## Query Parameters
| Name | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| type | integer | Yes | Must be 1. |
| senderid | string | Yes | Registered and approved Sender ID. |
| recipient | string | Yes | Recipient phone number. |
| message | string | Yes | Message content (max 160 characters). |

## Responses
### 200 - Success
SMS sent successfully.

```json
{
  "status": 1,
  "code": "SMS01",
  "message": "Success",
  "data": null,
  "go": null
}
```

### 401 - Authentication Error
The VAS Key provided is invalid or unauthorized.

```json
{
  "status": 0,
  "code": "AIN01",
  "message": "Authentication Error",
  "data": null,
  "go": null
}
```

