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

from flyteadmin.models.admin_task_closure import AdminTaskClosure  # noqa: F401,E501
from flyteadmin.models.core_identifier import CoreIdentifier  # noqa: F401,E501


class AdminTask(object):
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
        'id': 'CoreIdentifier',
        'closure': 'AdminTaskClosure',
        'short_description': 'str'
    }

    attribute_map = {
        'id': 'id',
        'closure': 'closure',
        'short_description': 'short_description'
    }

    def __init__(self, id=None, closure=None, short_description=None):  # noqa: E501
        """AdminTask - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._closure = None
        self._short_description = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if closure is not None:
            self.closure = closure
        if short_description is not None:
            self.short_description = short_description

    @property
    def id(self):
        """Gets the id of this AdminTask.  # noqa: E501

        id represents the unique identifier of the task.  # noqa: E501

        :return: The id of this AdminTask.  # noqa: E501
        :rtype: CoreIdentifier
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AdminTask.

        id represents the unique identifier of the task.  # noqa: E501

        :param id: The id of this AdminTask.  # noqa: E501
        :type: CoreIdentifier
        """

        self._id = id

    @property
    def closure(self):
        """Gets the closure of this AdminTask.  # noqa: E501

        closure encapsulates all the fields that maps to a compiled version of the task.  # noqa: E501

        :return: The closure of this AdminTask.  # noqa: E501
        :rtype: AdminTaskClosure
        """
        return self._closure

    @closure.setter
    def closure(self, closure):
        """Sets the closure of this AdminTask.

        closure encapsulates all the fields that maps to a compiled version of the task.  # noqa: E501

        :param closure: The closure of this AdminTask.  # noqa: E501
        :type: AdminTaskClosure
        """

        self._closure = closure

    @property
    def short_description(self):
        """Gets the short_description of this AdminTask.  # noqa: E501

        One-liner overview of the entity.  # noqa: E501

        :return: The short_description of this AdminTask.  # noqa: E501
        :rtype: str
        """
        return self._short_description

    @short_description.setter
    def short_description(self, short_description):
        """Sets the short_description of this AdminTask.

        One-liner overview of the entity.  # noqa: E501

        :param short_description: The short_description of this AdminTask.  # noqa: E501
        :type: str
        """

        self._short_description = short_description

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
        if issubclass(AdminTask, dict):
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
        if not isinstance(other, AdminTask):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
