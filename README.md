# MinecraftVersions.py
#### A simple minecraft version wrapper written in python

## Installing
#### Python 3.8 or higher is required
### To install the stable version:
#### For linux/MacOS
```bash
python3 -m pip install -U "minecraftVersions"
```
#### For Windows
```batch
pip install -U minecraftVersions
```
### To install the development version:
#### For linux/MacOS
```bash
python3 -m pip install -U git+https://github.com/tungdo0602/MinecraftVersions.py
```
#### For Windows
```batch
pip install -U git+https://github.com/tungdo0602/MinecraftVersions.py
```

## Example
#### Get the latest release minecraft server software:
```python
import minecraftVersions
from minecraftVersions import MCVersion
mc = MCVersion()
mc.latest().server().download("server.jar")
```

#### Get the specific minecraft version:
```python
import minecraftVersions
from minecraftVersions import MCVersion
mc = MCVersion()
mc.getVersion("1.18.2")
##Do something with it
```
