from dotenv import load_dotenv
load_dotenv()

import os
from supabase import create_client, Client

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")

if not url or not key:
    raise Exception("SUPABASE_URL or SUPABASE_KEY is missing from environment variables.")

supabase: Client = create_client(url, key)
