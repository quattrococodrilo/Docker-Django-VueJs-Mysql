#!/usr/bin/env bash

/wait-for-it.sh -t 0 backend:8000 --strict -- npm run dev
