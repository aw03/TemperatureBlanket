from meteoapi import fetch_data

def classify_color(temp):
    if temp < 32.5:
        return "Purple"
    elif 32.5 <= temp < 49.5:
        return "Blue"
    elif 49.5 <= temp < 64.5:
        return "Cyan"
    elif 64.5 <= temp < 77.5:
        return "Green"
    elif 77.5 <= temp < 87.5:
        return "Yellow"
    elif temp >= 87.5:
        return "Red"
    else:
        return ""  # Handle unexpected cases if needed
    
def anaylze_colors(daily_dataframe):

    daily_dataframe["day_color"] = daily_dataframe["temperature_2m_mean"].apply(classify_color)
    daily_dataframe["weighted_day_color"] = daily_dataframe.apply(lambda row: classify_color((float(row['temperature_2m_max']) + float(row['temperature_2m_mean'])) / 2.0),axis=1)

    print(daily_dataframe)

    counts = daily_dataframe["day_color"].value_counts()
    weighted_counts = daily_dataframe["weighted_day_color"].value_counts()
    print(counts)
    print(weighted_counts)

    daily_dataframe['date'] = daily_dataframe['date'].dt.tz_localize(None)
    daily_dataframe.to_excel("weather_data.xlsx", index=False)  # Save without row indices

if __name__ == "__main__":
    data = fetch_data()
    anaylze_colors(data)