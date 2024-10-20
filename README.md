# Picatend
Pic-at-end is an application designed to capture images from a webcam, saving the last frame as a JPG file upon closing the application. 
If multiple cameras are connected, the most recently connected one will be used (particularly relevant for notebooks).

## Demo
<img src="https://raw.githubusercontent.com/fibit/picatend/fd6bd9112a7da1eaba8e2093749263dd99980a41/demo.gif" alt="picanted">

## How use
1. ```git clone git@github.com:fibit/picatend.git```
2. ```cd picatend```
3. ```pip install -r requirements.txt```
4. ```python3 picatend.pyw```

## How build
To build, use [auto-py-to-exe](https://github.com/brentvollebregt/auto-py-to-exe):
1. ```git clone git@github.com:fibit/picatend.git```
2. ```cd picatend```
3. ```pip install -r requirements.txt```
4. ```auto-py-to-exe --config build.json```
