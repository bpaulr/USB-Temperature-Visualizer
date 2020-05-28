import requests
import json
from datetime import datetime
from typing import List
from typing import Dict
import os

TEMPERATURE_URL = "https://api.usb.urbanobservatory.ac.uk/" \
                  "api/v2/sensors/timeseries/"


def scrape_temps(room_name: str, room_timeseries_ids: List[str],
                 store_location: str) -> None:
    if store_location is None:
        raise SyntaxError("Insufficient arguments, please specify a"
                          "file path to store the scraped data.")

    room_data = []

    for room in room_timeseries_ids:
        response = __scrape_room_temp(room)
        print(room_name, room, response)
        if response:
            room_data.append(response)

    if not os.path.exists(store_location):
        os.mkdir(store_location)

    # remove ms and slug date
    datetime_suffix = str(datetime.now()).split(".")[0] \
        .replace(" ", "_").replace(":", "-")

    file_name = room_name + "_" + datetime_suffix + ".json"

    __write_to_file(room_data, store_location + "/" + file_name)


def __write_to_file(data: List[Dict], file_path):
    with open(file_path, "w+") as file:
        json.dump(data, file)


def __scrape_room_temp(timeseries_id: str) -> Dict:
    request_url = TEMPERATURE_URL + timeseries_id
    response = requests.get(request_url)
    if response.status_code != 200:
        return None
    return response.json()
