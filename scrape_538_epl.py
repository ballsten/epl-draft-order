# Scrapes the 538 predictions to a file

from selenium import webdriver
import pandas as pd

options = webdriver.ChromeOptions()
options.binary_location = '/Applications/Google Chrome Canary.app/Contents/MacOS/Google Chrome Canary'
options.add_argument('window-size=800x841')
options.add_argument('headless')

team_name_map = {
    'Manchester City': 'Man City',
    'Chelsea': 'Chelsea',
    'Liverpool': 'Liverpool',
    'Manchester United': 'Man United',
    'Tottenham Hotspur': 'Tottenham',
    'Arsenal': 'Arsenal',
    'Burnley': 'Burnley',
    'Leicester City': 'Leicester',
    'Everton': 'Everton',
    'Watford': 'Watford',
    'Crystal Palace': 'Crystal Palace',
    'Huddersfield Town': 'Huddersfield',
    'Southampton': 'Southampton',
    'Stoke City': 'Stoke',
    'Brighton and Hove Albion': 'Brighton',
    'West Ham United': 'West Ham',
    'AFC Bournemouth': 'Bournemouth',
    'Newcastle': 'Newcastle',
    'West Bromwich Albion': 'West Brom',
    'Swansea City': 'Swansea',
    'Fulham': 'Fulham',
    'Wolverhampton': 'Wolves',
    'Cardiff City': 'Cardiff'
}

def scrape_predictions():
    driver = webdriver.Chrome(chrome_options=options)
    driver.get('https://projects.fivethirtyeight.com/soccer-predictions/premier-league/')

    # get date
    pred_date = driver.find_elements_by_xpath('//*[@id="league-info-wrap"]/div/div[2]/h3')[0].text

    rows = driver.find_elements_by_xpath("/html/body/div[5]/div[3]/div[1]/div/table/tbody/tr")

    predictions = []

    for row in rows:
        team = team_name_map[row.get_attribute('data-str')]
        prediction = {
            'Team': team,
            'GD': row.find_elements_by_xpath("td[8]")[0].text,
            'Pts': row.find_elements_by_xpath("td[9]")[0].text
        }
        predictions.append(prediction)

    # write update date to last row
    predictions.append({'Team': pred_date, 'GD': '', 'Pts': ''})

    df = pd.DataFrame(predictions)

    df.to_csv("data/538.csv", sep='\t', columns=['Team', 'Pts', 'GD'], index=False)

    driver.quit()

if __name__ == "__main__":
    scrape_predictions()
