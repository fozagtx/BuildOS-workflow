# Send SMS API

The Send SMS (POST) API allows you to send bulk or single SMS messages to recipients across any network. Note: This API requires X-API-VASKEY in the header for authentication.

## Endpoint
`POST https://api.moolre.com/open/sms/send`

## Request Parameters
| Name | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| type | integer | Yes | ID of the sms sending function. Must be 1. |
| senderid | string | Yes | Your registered and approved Sender ID (max 11 chars). |
| messages | array | Yes | An array of message objects containing recipient, message, and optional ref. |

## Responses
### 200 - Success
SMS message(s) sent successfully.

```json
{
  "status": 1,
  "code": "SMS01",
  "message": "Success",
  "data": null,
  "go": null
}
```

### 400 - Unapproved Sender ID
The Sender ID provided is not yet approved or registered.

```json
{
  "status": 0,
  "code": "ASMS07",
  "message": "Sender ID is not approved, Please login on app.moolre.com and setup your Sender ID.",
  "data": "senderid",
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

