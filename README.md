# Claudie
Claudie is a :cloud: in our office that :zap: every time someone Prynt, scan a picture of interact with our social networks.

We use a Raspberry Pi to light our LEDs.

A video of the final project is visible on [our Facebook page](https://www.facebook.com/iamprynt/videos/1535504956468942/).



### How to run it

On your Raspberry Pi:
```
pip install RPi.GPIO
pip install Flask
git clone git@github.com:rvi/Claudie.git

sudo apt-get update
sudo apt-get install build-essential python-dev git scons swig
git clone git@github.com:rvi/rpi_ws281x.git
cd rpi_ws281x
scons
cd python
sudo python setup.py install

cd ../../Claudie
python app.py
```
