#! /bin/bash

pwd
scp -rp static/* root@wolksen.com:/home/dokku/wolksen-static-gambi/static
