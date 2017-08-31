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


class DestinyDefinitionsDestinyInventoryItemDefinition(object):
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
        'display_properties': 'ComponentsschemasDestinyDefinitionsCommonDestinyDisplayPropertiesDefinition',
        'secondary_icon': 'str',
        'secondary_overlay': 'str',
        'secondary_special': 'str',
        'screenshot': 'str',
        'item_type_display_name': 'str',
        'item_type_and_tier_display_name': 'str',
        'display_source': 'str',
        'tooltip_style': 'str',
        'investment_stats': 'list[ComponentsschemasDestinyDefinitionsDestinyItemInvestmentStatDefinition]',
        'perks': 'list[ComponentsschemasDestinyDefinitionsDestinyItemPerkEntryDefinition]',
        'lore_hash': 'int',
        'summary_item_hash': 'int',
        'animations': 'list[ComponentsschemasDestinyDefinitionsAnimationsDestinyAnimationReference]',
        'allow_actions': 'bool',
        'links': 'list[ComponentsschemasLinksHyperlinkReference]',
        'non_transferrable': 'bool',
        'item_category_hashes': 'list[int]',
        'equippable': 'bool',
        'damage_type_hashes': 'list[int]',
        'damage_types': 'list[ComponentsschemasDestinyDamageType]',
        'default_damage_type_hash': 'int',
        'hash': 'int',
        'index': 'int',
        'redacted': 'bool'
    }

    attribute_map = {
        'display_properties': 'displayProperties',
        'secondary_icon': 'secondaryIcon',
        'secondary_overlay': 'secondaryOverlay',
        'secondary_special': 'secondarySpecial',
        'screenshot': 'screenshot',
        'item_type_display_name': 'itemTypeDisplayName',
        'item_type_and_tier_display_name': 'itemTypeAndTierDisplayName',
        'display_source': 'displaySource',
        'tooltip_style': 'tooltipStyle',
        'investment_stats': 'investmentStats',
        'perks': 'perks',
        'lore_hash': 'loreHash',
        'summary_item_hash': 'summaryItemHash',
        'animations': 'animations',
        'allow_actions': 'allowActions',
        'links': 'links',
        'non_transferrable': 'nonTransferrable',
        'item_category_hashes': 'itemCategoryHashes',
        'equippable': 'equippable',
        'damage_type_hashes': 'damageTypeHashes',
        'damage_types': 'damageTypes',
        'default_damage_type_hash': 'defaultDamageTypeHash',
        'hash': 'hash',
        'index': 'index',
        'redacted': 'redacted'
    }

    def __init__(self, display_properties=None, secondary_icon=None, secondary_overlay=None, secondary_special=None, screenshot=None, item_type_display_name=None, item_type_and_tier_display_name=None, display_source=None, tooltip_style=None, investment_stats=None, perks=None, lore_hash=None, summary_item_hash=None, animations=None, allow_actions=None, links=None, non_transferrable=None, item_category_hashes=None, equippable=None, damage_type_hashes=None, damage_types=None, default_damage_type_hash=None, hash=None, index=None, redacted=None):
        """
        DestinyDefinitionsDestinyInventoryItemDefinition - a model defined in Swagger
        """

        self._display_properties = None
        self._secondary_icon = None
        self._secondary_overlay = None
        self._secondary_special = None
        self._screenshot = None
        self._item_type_display_name = None
        self._item_type_and_tier_display_name = None
        self._display_source = None
        self._tooltip_style = None
        self._investment_stats = None
        self._perks = None
        self._lore_hash = None
        self._summary_item_hash = None
        self._animations = None
        self._allow_actions = None
        self._links = None
        self._non_transferrable = None
        self._item_category_hashes = None
        self._equippable = None
        self._damage_type_hashes = None
        self._damage_types = None
        self._default_damage_type_hash = None
        self._hash = None
        self._index = None
        self._redacted = None
        self.discriminator = None

        if display_properties is not None:
          self.display_properties = display_properties
        if secondary_icon is not None:
          self.secondary_icon = secondary_icon
        if secondary_overlay is not None:
          self.secondary_overlay = secondary_overlay
        if secondary_special is not None:
          self.secondary_special = secondary_special
        if screenshot is not None:
          self.screenshot = screenshot
        if item_type_display_name is not None:
          self.item_type_display_name = item_type_display_name
        if item_type_and_tier_display_name is not None:
          self.item_type_and_tier_display_name = item_type_and_tier_display_name
        if display_source is not None:
          self.display_source = display_source
        if tooltip_style is not None:
          self.tooltip_style = tooltip_style
        if investment_stats is not None:
          self.investment_stats = investment_stats
        if perks is not None:
          self.perks = perks
        if lore_hash is not None:
          self.lore_hash = lore_hash
        if summary_item_hash is not None:
          self.summary_item_hash = summary_item_hash
        if animations is not None:
          self.animations = animations
        if allow_actions is not None:
          self.allow_actions = allow_actions
        if links is not None:
          self.links = links
        if non_transferrable is not None:
          self.non_transferrable = non_transferrable
        if item_category_hashes is not None:
          self.item_category_hashes = item_category_hashes
        if equippable is not None:
          self.equippable = equippable
        if damage_type_hashes is not None:
          self.damage_type_hashes = damage_type_hashes
        if damage_types is not None:
          self.damage_types = damage_types
        if default_damage_type_hash is not None:
          self.default_damage_type_hash = default_damage_type_hash
        if hash is not None:
          self.hash = hash
        if index is not None:
          self.index = index
        if redacted is not None:
          self.redacted = redacted

    @property
    def display_properties(self):
        """
        Gets the display_properties of this DestinyDefinitionsDestinyInventoryItemDefinition.

        :return: The display_properties of this DestinyDefinitionsDestinyInventoryItemDefinition.
        :rtype: ComponentsschemasDestinyDefinitionsCommonDestinyDisplayPropertiesDefinition
        """
        return self._display_properties

    @display_properties.setter
    def display_properties(self, display_properties):
        """
        Sets the display_properties of this DestinyDefinitionsDestinyInventoryItemDefinition.

        :param display_properties: The display_properties of this DestinyDefinitionsDestinyInventoryItemDefinition.
        :type: ComponentsschemasDestinyDefinitionsCommonDestinyDisplayPropertiesDefinition
        """

        self._display_properties = display_properties

    @property
    def secondary_icon(self):
        """
        Gets the secondary_icon of this DestinyDefinitionsDestinyInventoryItemDefinition.
        A secondary icon associated with the item.  Currently this is used in very context specificapplications, such as Emblem Nameplates.

        :return: The secondary_icon of this DestinyDefinitionsDestinyInventoryItemDefinition.
        :rtype: str
        """
        return self._secondary_icon

    @secondary_icon.setter
    def secondary_icon(self, secondary_icon):
        """
        Sets the secondary_icon of this DestinyDefinitionsDestinyInventoryItemDefinition.
        A secondary icon associated with the item.  Currently this is used in very context specificapplications, such as Emblem Nameplates.

        :param secondary_icon: The secondary_icon of this DestinyDefinitionsDestinyInventoryItemDefinition.
        :type: str
        """

        self._secondary_icon = secondary_icon

    @property
    def secondary_overlay(self):
        """
        Gets the secondary_overlay of this DestinyDefinitionsDestinyInventoryItemDefinition.
        Pulled from the secondary icon, this is the \"secondary background\" of the secondaryicon.  Confusing?  Sure, that's why I call it \"overlay\" here: because as far as it'sbeen used thus far, it has been for an optional overlay image.  We'll see if that holds up,but at least for now it explains what this image is a bit better.

        :return: The secondary_overlay of this DestinyDefinitionsDestinyInventoryItemDefinition.
        :rtype: str
        """
        return self._secondary_overlay

    @secondary_overlay.setter
    def secondary_overlay(self, secondary_overlay):
        """
        Sets the secondary_overlay of this DestinyDefinitionsDestinyInventoryItemDefinition.
        Pulled from the secondary icon, this is the \"secondary background\" of the secondaryicon.  Confusing?  Sure, that's why I call it \"overlay\" here: because as far as it'sbeen used thus far, it has been for an optional overlay image.  We'll see if that holds up,but at least for now it explains what this image is a bit better.

        :param secondary_overlay: The secondary_overlay of this DestinyDefinitionsDestinyInventoryItemDefinition.
        :type: str
        """

        self._secondary_overlay = secondary_overlay

    @property
    def secondary_special(self):
        """
        Gets the secondary_special of this DestinyDefinitionsDestinyInventoryItemDefinition.
        Pulled from the Secondary Icon, this is the \"special\" background for the item.For Emblems, this is the background image used on the Details view: but it neednot be limited to that for other types of items.

        :return: The secondary_special of this DestinyDefinitionsDestinyInventoryItemDefinition.
        :rtype: str
        """
        return self._secondary_special

    @secondary_special.setter
    def secondary_special(self, secondary_special):
        """
        Sets the secondary_special of this DestinyDefinitionsDestinyInventoryItemDefinition.
        Pulled from the Secondary Icon, this is the \"special\" background for the item.For Emblems, this is the background image used on the Details view: but it neednot be limited to that for other types of items.

        :param secondary_special: The secondary_special of this DestinyDefinitionsDestinyInventoryItemDefinition.
        :type: str
        """

        self._secondary_special = secondary_special

    @property
    def screenshot(self):
        """
        Gets the screenshot of this DestinyDefinitionsDestinyInventoryItemDefinition.
        If we were able to acquire an in-game screenshot for the item, the path to that screenshotwill be returned here.  Note that not all items have screenshots: particularly not any non-equippableitems.

        :return: The screenshot of this DestinyDefinitionsDestinyInventoryItemDefinition.
        :rtype: str
        """
        return self._screenshot

    @screenshot.setter
    def screenshot(self, screenshot):
        """
        Sets the screenshot of this DestinyDefinitionsDestinyInventoryItemDefinition.
        If we were able to acquire an in-game screenshot for the item, the path to that screenshotwill be returned here.  Note that not all items have screenshots: particularly not any non-equippableitems.

        :param screenshot: The screenshot of this DestinyDefinitionsDestinyInventoryItemDefinition.
        :type: str
        """

        self._screenshot = screenshot

    @property
    def item_type_display_name(self):
        """
        Gets the item_type_display_name of this DestinyDefinitionsDestinyInventoryItemDefinition.
        The localized title/name of the item's type.  This can be whatever the designers want, and has no guaranteeof consistency between items.

        :return: The item_type_display_name of this DestinyDefinitionsDestinyInventoryItemDefinition.
        :rtype: str
        """
        return self._item_type_display_name

    @item_type_display_name.setter
    def item_type_display_name(self, item_type_display_name):
        """
        Sets the item_type_display_name of this DestinyDefinitionsDestinyInventoryItemDefinition.
        The localized title/name of the item's type.  This can be whatever the designers want, and has no guaranteeof consistency between items.

        :param item_type_display_name: The item_type_display_name of this DestinyDefinitionsDestinyInventoryItemDefinition.
        :type: str
        """

        self._item_type_display_name = item_type_display_name

    @property
    def item_type_and_tier_display_name(self):
        """
        Gets the item_type_and_tier_display_name of this DestinyDefinitionsDestinyInventoryItemDefinition.
        It became a common enough pattern in our UI to show Item Type and Tier combined into a single localizedstring that I'm just going to go ahead and start pre-creating these for items.

        :return: The item_type_and_tier_display_name of this DestinyDefinitionsDestinyInventoryItemDefinition.
        :rtype: str
        """
        return self._item_type_and_tier_display_name

    @item_type_and_tier_display_name.setter
    def item_type_and_tier_display_name(self, item_type_and_tier_display_name):
        """
        Sets the item_type_and_tier_display_name of this DestinyDefinitionsDestinyInventoryItemDefinition.
        It became a common enough pattern in our UI to show Item Type and Tier combined into a single localizedstring that I'm just going to go ahead and start pre-creating these for items.

        :param item_type_and_tier_display_name: The item_type_and_tier_display_name of this DestinyDefinitionsDestinyInventoryItemDefinition.
        :type: str
        """

        self._item_type_and_tier_display_name = item_type_and_tier_display_name

    @property
    def display_source(self):
        """
        Gets the display_source of this DestinyDefinitionsDestinyInventoryItemDefinition.
        In theory, it is a localized string telling you about how you can find the item.I really wish this was more consistent.  Many times, it has nothing.  Sometimes, it's instead a more narrative-forwarddescription of the item.  Which is cool, and I wish all properties had that data, but it should really beits own property.

        :return: The display_source of this DestinyDefinitionsDestinyInventoryItemDefinition.
        :rtype: str
        """
        return self._display_source

    @display_source.setter
    def display_source(self, display_source):
        """
        Sets the display_source of this DestinyDefinitionsDestinyInventoryItemDefinition.
        In theory, it is a localized string telling you about how you can find the item.I really wish this was more consistent.  Many times, it has nothing.  Sometimes, it's instead a more narrative-forwarddescription of the item.  Which is cool, and I wish all properties had that data, but it should really beits own property.

        :param display_source: The display_source of this DestinyDefinitionsDestinyInventoryItemDefinition.
        :type: str
        """

        self._display_source = display_source

    @property
    def tooltip_style(self):
        """
        Gets the tooltip_style of this DestinyDefinitionsDestinyInventoryItemDefinition.
        An identifier that the game UI uses to determine what type of tooltip to show for the item.  These have nocorresponding definitions that BNet can link to: so it'll be up to you to interpret and display your UI differentlyaccording to these styles (or ignore it).

        :return: The tooltip_style of this DestinyDefinitionsDestinyInventoryItemDefinition.
        :rtype: str
        """
        return self._tooltip_style

    @tooltip_style.setter
    def tooltip_style(self, tooltip_style):
        """
        Sets the tooltip_style of this DestinyDefinitionsDestinyInventoryItemDefinition.
        An identifier that the game UI uses to determine what type of tooltip to show for the item.  These have nocorresponding definitions that BNet can link to: so it'll be up to you to interpret and display your UI differentlyaccording to these styles (or ignore it).

        :param tooltip_style: The tooltip_style of this DestinyDefinitionsDestinyInventoryItemDefinition.
        :type: str
        """

        self._tooltip_style = tooltip_style

    @property
    def investment_stats(self):
        """
        Gets the investment_stats of this DestinyDefinitionsDestinyInventoryItemDefinition.
        If the item has stats, this block will be defined.  It has the \"raw\" investment stats for the item.These investment stats don't take into account the ways that the items can spawn, nor do they takeinto account any Stat Group transformations.  I have retained them for debugging purposes, but Ido not know how useful people will find them.

        :return: The investment_stats of this DestinyDefinitionsDestinyInventoryItemDefinition.
        :rtype: list[ComponentsschemasDestinyDefinitionsDestinyItemInvestmentStatDefinition]
        """
        return self._investment_stats

    @investment_stats.setter
    def investment_stats(self, investment_stats):
        """
        Sets the investment_stats of this DestinyDefinitionsDestinyInventoryItemDefinition.
        If the item has stats, this block will be defined.  It has the \"raw\" investment stats for the item.These investment stats don't take into account the ways that the items can spawn, nor do they takeinto account any Stat Group transformations.  I have retained them for debugging purposes, but Ido not know how useful people will find them.

        :param investment_stats: The investment_stats of this DestinyDefinitionsDestinyInventoryItemDefinition.
        :type: list[ComponentsschemasDestinyDefinitionsDestinyItemInvestmentStatDefinition]
        """

        self._investment_stats = investment_stats

    @property
    def perks(self):
        """
        Gets the perks of this DestinyDefinitionsDestinyInventoryItemDefinition.
        If the item has any *intrinsic* Perks (Perks that it will provide regardless of Sockets, Talent Grid,and other transitory state), they will be defined here.

        :return: The perks of this DestinyDefinitionsDestinyInventoryItemDefinition.
        :rtype: list[ComponentsschemasDestinyDefinitionsDestinyItemPerkEntryDefinition]
        """
        return self._perks

    @perks.setter
    def perks(self, perks):
        """
        Sets the perks of this DestinyDefinitionsDestinyInventoryItemDefinition.
        If the item has any *intrinsic* Perks (Perks that it will provide regardless of Sockets, Talent Grid,and other transitory state), they will be defined here.

        :param perks: The perks of this DestinyDefinitionsDestinyInventoryItemDefinition.
        :type: list[ComponentsschemasDestinyDefinitionsDestinyItemPerkEntryDefinition]
        """

        self._perks = perks

    @property
    def lore_hash(self):
        """
        Gets the lore_hash of this DestinyDefinitionsDestinyInventoryItemDefinition.
        If the item has any related Lore (DestinyLoreDefinition), this will be the hash identifier you can useto look up the lore definition.

        :return: The lore_hash of this DestinyDefinitionsDestinyInventoryItemDefinition.
        :rtype: int
        """
        return self._lore_hash

    @lore_hash.setter
    def lore_hash(self, lore_hash):
        """
        Sets the lore_hash of this DestinyDefinitionsDestinyInventoryItemDefinition.
        If the item has any related Lore (DestinyLoreDefinition), this will be the hash identifier you can useto look up the lore definition.

        :param lore_hash: The lore_hash of this DestinyDefinitionsDestinyInventoryItemDefinition.
        :type: int
        """

        self._lore_hash = lore_hash

    @property
    def summary_item_hash(self):
        """
        Gets the summary_item_hash of this DestinyDefinitionsDestinyInventoryItemDefinition.
        There are times when the game will show you a \"summary/vague\" version of an item - such as a description of its typerepresented as a DestinyInventoryItemDefinition - rather than display the item itself.  This happens sometimes when summarizing possible rewards in a tooltip.  This is the item displayed instead, ifit exists.

        :return: The summary_item_hash of this DestinyDefinitionsDestinyInventoryItemDefinition.
        :rtype: int
        """
        return self._summary_item_hash

    @summary_item_hash.setter
    def summary_item_hash(self, summary_item_hash):
        """
        Sets the summary_item_hash of this DestinyDefinitionsDestinyInventoryItemDefinition.
        There are times when the game will show you a \"summary/vague\" version of an item - such as a description of its typerepresented as a DestinyInventoryItemDefinition - rather than display the item itself.  This happens sometimes when summarizing possible rewards in a tooltip.  This is the item displayed instead, ifit exists.

        :param summary_item_hash: The summary_item_hash of this DestinyDefinitionsDestinyInventoryItemDefinition.
        :type: int
        """

        self._summary_item_hash = summary_item_hash

    @property
    def animations(self):
        """
        Gets the animations of this DestinyDefinitionsDestinyInventoryItemDefinition.
        If any animations were extracted from game content for this item, these will be the definitionsof those animations.

        :return: The animations of this DestinyDefinitionsDestinyInventoryItemDefinition.
        :rtype: list[ComponentsschemasDestinyDefinitionsAnimationsDestinyAnimationReference]
        """
        return self._animations

    @animations.setter
    def animations(self, animations):
        """
        Sets the animations of this DestinyDefinitionsDestinyInventoryItemDefinition.
        If any animations were extracted from game content for this item, these will be the definitionsof those animations.

        :param animations: The animations of this DestinyDefinitionsDestinyInventoryItemDefinition.
        :type: list[ComponentsschemasDestinyDefinitionsAnimationsDestinyAnimationReference]
        """

        self._animations = animations

    @property
    def allow_actions(self):
        """
        Gets the allow_actions of this DestinyDefinitionsDestinyInventoryItemDefinition.
        BNet may forbid the execution of actions on this item via the API.  If that is occurring, allowActions will be set to false.

        :return: The allow_actions of this DestinyDefinitionsDestinyInventoryItemDefinition.
        :rtype: bool
        """
        return self._allow_actions

    @allow_actions.setter
    def allow_actions(self, allow_actions):
        """
        Sets the allow_actions of this DestinyDefinitionsDestinyInventoryItemDefinition.
        BNet may forbid the execution of actions on this item via the API.  If that is occurring, allowActions will be set to false.

        :param allow_actions: The allow_actions of this DestinyDefinitionsDestinyInventoryItemDefinition.
        :type: bool
        """

        self._allow_actions = allow_actions

    @property
    def links(self):
        """
        Gets the links of this DestinyDefinitionsDestinyInventoryItemDefinition.
        If we added any help or informational URLs about this item, these will be those links.

        :return: The links of this DestinyDefinitionsDestinyInventoryItemDefinition.
        :rtype: list[ComponentsschemasLinksHyperlinkReference]
        """
        return self._links

    @links.setter
    def links(self, links):
        """
        Sets the links of this DestinyDefinitionsDestinyInventoryItemDefinition.
        If we added any help or informational URLs about this item, these will be those links.

        :param links: The links of this DestinyDefinitionsDestinyInventoryItemDefinition.
        :type: list[ComponentsschemasLinksHyperlinkReference]
        """

        self._links = links

    @property
    def non_transferrable(self):
        """
        Gets the non_transferrable of this DestinyDefinitionsDestinyInventoryItemDefinition.
        The intrinsic transferability of an item.  I hate that this boolean is negative - but there's a reason.  Just because an item is intrinsically transferrable doesn't mean that it can be transferred,and we don't want to imply that this is the only source of that transferability.

        :return: The non_transferrable of this DestinyDefinitionsDestinyInventoryItemDefinition.
        :rtype: bool
        """
        return self._non_transferrable

    @non_transferrable.setter
    def non_transferrable(self, non_transferrable):
        """
        Sets the non_transferrable of this DestinyDefinitionsDestinyInventoryItemDefinition.
        The intrinsic transferability of an item.  I hate that this boolean is negative - but there's a reason.  Just because an item is intrinsically transferrable doesn't mean that it can be transferred,and we don't want to imply that this is the only source of that transferability.

        :param non_transferrable: The non_transferrable of this DestinyDefinitionsDestinyInventoryItemDefinition.
        :type: bool
        """

        self._non_transferrable = non_transferrable

    @property
    def item_category_hashes(self):
        """
        Gets the item_category_hashes of this DestinyDefinitionsDestinyInventoryItemDefinition.
        BNet attempts to make a more formal definition of item \"Categories\", as defined by DestinyItemCategoryDefinition.  This is a list of all Categories that we were able toalgorithmically determine that this item is a member of.  (for instance, that it's a \"Weapon\",that it's an \"Auto Rifle\", etc...)  The algorithm for these is, unfortunately, volatile.  If you believe you see a miscategorizeditem, please let us know on the Bungie API forums.

        :return: The item_category_hashes of this DestinyDefinitionsDestinyInventoryItemDefinition.
        :rtype: list[int]
        """
        return self._item_category_hashes

    @item_category_hashes.setter
    def item_category_hashes(self, item_category_hashes):
        """
        Sets the item_category_hashes of this DestinyDefinitionsDestinyInventoryItemDefinition.
        BNet attempts to make a more formal definition of item \"Categories\", as defined by DestinyItemCategoryDefinition.  This is a list of all Categories that we were able toalgorithmically determine that this item is a member of.  (for instance, that it's a \"Weapon\",that it's an \"Auto Rifle\", etc...)  The algorithm for these is, unfortunately, volatile.  If you believe you see a miscategorizeditem, please let us know on the Bungie API forums.

        :param item_category_hashes: The item_category_hashes of this DestinyDefinitionsDestinyInventoryItemDefinition.
        :type: list[int]
        """

        self._item_category_hashes = item_category_hashes

    @property
    def equippable(self):
        """
        Gets the equippable of this DestinyDefinitionsDestinyInventoryItemDefinition.
        If true, then you will be allowed to equip the item if you pass its other requirements.  This being false means that you cannot equip the item under any circumstances.

        :return: The equippable of this DestinyDefinitionsDestinyInventoryItemDefinition.
        :rtype: bool
        """
        return self._equippable

    @equippable.setter
    def equippable(self, equippable):
        """
        Sets the equippable of this DestinyDefinitionsDestinyInventoryItemDefinition.
        If true, then you will be allowed to equip the item if you pass its other requirements.  This being false means that you cannot equip the item under any circumstances.

        :param equippable: The equippable of this DestinyDefinitionsDestinyInventoryItemDefinition.
        :type: bool
        """

        self._equippable = equippable

    @property
    def damage_type_hashes(self):
        """
        Gets the damage_type_hashes of this DestinyDefinitionsDestinyInventoryItemDefinition.
        Theoretically, an item can have many possible damage types.  In *practice*, this is not true,but just in case weapons start being made that have multiple (for instance, an item where a sockethas reusable plugs for every possible damage type that you can choose from freely), this fieldwill return all of the possible damage types that are available to the weapon by default.

        :return: The damage_type_hashes of this DestinyDefinitionsDestinyInventoryItemDefinition.
        :rtype: list[int]
        """
        return self._damage_type_hashes

    @damage_type_hashes.setter
    def damage_type_hashes(self, damage_type_hashes):
        """
        Sets the damage_type_hashes of this DestinyDefinitionsDestinyInventoryItemDefinition.
        Theoretically, an item can have many possible damage types.  In *practice*, this is not true,but just in case weapons start being made that have multiple (for instance, an item where a sockethas reusable plugs for every possible damage type that you can choose from freely), this fieldwill return all of the possible damage types that are available to the weapon by default.

        :param damage_type_hashes: The damage_type_hashes of this DestinyDefinitionsDestinyInventoryItemDefinition.
        :type: list[int]
        """

        self._damage_type_hashes = damage_type_hashes

    @property
    def damage_types(self):
        """
        Gets the damage_types of this DestinyDefinitionsDestinyInventoryItemDefinition.
        This is the list of all damage types that we know ahead of time the item can take on.Unfortunately, this does not preclude the possibility of something funky happeningto give the item a damage type that cannot be predicted beforehand: for example,if some designer decides to create arbitrary non-reusable plugs that cause damage typeto change.  This damage type prediction will only use the following to determine potential damage types:  - Intrinsic perks  - Talent Node perks  - Known, reusable plugs for sockets

        :return: The damage_types of this DestinyDefinitionsDestinyInventoryItemDefinition.
        :rtype: list[ComponentsschemasDestinyDamageType]
        """
        return self._damage_types

    @damage_types.setter
    def damage_types(self, damage_types):
        """
        Sets the damage_types of this DestinyDefinitionsDestinyInventoryItemDefinition.
        This is the list of all damage types that we know ahead of time the item can take on.Unfortunately, this does not preclude the possibility of something funky happeningto give the item a damage type that cannot be predicted beforehand: for example,if some designer decides to create arbitrary non-reusable plugs that cause damage typeto change.  This damage type prediction will only use the following to determine potential damage types:  - Intrinsic perks  - Talent Node perks  - Known, reusable plugs for sockets

        :param damage_types: The damage_types of this DestinyDefinitionsDestinyInventoryItemDefinition.
        :type: list[ComponentsschemasDestinyDamageType]
        """

        self._damage_types = damage_types

    @property
    def default_damage_type_hash(self):
        """
        Gets the default_damage_type_hash of this DestinyDefinitionsDestinyInventoryItemDefinition.
        Similar to defaultDamageType, but represented as the hash identifier for a DestinyDamageTypeDefinition.  I will likely regret leaving in the enumeration versions of these properties, but for now they'revery convenient.

        :return: The default_damage_type_hash of this DestinyDefinitionsDestinyInventoryItemDefinition.
        :rtype: int
        """
        return self._default_damage_type_hash

    @default_damage_type_hash.setter
    def default_damage_type_hash(self, default_damage_type_hash):
        """
        Sets the default_damage_type_hash of this DestinyDefinitionsDestinyInventoryItemDefinition.
        Similar to defaultDamageType, but represented as the hash identifier for a DestinyDamageTypeDefinition.  I will likely regret leaving in the enumeration versions of these properties, but for now they'revery convenient.

        :param default_damage_type_hash: The default_damage_type_hash of this DestinyDefinitionsDestinyInventoryItemDefinition.
        :type: int
        """

        self._default_damage_type_hash = default_damage_type_hash

    @property
    def hash(self):
        """
        Gets the hash of this DestinyDefinitionsDestinyInventoryItemDefinition.
        The unique identifier for this entity.  Guaranteed to be unique for the type of entity, but not globally.  When entities refer to each other in Destiny content, it is this hash that they are referring to.

        :return: The hash of this DestinyDefinitionsDestinyInventoryItemDefinition.
        :rtype: int
        """
        return self._hash

    @hash.setter
    def hash(self, hash):
        """
        Sets the hash of this DestinyDefinitionsDestinyInventoryItemDefinition.
        The unique identifier for this entity.  Guaranteed to be unique for the type of entity, but not globally.  When entities refer to each other in Destiny content, it is this hash that they are referring to.

        :param hash: The hash of this DestinyDefinitionsDestinyInventoryItemDefinition.
        :type: int
        """

        self._hash = hash

    @property
    def index(self):
        """
        Gets the index of this DestinyDefinitionsDestinyInventoryItemDefinition.
        The index of the entity as it was found in the investment tables.

        :return: The index of this DestinyDefinitionsDestinyInventoryItemDefinition.
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """
        Sets the index of this DestinyDefinitionsDestinyInventoryItemDefinition.
        The index of the entity as it was found in the investment tables.

        :param index: The index of this DestinyDefinitionsDestinyInventoryItemDefinition.
        :type: int
        """

        self._index = index

    @property
    def redacted(self):
        """
        Gets the redacted of this DestinyDefinitionsDestinyInventoryItemDefinition.
        If this is true, then there is an entity with this identifier/type combination, but BNet isnot yet allowed to show it.  Sorry!

        :return: The redacted of this DestinyDefinitionsDestinyInventoryItemDefinition.
        :rtype: bool
        """
        return self._redacted

    @redacted.setter
    def redacted(self, redacted):
        """
        Sets the redacted of this DestinyDefinitionsDestinyInventoryItemDefinition.
        If this is true, then there is an entity with this identifier/type combination, but BNet isnot yet allowed to show it.  Sorry!

        :param redacted: The redacted of this DestinyDefinitionsDestinyInventoryItemDefinition.
        :type: bool
        """

        self._redacted = redacted

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
        if not isinstance(other, DestinyDefinitionsDestinyInventoryItemDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other