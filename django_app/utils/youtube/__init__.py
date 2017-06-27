import requests
from apiclient.discovery import build
from apiclient.errors import HttpError
from django.db.models import options
from oauth2client.tools import argparser

from post.views import youtube_search


def search_original(q):
    url_api_search = 'https://www.googleapis.com/youtube/v3/search'
    search_params = {
        'part': 'snippet',
        'key': 'AIzaSyACCLlnn_hlOpNk5XUBpRqs-iZWpbTm-J4',
        'maxResults': '10',
        'type': 'video',
        'q': q,
    }
    # YouTube의 search api에 요청, 응답 받음
    response = requests.get(url_api_search, params=search_params)
    # 응답은 JSON형태로 오며, json()메서드로 파이썬 객체 형식으로 변환
    data = response.json()
    return data



# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.
DEVELOPER_KEY = "REPLACE_ME"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def search(q):
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)

  # Call the search.list method to retrieve results matching the specified
  # query term.
  search_response = youtube.search().list(
    q=options.q,
    part="id,snippet",
    maxResults=options.max_results
  ).execute()

  youtube = build(

  )

  # videos = []
  # channels = []
  # playlists = []
#
#   # Add each result to the appropriate list, and then display the lists of
#   # matching videos, channels, and playlists.
#   for search_result in search_response.get("items", []):
#     if search_result["id"]["kind"] == "youtube#video":
#       videos.append("%s (%s)" % (search_result["snippet"]["title"],
#                                  search_result["id"]["videoId"]))
#     elif search_result["id"]["kind"] == "youtube#channel":
#       channels.append("%s (%s)" % (search_result["snippet"]["title"],
#                                    search_result["id"]["channelId"]))
#     elif search_result["id"]["kind"] == "youtube#playlist":
#       playlists.append("%s (%s)" % (search_result["snippet"]["title"],
#                                     search_result["id"]["playlistId"]))
#
#   print "Videos:\n", "\n".join(videos), "\n"
#   print "Channels:\n", "\n".join(channels), "\n"
#   print "Playlists:\n", "\n".join(playlists), "\n"
#
#
# if __name__ == "__main__":
#   argparser.add_argument("--q", help="Search term", default="Google")
#   argparser.add_argument("--max-results", help="Max results", default=25)
#   args = argparser.parse_args()
#
#   try:
#     youtube_search(args)
#   except HttpError as e:
#     print "An HTTP error %d occurred:\n%s" % (e.resp.status, e.content)