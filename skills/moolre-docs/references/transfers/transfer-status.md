# Transfer Status API

Check the final status of a previously initiated transfer.

## Endpoint
`POST https://api.moolre.com/open/transact/status`

## Headers
| Name | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| X-API-USER | string | Yes | Your Moolre username. |
| X-API-KEY | string | Yes | Your API Key (accepts both Public Key and Private Key). *(Not required in Sandbox)* |

## Request Parameters
| Name | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| type | integer | Yes | Must be 1. |
| idtype | string | Yes | 1 = Unique externalref, 2 = Moolre Generated ID. |
| id | string | Yes | The reference ID to check. |
| accountnumber | string | Yes | Your Moolre Account Number. |

## Responses
### 200 - Success
Transfer status details.

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
    "payee": "0246798993",
    "amount": "5",
    "value": "5",
    "transactionid": "31830714",
    "externalref": "1231231-12985",
    "thirdpartyref": "141704447750",
    "ts": "2024-01-05 09:42:33"
  },
  "go": null
}
```

