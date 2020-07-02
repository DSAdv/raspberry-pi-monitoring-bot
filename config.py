import os
import dotenv

dotenv.load_dotenv()

IP_STACK_ACCESS_KEY: str = os.environ.get("IP_STACK_ACCESS_KEY")
OPEN_WEATHER_ACCESS_KEY: str = os.environ.get("OPEN_WEATHER_ACCESS_KEY")