import sys

from usbtempdata import scrapetemps
from usbtempdata import creategraph

# room number string to list of UrbanObservatory timeseries ids
ROOMS = {
    "3.005": ["52bbd41d-56f8-4dec-8cb6-33131a08ecdf",
              "5b917b42-c80f-454a-922a-691d7ae36120",
              "9e894da9-3bfd-45ec-96de-78c8611dd787",
              "f9735a6a-a89f-4008-b468-0d18e6ad60ae"],
    "3.015": ["04f78540-d072-4a61-af82-d9247d042e89",
              "721b178c-8776-4465-b0f0-659963a9e0c1",
              "2886febb-e170-4f61-a1d2-692fdd8ad392",
              "d3f814bd-daa0-4f31-beca-70c1cb3e3d7d",
              "957c8414-f6b7-41b8-88ab-ac0d9148f176",
              "594f49e5-bb06-4283-b123-2e2bf5a196de",
              "801d1a42-51ac-4c0e-916b-dc5706f93e44",
              "afba0627-32ee-48fa-b56b-ea39be6f0f39",
              "58081326-b11e-49c6-a84c-bc30b3e10187"],
    "3.018": ["c989bedf-b14f-4a72-aec7-b045052a4ec6",
              "7762fc34-8556-4afe-b1de-5d964d9ef778",
              "d6c2f9ff-1e76-4702-8fad-3bf84ac62e6a",
              "201083cc-76b9-4697-8909-ab364d61e246"],
    # "4.018": ["37e41784-a0f7-49f0-b0bc-863bbf158c8f"],
}


def main(file_path: str = "usbtempdata/data", output_file: str = "graph.html"):
    for k, v in ROOMS.items():
        scrapetemps.scrape_temps(k, v, file_path)
    file = creategraph.create_graph(file_path, file_path, output_file)
    print("Created file " + file)


if __name__ == '__main__':
    args = len(sys.argv)
    if args <= 1:
        main()
        # raise SyntaxError("Insufficient arguments, please specify a file path to place the graph.")
    elif args == 2:
        main(sys.argv[1])
    else:
        main(sys.argv[1], sys.argv[2])
