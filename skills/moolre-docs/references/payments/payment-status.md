# Payment Status API

Check the final status of a previously initiated payment collection.

## Endpoint
`POST https://api.moolre.com/open/transact/status`

## Headers
| Name | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| X-API-USER | string | Yes | Your Moolre username. |
| X-API-PUBKEY | string | Yes | Your Public API Key. *(Not required in Sandbox)* |

## Request Parameters
| Name | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| type | integer | Yes | Must be 1. |
| idtype | string | Yes | 1 = Unique externalref, 2 = Moolre Generated ID. |
| id | string | Yes | The reference ID to check. |
| accountnumber | string | Yes | Your Moolre Account Number. |

## Responses
### 200 - Success
Payment status details.

```json
{
  "status": 1,
  "code": "SS01",
  "message": "Transaction Successful",
  "data": {
    "txstatus": 1,
    "txtype": 2,
    "accountnumber": "100000100002",
    "payer": "",
    "payee": "0209151872",
    "amount": "1",
    "value": "1",
    "transactionid": "31772290",
    "externalref": "1231231-128",
    "thirdpartyref": "471700539041",
    "ts": "2023-11-21 03:57:25"
  },
  "go": null
}
```

