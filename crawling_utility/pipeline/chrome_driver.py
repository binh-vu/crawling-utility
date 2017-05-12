#!/usr/bin/python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

from crawling_utility.base import Pipe, PipeObject


class ChromeDriver(Pipe):
    def __init__(self, proxy: str = None):
        """
        :param proxy: "protocol://host:port" e.g: socks5://localhost:8080 
        """
        self.chrome_options = webdriver.ChromeOptions()
        if proxy is not None:
            self.chrome_options.add_argument('--proxy-server=%s' % proxy)
        self.driver: WebDriver = None

    def run(self, data: PipeObject) -> PipeObject:
        assert self.driver is not None
        data.driver = self.driver
        return data

    def __enter__(self):
        assert self.driver is None
        self.driver = webdriver.Chrome(chrome_options=self.chrome_options)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.driver.close()
        self.driver = None
