BENSONHURST = '11204'
JERSEY_CITY = '07302'
MORRISTOWN = '07960'

import json
import requests
import argparse
from rite_aid import zip_search, stores

# BENSONHURST = '11204'
# JERSEY_CITY = '07302'
# MORRISTOWN = '07960'

parser = argparse.ArgumentParser()
parser.add_argument("zip_code", help="currently supported zips: 11204, 07302, 07960")
parser.add_argument("--shot", help="shot number to check availability for", default=1, type=int)
args = parser.parse_args()

def check_appointments(zip_code:str, shot_number:int = 1) -> list:
    stores = zip_search[zip_code]
    BASE_URL = "https://www.riteaid.com/services/ext/v2/vaccine/checkSlots?storeNumber={store_num}"
    
    availabilities = list()

    return {
        store : json.loads(
            requests.get(BASE_URL.format(store_num = store)).content
        )['Data']['slots'][str(shot_number)] for store in stores 
    }
    
if __name__ == '__main__':
    result = check_appointments(zip_code=args.zip_code, shot_number=args.shot)
    print(result)