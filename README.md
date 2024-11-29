# TemperatureBlanket

A short script created for aiding my personal knitting project called a "temperature blanket".

This script uses API called to Meteo API to gather weather history data in NYC. Then uses pandas, to parse through data, calculate the temperature during the day and analyze which yarn color I should use to represent that day.

## Dependencies

```
pip install openmeteo-requests
pip install requests-cache retry-requests numpy pandas
pip install openpyxl
```