#!/bin/bash

# This logs the screentime of the user
./time-logger.sh | tee -a test.txt | ./archiver.sh
