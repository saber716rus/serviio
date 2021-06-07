#!/bin/bash
if which xdg-open > /dev/null
then
  xdg-open "http://localhost:23423/console"
elif which gnome-open > /dev/null
then
  gnome-open "http://localhost:23423/console"
fi
