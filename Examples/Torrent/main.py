from YT2TG import YT2TG

if __name__ == "__main__":

    # API KEYS
    key = 1234
    hash = '1234'

    # CHANNELS
    # to search pass a list inside where a link is normally at, the search terms will be collected to the channel
    channels = {
        #"apple": ('__link__', 0),
        'Maldives': (["Maldives vlog", "vlog maldives", "Trip to Maldives"], 0)
    }


    # THE ACT
    for channel_name, channel_link in channels.items():
        YT2TG(channel_name, channel_link[0], key, hash, limit=1, root='uploads', force_id=channel_link[1])
