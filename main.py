import pandas as pd
import os
from config import Hyper
from sentiment import Sentiment
from helper import Helper

'''
    This program is the third in a suite of programs to be executed in this order
    1/ App - gets tweets from Twitter API
    2/ Location - gets the country of the tweet from user location
    3/ Annotate - calculates the sentiment of each tweet
    4/ Wordcload - shows the words most in use in tweets from different countries
    5/ Datapreparation - gets the data in the correct form
    6/ Transformer - builds a transformer model from the tweets
'''
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
        save_csv(csv_input, sent, Hyper.HyrdatedTweetFile)
        Helper.printline(f"Country: {i}. {country} saving {len(csv_input)} entries")
        facemask_perc = Helper.get_perc(sum(sent.is_facemask), len(csv_input))
        Helper.printline(f"Number of facemask comments are {sum(sent.is_facemask)} which is {facemask_perc}%")
        lockdown_perc = Helper.get_perc(sum(sent.is_lockdown), len(csv_input))
        Helper.printline(f"Number of lockdown comments are {sum(sent.is_lockdown)} which is {lockdown_perc}%")
        vax_perc = Helper.get_perc(sum(sent.is_vaccine), len(csv_input))
        Helper.printline(f"Number of vaccination comments are {sum(sent.is_vaccine)} which is {vax_perc}%")    
    Helper.printline("    Finished")

def save_csv(csv_input, sent, file):
    if Hyper.is_data_clean:
        csv_input["clean_text"] = sent.clean_text
    csv_input["s_pos"] = sent.pos
    csv_input["s_neu"] = sent.neu
    csv_input["s_neg"] = sent.neg
    csv_input["s_compound"] = sent.com
    csv_input["sentiment"] = sent.sent
    csv_input["is_facemask"] = sent.is_facemask
    csv_input["is_lockdown"] = sent.is_lockdown
    csv_input["is_vaccine"] = sent.is_vaccine
    csv_input.query(f"sentiment < {sent.NEUTRAL}", inplace=True)
    csv_input.to_csv(file) 
    
def get_country_dir(i, country):
    if i == 1:
        return country
    
    return f"../{country}"


if __name__ == "__main__":
    main()