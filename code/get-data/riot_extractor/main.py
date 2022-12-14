from extractor import UserDataExtractor, MatchDataExtractor
from dataparser import GameParser
from config import *
import pandas as pd
import numpy as np



def extract_and_parse_match(
        summoner_name, 
        server, 
        user_extractor, 
        match_extractor, 
        game_parser,
        write_columns=False
    ):
    """
        given a summoner'name retrieve its matches as a dictionnary 
    """

    try: 
        summoner_payload = user_extractor.get_summoner_info(summoner_name, server)
        puuid = summoner_payload["puuid"]
    except Exception as e:
        print(f"Could not extract puuid for summoner : {summoner_name} with server : {server}")
        print("Following exception has been raised : ")
        print(e)
        print()
        return

    try: 
        print(f"---- retrieving matches for user : {summoner_name} ----")
        summoner_matches_payload = user_extractor.get_matches(puuid, server)
        matches = summoner_matches_payload
        print("---- Succesffuly retrieved matches ----", "\n")

    except Exception as e: 
        print(f"Could not retrieve matches with puuid : {puuid}")
        print("Following exception has been raised : ")
        # raise ValueError(e)
        print()
        return 
    
    for match_id in matches: 
        
        try: 
            print(f"---- retrieving match content for user : {summoner_name} ----")
            print(match_id)
            content_payload = match_extractor.retrieve_match_content(match_id, server)
            match_content = content_payload
            d_content = game_parser.preprocess_content(match_content, puuid)
            print("---- Succesffuly retrieved match content ----", "\n")
            # print(d_content.values())
            # write to csv
            if d_content is not None: 
                if write_columns: 
                    game_parser.write_into(d_content.keys())
                else: 
                    game_parser.write_into(d_content.values())    
            write_columns = False

        except Exception as e: 
            print(f"Could not retrieve matche with id : {match_id}")
            print("Following exception has been raised : ")
            # raise ValueError(e)
    


def main():
    
    pro_df = pd.read_csv(PRO_CSV_PATH)
    print(pro_df.head())
    nb_players = pro_df.shape[0]
    print(f"-----  Iterating over {nb_players} players -----", "\n")
    # extract data from api
    user_extractor = UserDataExtractor()
    # extract data from api 
    match_extractor = MatchDataExtractor() 
    # parse data for games
    game_parser = GameParser(filename=MATCH_CSV_PATH)
    # parse data for players 
    
    players = pro_df["name"].tolist()
    summoners = pro_df["summoner_names"].tolist()
    servers = pro_df["server"].tolist()    

    write_columns = True
    
    for i, player in enumerate(players, 791):

        summs = eval(summoners[i])
        
        server = servers[i]
        print("FETCHING FOR SERVER : ", server)
        for j, summoner_name in enumerate(summs): 
            
            # add columns for the first summoner name 
            extract_and_parse_match(
                summoner_name, 
                    server, 
                    user_extractor, 
                    match_extractor, 
                    game_parser,
                    write_columns=write_columns
            )
            write_columns = False



    # iterating over summoner names
    





    # d_puuid = user_extract.get_user_info("eK-5G4INu5yvmAbQmxHkS3gSdan6EUCzfZ9dS0EbJCmlawM")
    # puuid = d_puuid["puuid"]
    # matches = user_extract.get_matches(puuid)
    # content = match_extractor.retrieve_match_content(matches[0])

    # d_content = player_parser.preprocess_content(content, puuid)
    # print(d_content)
    # player_parser.write_into(d_content.keys())



if __name__ == "__main__": 
    main()