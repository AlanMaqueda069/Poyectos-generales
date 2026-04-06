from supabase import create_client
from app.core.config import config
from typing import Any

def get_supabase() -> Any:
    return create_client(config.supabase_url, config.supabase_key)