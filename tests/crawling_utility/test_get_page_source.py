#!/usr/bin/python
# -*- coding: utf-8 -*-
import subprocess
import time
import uuid

from nose.tools import eq_

from crawling_utility.base import Pipeline
from crawling_utility.pipeline import LoadPage, ChromeDriver, GetPageSource

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


def test_get_page_source():
    global html_file

    se_driver = ChromeDriver()
    with se_driver:
        pipeline = Pipeline()
        pipeline.add_pipe(se_driver)
        pipeline.add_pipe(LoadPage())
        pipeline.add_pipe(GetPageSource())

        data = pipeline.run(url=f'http://localhost:8000/{html_file}.html')
        eq_(data.content, '''<!DOCTYPE html><html xmlns="http://www.w3.org/1999/xhtml"><head></head><body>
        <h1 id="greeting">Hello world</h1>
    
</body></html>''')
