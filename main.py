import pandas as pd
import os
from config import Hyper
from sentiment import Sentiment
from helper import Helper


# Create the sentiment columns on the tweet files
# See https://stackoverflow.com/questions/11070527/how-to-add-a-new-column-to-a-csv-file
def main():
    curr_dir = os.getcwd()
    Helper.printline("   Started")
    Helper.printline(f"Current directory: {curr_dir}")
    dir = Hyper.HyrdatedTweetLangDir
    os.chdir(dir)
    Helper.printline(f"Changed directory to {dir}")
    list_dirs = Helper.list_country_folders()
    sent = Sentiment()
    i = 0
    Helper.printline(f"Iterate through {len(list_dirs)} countries")
    for country in list_dirs:
        i += 1
        country_dir = get_country_dir(i, country)
        os.chdir(country_dir)
        csv_input = pd.read_csv(Hyper.HyrdatedTweetFile, sep=',', error_bad_lines=False, index_col=False, dtype='unicode')
        csv_input = csv_input.drop_duplicates()     # remove duplicate tweets
        sent.get(csv_input)
        csv_input["s_pos"] = sent.pos
        csv_input["s_neu"] = sent.neu
        csv_input["s_neg"] = sent.neg
        csv_input["s_compound"] = sent.com
        csv_input["sentiment"] = sent.sent
        csv_input = csv_input.drop(csv_input.query(f'sentiment=={sent.NEUTRAL}').index)
        Helper.printline(f"Country: {i}. {country} saving {len(csv_input)} entries")
        csv_input.to_csv(Hyper.HyrdatedTweetFile)
    
    Helper.printline("    Finished")

def get_country_dir(i, country):
    if i == 1:
        return country
    
    return f"../{country}"


if __name__ == "__main__":
    main()