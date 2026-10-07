# Initiate Transfer API

Send money to a Mobile Money or Bank Account instantly.

## Endpoint
`POST https://api.moolre.com/open/transact/transfer`

## Headers
| Name | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| X-API-USER | string | Yes | Your Moolre username. |
| X-API-KEY | string | Yes | Your API Key (Private Key only). *(Not required in Sandbox)* |

## Request Parameters
| Name | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| type | integer | Yes | Must be 1. |
| channel | string | Yes | 1=MTN, 6=Telecel, 7=AT, 2=Instant Bank Transfer. |
| currency | string | Yes | Currency code (e.g., GHS). |
| amount | string | Yes | Amount to transfer. |
| receiver | string | Yes | Recipient phone or account number. |
| sublistid | string | No | Bank ID if channel is Bank Transfer. |
| externalref | string | Yes | Unique reference for the transfer. |
| reference | string | No | Optional message/reference. |
| accountnumber | string | Yes | Your Moolre Account Number. |

## Responses
### 200 - Success
Transfer request received.

```json
{
  "status": "1",
  "code": "OBGH01",
  "message": [
    "Pay out Successful",
    "Click close to view transactions."
  ],
  "data": {
    "txstatus": 1,
    "receiver": "0246798993",
    "transactionid": "32759150",
    "externalref": "28171451",
    "thirdpartyref": "901733241086",
    "receivername": "YUSIF YA-ADZAGEY",
    "amount": "1",
    "amountfee": "1.01",
    "networkfee": "0.00",
    "fee": "0.01"
  },
  "go": null
}
```

