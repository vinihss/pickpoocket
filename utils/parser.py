from fastapi import Request, requests


class Silhouette:
    def __init__(self):
        self.request = {}
        self.token = "884f974e7198dc"
        self.location = {
            "city": "Unknown",
            "region": "Unknown",
            "country": "Unknown",
            "loc": "Unknown"
        }
        self.browser_info=""
        self.cookies=""

    def set_cookies(self, request: Request):
        self.request = self.request.headers.get('cookie', '')

    def set_location(self, ip):
        url = f"https://ipinfo.io/{ip}/json?token={self.token}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            location = {
                "city": data.get("city", "Unknown"),
                "region": data.get("region", "Unknown"),
                "country": data.get("country", "Unknown"),
                "loc": data.get("loc", "Unknown")
            }

    def set_motherfuckin_host_info(self, socket):
        self.host_info = {
            "hostname" : socket.gethostname(),
            "ip" : socket.gethostbyname(socket.gethostname())
        }

    def get_browser_info(self):
        return

    def define_figure(self):
        return {
                "host_info": self.host_info,
                "location": self.location,
            }


