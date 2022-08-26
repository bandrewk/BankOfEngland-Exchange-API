Python script to make an api call and get the exchange rates for `GBP` to `USD` on a specific date.

Response from Bank of England comes in CSV format (`response.text`).

Keeping it here as an example for future use.

Can be easily implemented in other languages too.

Output of the script:

```
200
https://www.bankofengland.co.uk/boeapps/database/_iadb-fromshowcolumns.asp?csv.x=yes&Datefrom=25%2FAug%2F2022&Dateto=26%2FAug%2F2022&SeriesCodes=XUDLGBD&CSVF=TN&UsingCodes=Y&VPD=Y&VFD=N
DATE,XUDLGBD

25 Aug 2022,0.8456


>
```
