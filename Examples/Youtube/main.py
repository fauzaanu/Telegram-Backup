from YT2TG import YT2TG

if __name__ == "__main__":

    # API KEYS
    key = 123
    hash = '4564'

    # CHANNELS
    channels = {
        "Apple": 'https://www.youtube.com/c/CusterPlays/videos',
    }

    # THE ACT
    for channel_name, channel_link in channels.items():
        YT2TG(channel_name, channel_link, key, hash, limit=1, root='uploads')
