from YT2TG import YT2TG

if __name__ == "__main__":

    # API KEYS
    key = 1234
    hash = '1234'

    # CHANNELS
    channels = {
        "IBU": ('https://www.youtube.com/playlist?list=PLmhEztcg6lpBNsiW65VZchXljxLBq-Ie6', 0),
    }



    # channels['key'][0] means channel link
    # channels['key'][1] means channel id

    # THE ACT
    for channel_name, channel_link in channels.items():
        YT2TG(channel_name, channel_link[0], key, hash, limit=1, root='uploads', force_id=channel_link[1])
