import neattext.functions as nfx
import re
from config import Constants

class DataCleaner:
    # Data cleaning methods taken from https://www.kaggle.com/friskycodeur/nlp-with-disaster-tweets-bert-explained
    # Also refer to how the Vader library calculates sentiment analysis 
    # https://medium.com/analytics-vidhya/simplifying-social-media-sentiment-analysis-using-vader-in-python-f9e6ec6fc52f
    def lowercase_text(text):
        # The token id for a word should be the same whether it is capitalised or not
        # To ensure this happens, make the word lowercase
        # However Vader takes into account letter casing for sentiment, and it is possible to use a cased model for Bert.
        # So on balance, best not to use this method
        # 
        return text.lower()

    def remove_noise(text):
        text = nfx.remove_html_tags(text)
        # Replace User handles with the <USER> token. 
        # This can keep the context of using a user handle, but we do not need to know what it is.
        text = re.sub(Constants.USER_HANDLES_REGEX, "<USER>", text)
        text = nfx.remove_urls(text)
        text = nfx.remove_multiple_spaces(text)
        text = re.sub(Constants.NEW_LINE, " ", text)     # remove /n
        text = nfx.remove_non_ascii(text)
        return text