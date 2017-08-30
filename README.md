# swagger-client
These endpoints constitute the functionality exposed by Bungie.net, both for more traditional website functionality and for connectivity to Bungie video games and their related functionality.

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 3.0.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen
For more information, please visit [https://github.com/Bungie-net/api](https://github.com/Bungie-net/api)

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# create an instance of the API class
api_instance = swagger_client.CommunityContentApi()
media_filter = 'media_filter_example' # str | The type of media to get
page = 'page_example' # str | Zero based page
sort = 'sort_example' # str | The sort mode.

try:
    api_instance.community_content_get_community_content(media_filter, page, sort)
except ApiException as e:
    print("Exception when calling CommunityContentApi->community_content_get_community_content: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*CommunityContentApi* | [**community_content_get_community_content**](docs/CommunityContentApi.md#community_content_get_community_content) | **GET** /CommunityContent/Get/{sort}/{mediaFilter}/{page}/ | 
*CommunityContentApi* | [**community_content_get_community_live_statuses**](docs/CommunityContentApi.md#community_content_get_community_live_statuses) | **GET** /CommunityContent/Live/All/{partnershipType}/{sort}/{page}/ | 
*CommunityContentApi* | [**community_content_get_community_live_statuses_for_clanmates**](docs/CommunityContentApi.md#community_content_get_community_live_statuses_for_clanmates) | **GET** /CommunityContent/Live/Clan/{partnershipType}/{sort}/{page}/ | 
*CommunityContentApi* | [**community_content_get_community_live_statuses_for_friends**](docs/CommunityContentApi.md#community_content_get_community_live_statuses_for_friends) | **GET** /CommunityContent/Live/Friends/{partnershipType}/{sort}/{page}/ | 
*CommunityContentApi* | [**community_content_get_featured_community_live_statuses**](docs/CommunityContentApi.md#community_content_get_featured_community_live_statuses) | **GET** /CommunityContent/Live/Featured/{partnershipType}/{sort}/{page}/ | 
*CommunityContentApi* | [**community_content_get_streaming_status_for_member**](docs/CommunityContentApi.md#community_content_get_streaming_status_for_member) | **GET** /CommunityContent/Live/Users/{partnershipType}/{membershipType}/{membershipId}/ | 
*Destiny2Api* | [**destiny2_activate_talent_node**](docs/Destiny2Api.md#destiny2_activate_talent_node) | **POST** /Destiny2/Actions/Items/ActivateTalentNode/ | 
*Destiny2Api* | [**destiny2_equip_item**](docs/Destiny2Api.md#destiny2_equip_item) | **POST** /Destiny2/Actions/Items/EquipItem/ | 
*Destiny2Api* | [**destiny2_equip_items**](docs/Destiny2Api.md#destiny2_equip_items) | **POST** /Destiny2/Actions/Items/EquipItems/ | 
*Destiny2Api* | [**destiny2_get_activity_history**](docs/Destiny2Api.md#destiny2_get_activity_history) | **GET** /Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/{characterId}/Stats/Activities/ | 
*Destiny2Api* | [**destiny2_get_character**](docs/Destiny2Api.md#destiny2_get_character) | **GET** /Destiny2/{membershipType}/Profile/{destinyMembershipId}/Character/{characterId}/ | 
*Destiny2Api* | [**destiny2_get_clan_aggregate_stats**](docs/Destiny2Api.md#destiny2_get_clan_aggregate_stats) | **GET** /Destiny2/Stats/AggregateClanStats/{groupId}/ | 
*Destiny2Api* | [**destiny2_get_clan_leaderboards**](docs/Destiny2Api.md#destiny2_get_clan_leaderboards) | **GET** /Destiny2/Stats/Leaderboards/Clans/{groupId}/ | 
*Destiny2Api* | [**destiny2_get_clan_weekly_reward_state**](docs/Destiny2Api.md#destiny2_get_clan_weekly_reward_state) | **GET** /Destiny2/Clan/{groupId}/WeeklyRewardState/ | 
*Destiny2Api* | [**destiny2_get_destiny_aggregate_activity_stats**](docs/Destiny2Api.md#destiny2_get_destiny_aggregate_activity_stats) | **GET** /Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/{characterId}/Stats/AggregateActivityStats/ | 
*Destiny2Api* | [**destiny2_get_destiny_manifest**](docs/Destiny2Api.md#destiny2_get_destiny_manifest) | **GET** /Destiny2/Manifest/ | 
*Destiny2Api* | [**destiny2_get_historical_stats**](docs/Destiny2Api.md#destiny2_get_historical_stats) | **GET** /Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/{characterId}/Stats/ | 
*Destiny2Api* | [**destiny2_get_historical_stats_definition**](docs/Destiny2Api.md#destiny2_get_historical_stats_definition) | **GET** /Destiny2/Stats/Definition/ | 
*Destiny2Api* | [**destiny2_get_historical_stats_for_account**](docs/Destiny2Api.md#destiny2_get_historical_stats_for_account) | **GET** /Destiny2/{membershipType}/Account/{destinyMembershipId}/Stats/ | 
*Destiny2Api* | [**destiny2_get_item**](docs/Destiny2Api.md#destiny2_get_item) | **GET** /Destiny2/{membershipType}/Profile/{destinyMembershipId}/Item/{itemInstanceId}/ | 
*Destiny2Api* | [**destiny2_get_leaderboards**](docs/Destiny2Api.md#destiny2_get_leaderboards) | **GET** /Destiny2/{membershipType}/Account/{destinyMembershipId}/Stats/Leaderboards/ | 
*Destiny2Api* | [**destiny2_get_leaderboards_for_character**](docs/Destiny2Api.md#destiny2_get_leaderboards_for_character) | **GET** /Destiny2/Stats/Leaderboards/{membershipType}/{destinyMembershipId}/{characterId}/ | 
*Destiny2Api* | [**destiny2_get_post_game_carnage_report**](docs/Destiny2Api.md#destiny2_get_post_game_carnage_report) | **GET** /Destiny2/Stats/PostGameCarnageReport/{activityId}/ | 
*Destiny2Api* | [**destiny2_get_profile**](docs/Destiny2Api.md#destiny2_get_profile) | **GET** /Destiny2/{membershipType}/Profile/{destinyMembershipId}/ | 
*Destiny2Api* | [**destiny2_get_public_milestone_content**](docs/Destiny2Api.md#destiny2_get_public_milestone_content) | **GET** /Destiny2/Milestones/{milestoneHash}/Content/ | 
*Destiny2Api* | [**destiny2_get_public_milestones**](docs/Destiny2Api.md#destiny2_get_public_milestones) | **GET** /Destiny2/Milestones/ | 
*Destiny2Api* | [**destiny2_get_unique_weapon_history**](docs/Destiny2Api.md#destiny2_get_unique_weapon_history) | **GET** /Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/{characterId}/Stats/UniqueWeapons/ | 
*Destiny2Api* | [**destiny2_get_vendor**](docs/Destiny2Api.md#destiny2_get_vendor) | **GET** /Destiny2/{membershipType}/Profile/{destinyMembershipId}/Character/{characterId}/Vendors/{vendorHash}/ | 
*Destiny2Api* | [**destiny2_get_vendors**](docs/Destiny2Api.md#destiny2_get_vendors) | **GET** /Destiny2/{membershipType}/Profile/{destinyMembershipId}/Character/{characterId}/Vendors/ | 
*Destiny2Api* | [**destiny2_insert_socket_plug**](docs/Destiny2Api.md#destiny2_insert_socket_plug) | **POST** /Destiny2/Actions/Items/InsertSocketPlug/ | 
*Destiny2Api* | [**destiny2_search_destiny_entities**](docs/Destiny2Api.md#destiny2_search_destiny_entities) | **GET** /Destiny2/Armory/Search/{type}/{searchTerm}/ | 
*Destiny2Api* | [**destiny2_search_destiny_player**](docs/Destiny2Api.md#destiny2_search_destiny_player) | **GET** /Destiny2/SearchDestinyPlayer/{membershipType}/{displayName}/ | 
*Destiny2Api* | [**destiny2_set_item_lock_state**](docs/Destiny2Api.md#destiny2_set_item_lock_state) | **POST** /Destiny2/Actions/Items/SetLockState/ | 
*Destiny2Api* | [**destiny2_transfer_item**](docs/Destiny2Api.md#destiny2_transfer_item) | **POST** /Destiny2/Actions/Items/TransferItem/ | 
*ForumApi* | [**forum_approve_fireteam_thread**](docs/ForumApi.md#forum_approve_fireteam_thread) | **POST** /Forum/Recruit/Approve/{topicId}/ | 
*ForumApi* | [**forum_get_core_topics_paged**](docs/ForumApi.md#forum_get_core_topics_paged) | **GET** /Forum/GetCoreTopicsPaged/{page}/{sort}/{quickDate}/{categoryFilter}/ | 
*ForumApi* | [**forum_get_forum_tag_suggestions**](docs/ForumApi.md#forum_get_forum_tag_suggestions) | **GET** /Forum/GetForumTagSuggestions/ | 
*ForumApi* | [**forum_get_poll**](docs/ForumApi.md#forum_get_poll) | **GET** /Forum/Poll/{topicId}/ | 
*ForumApi* | [**forum_get_post_and_parent**](docs/ForumApi.md#forum_get_post_and_parent) | **GET** /Forum/GetPostAndParent/{childPostId}/ | 
*ForumApi* | [**forum_get_post_and_parent_awaiting_approval**](docs/ForumApi.md#forum_get_post_and_parent_awaiting_approval) | **GET** /Forum/GetPostAndParentAwaitingApproval/{childPostId}/ | 
*ForumApi* | [**forum_get_posts_threaded_paged**](docs/ForumApi.md#forum_get_posts_threaded_paged) | **GET** /Forum/GetPostsThreadedPaged/{parentPostId}/{page}/{pageSize}/{replySize}/{getParentPost}/{rootThreadMode}/{sortMode}/ | 
*ForumApi* | [**forum_get_posts_threaded_paged_from_child**](docs/ForumApi.md#forum_get_posts_threaded_paged_from_child) | **GET** /Forum/GetPostsThreadedPagedFromChild/{childPostId}/{page}/{pageSize}/{replySize}/{rootThreadMode}/{sortMode}/ | 
*ForumApi* | [**forum_get_recruitment_thread_summaries**](docs/ForumApi.md#forum_get_recruitment_thread_summaries) | **POST** /Forum/Recruit/Summaries/ | 
*ForumApi* | [**forum_get_topic_for_content**](docs/ForumApi.md#forum_get_topic_for_content) | **GET** /Forum/GetTopicForContent/{contentId}/ | 
*ForumApi* | [**forum_get_topics_paged**](docs/ForumApi.md#forum_get_topics_paged) | **GET** /Forum/GetTopicsPaged/{page}/{pageSize}/{group}/{sort}/{quickDate}/{categoryFilter}/ | 
*ForumApi* | [**forum_join_fireteam_thread**](docs/ForumApi.md#forum_join_fireteam_thread) | **POST** /Forum/Recruit/Join/{topicId}/ | 
*ForumApi* | [**forum_kick_ban_fireteam_applicant**](docs/ForumApi.md#forum_kick_ban_fireteam_applicant) | **POST** /Forum/Recruit/KickBan/{topicId}/{targetMembershipId}/ | 
*ForumApi* | [**forum_leave_fireteam_thread**](docs/ForumApi.md#forum_leave_fireteam_thread) | **POST** /Forum/Recruit/Leave/{topicId}/ | 
*PreviewApi* | [**destiny2_activate_talent_node**](docs/PreviewApi.md#destiny2_activate_talent_node) | **POST** /Destiny2/Actions/Items/ActivateTalentNode/ | 
*PreviewApi* | [**destiny2_get_activity_history**](docs/PreviewApi.md#destiny2_get_activity_history) | **GET** /Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/{characterId}/Stats/Activities/ | 
*PreviewApi* | [**destiny2_get_clan_aggregate_stats**](docs/PreviewApi.md#destiny2_get_clan_aggregate_stats) | **GET** /Destiny2/Stats/AggregateClanStats/{groupId}/ | 
*PreviewApi* | [**destiny2_get_clan_leaderboards**](docs/PreviewApi.md#destiny2_get_clan_leaderboards) | **GET** /Destiny2/Stats/Leaderboards/Clans/{groupId}/ | 
*PreviewApi* | [**destiny2_get_destiny_aggregate_activity_stats**](docs/PreviewApi.md#destiny2_get_destiny_aggregate_activity_stats) | **GET** /Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/{characterId}/Stats/AggregateActivityStats/ | 
*PreviewApi* | [**destiny2_get_historical_stats**](docs/PreviewApi.md#destiny2_get_historical_stats) | **GET** /Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/{characterId}/Stats/ | 
*PreviewApi* | [**destiny2_get_historical_stats_for_account**](docs/PreviewApi.md#destiny2_get_historical_stats_for_account) | **GET** /Destiny2/{membershipType}/Account/{destinyMembershipId}/Stats/ | 
*PreviewApi* | [**destiny2_get_leaderboards**](docs/PreviewApi.md#destiny2_get_leaderboards) | **GET** /Destiny2/{membershipType}/Account/{destinyMembershipId}/Stats/Leaderboards/ | 
*PreviewApi* | [**destiny2_get_leaderboards_for_character**](docs/PreviewApi.md#destiny2_get_leaderboards_for_character) | **GET** /Destiny2/Stats/Leaderboards/{membershipType}/{destinyMembershipId}/{characterId}/ | 
*PreviewApi* | [**destiny2_get_unique_weapon_history**](docs/PreviewApi.md#destiny2_get_unique_weapon_history) | **GET** /Destiny2/{membershipType}/Account/{destinyMembershipId}/Character/{characterId}/Stats/UniqueWeapons/ | 
*PreviewApi* | [**destiny2_get_vendor**](docs/PreviewApi.md#destiny2_get_vendor) | **GET** /Destiny2/{membershipType}/Profile/{destinyMembershipId}/Character/{characterId}/Vendors/{vendorHash}/ | 
*PreviewApi* | [**destiny2_get_vendors**](docs/PreviewApi.md#destiny2_get_vendors) | **GET** /Destiny2/{membershipType}/Profile/{destinyMembershipId}/Character/{characterId}/Vendors/ | 
*PreviewApi* | [**destiny2_insert_socket_plug**](docs/PreviewApi.md#destiny2_insert_socket_plug) | **POST** /Destiny2/Actions/Items/InsertSocketPlug/ | 
*PreviewApi* | [**destiny2_search_destiny_entities**](docs/PreviewApi.md#destiny2_search_destiny_entities) | **GET** /Destiny2/Armory/Search/{type}/{searchTerm}/ | 
*TrendingApi* | [**trending_get_trending_categories**](docs/TrendingApi.md#trending_get_trending_categories) | **GET** /Trending/Categories/ | 
*TrendingApi* | [**trending_get_trending_category**](docs/TrendingApi.md#trending_get_trending_category) | **GET** /Trending/Categories/{categoryId}/{pageNumber}/ | 
*TrendingApi* | [**trending_get_trending_entry_detail**](docs/TrendingApi.md#trending_get_trending_entry_detail) | **GET** /Trending/Details/{trendingEntryType}/{identifier}/ | 
*UserApi* | [**user_get_available_themes**](docs/UserApi.md#user_get_available_themes) | **GET** /User/GetAvailableThemes/ | 
*UserApi* | [**user_get_bungie_net_user_by_id**](docs/UserApi.md#user_get_bungie_net_user_by_id) | **GET** /User/GetBungieNetUserById/{id}/ | 
*UserApi* | [**user_get_membership_data_by_id**](docs/UserApi.md#user_get_membership_data_by_id) | **GET** /User/GetMembershipsById/{membershipId}/{membershipType}/ | 
*UserApi* | [**user_get_membership_data_for_current_user**](docs/UserApi.md#user_get_membership_data_for_current_user) | **GET** /User/GetMembershipsForCurrentUser/ | 
*UserApi* | [**user_get_partnerships**](docs/UserApi.md#user_get_partnerships) | **GET** /User/{membershipId}/Partnerships/ | 
*UserApi* | [**user_get_user_aliases**](docs/UserApi.md#user_get_user_aliases) | **GET** /User/GetUserAliases/{id}/ | 
*UserApi* | [**user_search_users**](docs/UserApi.md#user_search_users) | **GET** /User/SearchUsers/ | 


## Documentation For Models



## Documentation For Authorization

 All endpoints do not require authorization.


## Author

support@bungie.com

