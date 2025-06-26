from fastapi import APIRouter
import random
import string
from supabase import create_client
from fastapi.responses import RedirectResponse

supabase_url = "https://lymdncfrgljnlkozuvxl.supabase.co"
supabase_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imx5bWRuY2ZyZ2xqbmxrb3p1dnhsIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTA1MTA5MjQsImV4cCI6MjA2NjA4NjkyNH0.okDaMSFSxxc09jvtckUHpPwxolItOH8AvTwE4nuH5q8"

db = create_client(supabase_url,supabase_key)

router = APIRouter()

def create_short_phrase(length):
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
    return random_string

@router.post("/shorten")
def shorten_url(long_url):
    phrase = create_short_phrase(length=7)
    result = db.table("shorten_url").insert({
        'long_url':long_url,
        'short_phrase':phrase
    }).execute()
    return "http://127.0.0.1:8000/"+ result.data[0]['short_phrase']

@router.get("/{short_phrase}")
def redirect_url(short_phrase):
    result_1 = db.table("shorten_url").select('long_url').eq("short_phrase",short_phrase).execute()
    return RedirectResponse(result_1.data[0]["long_url"])

