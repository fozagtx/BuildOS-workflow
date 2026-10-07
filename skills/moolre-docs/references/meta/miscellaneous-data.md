# Miscellaneous Data API

Fetch real-time system data such as supported banks, mobile money channels, and other configuration data.

## Endpoint
`GET https://api.moolre.com/open/transact/data`

## Query Parameters
| Name | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| country | string | Yes | Country code (e.g., gha). |
| data | string | Yes | Type of data to fetch (e.g., banks). |

## Responses
### 200 - Success
Data list returned.

```json
{
  "status": 1,
  "code": "SD01",
  "message": "Banks Found",
  "data": [
    {
      "name": "ABSA BANK GHANA LTD",
      "code": "030100"
    },
    {
      "name": "ACCESS BANK GHANA LTD",
      "code": "030402"
    },
    {
      "name": "ADB BANK GHANA LTD",
      "code": "030301"
    }
  ],
  "go": null
}
```

