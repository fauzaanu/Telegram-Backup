# Telegram Backup

Telegram has an unlimited cloud file storage.
The limit however is a per file limit which is 2GB for normal users & 4GB for premium users. So Telegram seems to be a good place to backup files. & This is a tool to do just that.

## Telethon is used
A user account is used because Bots have limits and users dont. And premium users get extra 2GB while there isnt anything like a premium bot yet. Telethon seems to achieve this fairly easily.

## Structure of main script
The script will first look into a ROOT directory. This directory is defined by the user. In this case this ROOT directory is called 'upload'.

### ROOT / folder
- Every Folder in the ROOT is a new telegram Channel.
- DONT KEEP FILES OUTSIDE OF A FOLDER ON ROOT THEY WILL BE IGNORED

### Root / folder / Subfolder
* Subfolders inside them are going to be described in the telegram channel as a directory. 
* The Folder layout gets sent along with a directory emoji. 
Example: 📂 personal docs\
* In some cases sending the directory is not needed and in those cases silence = True must be sent.
* Example:
  * t_id is a variable holding the API_ID
  * t_hash is a variable holding the API_HASH
  * Both needs to be obtained by logging into [my.telegram.org](https://my.telegram.org)
  * 'upload' is referring to the ROOT

```python
from Telegram_Backup import Backup

if __name__ == "__main__":
    t_id = '1234'
    t_hash = 'example_hash'

    personal_docs = Backup('upload', api_id=t_id, api_hash=t_hash)
    personal_docs.back_all(silent=True)
    
   ```

### Root / folder / Files.extention
* Any file within any directory will be sent to the telegram channel with a caption of the folder structure. 
* This way it will be easy to navigate within the channel to know which file is inside where.

### TODO:
* [ ] auto generate a folder structure image with code and send that to the channel at the end of the channel processes.
* [ ] make it ready for windows, to keep running on the background
  * [ ] Introduce a snail mode to allow users to get a normal connection while big uploads happen on the background
* [ ] Corrupt file detection: if corrupt we should delete it
* [ ] BUG: Files inside root are not detected. (outside of any folder): script has no idea where to back them up.

### Examples:
#### YT2TG - Copies the full content of a Youtube channel to a telegram channel
   * Functional but needs improvement..
   * Sample: 
      * [Dharus Library Youtube](https://www.youtube.com/c/DharusLibrary/) copies to [t.me/dhivehidharus](https://t.me/dhivehidharus)
      * [James Vietch](https://www.youtube.com/c/jamesveitch/) copied to [t.me/jamesveitch](https://t.me/jamesveitch)
   *
   * [ ] Cleaning up on keyboard interrupt
   * [ ] instead of deleting files - Delete directory?
   * [ ] Ban more characters from file names to work better on all systems
   * [ ] Channels should be able to pick up from where things ended
     * [ ] Store the links list, update their status, output to a txt file as a dictionary with channel id
   * [ ] Pytube sometimes raises a regex error for a minority of videos. Need a work around.

#### Index CDU - A script to crawl 'index of' sites with different keywords
* [ ] we would need proxies
* [ ] where do the keywords come from? Search for API's involved with names names or use a JSON/TXT file already built
* [ ] download files, upload files, detect capthca screen, switch proxies, keep running

#### Libraries Currently being used
* pytube
* Telethon
* moviepy
* cryptg
* pillow
* hachoir







