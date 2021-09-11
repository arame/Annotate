import re

class Hyper:
    time = "2021_08_08 22_58_57"
    version = 15
    language = "en"
    HyrdatedTweetLangDir = f"../Summary_Details_files{time}/{language}"
    HyrdatedTweetFile = "tweets.csv"
    HyrdatedTweetLangFile = f"{language}_tweets.csv"
    is_data_clean = False
    is_vaccine_included = True
    
class Constants:
    USER_HANDLES_REGEX = re.compile(r"@\S+")
    NEW_LINE = re.compile(r'\s+|\\n')