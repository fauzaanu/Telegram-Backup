import glob
from telethon.sync import TelegramClient
import os
from telethon.tl import functions
from moviepy.video.io.VideoFileClip import VideoFileClip


linux_windows = os.sep
class Backup:
    def __init__(self, root_folder, api_id, api_hash):
        pass

        # API STUFF
        self.api_id = int(api_id)
        self.api_hash = str(api_hash)
        self.client = TelegramClient('folder_uploader', api_id, api_hash)

        # EMOJI STUFF
        self.folder_emoji = "📂"
        self.file_emoji = "📄"
        self.media_emoji = "🎬"

        # ROOT FOLDER
        self.root = root_folder

    def back_all(self, silent=False, channel_id=0):
        for directory in os.listdir(self.root):
            if 1 == 2:
                pass
            # this protection is clearly not working: need to know why
            # print(os.path.isdir(f'{os.getcwd()}//{self.root}//{directory}//main.txt'))
            # if not os.path.isdir(f'{os.getcwd()}//{self.root}//{directory}'):
            #     print(directory,'NON Directory FIle present inside the uploads. This file will be ignored!')
            else:
                if channel_id == 0:
                    channel_id = self.create_channel(directory)
                with open("../channels_log.txt", "w") as file:
                    file.close()
                    pass
                with open("../channels_log.txt", "a") as file:
                    file.write(f'{directory},{channel_id} \n')
                if silent:
                    self.upload(directory, channel_id, silent=True)
                else:
                    self.upload(directory, channel_id, silent=False)
        return channel_id

    def create_channel(self, channel_name):
        # let's start the main process
        with self.client as clientx:
            result = clientx(functions.channels.CreateChannelRequest(
                title=channel_name,
                about='An autogenerated channel via a script',
                megagroup=None,
                for_import=None,
                # geo_point=types.InputGeoPoint(
                #     lat=7.13,
                #     long=7.13,
                #     accuracy_radius=42
                # ),
                address=None
            ))
            data = result.to_dict()
            return data['updates'][1]['channel_id']  # channel_id of created channel

    def upload(self, folder, channel_id, silent):
        # if the folder is not present we should report an error
        root = self.root
        if folder not in os.listdir(root):
            print('error')
            return 'error'

        # if folder is present then lets go ahead
        else:
            for filename in glob.iglob(f'{root}{linux_windows}{folder}{linux_windows}**', recursive=True):

                print(filename)
                pretty_filename = str(filename).replace(f'{root}{linux_windows}', '')

                if os.path.isdir(filename):
                    if not silent:
                        with self.client as clientx:
                            print(filename, "sending msg")
                            clientx.send_message(channel_id, f"```{self.folder_emoji} {pretty_filename}```")

                else:
                    if 'mp4' in filename:
                        emoji = self.media_emoji
                        self.generate_thumb(filename,"thumb.png")
                    else:
                        emoji = self.file_emoji

                    with self.client as clientx:
                        print(filename, "sending file")
                        if 'mp4' in filename:
                            clientx.send_file(channel_id, filename, supports_streaming=True, force_document=False,
                                              caption=f"```{emoji} {pretty_filename}```", thumb = 'thumb.png')
                        else:
                            clientx.send_file(channel_id, filename, supports_streaming=True, force_document=False,
                                              caption=f"```{emoji} {pretty_filename}```")
                        os.remove('thumb.png')

    def clean(self):
        """
        cleans the root folder

        :return:
        """
        pass
        # remove the directory - this cleaning up should be present in the backup
        # os.rmdir(f'{thisdir}{linux_windows}{self.root}{linux_windows}{self.channel}')

    def generate_thumb(self,clip,save_location):
        with VideoFileClip(f"{clip}") as clip:
            clip.save_frame(f"{save_location}", t=10)
