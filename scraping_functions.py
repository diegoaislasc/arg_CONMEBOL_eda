import requests
import csv
import logging


FULL_MATCH = 'Full Match'
FIRST_HALF = 'First Half'
SECOND_HALF = 'Second Half'
EXTRA_TIME_1 = 'Extra Time 1'
EXTRA_TIME_2 = 'Extra Time 2'


def write_statistics_to_csv(writer, period, groups):
    for group in groups:
        group_name = group['groupName']
        for item in group['statisticsItems']:
            writer.writerow([period, group_name, item['name'], item['home'], item['away']])


def extract_stats(url, filename):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as error:
        logging.error(f"There has been an error while requesting to {url}: {error}")
        return

    try:
        data = response.json()
        match_stats = data['statistics']
    except (ValueError, KeyError) as error:
        logging.error(f"There has been an error while processing JSON data: {error}")
        return

    if not match_stats:
        logging.warning(f"No statistics found in the gathered data from {url}")
        return

    try:
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Period', 'Group', 'Statistic', 'Home', 'Away'])

            if len(match_stats) >= 3:
                write_statistics_to_csv(writer, FULL_MATCH, match_stats[0]['groups'])
                write_statistics_to_csv(writer, FIRST_HALF, match_stats[1]['groups'])
                write_statistics_to_csv(writer, SECOND_HALF, match_stats[2]['groups'])

            if len(match_stats) == 5:
                write_statistics_to_csv(writer, EXTRA_TIME_1, match_stats[3]['groups'])
                write_statistics_to_csv(writer, EXTRA_TIME_2, match_stats[4]['groups'])

            logging.info(f"Statistics written succesfully in {filename}")

    except IOError as error:
        logging.error(f"Could not write in file {filename}: {error}")


def extract_shotmap(url, filename):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as error:
        logging.error(f"There has been an error while requesting {url}: {error}")
        return

    try:
        data = response.json()
        shotmap = data['shotmap']
    except (ValueError, KeyError) as error:
        logging.error(f"There has been an error while processing JSON data: {error}")
        return

    if not shotmap:
        logging.warning(f"Shotmap data was not found in {url}")
        return

    try:
        with open(filename, mode='w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Name', 'Position', 'Outcome', 'Situation', 'Player Coordinates', 'Body Part',
                             'Shot Location', 'Shot Coordinates', 'Expected Goal (xG)',
                             'Expected Goal on Target (xGOT)'])

            for shot in shotmap:
                player_name = shot['player'].get('name', '')
                player_position = shot['player'].get('position', '')
                outcome = shot.get('shotType', '')
                situation = shot.get('situation', '')
                player_coordinates = shot.get('playerCoordinates', {})
                body_part = shot.get('bodyPart', '')
                shot_location = shot.get('goalMouthLocation', '')
                shot_coordinates = shot.get('goalMouthCoordinates', {})
                xg = shot.get('xg', 0)
                xgot = shot.get('xgot', 0)

                writer.writerow([player_name, player_position, outcome, situation, player_coordinates,
                                 body_part, shot_location, shot_coordinates, xg, xgot])

            logging.info(f"Shotmap data written succesfully in {filename}")
    except IOError as error:
        logging.error(f"Error while writing in {filename}: {error}")
