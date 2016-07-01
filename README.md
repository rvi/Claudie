# Claudie
Claudie is a :cloud: in our office that :zap: every time someone Prynt, scan a picture of interact with our social networks.

We started this project on a creativity day, which happens once a month.

We use a Raspberry Pi to light our LEDs. This project is still in early stage.


### How to run it

On your Raspberry Pi:
```
pip install RPi.GPIO
pip install Flask
git clone git@github.com:prynt/Claudie.git

sudo apt-get update
sudo apt-get install build-essential python-dev git scons swig
git clone git@github.com:prynt/rpi_ws281x.git
cd rpi_ws281x
scons
cd python
sudo python setup.py install

cd ../../Claudie
python app.py
```
