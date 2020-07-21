# Karlie
<img src="https://svgshare.com/i/N5x.svg" width="200">


[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://www.python.org/)  [![forthebadge](https://forthebadge.com/images/badges/uses-html.svg)](https://en.wikipedia.org/wiki/HTML)

[![forthebadge](https://forthebadge.com/images/badges/does-not-contain-treenuts.svg)](https://i.pinimg.com/originals/84/0e/5f/840e5fe01951213fe54ceb0786e3cf7c.gif)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)



Karlie is an open source statistics maker, based on user privacy

## Installation

That's so simple ! 

Just clone repository

`` git clone https://github.com/Kaporos/Karlie``

And then, install all dependencies

`` (sudo) pip install -r requirements.txt ``

For the last step do:

`` cp karlie.js.exemple karlie.js ``

And edit karlie.js to replace SERVER_ADDR by your server adress
Ex:
```async function hello()
{
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", "https://yourserver.com:9999"+window.location.search); // false for synchronous request
    xmlHttp.send( null );
}
hello();
```

### How to start it

There are two ways to start Karlie, the first is to simply do:

`` python main.py``

The second, lets launch it with gunicorn

`` gunicorn -b 0.0.0.0:9999 -w 1 main: app``


Be careful to put only one worker, otherwise the modifications to the db will be overwrited between workers

By default, the working port of karlie is 9999, it can be changed either in main.py or in the gunicorn command

Here is a configuration for a systemd service: 
```
[Unit]
Description=Karlie
After=network.target

[Service]
User=theo
WorkingDirectory=/home/yourhome/Karlie
ExecStart=/usr/local/bin/gunicorn -b 0.0.0.0:9999 -w 1 main:app
#Restart=always

[Install]
WantedBy=multi-user.target
```


Done ! For test your installation, simply go to http://yourserver.com:9999/main.js

See if your server is returning some javascript, and if in javascript, SERVER_ADDR is replaced by yourserver.com:9999

## Setup in your website

For starting using Karlie with your website , that's very simple !
Just include 

``<script src="http://yourserver.com:9999/main.js"></script>``

Now , Karlie with start doing its job

Karlie will include all url params in stats , for apply filter.

So, if your website url is ``https://mywebsite.com" , do not hesitate to add url parameters according to the sources of links, example:

If you put your website link on your facebook , put this : 
``https://mywebsite.com?source=Facebook``

Karlie will detect all url params , and save them , so later, you can filter the statistics to see for example all the visits to your site coming from your Facebook

It works for the source parameter, but it works for all the other possible and unimaginable parameters

If you want some ideas : 

| URL Param       | Why                                                                                    |
| --------------- | -------------------------------------------------------------------------------------- |
| source          | To know where people come from                                                         |
| provider        | If more than one of you own the website, you can see who has attracted the most people |
| And many more ! | You can use whatever you want !                                                        |  |  |

## Anonymity

Karlie only saves your approximate location (Country), and the hash of your ip to know if you have already visited the tracked page, but in any case we can not find your ip address, your precise location or something else about your users

## Web GUI
in development

## Made By :

[Kaporos](https://github.com/Kaporos/)

[Charlie08](https://github.com/charlie08-dev)

