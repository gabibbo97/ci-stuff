#!/usr/bin/env python3
#
# Retries the provided script
#
import os
import random
import subprocess
import sys
import time

MAX_RETRIES = os.environ.get('BACKOFF_MAX_RETRIES', 3)
MAX_DELAY_SECONDS = os.environ.get('BACKOFF_MAX_DELAY', 10)

def try_launching():
  CURRENT_DELAY = 0
  CURRENT_RETRIES = 0
  MAX_DELAY = MAX_DELAY_SECONDS * 1000

  while True:
    program = subprocess.run(sys.argv[1:])
    if program.returncode != 0:
      CURRENT_DELAY += CURRENT_DELAY + random.randint(0, 1000)

      if CURRENT_DELAY > MAX_DELAY:
        CURRENT_DELAY = MAX_DELAY
        CURRENT_RETRIES += 1
        if CURRENT_RETRIES > MAX_RETRIES:
          print(f"FAILED after {MAX_RETRIES} retries at maximum backoff time", file=sys.stderr)
          sys.exit(program.returncode)
        print(f"Failed, waiting for {CURRENT_DELAY} ms ({CURRENT_RETRIES}/{MAX_RETRIES})")
      else:
        print(f"Failed, waiting for {CURRENT_DELAY} ms")

      time.sleep(CURRENT_DELAY / 1000)
    else:
      break

try_launching()
