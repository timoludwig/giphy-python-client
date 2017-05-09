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


class GifImagesDownsizedMedium(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, url=None, width=None, height=None, size=None):
        """
        GifImagesDownsizedMedium - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'url': 'str',
            'width': 'str',
            'height': 'str',
            'size': 'str'
        }

        self.attribute_map = {
            'url': 'url',
            'width': 'width',
            'height': 'height',
            'size': 'size'
        }

        self._url = url
        self._width = width
        self._height = height
        self._size = size

    @property
    def url(self):
        """
        Gets the url of this GifImagesDownsizedMedium.
        The publicly-accessible direct URL for this GIF.

        :return: The url of this GifImagesDownsizedMedium.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this GifImagesDownsizedMedium.
        The publicly-accessible direct URL for this GIF.

        :param url: The url of this GifImagesDownsizedMedium.
        :type: str
        """

        self._url = url

    @property
    def width(self):
        """
        Gets the width of this GifImagesDownsizedMedium.
        The width of this GIF in pixels.

        :return: The width of this GifImagesDownsizedMedium.
        :rtype: str
        """
        return self._width

    @width.setter
    def width(self, width):
        """
        Sets the width of this GifImagesDownsizedMedium.
        The width of this GIF in pixels.

        :param width: The width of this GifImagesDownsizedMedium.
        :type: str
        """

        self._width = width

    @property
    def height(self):
        """
        Gets the height of this GifImagesDownsizedMedium.
        The height of this GIF in pixels.

        :return: The height of this GifImagesDownsizedMedium.
        :rtype: str
        """
        return self._height

    @height.setter
    def height(self, height):
        """
        Sets the height of this GifImagesDownsizedMedium.
        The height of this GIF in pixels.

        :param height: The height of this GifImagesDownsizedMedium.
        :type: str
        """

        self._height = height

    @property
    def size(self):
        """
        Gets the size of this GifImagesDownsizedMedium.
        The size of this GIF in bytes.

        :return: The size of this GifImagesDownsizedMedium.
        :rtype: str
        """
        return self._size

    @size.setter
    def size(self, size):
        """
        Sets the size of this GifImagesDownsizedMedium.
        The size of this GIF in bytes.

        :param size: The size of this GifImagesDownsizedMedium.
        :type: str
        """

        self._size = size

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
        if not isinstance(other, GifImagesDownsizedMedium):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
