#!/usr/bin/env python
# -*- coding: utf-8 -*-
import traceback
import StringIO
import logging
import os, sys

def my_excepthook(excType, excValue, traceback, logger=logger):
    logger.error("Logging an uncaught exception",
                 exc_info=(excType, excValue, traceback))

sys.excepthook = my_excepthook  