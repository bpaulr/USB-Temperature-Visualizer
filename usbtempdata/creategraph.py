import os
from typing import Dict
from typing import List

import matplotlib.pyplot as plt
import mpld3
import json
import dateutil.parser


def create_graph(data_directory: str, output_dir: str, output_file: str = "graph.html") -> str:  # file path
    room_data = {}
    files = [f for f in os.listdir(data_directory) if os.path.isfile(os.path.join(data_directory, f))]
    for file in files:
        with open(os.path.join(data_directory, file)) as fp:
            json_data = json.load(fp)

            avg_temp = __get_average(json_data)
            date_str = json_data[0]["latest"]["time"]
            room_str = json_data[0]["parentFeed"]["parentEntity"]["meta"]["roomNumber"]

            if room_str not in room_data:
                room_data[room_str] = {
                    "dates": [],
                    "temps": [],
                }

            room_data[room_str]["dates"].append(date_str)
            room_data[room_str]["temps"].append(avg_temp)

    __add_to_graph(room_data)

    plt.title("USB PC Cluster Temperatures")
    plt.xlabel("Date-Time")
    plt.ylabel("Temperature (Degrees)")
    plt.legend()
    plt.gcf().autofmt_xdate()

    html = __get_html_graph()

    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    file_path = os.path.join(output_dir, output_file)

    with open(file_path, "w+") as file:
        file.write(html)

    return file_path


def __get_html_graph():
    return f"""
        <!DOCTYPE html>
        <html>
          <head>
            <meta charset="UTF-8">
            <title>title</title>
          </head>
          <body>
            {mpld3.fig_to_html(plt.gcf())}
          </body>
        </html>
    """


def __get_average(json_data: Dict):
    temps = []
    for zone in json_data:
        temp = zone["latest"]["value"]
        temps.append(temp)

    return sum(temps) / len(temps)


# def __add_to_graph(room: str, xdatestrs: List[str], ytempfloats: List[float]) -> None:
def __add_to_graph(room_data: Dict) -> None:
    print()
    for k, v in room_data.items():
        datetime_dates = [dateutil.parser.parse(d) for d in v["dates"]]
        print(datetime_dates)
        plt.plot(datetime_dates, v["temps"], label=k)
