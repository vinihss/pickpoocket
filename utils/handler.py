import json


class File:

    def save_info(self, info, filename="info3.txt"):
        with open(filename, "w") as file:
            file.write(json.dumps(info, indent=4))