# coding: utf-8

"""
    giphy-api

    Giphy's public api.

    OpenAPI spec version: 0.9.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import giphy_client
from giphy_client.rest import ApiException
from giphy_client.models.gif_images_fixed_height_downsampled import GifImagesFixedHeightDownsampled


class TestGifImagesFixedHeightDownsampled(unittest.TestCase):
    """ GifImagesFixedHeightDownsampled unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testGifImagesFixedHeightDownsampled(self):
        """
        Test GifImagesFixedHeightDownsampled
        """
        model = giphy_client.models.gif_images_fixed_height_downsampled.GifImagesFixedHeightDownsampled()


if __name__ == '__main__':
    unittest.main()
