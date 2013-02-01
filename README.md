simple-testing-server
=====================

A stupidly simple python server that allows you to test client code before you have a server that actually works
Allows you to test json responses with the proper headers built in, and also custom error codes.



Motivation
---

So say you want to build some sort of app that connects to a client... great! Sounds like you are working on
a cool project. But how are you going to deal with separating the development between the application logic
and the backend api? Where are your api calls supposed to go before that server exists? Enter this project.

![nahmsayin](http://4.bp.blogspot.com/-O8eUpIhq_Qs/TxzG47NqOHI/AAAAAAAADIw/Qp38AQeU7Jk/s640/namsayin.jpg)

Example Usage
---

Start by spinning up the server using

```sh
python simple-testing-server.py --port <PORT>
```

### GET

Like JSON? Of course you do. Say you want to get some example json response from your server.
Suppose you're modeling some data in your app. Let's call an example model ```events```. Then do a little 

```GET http://localhost:<PORT>/events``` 

action. This will return to you the contents of a 
file called ```events.json``` with proper headers. This file is up to you to create and place in the same folder as the python
script.

More generally, ```GET http://localhost:<PORT>/<model_name>``` will return an ```application/json``` response 
with content taken from a file called ```<model_name>.json``` placed in the same folder as the script.
BYO example json files.

### POST

Eventually you'll probably want to do some POST'ing. Don't worry, we've got you covered. Want to 
try a post request with a successfull (200) response?

```POST http://localhost:<PORT>/success```

easy.

Want a failure (500)? Try

```POST http://localhost:<PORT>/error```

Those two response codes aren't good enough for you? Fine.

```POST http://localhost:<PORT>/<response_code>```

There you have it.


Compatibility
---

AFAIK all versions of python. If you don't have ```argparse``` installed, the custom port won't
work and it will just default to ```PORT=8003``` every time.


Authors
-----

- Matthew Conlen, github@mathisonian.com

License
-----

This program is free software. It comes without any warranty, to
the extent permitted by applicable law. You can redistribute it
and/or modify it under the terms of the WTFPL, Version 2, as
published by Sam Hocevar. See http://sam.zoy.org/wtfpl/
for more details.
