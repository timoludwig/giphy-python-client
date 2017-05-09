# coding: utf-8

"""
    giphy-api

    Giphy's public api.

    OpenAPI spec version: 0.9.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class GifImagesDownsizedSmall(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, mp4=None, width=None, height=None, mp4_size=None):
        """
        GifImagesDownsizedSmall - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'mp4': 'str',
            'width': 'str',
            'height': 'str',
            'mp4_size': 'str'
        }

        self.attribute_map = {
            'mp4': 'mp4',
            'width': 'width',
            'height': 'height',
            'mp4_size': 'mp4_size'
        }

        self._mp4 = mp4
        self._width = width
        self._height = height
        self._mp4_size = mp4_size

    @property
    def mp4(self):
        """
        Gets the mp4 of this GifImagesDownsizedSmall.
        The publicly-accessible direct URL for this GIF.

        :return: The mp4 of this GifImagesDownsizedSmall.
        :rtype: str
        """
        return self._mp4

    @mp4.setter
    def mp4(self, mp4):
        """
        Sets the mp4 of this GifImagesDownsizedSmall.
        The publicly-accessible direct URL for this GIF.

        :param mp4: The mp4 of this GifImagesDownsizedSmall.
        :type: str
        """

        self._mp4 = mp4

    @property
    def width(self):
        """
        Gets the width of this GifImagesDownsizedSmall.
        The width of this GIF in pixels.

        :return: The width of this GifImagesDownsizedSmall.
        :rtype: str
        """
        return self._width

    @width.setter
    def width(self, width):
        """
        Sets the width of this GifImagesDownsizedSmall.
        The width of this GIF in pixels.

        :param width: The width of this GifImagesDownsizedSmall.
        :type: str
        """

        self._width = width

    @property
    def height(self):
        """
        Gets the height of this GifImagesDownsizedSmall.
        The height of this GIF in pixels.

        :return: The height of this GifImagesDownsizedSmall.
        :rtype: str
        """
        return self._height

    @height.setter
    def height(self, height):
        """
        Sets the height of this GifImagesDownsizedSmall.
        The height of this GIF in pixels.

        :param height: The height of this GifImagesDownsizedSmall.
        :type: str
        """

        self._height = height

    @property
    def mp4_size(self):
        """
        Gets the mp4_size of this GifImagesDownsizedSmall.
        The size of this GIF in bytes.

        :return: The mp4_size of this GifImagesDownsizedSmall.
        :rtype: str
        """
        return self._mp4_size

    @mp4_size.setter
    def mp4_size(self, mp4_size):
        """
        Sets the mp4_size of this GifImagesDownsizedSmall.
        The size of this GIF in bytes.

        :param mp4_size: The mp4_size of this GifImagesDownsizedSmall.
        :type: str
        """

        self._mp4_size = mp4_size

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, GifImagesDownsizedSmall):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
