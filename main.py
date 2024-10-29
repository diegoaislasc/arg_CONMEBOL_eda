from scraping_functions import *
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def main():
    
    data_dicts = [
        {
            # Argentina vs Canada (2 - 0) - Groups phase
            'stats_url': 'https://www.sofascore.com/api/v1/event/11886373/statistics',
            'shotmap_url': 'https://www.sofascore.com/api/v1/event/11886373/shotmap',
            'stats_filename': 'match1_stats.csv',
            'shotmap_filename': 'match1_shotmap.csv'
        },
        {
            # Chile vs Argentina (0 - 1) - Groups phase
            'stats_url': 'https://www.sofascore.com/api/v1/event/11886369/statistics',
            'shotmap_url': 'https://www.sofascore.com/api/v1/event/11886369/shotmap',
            'stats_filename': 'match2_stats.csv',
            'shotmap_filename': 'match2_shotmap.csv'
        },
        {
            # Argentina vs Peru (2 - 0) - Groups phase
            'stats_url': 'https://www.sofascore.com/api/v1/event/11886396/statistics',
            'shotmap_url': 'https://www.sofascore.com/api/v1/event/11886396/shotmap',
            'stats_filename': 'match3_stats.csv',
            'shotmap_filename': 'match3_shotmap.csv'
        },
        {
            # Argentina vs Ecuador (1 - 1)(Penalties: 4 - 2) - Quarter finals
            'stats_url': 'https://www.sofascore.com/api/v1/event/11886594/statistics',
            'shotmap_url': 'https://www.sofascore.com/api/v1/event/11886594/shotmap',
            'stats_filename': 'match4_stats.csv',
            'shotmap_filename': 'match4_shotmap.csv'
        },
        {
            # Argentina vs Canada (2 - 0) - Semi finals
            'stats_url': 'https://www.sofascore.com/api/v1/event/11886259/statistics',
            'shotmap_url': 'https://www.sofascore.com/api/v1/event/11886259/shotmap',
            'stats_filename': 'match5_stats.csv',
            'shotmap_filename': 'match5_shotmap.csv'
        },
        {
            # Argentina vs Colombia (1 - 0) - Final
            'stats_url': 'https://www.sofascore.com/api/v1/event/11886600/statistics',
            'shotmap_url': 'https://www.sofascore.com/api/v1/event/11886600/shotmap',
            'stats_filename': 'match6_stats.csv',
            'shotmap_filename': 'match6_shotmap.csv'
        }
    ]

    try:
        for match_data in data_dicts:
            extract_stats(match_data['stats_url'], match_data['stats_filename'])
            extract_shotmap(match_data['shotmap_url'], match_data['shotmap_filename'])
    except Exception as error:
        logging.error(f"An unexpected error ocurred: {error}")


if __name__ == "__main__":
    main()
