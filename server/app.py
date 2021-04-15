from dotenv import load_dotenv

from src.web import create_app

load_dotenv()

app = create_app()
