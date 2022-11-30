# (c) @AbirHasan2005

import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", 17189115))
    API_HASH = os.environ.get("API_HASH", ad6127f6f268f1570e71816fe8d4b337)
    STRING_SESSION = os.environ.get("STRING_SESSION", "BABb62y3Ho97oz_Dsc39zJx3NJ0HSCSu8qIRZwkapE8fKSh2jMqhcttGfjK4eciBva4JJOBfGjJEtGkqt9J0Qr1iaQ0f0S8E81RJzeYhzMenFHTdfH7896HoO5EwCLihEsGCR2hNGgzTsVfUJZzpSyMEG83o6gczQMUN426QUQUP-zsb5XVYOfigqwpgTgsjcmr3Clrvy1sbxLndua9gNTNWVxBkxB0qAjlRUOVaUVn-Ccfc2wViFqi-_cNfg5hJondZVgeoZm5cAsZFx1FuITKNmkrOAhtlHpGeeMR--0_aoWj6pAi0Y6OPRE4j1ON3gqLoJ6MoPhbAP71jWwDUk74WfaTslgA")
    DB_CHANNEL_ID = int(os.environ.get("DB_CHANNEL_ID", -100))
    FORCE_SUB_CHANNEL = os.environ.get("FORCE_SUB_CHANNEL", None)
    MONGODB_URI = os.environ.get("MONGODB_URI", "mongodb+srv://dragon:t.me.yy8gg@dragon.7v7baed.mongodb.net/mohamed?retryWrites=true&w=majority")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5559194720:AAEgixceQWufCQ2o0oxWIkHW6CeHZokFJ_A")
    DEFAULT_BLOCKED_EXTENSIONS = "srt txt jpg jpeg png torrent html aio pdf"
    BLOCKED_EXTENSIONS = list(set(x for x in os.environ.get("BLOCKED_EXTENSIONS", DEFAULT_BLOCKED_EXTENSIONS).split()))
