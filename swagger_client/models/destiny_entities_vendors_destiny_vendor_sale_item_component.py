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


class DestinyEntitiesVendorsDestinyVendorSaleItemComponent(object):
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
        'vendor_item_index': 'int',
        'item_hash': 'int',
        'costs': 'list[ComponentsschemasDestinyDestinyItemQuantity]',
        'required_unlocks': 'list[int]',
        'unlock_statuses': 'list[ComponentsschemasDestinyDestinyUnlockStatus]',
        'failure_indexes': 'list[int]'
    }

    attribute_map = {
        'vendor_item_index': 'vendorItemIndex',
        'item_hash': 'itemHash',
        'costs': 'costs',
        'required_unlocks': 'requiredUnlocks',
        'unlock_statuses': 'unlockStatuses',
        'failure_indexes': 'failureIndexes'
    }

    def __init__(self, vendor_item_index=None, item_hash=None, costs=None, required_unlocks=None, unlock_statuses=None, failure_indexes=None):
        """
        DestinyEntitiesVendorsDestinyVendorSaleItemComponent - a model defined in Swagger
        """

        self._vendor_item_index = None
        self._item_hash = None
        self._costs = None
        self._required_unlocks = None
        self._unlock_statuses = None
        self._failure_indexes = None
        self.discriminator = None

        if vendor_item_index is not None:
          self.vendor_item_index = vendor_item_index
        if item_hash is not None:
          self.item_hash = item_hash
        if costs is not None:
          self.costs = costs
        if required_unlocks is not None:
          self.required_unlocks = required_unlocks
        if unlock_statuses is not None:
          self.unlock_statuses = unlock_statuses
        if failure_indexes is not None:
          self.failure_indexes = failure_indexes

    @property
    def vendor_item_index(self):
        """
        Gets the vendor_item_index of this DestinyEntitiesVendorsDestinyVendorSaleItemComponent.
        The index into the DestinyVendorDefinition.itemList property.  Note that this means Vendor data*is* Content Version dependent: make sure you have the latest content before you use Vendor data,or these indexes may mismatch.    Most systems avoid this problem, but Vendors is one area where weare unable to reasonably avoid content dependency at the moment.

        :return: The vendor_item_index of this DestinyEntitiesVendorsDestinyVendorSaleItemComponent.
        :rtype: int
        """
        return self._vendor_item_index

    @vendor_item_index.setter
    def vendor_item_index(self, vendor_item_index):
        """
        Sets the vendor_item_index of this DestinyEntitiesVendorsDestinyVendorSaleItemComponent.
        The index into the DestinyVendorDefinition.itemList property.  Note that this means Vendor data*is* Content Version dependent: make sure you have the latest content before you use Vendor data,or these indexes may mismatch.    Most systems avoid this problem, but Vendors is one area where weare unable to reasonably avoid content dependency at the moment.

        :param vendor_item_index: The vendor_item_index of this DestinyEntitiesVendorsDestinyVendorSaleItemComponent.
        :type: int
        """

        self._vendor_item_index = vendor_item_index

    @property
    def item_hash(self):
        """
        Gets the item_hash of this DestinyEntitiesVendorsDestinyVendorSaleItemComponent.
        The hash of the item being sold, as a quick shortcut for looking up the DestinyInventoryItemDefinitionof the sale item.

        :return: The item_hash of this DestinyEntitiesVendorsDestinyVendorSaleItemComponent.
        :rtype: int
        """
        return self._item_hash

    @item_hash.setter
    def item_hash(self, item_hash):
        """
        Sets the item_hash of this DestinyEntitiesVendorsDestinyVendorSaleItemComponent.
        The hash of the item being sold, as a quick shortcut for looking up the DestinyInventoryItemDefinitionof the sale item.

        :param item_hash: The item_hash of this DestinyEntitiesVendorsDestinyVendorSaleItemComponent.
        :type: int
        """

        self._item_hash = item_hash

    @property
    def costs(self):
        """
        Gets the costs of this DestinyEntitiesVendorsDestinyVendorSaleItemComponent.
        A summary of the current costs of the item.

        :return: The costs of this DestinyEntitiesVendorsDestinyVendorSaleItemComponent.
        :rtype: list[ComponentsschemasDestinyDestinyItemQuantity]
        """
        return self._costs

    @costs.setter
    def costs(self, costs):
        """
        Sets the costs of this DestinyEntitiesVendorsDestinyVendorSaleItemComponent.
        A summary of the current costs of the item.

        :param costs: The costs of this DestinyEntitiesVendorsDestinyVendorSaleItemComponent.
        :type: list[ComponentsschemasDestinyDestinyItemQuantity]
        """

        self._costs = costs

    @property
    def required_unlocks(self):
        """
        Gets the required_unlocks of this DestinyEntitiesVendorsDestinyVendorSaleItemComponent.
        If you can't buy the item due to a complex character state, these will be hashes forDestinyUnlockDefinitions that you can check to see messages regarding the failure (if the unlockshave human readable information: it is not guaranteed that Unlocks will have human readable strings, andyour application will have to handle that)  Prefer using failureIndexes instead.  These are provided for informational purposes, but have largelybeen supplanted by failureIndexes.

        :return: The required_unlocks of this DestinyEntitiesVendorsDestinyVendorSaleItemComponent.
        :rtype: list[int]
        """
        return self._required_unlocks

    @required_unlocks.setter
    def required_unlocks(self, required_unlocks):
        """
        Sets the required_unlocks of this DestinyEntitiesVendorsDestinyVendorSaleItemComponent.
        If you can't buy the item due to a complex character state, these will be hashes forDestinyUnlockDefinitions that you can check to see messages regarding the failure (if the unlockshave human readable information: it is not guaranteed that Unlocks will have human readable strings, andyour application will have to handle that)  Prefer using failureIndexes instead.  These are provided for informational purposes, but have largelybeen supplanted by failureIndexes.

        :param required_unlocks: The required_unlocks of this DestinyEntitiesVendorsDestinyVendorSaleItemComponent.
        :type: list[int]
        """

        self._required_unlocks = required_unlocks

    @property
    def unlock_statuses(self):
        """
        Gets the unlock_statuses of this DestinyEntitiesVendorsDestinyVendorSaleItemComponent.
        If any complex unlock states are checked in determining purchasability, these willbe returned here along with the status of the unlock check.  Prefer using failureIndexes instead.  These are provided for informational purposes, but have largelybeen supplanted by failureIndexes.

        :return: The unlock_statuses of this DestinyEntitiesVendorsDestinyVendorSaleItemComponent.
        :rtype: list[ComponentsschemasDestinyDestinyUnlockStatus]
        """
        return self._unlock_statuses

    @unlock_statuses.setter
    def unlock_statuses(self, unlock_statuses):
        """
        Sets the unlock_statuses of this DestinyEntitiesVendorsDestinyVendorSaleItemComponent.
        If any complex unlock states are checked in determining purchasability, these willbe returned here along with the status of the unlock check.  Prefer using failureIndexes instead.  These are provided for informational purposes, but have largelybeen supplanted by failureIndexes.

        :param unlock_statuses: The unlock_statuses of this DestinyEntitiesVendorsDestinyVendorSaleItemComponent.
        :type: list[ComponentsschemasDestinyDestinyUnlockStatus]
        """

        self._unlock_statuses = unlock_statuses

    @property
    def failure_indexes(self):
        """
        Gets the failure_indexes of this DestinyEntitiesVendorsDestinyVendorSaleItemComponent.
        Indexes in to the \"failureStrings\" lookup table in DestinyVendorDefinition for the given Vendor.Gives some more reliable failure information for why you can't purchase an item.  It is preferred to use these over requiredUnlocks and unlockStatuses: the latter are providedmostly in case someone can do something interesting with it that I didn't anticipate.

        :return: The failure_indexes of this DestinyEntitiesVendorsDestinyVendorSaleItemComponent.
        :rtype: list[int]
        """
        return self._failure_indexes

    @failure_indexes.setter
    def failure_indexes(self, failure_indexes):
        """
        Sets the failure_indexes of this DestinyEntitiesVendorsDestinyVendorSaleItemComponent.
        Indexes in to the \"failureStrings\" lookup table in DestinyVendorDefinition for the given Vendor.Gives some more reliable failure information for why you can't purchase an item.  It is preferred to use these over requiredUnlocks and unlockStatuses: the latter are providedmostly in case someone can do something interesting with it that I didn't anticipate.

        :param failure_indexes: The failure_indexes of this DestinyEntitiesVendorsDestinyVendorSaleItemComponent.
        :type: list[int]
        """

        self._failure_indexes = failure_indexes

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
        if not isinstance(other, DestinyEntitiesVendorsDestinyVendorSaleItemComponent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other