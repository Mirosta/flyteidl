# coding: utf-8

"""
    flyteidl/service/admin.proto

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: version not set
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from flyteadmin.models.artifact_artifact_key import ArtifactArtifactKey  # noqa: F401,E501
from flyteadmin.models.artifact_tag import ArtifactTag  # noqa: F401,E501
from flyteadmin.models.flyteidlartifact_alias import FlyteidlartifactAlias  # noqa: F401,E501


class ArtifactArtifactQuery(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'artifact_key': 'ArtifactArtifactKey',
        'version': 'str',
        'alias': 'FlyteidlartifactAlias',
        'tags': 'list[ArtifactTag]'
    }

    attribute_map = {
        'artifact_key': 'artifact_key',
        'version': 'version',
        'alias': 'alias',
        'tags': 'tags'
    }

    def __init__(self, artifact_key=None, version=None, alias=None, tags=None):  # noqa: E501
        """ArtifactArtifactQuery - a model defined in Swagger"""  # noqa: E501

        self._artifact_key = None
        self._version = None
        self._alias = None
        self._tags = None
        self.discriminator = None

        if artifact_key is not None:
            self.artifact_key = artifact_key
        if version is not None:
            self.version = version
        if alias is not None:
            self.alias = alias
        if tags is not None:
            self.tags = tags

    @property
    def artifact_key(self):
        """Gets the artifact_key of this ArtifactArtifactQuery.  # noqa: E501


        :return: The artifact_key of this ArtifactArtifactQuery.  # noqa: E501
        :rtype: ArtifactArtifactKey
        """
        return self._artifact_key

    @artifact_key.setter
    def artifact_key(self, artifact_key):
        """Sets the artifact_key of this ArtifactArtifactQuery.


        :param artifact_key: The artifact_key of this ArtifactArtifactQuery.  # noqa: E501
        :type: ArtifactArtifactKey
        """

        self._artifact_key = artifact_key

    @property
    def version(self):
        """Gets the version of this ArtifactArtifactQuery.  # noqa: E501


        :return: The version of this ArtifactArtifactQuery.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ArtifactArtifactQuery.


        :param version: The version of this ArtifactArtifactQuery.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def alias(self):
        """Gets the alias of this ArtifactArtifactQuery.  # noqa: E501


        :return: The alias of this ArtifactArtifactQuery.  # noqa: E501
        :rtype: FlyteidlartifactAlias
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this ArtifactArtifactQuery.


        :param alias: The alias of this ArtifactArtifactQuery.  # noqa: E501
        :type: FlyteidlartifactAlias
        """

        self._alias = alias

    @property
    def tags(self):
        """Gets the tags of this ArtifactArtifactQuery.  # noqa: E501


        :return: The tags of this ArtifactArtifactQuery.  # noqa: E501
        :rtype: list[ArtifactTag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ArtifactArtifactQuery.


        :param tags: The tags of this ArtifactArtifactQuery.  # noqa: E501
        :type: list[ArtifactTag]
        """

        self._tags = tags

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(ArtifactArtifactQuery, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ArtifactArtifactQuery):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
