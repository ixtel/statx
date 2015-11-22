#!/usr/bin/env python
# coding: utf-8
from unittest import TestCase
import unittest

from statx import Stat


class StatTestCase(TestCase):
    def setUp(self):
        pass

    def test_zero_division_error(self):
        stat = Stat()
        stat.get_speed_line(stat.time)


if __name__ == '__main__':
    unittest.main()
