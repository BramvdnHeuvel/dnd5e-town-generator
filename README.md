# The dnd5e town generator

This repository contains a program that allows you to look up humongous cities in a "memory free" manner. This program is running live on [this website](http://town.noordstar.me/)!

## How does it work?

The dnd5e-town-generator makes use of what's called pseudo-randomness.
Pseudo-randomness is given a determined seed, which will always reproduce the same "random" values.

We are using this property to regenerate the town.
This means that the program is way more memory-friendly, but requires quite a bit more CPU-time,
as the town needs to be regenerated every time.

The reason why that's efficient, is the assumption that a Dungeon Master will only look up data
at a human's speed - not at a computer's. This means that they'll look up people at a relatively
low speed.

## How to set up

You can install the requirements and run `main.py`. Alternatively, you can run the town generator in a Docker container. Build the Docker image with the following command:

```
docker build -t dnd-town-gen ./
```

And then run the docker container with the following data.

```
docker run -p 5000:5000 \
--name town-generator \
-e HOST='<desired ip address, usually 127.0.0.1 or 0.0.0.0>' \
-e SECRET_KEY='<random password if desired>' \
dnd-town-gen
```