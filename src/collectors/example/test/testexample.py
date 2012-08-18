#!/usr/bin/python
# coding=utf-8
################################################################################

from test import CollectorTestCase
from test import get_collector_config
from test import unittest
from mock import patch

from diamond.collector import Collector
from example import ExampleCollector

################################################################################


class TestExampleCollector(CollectorTestCase):
    def setUp(self):
        config = get_collector_config('ExampleCollector', {
            'interval': 10
        })

        self.collector = ExampleCollector(config, None)

    @patch.object(Collector, 'publish')
    def test(self, publish_mock):
        self.collector.collect()

        metrics = {
            'my.example.metric':  42
        }

        self.setDocExample(self.collector.__class__.__name__, metrics)
        self.assertPublishedMany(publish_mock, metrics)

################################################################################
if __name__ == "__main__":
    unittest.main()
