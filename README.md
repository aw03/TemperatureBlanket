# TemperatureBlanket

A short script created for aiding my personal knitting project called a "temperature blanket".

This script uses API called to MeteoAPI to gather weather history data in NYC. Then uses pandas to parse through data, calculate the temperature during the day and analyze which yarn color I should use to represent that day. Finally saves the data in excel sheet for easy access.

## Dependencies

```
pip install openmeteo-requests
pip install requests-cache retry-requests numpy pandas
pip install openpyxl
```