#!/usr/bin/python
# -*- coding: utf-8 -*-
import abc
import logging
from typing import Any, List

from .exception import ResourceNotAvailable


class PipeObject(object):
    def __init__(self, **kwargs: Any) -> None:
        self.__dict__['data'] = dict(kwargs)

    def __setattr__(self, name: str, value: Any) -> None:
        self.data[name] = value

    def __getattr__(self, name: str) -> Any:
        return self.data[name]

    def __contains__(self, name: str) -> bool:
        return name in self.data


class Pipe(object):

    @abc.abstractmethod
    def run(self, event: PipeObject) -> PipeObject:
        pass


class Pipeline(object):
    def __init__(self):
        self.pipes: List[Pipe] = []

    def add_pipe(self, pipe: Pipe) -> None:
        self.pipes.append(pipe)

    def run(self, **kwargs: Any):
        data = PipeObject(**kwargs)

        for pipe in self.pipes:
            data = pipe.run(data)

        return data
