CMPUT404-assignment-websockets
==============================

CMPUT404-assignment-websockets

See requirements.org (plain-text) for a description of the project.

Make a shared state Websockets drawing program

Prereqs
=======

pip install flask-sockets

pip install ws4py

pip install gunicorn

Contributors / Licensing
========================

Generally everything is LICENSE'D under the Apache 2 license by Abram Hindle.

freetests.py is LICENSE'D under a BSD-like license:

From ws4py

Copyright (c) 2011-2014, Sylvain Hellegouarch, Abram Hindle
All rights reserved.

Additions made for CMPUT 404 Winter 2017 by David Yee are similarly licensed
under the Apache 2 license. Additional resources and their respective licenses
are cited below.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

 * Redistributions of source code must retain the above copyright notice,
   this list of conditions and the following disclaimer.
 * Redistributions in binary form must reproduce the above copyright
   notice, this list of conditions and the following disclaimer in the
   documentation and/or other materials provided with the distribution.
 * Neither the name of ws4py nor the names of its contributors may be used
   to endorse or promote products derived from this software without
   specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
POSSIBILITY OF SUCH DAMAGE.

Contributors
============

* Mark Galloway
* Abram Hindle
* David Yee

Sources
=======

* Flask JSONify (http://flask.pocoo.org/docs/0.12/api/#flask.json.jsonify)

* Queue (https://docs.python.org/2/library/queue.html)

* json dump (https://docs.python.org/2/library/json.html#json.dumps)

* Spawning greenlets idea from 
  http://sdiehl.github.io/gevent-tutorial/#spawning-greenlets

* Dictionary iteration idea by
  sberry (http://stackoverflow.com/users/141555/sberry) from
  http://stackoverflow.com/a/3294899/2557554 and licensed under
  CC-BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)

* JSON response idea by
  Torben (http://stackoverflow.com/users/398844/torben) from
  http://stackoverflow.com/a/8416963/2557554 and licensed under
  CC-BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)

* Circle formula and code idea by
  Philipp Jahoda (http://stackoverflow.com/users/1590502/philipp-jahoda) at
  http://stackoverflow.com/a/25929952/2557554 and licensed under
  CC-BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)

* Star drawing code based on code written by
  markE (http://stackoverflow.com/users/411591/marke) at
  http://stackoverflow.com/a/25840319/2557554 and licensed under
  CC-BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0/)
