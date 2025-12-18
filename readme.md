# Premier League Position Tracker

A Python web scraper that tracks Premier League team positions over multiple seasons and visualizes the data with interactive charts.

## Overview

This project scrapes historical Premier League standings data from FotMob and creates an interactive line chart showing how the top 6 teams' positions have changed from the 2015/16 to 2024/25 seasons.

<img width="1920" height="624" alt="image" src="https://github.com/user-attachments/assets/754fd8f5-4a67-4745-a9ed-b34ce3d35fc6" />

## Features

- **Web Scraping**: Automatically extracts league table data from FotMob for multiple seasons
- **Data Storage**: Saves scraped data to CSV for easy access and analysis
- **Interactive Visualization**: Generates a Plotly chart showing position trends over time
- **Focus on Top Teams**: Highlights the "Big Six" Premier League teams

## Requirements

```bash
pip install beautifulsoup4 requests pandas plotly
```

## Dependencies

- `beautifulsoup4` - HTML parsing
- `requests` - HTTP requests
- `pandas` - Data manipulation
- `plotly` - Interactive visualizations

## Usage

Simply run the script:

```bash
python script.py
```

The script will:
1. Scrape Premier League standings for seasons 2015/16 through 2024/25
2. Save all data to `premier_league_positions.csv`
3. Generate an interactive chart (`premier_league_chart.html`)
4. Display the chart in your default browser

## Output Files

- **premier_league_positions.csv** - Complete dataset of all teams and seasons
- **premier_league_chart.html** - Interactive visualization focusing on top 6 teams

## Teams Tracked in Visualization

- Arsenal
- Manchester City
- Liverpool
- Chelsea
- Manchester United
- Tottenham Hotspur

## How It Works

1. **Scraping**: The script sends HTTP requests to FotMob for each season, parses the HTML, and extracts JSON data containing league standings
2. **Data Extraction**: Parses team names and positions using regex and JSON processing
3. **Data Processing**: Combines data from all seasons into a single DataFrame
4. **Visualization**: Creates a line chart with reversed y-axis (position 1 at top) showing trends over time

## Notes

- The chart's y-axis is reversed so that 1st place appears at the top
- Hover over the chart for detailed information about each data point
- The script includes progress indicators while scraping
- All 20 teams per season are saved to CSV, but only the top 6 are visualized

## Customization

To track different teams, modify the `top_teams` list:

```python
top_teams = ['Arsenal', 'Manchester City', 'Liverpool', 'Chelsea', 
             'Manchester United', 'Tottenham']
```

To change the season range, adjust the range in the loop:

```python
for year in range(2015, 2025):  # Change start/end years here
```

## Disclaimer

This script scrapes publicly available data from FotMob. Please respect the website's terms of service and use responsibly. Consider adding delays between requests if scraping large amounts of data.
