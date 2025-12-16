from bs4 import BeautifulSoup
import requests
import json
import re
import pandas as pd
import plotly.express as px

def scrape_season_table(year_start, year_end):
    season = f"{year_start}/{year_end}"
    url = f"https://www.fotmob.com/leagues/47/table/premier-league?season={season}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    scripts = soup.find_all('script')
    for script in scripts:
        if script.string and '"table"' in script.string:
            json_text = script.string
            match = re.search(r'"props":\s*({.+?}),"page":', json_text)
            if match:
                props_data = json.loads(match.group(1))
                table_data = props_data['pageProps']['table'][0]['data']['table']['all']
                
                teams = []
                for team in table_data:
                    teams.append({
                        'Season': season,
                        'Team': team['name'],
                        'Position': team['idx']
                    })
                return teams
    return []

all_data = []
for year in range(2015, 2025):
    print(f"Scraping {year}/{year+1}...")
    season_data = scrape_season_table(year, year+1)
    all_data.extend(season_data)

df = pd.DataFrame(all_data)
df.to_csv('premier_league_positions.csv', index=False)
print(f"\n✅ Scraped {len(df)} records!")
print(df.head(20))

df = pd.read_csv('premier_league_positions.csv')

top_teams = ['Arsenal', 'Manchester City', 'Liverpool', 'Chelsea', 
             'Manchester United', 'Tottenham']
df = df[df['Team'].isin(top_teams)]

fig = px.line(df, 
              x='Season', 
              y='Position',
              color='Team',
              markers=True,
              title='Premier League Position Changes Over Time')

fig.update_yaxes(autorange='reversed', title='League Position')
fig.update_xaxes(title='Season')

fig.update_layout(height=600, hovermode='x unified')

fig.write_html('premier_league_chart.html')

fig.show()