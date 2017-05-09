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


class Gif(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, type='gif', id=None, slug=None, url=None, bitly_gif_url=None, bitly_url=None, embed_url=None, username=None, source=None, rating=None, content_url=None, tags=None, featured_tags=None, user=None, source_tld=None, source_post_url=None, is_hidden=None, is_removed=None, is_community=None, is_anonymous=None, is_featured=None, is_realtime=None, is_indexable=None, is_sticker=None, update_datetime=None, create_datetime=None, import_datetime=None, trending_datetime=None, images=None):
        """
        Gif - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'type': 'str',
            'id': 'str',
            'slug': 'str',
            'url': 'str',
            'bitly_gif_url': 'str',
            'bitly_url': 'str',
            'embed_url': 'str',
            'username': 'str',
            'source': 'str',
            'rating': 'str',
            'content_url': 'str',
            'tags': 'list[str]',
            'featured_tags': 'list[str]',
            'user': 'User',
            'source_tld': 'str',
            'source_post_url': 'str',
            'is_hidden': 'bool',
            'is_removed': 'bool',
            'is_community': 'bool',
            'is_anonymous': 'bool',
            'is_featured': 'bool',
            'is_realtime': 'bool',
            'is_indexable': 'bool',
            'is_sticker': 'bool',
            'update_datetime': 'str',
            'create_datetime': 'str',
            'import_datetime': 'str',
            'trending_datetime': 'str',
            'images': 'GifImages'
        }

        self.attribute_map = {
            'type': 'type',
            'id': 'id',
            'slug': 'slug',
            'url': 'url',
            'bitly_gif_url': 'bitly_gif_url',
            'bitly_url': 'bitly_url',
            'embed_url': 'embed_url',
            'username': 'username',
            'source': 'source',
            'rating': 'rating',
            'content_url': 'content_url',
            'tags': 'tags',
            'featured_tags': 'featured_tags',
            'user': 'user',
            'source_tld': 'source_tld',
            'source_post_url': 'source_post_url',
            'is_hidden': 'is_hidden',
            'is_removed': 'is_removed',
            'is_community': 'is_community',
            'is_anonymous': 'is_anonymous',
            'is_featured': 'is_featured',
            'is_realtime': 'is_realtime',
            'is_indexable': 'is_indexable',
            'is_sticker': 'is_sticker',
            'update_datetime': 'update_datetime',
            'create_datetime': 'create_datetime',
            'import_datetime': 'import_datetime',
            'trending_datetime': 'trending_datetime',
            'images': 'images'
        }

        self._type = type
        self._id = id
        self._slug = slug
        self._url = url
        self._bitly_gif_url = bitly_gif_url
        self._bitly_url = bitly_url
        self._embed_url = embed_url
        self._username = username
        self._source = source
        self._rating = rating
        self._content_url = content_url
        self._tags = tags
        self._featured_tags = featured_tags
        self._user = user
        self._source_tld = source_tld
        self._source_post_url = source_post_url
        self._is_hidden = is_hidden
        self._is_removed = is_removed
        self._is_community = is_community
        self._is_anonymous = is_anonymous
        self._is_featured = is_featured
        self._is_realtime = is_realtime
        self._is_indexable = is_indexable
        self._is_sticker = is_sticker
        self._update_datetime = update_datetime
        self._create_datetime = create_datetime
        self._import_datetime = import_datetime
        self._trending_datetime = trending_datetime
        self._images = images

    @property
    def type(self):
        """
        Gets the type of this Gif.
        By default, this is almost always gif

        :return: The type of this Gif.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Gif.
        By default, this is almost always gif

        :param type: The type of this Gif.
        :type: str
        """

        self._type = type

    @property
    def id(self):
        """
        Gets the id of this Gif.
        This GIF's unique ID

        :return: The id of this Gif.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Gif.
        This GIF's unique ID

        :param id: The id of this Gif.
        :type: str
        """

        self._id = id

    @property
    def slug(self):
        """
        Gets the slug of this Gif.
        The unique slug used in this GIF's URL

        :return: The slug of this Gif.
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """
        Sets the slug of this Gif.
        The unique slug used in this GIF's URL

        :param slug: The slug of this Gif.
        :type: str
        """

        self._slug = slug

    @property
    def url(self):
        """
        Gets the url of this Gif.
        The unique URL for this GIF

        :return: The url of this Gif.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this Gif.
        The unique URL for this GIF

        :param url: The url of this Gif.
        :type: str
        """

        self._url = url

    @property
    def bitly_gif_url(self):
        """
        Gets the bitly_gif_url of this Gif.
        The unique bit.ly URL for this GIF

        :return: The bitly_gif_url of this Gif.
        :rtype: str
        """
        return self._bitly_gif_url

    @bitly_gif_url.setter
    def bitly_gif_url(self, bitly_gif_url):
        """
        Sets the bitly_gif_url of this Gif.
        The unique bit.ly URL for this GIF

        :param bitly_gif_url: The bitly_gif_url of this Gif.
        :type: str
        """

        self._bitly_gif_url = bitly_gif_url

    @property
    def bitly_url(self):
        """
        Gets the bitly_url of this Gif.
        The unique bit.ly URL for this GIF

        :return: The bitly_url of this Gif.
        :rtype: str
        """
        return self._bitly_url

    @bitly_url.setter
    def bitly_url(self, bitly_url):
        """
        Sets the bitly_url of this Gif.
        The unique bit.ly URL for this GIF

        :param bitly_url: The bitly_url of this Gif.
        :type: str
        """

        self._bitly_url = bitly_url

    @property
    def embed_url(self):
        """
        Gets the embed_url of this Gif.
        A URL used for embedding this GIF

        :return: The embed_url of this Gif.
        :rtype: str
        """
        return self._embed_url

    @embed_url.setter
    def embed_url(self, embed_url):
        """
        Sets the embed_url of this Gif.
        A URL used for embedding this GIF

        :param embed_url: The embed_url of this Gif.
        :type: str
        """

        self._embed_url = embed_url

    @property
    def username(self):
        """
        Gets the username of this Gif.
        The username this GIF is attached to, if applicable

        :return: The username of this Gif.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this Gif.
        The username this GIF is attached to, if applicable

        :param username: The username of this Gif.
        :type: str
        """

        self._username = username

    @property
    def source(self):
        """
        Gets the source of this Gif.
        The page on which this GIF was found

        :return: The source of this Gif.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """
        Sets the source of this Gif.
        The page on which this GIF was found

        :param source: The source of this Gif.
        :type: str
        """

        self._source = source

    @property
    def rating(self):
        """
        Gets the rating of this Gif.
        The MPAA-style rating for this content. Examples include Y, G, PG, PG-13 and R

        :return: The rating of this Gif.
        :rtype: str
        """
        return self._rating

    @rating.setter
    def rating(self, rating):
        """
        Sets the rating of this Gif.
        The MPAA-style rating for this content. Examples include Y, G, PG, PG-13 and R

        :param rating: The rating of this Gif.
        :type: str
        """

        self._rating = rating

    @property
    def content_url(self):
        """
        Gets the content_url of this Gif.
        Currently unused

        :return: The content_url of this Gif.
        :rtype: str
        """
        return self._content_url

    @content_url.setter
    def content_url(self, content_url):
        """
        Sets the content_url of this Gif.
        Currently unused

        :param content_url: The content_url of this Gif.
        :type: str
        """

        self._content_url = content_url

    @property
    def tags(self):
        """
        Gets the tags of this Gif.
        An array of tags for this GIF (Note\\: Not available when using the Public Beta Key)

        :return: The tags of this Gif.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this Gif.
        An array of tags for this GIF (Note\\: Not available when using the Public Beta Key)

        :param tags: The tags of this Gif.
        :type: list[str]
        """

        self._tags = tags

    @property
    def featured_tags(self):
        """
        Gets the featured_tags of this Gif.
        An array of featured tags for this GIF (Note\\: Not available when using the Public Beta Key)

        :return: The featured_tags of this Gif.
        :rtype: list[str]
        """
        return self._featured_tags

    @featured_tags.setter
    def featured_tags(self, featured_tags):
        """
        Sets the featured_tags of this Gif.
        An array of featured tags for this GIF (Note\\: Not available when using the Public Beta Key)

        :param featured_tags: The featured_tags of this Gif.
        :type: list[str]
        """

        self._featured_tags = featured_tags

    @property
    def user(self):
        """
        Gets the user of this Gif.
        An object containing data about the user associated with this GIF, if applicable.

        :return: The user of this Gif.
        :rtype: User
        """
        return self._user

    @user.setter
    def user(self, user):
        """
        Sets the user of this Gif.
        An object containing data about the user associated with this GIF, if applicable.

        :param user: The user of this Gif.
        :type: User
        """

        self._user = user

    @property
    def source_tld(self):
        """
        Gets the source_tld of this Gif.
        The top level domain of the source URL.

        :return: The source_tld of this Gif.
        :rtype: str
        """
        return self._source_tld

    @source_tld.setter
    def source_tld(self, source_tld):
        """
        Sets the source_tld of this Gif.
        The top level domain of the source URL.

        :param source_tld: The source_tld of this Gif.
        :type: str
        """

        self._source_tld = source_tld

    @property
    def source_post_url(self):
        """
        Gets the source_post_url of this Gif.
        The URL of the webpage on which this GIF was found.

        :return: The source_post_url of this Gif.
        :rtype: str
        """
        return self._source_post_url

    @source_post_url.setter
    def source_post_url(self, source_post_url):
        """
        Sets the source_post_url of this Gif.
        The URL of the webpage on which this GIF was found.

        :param source_post_url: The source_post_url of this Gif.
        :type: str
        """

        self._source_post_url = source_post_url

    @property
    def is_hidden(self):
        """
        Gets the is_hidden of this Gif.
        Denotes whether or not this GIF is private.

        :return: The is_hidden of this Gif.
        :rtype: bool
        """
        return self._is_hidden

    @is_hidden.setter
    def is_hidden(self, is_hidden):
        """
        Sets the is_hidden of this Gif.
        Denotes whether or not this GIF is private.

        :param is_hidden: The is_hidden of this Gif.
        :type: bool
        """

        self._is_hidden = is_hidden

    @property
    def is_removed(self):
        """
        Gets the is_removed of this Gif.
        Denotes whether or not this GIF has been deleted.

        :return: The is_removed of this Gif.
        :rtype: bool
        """
        return self._is_removed

    @is_removed.setter
    def is_removed(self, is_removed):
        """
        Sets the is_removed of this Gif.
        Denotes whether or not this GIF has been deleted.

        :param is_removed: The is_removed of this Gif.
        :type: bool
        """

        self._is_removed = is_removed

    @property
    def is_community(self):
        """
        Gets the is_community of this Gif.
        Denotes whether or not this GIF has been uploaded by a GIPHY user.

        :return: The is_community of this Gif.
        :rtype: bool
        """
        return self._is_community

    @is_community.setter
    def is_community(self, is_community):
        """
        Sets the is_community of this Gif.
        Denotes whether or not this GIF has been uploaded by a GIPHY user.

        :param is_community: The is_community of this Gif.
        :type: bool
        """

        self._is_community = is_community

    @property
    def is_anonymous(self):
        """
        Gets the is_anonymous of this Gif.
        Denotes whether or not this GIF has been uploaded to GIPHY by an anonymous user.

        :return: The is_anonymous of this Gif.
        :rtype: bool
        """
        return self._is_anonymous

    @is_anonymous.setter
    def is_anonymous(self, is_anonymous):
        """
        Sets the is_anonymous of this Gif.
        Denotes whether or not this GIF has been uploaded to GIPHY by an anonymous user.

        :param is_anonymous: The is_anonymous of this Gif.
        :type: bool
        """

        self._is_anonymous = is_anonymous

    @property
    def is_featured(self):
        """
        Gets the is_featured of this Gif.
        Denotes whether or not this GIF is featured on giphy.com (deprecated).

        :return: The is_featured of this Gif.
        :rtype: bool
        """
        return self._is_featured

    @is_featured.setter
    def is_featured(self, is_featured):
        """
        Sets the is_featured of this Gif.
        Denotes whether or not this GIF is featured on giphy.com (deprecated).

        :param is_featured: The is_featured of this Gif.
        :type: bool
        """

        self._is_featured = is_featured

    @property
    def is_realtime(self):
        """
        Gets the is_realtime of this Gif.
        Denotes whether or not this GIF has been sourced from a realtime crawl.

        :return: The is_realtime of this Gif.
        :rtype: bool
        """
        return self._is_realtime

    @is_realtime.setter
    def is_realtime(self, is_realtime):
        """
        Sets the is_realtime of this Gif.
        Denotes whether or not this GIF has been sourced from a realtime crawl.

        :param is_realtime: The is_realtime of this Gif.
        :type: bool
        """

        self._is_realtime = is_realtime

    @property
    def is_indexable(self):
        """
        Gets the is_indexable of this Gif.
        Denotes whether or not this GIF is indexable.

        :return: The is_indexable of this Gif.
        :rtype: bool
        """
        return self._is_indexable

    @is_indexable.setter
    def is_indexable(self, is_indexable):
        """
        Sets the is_indexable of this Gif.
        Denotes whether or not this GIF is indexable.

        :param is_indexable: The is_indexable of this Gif.
        :type: bool
        """

        self._is_indexable = is_indexable

    @property
    def is_sticker(self):
        """
        Gets the is_sticker of this Gif.
        Denotes whether this GIF is a sticker (has a transparent background).

        :return: The is_sticker of this Gif.
        :rtype: bool
        """
        return self._is_sticker

    @is_sticker.setter
    def is_sticker(self, is_sticker):
        """
        Sets the is_sticker of this Gif.
        Denotes whether this GIF is a sticker (has a transparent background).

        :param is_sticker: The is_sticker of this Gif.
        :type: bool
        """

        self._is_sticker = is_sticker

    @property
    def update_datetime(self):
        """
        Gets the update_datetime of this Gif.
        The date on which this GIF was last updated.

        :return: The update_datetime of this Gif.
        :rtype: str
        """
        return self._update_datetime

    @update_datetime.setter
    def update_datetime(self, update_datetime):
        """
        Sets the update_datetime of this Gif.
        The date on which this GIF was last updated.

        :param update_datetime: The update_datetime of this Gif.
        :type: str
        """

        self._update_datetime = update_datetime

    @property
    def create_datetime(self):
        """
        Gets the create_datetime of this Gif.
        The date this GIF was added to the GIPHY database.

        :return: The create_datetime of this Gif.
        :rtype: str
        """
        return self._create_datetime

    @create_datetime.setter
    def create_datetime(self, create_datetime):
        """
        Sets the create_datetime of this Gif.
        The date this GIF was added to the GIPHY database.

        :param create_datetime: The create_datetime of this Gif.
        :type: str
        """

        self._create_datetime = create_datetime

    @property
    def import_datetime(self):
        """
        Gets the import_datetime of this Gif.
        The creation or upload date from this GIF's source.

        :return: The import_datetime of this Gif.
        :rtype: str
        """
        return self._import_datetime

    @import_datetime.setter
    def import_datetime(self, import_datetime):
        """
        Sets the import_datetime of this Gif.
        The creation or upload date from this GIF's source.

        :param import_datetime: The import_datetime of this Gif.
        :type: str
        """

        self._import_datetime = import_datetime

    @property
    def trending_datetime(self):
        """
        Gets the trending_datetime of this Gif.
        The date on which this gif was marked trending, if applicable.

        :return: The trending_datetime of this Gif.
        :rtype: str
        """
        return self._trending_datetime

    @trending_datetime.setter
    def trending_datetime(self, trending_datetime):
        """
        Sets the trending_datetime of this Gif.
        The date on which this gif was marked trending, if applicable.

        :param trending_datetime: The trending_datetime of this Gif.
        :type: str
        """

        self._trending_datetime = trending_datetime

    @property
    def images(self):
        """
        Gets the images of this Gif.

        :return: The images of this Gif.
        :rtype: GifImages
        """
        return self._images

    @images.setter
    def images(self, images):
        """
        Sets the images of this Gif.

        :param images: The images of this Gif.
        :type: GifImages
        """

        self._images = images

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
        if not isinstance(other, Gif):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
