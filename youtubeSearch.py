# -*- coding: utf-8 -*-

# Based on sample Python code for youtube.search.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/code-samples#python

# To get Google's API Key from .env file
from dotenv import load_dotenv

import os

import googleapiclient.discovery
import googleapiclient.errors

def song_search(song_title):
    # Loads .env variables (API Keys)
    load_dotenv()

    # Gets Youtube API key from .env
    YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")

    api_service_name = "youtube"
    api_version = "v3"

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=YOUTUBE_API_KEY)

    request = youtube.search().list(
        part="snippet",
        channelType="any",
        maxResults=1,
        q=song_title,
        order="relevance",
        safeSearch="moderate",
        type="video",
        videoCaption="any",
        videoDefinition="any",
        videoDimension="any",
        videoDuration="any",
        videoEmbeddable="true",
        videoLicense="any",
        videoPaidProductPlacement="any",
        videoSyndicated="any",
        videoType="any"
    )
    response = request.execute()

    # Organized into a list with a list called items with data fields "snippet", "medium", "high"
    # Iterates over every element in "items" to find the title, and video id
    for item in response["items"]:
        title = item["snippet"]["title"]
        video_id = item["id"]["videoId"]

    # Video URL Format is "https://www.youtube.com/watch?v=" + video_id
    video_url = f"https://www.youtube.com/watch?v={video_id}"

    return video_url