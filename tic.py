from telethon.sync import TelegramClient

api_id = YOUR_API_ID
api_hash = 'YOUR_API_HASH'

with TelegramClient('session_name', api_id, api_hash) as client:
    dialogs = client.get_dialogs()

    print("Liste des canaux :")
    for dialog in dialogs:
        if dialog.is_channel:
            print(f"Nom : {dialog.name}, Identifiant : {dialog.id}")