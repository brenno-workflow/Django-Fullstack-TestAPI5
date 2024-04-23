#!/usr/bin/env bash

cd mysite
gunicorn mysite.wsgi:application