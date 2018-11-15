#!/usr/bin/env python
# -*- coding: utf-8 -*
# Copyright: [CUP] - See LICENSE for details.
# Authors: Guannan Ma (@mythmgn),
"""
:description:
    unittest for cup.cache
"""

import os
import sys
import time

_NOW_PATH = os.path.dirname(os.path.abspath(__file__)) + '/'
sys.path.insert(0, _NOW_PATH + '../')

import cup
from cup import cache
from cup import unittest


def test_cache():
    kvcache = cache.KvCache()
    kvcache.set(
        {
            'test-0': 'test_value0',
            'test-1': 'test_value1'
        }
    )
    stat_info = kvcache.stat()
    unittest.assert_eq(stat_info[0], 2)
    unittest.assert_eq(stat_info[1], 0)
    unittest.assert_eq(kvcache.get('test-0'), 'test_value0')
    kvcache.set(
        {
            'test-0': 'test_value0',
            'test-1': 'test_value1'
        },
        2
    )
    time.sleep(3)
    stat_info = kvcache.stat()
    unittest.assert_eq(stat_info[0], 2)
    unittest.assert_eq(stat_info[1], 2)
    unittest.assert_eq(kvcache.get('test-0'), None)
    unittest.assert_eq(kvcache.get('test-1'), None)
    kvcache.cleanup_expired()
    stat_info = kvcache.stat()
    unittest.assert_eq(stat_info[0], 0)
    unittest.assert_eq(stat_info[1], 0)
    kvcache.set(
        {
            'test-0': 'test_value0',
            'test-1': 'test_value1'
        },
        2
    )
    kvcache.clear()
    stat_info = kvcache.stat()
    unittest.assert_eq(stat_info[0], 0)
    unittest.assert_eq(stat_info[1], 0)

# vi:set tw=0 ts=4 sw=4 nowrap fdm=indent
