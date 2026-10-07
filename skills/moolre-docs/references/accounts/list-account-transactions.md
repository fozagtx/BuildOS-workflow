# List Transactions API

Fetch a list of transactions linked with a specific account.

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
| type | integer | Yes | Must be 2. |
| accountnumber | string | Yes | Your Account Number. |
| startdate | string | No | Start date (YYYY-MM-DD HH:MM:SS). |
| enddate | string | No | End date (YYYY-MM-DD HH:MM:SS). |
| limit | string | No | Max transactions per page. |
| status | string | No | Filter by status (0=Pending, 1=Success, 2=Failed). |

## Responses
### 200 - Success
List of transactions returned.

```json
{
  "status": 1,
  "code": "ST08",
  "message": "Transactions Found",
  "data": {
    "txcount": "1",
    "transactions": [
      {
        "txstatus": 1,
        "txtype": 1,
        "accountnumber": "100000100002",
        "payer": "233551300186",
        "payee": "Zagey",
        "amount": "1.00",
        "value": "1",
        "transactionid": "34008096",
        "externalref": "0",
        "thirdpartyref": "55730796319",
        "ts": "2025-04-15 12:36:28"
      }
    ]
  },
  "go": null
}
```

