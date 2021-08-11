import pandas as pd
import os
from more_itertools import locate
from pandas.core.frame import DataFrame
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
        csv_input = csv_input.drop(csv_input.query(f'sentiment=={sent.NEUTRAL}').index)
        save_csv(sent, Hyper.HyrdatedTweetFile)
        Helper.printline(f"Country: {i}. {country} saving {len(csv_input)} entries")
        facemask_perc = Helper.get_perc(sum(sent.is_facemask), len(csv_input))
        Helper.printline(f"NUmber of facemask comments are {sum(sent.is_facemask)} which is {facemask_perc}%")
        lockdown_perc = Helper.get_perc(sum(sent.is_lockdown), len(csv_input))
        Helper.printline(f"lockdown comments are {sum(sent.is_lockdown)} which is {lockdown_perc}%")
    
    Helper.printline("    Finished")

def save_csv(sent, file):
    df = DataFrame()
    df["s_pos"] = sent.pos
    df["s_neu"] = sent.neu
    df["s_neg"] = sent.neg
    df["s_compound"] = sent.com
    df["sentiment"] = sent.sent
    df["is_facemask"] = sent.is_facemask
    df["is_lockdown"] = sent.is_lockdown
    df.to_csv(file) 
    
def get_country_dir(i, country):
    if i == 1:
        return country
    
    return f"../{country}"


if __name__ == "__main__":
    main()