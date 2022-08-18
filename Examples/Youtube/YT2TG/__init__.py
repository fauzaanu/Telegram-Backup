import os
from pytube import Channel, YouTube
import Telegram_Backup

linux_windows = os.sep


# Default limit is 2: You might want to change that
class YT2TG:
    def __init__(self, channel_name, channel_link, api_key, hash, limit=2, root='uploads'):
        self.channel = channel_name
        self.all_vids = Channel(channel_link).video_urls
        self.root = root
        self.limit = limit  # does nothing now

        try:
            # folder structure
            thisdir = os.getcwd()
            try:
                os.mkdir(f'{thisdir}{linux_windows}{self.root}')
                os.mkdir(f'{thisdir}{linux_windows}{self.root}{linux_windows}{self.channel}')
            except FileExistsError:
                pass

            self.api_key = int(api_key)
            self.hash = hash

            # variable to hold channel_id
            # modify this to continue to same channel
            self.channel_id = 0

            vackup_obj = Telegram_Backup.Backup(f'{thisdir}{linux_windows}{self.root}', api_id=self.api_key,
                                                api_hash=self.hash)

            # downloading videos

            for video_url in self.all_vids:
                try:
                    yt = YouTube(video_url)

                    banned_chars = ["!", "?", "-", ":", "|", " ", "<", ">", ":", '"', '/', '\\', "+", "&", "^", "="]

                    video_name = str(yt.title)
                    for char in banned_chars:
                        video_name = video_name.replace(char, "_")

                    saved_file = yt.streams.get_highest_resolution().download(
                        output_path=f"{thisdir}{linux_windows}{self.root}{linux_windows}{self.channel}{linux_windows}",
                        filename=f'main.mp4')
                    # print(saved_file)
                    # if file already exists cannot go forward FIX THIS
                    os.rename(saved_file,
                              f'{thisdir}{linux_windows}{self.root}{linux_windows}{self.channel}{linux_windows}{video_name}.mp4')

                    self.channel_id = vackup_obj.back_all(silent=True, channel_id=self.channel_id)
                    print(self.channel_id)

                    os.remove(
                        f'{thisdir}{linux_windows}{self.root}{linux_windows}{self.channel}{linux_windows}{video_name}.mp4')
                except Exception as e:
                    print(e)
                    # some errors happening. Until they are properly addresssed we should continue loop
                    continue

            # clean up on exit
            os.rmdir(f'{thisdir}{linux_windows}{self.root}{linux_windows}{self.channel}')
        except KeyboardInterrupt:

            # remove the root on interrupt - because it would have corrupt files in some cases
            os.rmdir(f'{thisdir}{linux_windows}{self.root}')
