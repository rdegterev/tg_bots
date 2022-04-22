import os


class Settings:
    # Telegram API configs
    TELEGRAM_API_TOKEN = os.getenv('TELEGRAM_API_TOKEN', default="5305064307:AAEqdMVGr6hQrhG_EPTwUhOpqJkZo7H4QUw")

    # TIMEOUTS block
    DROP_RUBY_STICK_TIMEOUT = int(os.getenv('SEND_CATS_TIMEOUT', 10))
    DROP_WORDLE_TIMEOUT = int(os.getenv('SEND_CATS_TIMEOUT', 900))

    # Admin IDs
    ADMINS_IDS = (334329237, 220120538)

    # REGEX block
    # CATS_REGEXP = os.getenv('CATS_REGEXP', "\^|[Уу]кра.н|$^|[Пп]олит|$^|[Пп]утин|$^|[Зз]еленс|$^|[Ээ]кономик|$^|[Нн][Аа][Тт][Оо]|$^|[Сс]анкц|$/")

    # DATABASE
    # DATABASE_URI = "postgresql://db_user:db_secreet_password@bot_db:5432/sorting_hat"
    DATABASE_URI = "postgresql://db_user:db_secreet_password@0.0.0.0:5441/sorting_hat"

