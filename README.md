# MinecraftVersions.py
#### A simple minecraft version wrapper written in python

## Installing
#### Python 3.8 or higher is required
### To install the stable version:
#### For linux/MacOS
```bash
python3 -m pip install -U ""
```
#### For Windows
```batch
pip install -U 
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
mc = minecraftVersion()
mc.latest().server().download("server.jar")
```

#### Get the specific minecraft version:
```python
mc = minecraftVersion()
mc.getVersion("1.18.2")
##Do something with it
```
