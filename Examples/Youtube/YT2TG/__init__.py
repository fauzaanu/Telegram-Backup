import os
from pytube import Channel, YouTube, Playlist, Search
from pytube.exceptions import RegexMatchError

import Telegram_Backup
import shutil

# G
linwin_sep = os.sep


class YT2TG:
    def __init__(self, channel_name, channel_link, api_key, hash, limit=2, root='uploads', force_id=0):
        self.channel = channel_name
        self.root = root
        self.limit = limit  # does nothing as of now
        self.search_mode = []

        self.api_key = int(api_key)
        self.hash = hash

        # trying to speed up the asking for number and code
        print("initializing... Phone number and code will be asked now")
        self.thisdir = os.getcwd()
        self.backup_obj = Telegram_Backup.Backup(f'{self.thisdir}{linwin_sep}{self.root}', api_id=self.api_key,
                                                 api_hash=self.hash)

        try:
            if "/videos" in channel_link:
                self.all_vids = Channel(channel_link).video_urls
            elif "/playlist" in channel_link:
                self.all_vids = Playlist(channel_link).video_urls

            elif isinstance(channel_link,list):
                print(isinstance(channel_link,list))
                for search_term in channel_link:
                    yt_objs = Search(search_term).results
                    for yt_object in yt_objs:
                        self.search_mode.append(yt_object)
                self.all_vids = self.search_mode

            else:
                print("Your link cannot be recognized. /videos or /playlist must be present on the link")
                return
        except RegexMatchError:
            print("Regex Match Error")
            return

        self.channel_id = 0

        if force_id != 0:
            print("A channel ID was force. A new channel will not be created")
            self.channel_id = force_id

        # when making things persistent use this: now persistence should be manual by passing force_id
        # self.object_data = {
        # "channel_id": "",
        # "all_links": [],
        # "posted_links": [],
        # "error_links": [],
        # }

        try:
            # folder structure

            try:
                print("Creating Directories")
                os.mkdir(f'{self.thisdir}{linwin_sep}{self.root}')
                os.mkdir(f'{self.thisdir}{linwin_sep}{self.root}{linwin_sep}{self.channel}')
            except FileExistsError:
                print("We got file exist error. Continuing..")

            for video_url in self.all_vids:
                output_dir = f'{self.thisdir}{linwin_sep}{self.root}{linwin_sep}{self.channel}{linwin_sep}'
                # ENSURE THAT NO FILES ARE PRESENT ON THE PROCESS START
                print(f"Amount of Files inside {output_dir} is {len(os.listdir(output_dir))}")
                if len(os.listdir(output_dir)) > 0:
                    print("Cleaning dir")
                    shutil.rmtree(output_dir)
                    os.makedirs(output_dir)
                    print(f"Amount of Files inside {output_dir} is {len(os.listdir(output_dir))}")

                try:
                    if len(self.search_mode) == 0:
                        yt = YouTube(video_url)
                    else:
                        yt = video_url



                    banned_chars = ["!", "?", "-", ":", "|", " ", "<", ">", ":", '"', '/', '\\', "+", "&", "^", "="]

                    video_name = str(yt.title)
                    for char in banned_chars:
                        video_name = video_name.replace(char, "_")

                    # YouTube Download
                    print(f"Begginign download of {video_url} as {video_name}")
                    saved_file = yt.streams.get_highest_resolution().download(
                        output_path=output_dir,
                        filename=f'main.mp4')
                    print(f"Youtube Downloading complete {saved_file}")

                    # Renaming file with name
                    print(f"Re-naming {saved_file} to {video_name}")
                    os.rename(saved_file,
                              f'{output_dir}{video_name}.mp4')

                    # Upload process
                    try:
                        # ensure that only 1 file is present
                        if len(os.listdir(output_dir)) == 1:
                            print("Backup is starting only 1 file is present")
                            self.channel_id = self.backup_obj.back_all(silent=True, channel_id=self.channel_id)
                            print(self.channel_id)
                        else:
                            print("More than one file found. Breaking script")
                            break
                    except ValueError:
                        print("We are getting channel not found error")
                        break

                except Exception as e:
                    print(e)
                    continue

            # END OF LOOP
            print("End of the main process reached. Cleaning up")
            shutil.rmtree(f'{self.thisdir}{linwin_sep}{self.root}{linwin_sep}{self.channel}')

        except Exception as e:
            print(e)

            # remove the root on interrupt - because it would have corrupt files in some cases
            shutil.rmtree(f'{self.thisdir}{linwin_sep}{self.root}')

        # END OF PROGRAM
        finally:
            # remove the root anyway..
            print("End of the main process reached. Cleaning up final")
            shutil.rmtree(f'{self.thisdir}{linwin_sep}{self.root}')
