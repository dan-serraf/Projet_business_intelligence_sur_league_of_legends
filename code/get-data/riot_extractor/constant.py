"""
    URLS
"""

RIOT_URL_EUW1 = "https://euw1.api.riotgames.com"
RIOT_URL_BR1 = "https://br1.api.riotgames.com"
RIOT_URL_EUN1 = "https://eun1.api.riotgames.com"
RIOT_URL_JP1 = "https://jp1.api.riotgames.com"
RIOT_URL_KR = "https://kr.api.riotgames.com"
RIOT_URL_LA1 = "https://la1.api.riotgames.com"
RIOT_URL_LA2 = "https://la2.api.riotgames.com"
RIOT_URL_NA1 = "https://na1.api.riotgames.com"
RIOT_URL_OC1 = "https://oc1.api.riotgames.com"
RIOT_URL_RU = "https://ru.api.riotgames.com"
RIOT_URL_TR1 = "https://br1.api.riotgames.com"


EUROPE = "https://europe.api.riotgames.com"
ASIA = "https://asia.api.riotgames.com" 
AMERICAS = "https://americas.api.riotgames.com"

RIOT_SERVER = {
    "euw1" : (RIOT_URL_EUW1, EUROPE), 
    "br1" : (RIOT_URL_BR1, AMERICAS), 
    "eun1" : (RIOT_URL_EUN1, EUROPE), 
    "jp1" : (RIOT_URL_JP1, ASIA), 
    "kr1" : (RIOT_URL_KR, ASIA), 
    "la1" : (RIOT_URL_LA1, AMERICAS), 
    "la2" : (RIOT_URL_LA2, AMERICAS), 
    "us1" : (RIOT_URL_NA1, AMERICAS),  # to avoid nan we use US
    "oc1" : (RIOT_URL_OC1, AMERICAS), 
    "ru1" : (RIOT_URL_RU, EUROPE), 
    "tr1" : (RIOT_URL_TR1, EUROPE)
}



# PUUID_ENDPOINT : information regarding the user's account
SUMM_ENDPOINT = "/lol/summoner/v4/summoners/by-name/"#{summoner_name}
PUUID_ENDPOINT = "/lol/summoner/v4/summoners/by-account/"#{encryptedAccountId}
# MATCH_ENDPOINT : list of match ids
MATCH_ENDPOINT = "/lol/match/v5/matches/by-puuid/" #{puuid}/idsGet
# MATCH_DETAIL_ENDPOINTS : a game's details
MATCH_DETAIL_ENDPOINTS = "/lol/match/v5/matches/" #{matchId}
# MACH_DETAIL_TIMELINE : a game's timeline info 
MATCH_DETAIL_TIMELINE = "/lol/match/v5/matches/" #{matchId}/timelineGet

API_TOKEN = "RGAPI-2fc4a88a-175a-4c59-9d8a-17f58c56ddf3"

HEADERS = {
    "X-Riot-Token" : API_TOKEN
}


