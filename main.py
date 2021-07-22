import pandas as pd
import os
import time
from config import Hyper
from sentiment import Sentiment


# Create the sentiment columns on the tweet files
# See https://stackoverflow.com/questions/11070527/how-to-add-a-new-column-to-a-csv-file
def main():
    curr_dir = os.getcwd()
    _date_time = time.strftime('%Y/%m/%d %H:%M:%S')
    print(f"Started at {_date_time}")
    print(f"Current directory: {curr_dir}")
    dir = Hyper.HyrdatedTweetLangDir
    os.chdir(dir)
    print(f"Changed directory to {dir}")
    list_dirs = os.listdir()
    sent = Sentiment()
    i = -1
    for country in list_dirs:
        if country.endswith("csv"):
            continue

        if country == "no_country":
            continue
        _time = time.strftime('%H:%M:%S')
        print(f"{_time} Country: {country}")
        i += 1
        country_dir = get_country_dir(i, country)
        os.chdir(country_dir)
        csv_input = pd.read_csv(Hyper.HyrdatedTweetFile, sep=',', error_bad_lines=False, index_col=False, dtype='unicode')
        sent.get(csv_input)
        csv_input["s_pos"] = sent.pos
        csv_input["s_neu"] = sent.neu
        csv_input["s_neg"] = sent.neg
        csv_input["s_compound"] = sent.com
        csv_input["sentiment"] = sent.sent
        csv_input.to_csv(Hyper.HyrdatedTweetFile)
    
    _date_time = time.strftime('%Y/%m/%d %H:%M:%S')
    print(f"Finished at {_date_time}")

def get_country_dir(i, country):
    if i == 0:
        return country
    
    return f"../{country}"


if __name__ == "__main__":
    main()