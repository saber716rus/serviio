Starting the server from command line
=====================================

Serviio consists from 2 executable files, a server and a console. To start using Serviio
do the following:

1) Windows - the server starts automatically after Windows start. Run ServiioConsole or open 
           	 http://localhost:23423/console in your browser to start the console. Alternatively 
           	 you don't have to start Serviio as a service but use bin/serviio.bat 
           	 (with -stop attribute to stop a running instance).
             
2) Linux - run Serviio server with bin/serviio.sh (with -stop attribute to stop a running 
           instance). To start the console run bin/serviio-console.sh or open 
           http://localhost:23423/console in your browser.

3) OSX - the server starts automatically after the OS start. To start the console execute
         Serviio-Console application from your Applications folder or open 
         http://localhost:23423/console in your browser.
         
         To stop the server, run this in the Terminal:
         
         sudo launchctl unload /Library/LaunchDaemons/org.serviio.server.plist
         
         To start the server, run this in the Terminal:
         
         sudo launchctl load /Library/LaunchDaemons/org.serviio.server.plist
           

Only one instance of the server and client can run at a given time on a single machine.

To set up a Serviio server running on another machine (and possibly OS),
open http://server_ip:23423/console in your browser.

Secure HTTP protocol
====================

To communicate with the Serviio server securely via HTTPS, use these URLs to access the
console and MediaBrowser:

https://localhost:23523/console
https://localhost:23524/mediabrowser


Included libraries and tools
============================

 
LAME MP3 Encoder
----------------

This software includes (in its Windows and OSX distributions) LAME MP3 Encoder (http://lame.sourceforge.net/). 
It is statically linked to FFmpeg. Source code used to build it can be found here (ver. 3.99.5): 
http://download.serviio.org/opensource/lame-3.99.5.tar.gz

libRTMP
-------

This software includes (in its Windows and OSX distributions) librtmp (http://rtmpdump.mplayerhq.hu/librtmp.3.html).
It is statically linked to FFmpeg. Source code used to build it can be found here (ver. 2.4 +): 
http://download.serviio.org/opensource/rtmpdump.tar.gz

x264
----

This software includes (in its Windows and OSX distributions) x264 (http://www.videolan.org/developers/x264.html).
It is statically linked to FFmpeg. Source code used to build it can be found here: 
http://download.serviio.org/opensource/last_x264.tar.bz2


libass
------

This software includes (in its Windows and OSX distributions) libass (http://code.google.com/p/libass/).
It is statically linked to FFmpeg. Source code used to build it can be found here (ver. 0.10.1): 
http://download.serviio.org/opensource/libass-0.10.1.tar.gz

FontConfig
----------

This software includes (in its Windows and OSX distributions) Fontconfig (http://www.fontconfig.org/).
It is statically linked to FFmpeg. Source code used to build it can be found here (ver. 2.10.91): 
http://download.serviio.org/opensource/fontconfig-2.10.91.tar.gz

Freetype2
---------

This software includes (in its Windows and OSX distributions) Freetype2 (www.freetype.org/freetype2/index.html).
It is statically linked to FFmpeg. Source code used to build it can be found here (ver. 2.4.11): 
http://download.serviio.org/opensource/freetype-2.4.11.tar.gz

Speex
-----

This software includes (in its Windows and OSX distributions) Speex (http://www.speex.org/).
It is statically linked to FFmpeg. Source code used to build it can be found here (ver. 1.2rc1): 
http://download.serviio.org/opensource/speex-1.2rc1.tar.gz

Ogg
---

This software includes (in its Windows and OSX distributions) libOgg (http://xiph.org/ogg/).
It is statically linked to FFmpeg. Source code used to build it can be found here (ver. 1.3.2): 
http://download.serviio.org/opensource/libogg-1.3.2.tar.gz

FFmpeg
------

This software includes (in its Windows and OSX distributions) FFmpeg (a great video library).
Source code used to build it can be found here: 
http://download.serviio.org/opensource/ffmpeg-3.4.4.tar.bz2

*Linux* users should use the latest FFmpeg included in their OS distributions or compile the above sources. It should
include librtmp for RTMP streaming support and libass for subtitles rendering.


dcraw
-----

This software includes dcraw.c - Dave Coffin's raw photo decoder. Source code can be found at
http://www.cybercom.net/~dcoffin/dcraw/dcraw.c
