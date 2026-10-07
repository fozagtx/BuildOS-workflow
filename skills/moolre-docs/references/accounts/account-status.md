# Account Status API

Check wallet balance and status.

## Endpoint
`POST https://api.moolre.com/open/account/status`

## Headers
| Name | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| X-API-USER | string | Yes | Your Moolre username. |
| X-API-KEY | string | Yes | Your API Key. *(Not required in Sandbox)* |

## Request Parameters
| Name | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| type | integer | Yes | Must be 1. |
| accountnumber | string | Yes | Account number to check. |

## Responses
### 200 - Success
Balance and status returned.

```json
{
  "status": 1,
  "code": "SW01",
  "message": "Wallet Found",
  "data": {
    "balance": 10.67,
    "accountname": "Zagey",
    "callback": "https://moolre.requestcatcher.com/test"
  },
  "go": null
}
```

### 401 - Authentication Error
API Access not activated.

```json
{
  "status": 0,
  "code": "AIN04",
  "message": "Authentication Error, API Access not activated.",
  "data": "all",
  "go": null
}
```

