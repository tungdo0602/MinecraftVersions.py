import requests
from urllib.parse import urlparse, unquote

class MCVersion():
    def __init__(self, src=None, isRes=True):
        if isRes:
            data = requests.get(src if src else "https://launchermeta.mojang.com/mc/game/version_manifest_v2.json")
            if data.status_code == 200:
                self.data = data.json()
            else:
                raise Exception("Failed to get data from the server!")
        else:
            self.data = src
        
    def latest(self):
        return latest(self.data)
    
    def getVersion(self, version: str):
        for v in self.data["versions"]:
            if version == v["id"]:
                return versionManager(v)
        raise ValueError("Could not find that Minecraft version!")
    
    get = getVersion
    version = getVersion
    
    def versionInclude(self, s, first=True):
        versions = []
        for v in self.data["versions"]:
            if s in v["id"]:
                if first:
                    return v["id"]
                else:
                    versions.append(v["id"])
        return versions
    
    getVersionInclude = versionInclude
    
    def getByInclude(self, s, first=True):
        return self.versionInclude(s, first)
    
    getByInclude = versionInclude
    
    def getAllVersions(self):
        """
        versions = []
        for v in self.data["versions"]:
            versions.append(v["id"])
        """
        return allVersions(self.data)
    
    getAllVersion = getAllVersions
    
    def getAll(self, s="", first=True):
        if s:
            return self.versionInclude(s, first)
        else:
            return allVersions(self.data)

class allVersions():
    def __init__(self, data):
        self.data = data
        
    def __str__(self):
        return " ".join([i["id"] for i in self.data["versions"]])
    
    def toList(self):
        return [i["id"] for i in self.data["versions"]]
    
    def list(self):
        return self.toList()
    
    def get(self, version):
        return MCVersion(self.data, False).getVersion(version)
    
    getVersion = get
    
    version = get
    
    def versionIncludes(self, s, first=True):
        return MCVersion(self.data, False).versionInclude(s, first)
    
    getVersionInclude = versionIncludes
    
    getByInclude = versionIncludes
    
    def getAll(self, s="", first=True):
        if s:
            MCVersion(self.data, False).versionInclude(s, first)
        else:
            return allVersions(self.data)

class latest():
    def __init__(self, data):
        self.data = data
    
    def release(self):
        return MCVersion(self.data, False).getVersion(self.data["latest"]["release"])
    
    def snapshot(self):
        return MCVersion(self.data, False).getVersion(self.data["latest"]["snapshot"])

class versionManager():
    def __init__(self, data):
        self.data = data
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
    
    def __str__(self):
        return self.data["id"]
    
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
