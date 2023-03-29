import requests
from urllib.parse import urlparse, unquote

class minecraftVersion():
    def __init__(self):
        data = requests.get("https://launchermeta.mojang.com/mc/game/version_manifest_v2.json")
        if data.status_code == 200:
            self.data = data.json()
        else:
            raise Exception("Failed to get data from mojang server!")
        
    def latest(self):
        return latest(self.data["latest"], self.data["versions"])
    
    def getVersion(self, version: str):
        for v in self.data["versions"]:
            if version == v["id"]:
                return versionManager(v)
        raise ValueError("Could not find that Minecraft version!")
    
    def getAllVersions(self):
        versions = []
        for v in self.data["versions"]:
            versions.append(v["id"])
        return versions

class latest():
    def __init__(self, data, vdata):
        self.data = data
        self.vdata = vdata
    
    def getVersion(self, version: str):
        for v in self.vdata:
            if version == v["id"]:
                return versionManager(v)
        raise ValueError("Could not find that Minecraft version!")
    
    def release(self):
        return self.getVersion(self.data["release"])
    
    def snapshot(self):
        return self.getVersion(self.data["snapshot"])

class versionManager():
    def __init__(self, data):
        self.version = data["id"]
        self.type = data["type"]
        self.url = data["url"]
        self.time = data["time"]
        self.releaseTime = data["releaseTime"]
        self.sha1 = data["sha1"]
        self.complianceLevel = data["complianceLevel"]
        versionData = requests.get(self.url)
        if versionData.status_code == 200:
            self.data = versionData.json()
        else:
            raise Exception("Failed to get data from mojang server!")
    
    def client(self):
        return downloadObj(self.data["downloads"]["client"])
        
    def server(self):
        return downloadObj(self.data["downloads"]["server"])
    
class downloadObj():
    def __init__(self, data):
        self.data = data
        self.sha1 = data["sha1"]
        self.size = data["size"]
        self.url = data["url"]
    
    def download(self, filename=None):
        with requests.get(self.url, stream=True) as r:
            r.raise_for_status()
            with open(filename if filename else unquote(urlparse(self.url).path.split("/")[-1]), "r") as f:
                for c in r.iter_content(chunk_size=1048576): #1MB
                    f.write(c)
        return self.url