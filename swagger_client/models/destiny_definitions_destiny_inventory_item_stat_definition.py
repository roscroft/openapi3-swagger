# coding: utf-8

"""
    Bungie.Net API

    These endpoints constitute the functionality exposed by Bungie.net, both for more traditional website functionality and for connectivity to Bungie video games and their related functionality.

    OpenAPI spec version: 2.0.0
    Contact: support@bungie.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class DestinyDefinitionsDestinyInventoryItemStatDefinition(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'stat_hash': 'int',
        'value': 'int',
        'minimum': 'int',
        'maximum': 'int'
    }

    attribute_map = {
        'stat_hash': 'statHash',
        'value': 'value',
        'minimum': 'minimum',
        'maximum': 'maximum'
    }

    def __init__(self, stat_hash=None, value=None, minimum=None, maximum=None):
        """
        DestinyDefinitionsDestinyInventoryItemStatDefinition - a model defined in Swagger
        """

        self._stat_hash = None
        self._value = None
        self._minimum = None
        self._maximum = None
        self.discriminator = None

        if stat_hash is not None:
          self.stat_hash = stat_hash
        if value is not None:
          self.value = value
        if minimum is not None:
          self.minimum = minimum
        if maximum is not None:
          self.maximum = maximum

    @property
    def stat_hash(self):
        """
        Gets the stat_hash of this DestinyDefinitionsDestinyInventoryItemStatDefinition.
        The hash for the DestinyStatDefinition representing this stat.

        :return: The stat_hash of this DestinyDefinitionsDestinyInventoryItemStatDefinition.
        :rtype: int
        """
        return self._stat_hash

    @stat_hash.setter
    def stat_hash(self, stat_hash):
        """
        Sets the stat_hash of this DestinyDefinitionsDestinyInventoryItemStatDefinition.
        The hash for the DestinyStatDefinition representing this stat.

        :param stat_hash: The stat_hash of this DestinyDefinitionsDestinyInventoryItemStatDefinition.
        :type: int
        """

        self._stat_hash = stat_hash

    @property
    def value(self):
        """
        Gets the value of this DestinyDefinitionsDestinyInventoryItemStatDefinition.
        This value represents the stat value assuming the minimum possible rollbut accounting for any mandatory bonuses that should be applied to the stat on item creation.  In Destiny 1, this was different from the \"minimum\" value because there were certain conditionswhere an item could be theoretically lower level/value than the initial roll.    In Destiny 2, this is not possible unless Talent Grids begin to be used again for these purposes or some othersystem change occurs... thus in practice, value and minimum should be the same in Destiny 2.  Good riddance.

        :return: The value of this DestinyDefinitionsDestinyInventoryItemStatDefinition.
        :rtype: int
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this DestinyDefinitionsDestinyInventoryItemStatDefinition.
        This value represents the stat value assuming the minimum possible rollbut accounting for any mandatory bonuses that should be applied to the stat on item creation.  In Destiny 1, this was different from the \"minimum\" value because there were certain conditionswhere an item could be theoretically lower level/value than the initial roll.    In Destiny 2, this is not possible unless Talent Grids begin to be used again for these purposes or some othersystem change occurs... thus in practice, value and minimum should be the same in Destiny 2.  Good riddance.

        :param value: The value of this DestinyDefinitionsDestinyInventoryItemStatDefinition.
        :type: int
        """

        self._value = value

    @property
    def minimum(self):
        """
        Gets the minimum of this DestinyDefinitionsDestinyInventoryItemStatDefinition.
        The minimum possible value for this stat that we think the item can roll.

        :return: The minimum of this DestinyDefinitionsDestinyInventoryItemStatDefinition.
        :rtype: int
        """
        return self._minimum

    @minimum.setter
    def minimum(self, minimum):
        """
        Sets the minimum of this DestinyDefinitionsDestinyInventoryItemStatDefinition.
        The minimum possible value for this stat that we think the item can roll.

        :param minimum: The minimum of this DestinyDefinitionsDestinyInventoryItemStatDefinition.
        :type: int
        """

        self._minimum = minimum

    @property
    def maximum(self):
        """
        Gets the maximum of this DestinyDefinitionsDestinyInventoryItemStatDefinition.
        The maximum possible value for this stat that we think the item can roll.

        :return: The maximum of this DestinyDefinitionsDestinyInventoryItemStatDefinition.
        :rtype: int
        """
        return self._maximum

    @maximum.setter
    def maximum(self, maximum):
        """
        Sets the maximum of this DestinyDefinitionsDestinyInventoryItemStatDefinition.
        The maximum possible value for this stat that we think the item can roll.

        :param maximum: The maximum of this DestinyDefinitionsDestinyInventoryItemStatDefinition.
        :type: int
        """

        self._maximum = maximum

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
        if not isinstance(other, DestinyDefinitionsDestinyInventoryItemStatDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other