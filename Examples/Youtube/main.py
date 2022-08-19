from YT2TG import YT2TG

if __name__ == "__main__":

    # API KEYS
    key = 1234
    hash = '1234'

    # CHANNELS
    channels = {
        "Apple": ('https://www.youtube.com/c/CusterPlays/videos', 0),
    }

    # channels['key'][0] means channel link
    # channels['key'][1] means channel id

    # THE ACT
    for channel_name, channel_link in channels.items():
        YT2TG(channel_name, channel_link[0], key, hash, limit=1, root='uploads', force_id=channel_link[1])
