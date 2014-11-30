__author__ = 'hkapadia'
# -*- coding: utf-8 -*-
import os
import codecs
import sys
import datetime
import time

def safe_print(text):
    '''
    This prints text to the terminal, regardless of the OS.

    It uses sys.stdout plus the codecs module to enforce UTF-8.
    '''
    if os.name == 'nt':     # Windows
        codec = codecs.lookup('cp437')
    else:                   # Mac / Linux
        codec = codecs.lookup('utf8')
    wrapped_stdout = codec.streamwriter(sys.stdout, errors='replace')
    wrapped_stdout.write(text)
    wrapped_stdout.write('\n')

def test_safe_print():
    '''
    This has a bunch of possibly scary Unicode test cases to make
    sure that safe_print works on your platform.
    '''
    safe_print(u'☂☀♠')

def twitter_to_datetime(twitter_date_string):
    return datetime.datetime.strptime(twitter_date_string,'%a %b %d %H:%M:%S +0000 %Y')


def YMD_to_datetime(ymd):
    return datetime.datetime.strptime(ymd,'%Y-%m-%d')

def datetime_to_YMD(dtime):
    return time.strftime('%Y-%m-%d', dtime.timetuple())


