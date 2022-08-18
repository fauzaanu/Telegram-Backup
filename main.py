from Telegram_Backup import Backup



if __name__ == "__main__":
    t_id = '1234'
    t_hash = 'example_hash'

    personal_docs = Backup('upload', api_id=t_id, api_hash=t_hash)
    personal_docs.back_all(silent=True)
