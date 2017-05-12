#!/usr/bin/python
# -*- coding: utf-8 -*-

import subprocess
import uuid

import time
from nose.tools import eq_
from selenium.webdriver.remote.webdriver import WebDriver

from crawling_utility.base.base import Pipeline
from crawling_utility.pipeline import LoadPage, ChromeDriver

http_server = None
html_file = None


def setup():
    """Start the testing environment, including: a local python webserver and selenium hub in docker"""
    global http_server, html_file
    http_server = subprocess.Popen(['python', '-m', 'http.server'], cwd='/tmp')
    time.sleep(1)  # waiting for server to start

    html_file = str(uuid.uuid4())
    with open(f'/tmp/{html_file}.html', 'w') as f:
        f.write('''<!DOCTYPE html>
<html>
    <body>
        <h1 id='greeting'>Hello world</h1>
    </body>
</html>''')


def teardown():
    """stop python webserver"""
    global http_server, html_file

    if http_server is not None:
        http_server.kill()
        http_server = None
        html_file = None


def test_load_server():
    global html_file

    se_driver = ChromeDriver()
    with se_driver:
        pipeline = Pipeline()
        pipeline.add_pipe(se_driver)
        pipeline.add_pipe(LoadPage())

        data = pipeline.run(url=f'http://localhost:8000/{html_file}.html')
        driver: WebDriver = data.driver
        eq_(driver.find_element_by_id('greeting').text, 'Hello world')
