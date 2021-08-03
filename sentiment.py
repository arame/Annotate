from math import nan
import nltk
nltk.download("vader_lexicon")
from nltk.sentiment.vader import SentimentIntensityAnalyzer

class Sentiment:
    def __init__(self) -> None:
        self.POSITIVE = 1
        self.NEUTRAL = 9
        self.NEGATIVE = 0

    def get(self, csv_file):
        text_list = csv_file["English Tweet"].tolist()
        self.pos = []
        self.neu = []
        self.neg = []
        self.com = []
        self.sent = []
        self.count = 0
        self.prev_text = "N/A"
        for _text in text_list:
            self.calc(_text)
            self.pos.append(self.positive)
            self.neu.append(self.neutral)
            self.neg.append(self.negative)
            self.com.append(self.compound)
            self.sent.append(self._sentiment)

    def calc(self, text):
        self.count += 1
        self.text = text
        analyzer = SentimentIntensityAnalyzer()
        try:
            scores = analyzer.polarity_scores(self.text)
            self.positive = scores["pos"]
            self.negative = scores["neg"]
            self.neutral = scores["neu"]
            self.compound = scores["compound"]
            self._sentiment = self.get_sentiment()
            self.prev_text = text
        except:
            _t = str(text).encode('utf8')
            print(f"!! Data Error - row: {self.count}, text: {self.text}, previous text: {self.prev_text}")
            self.positive = 9
            self.negative = 9
            self.neutral = 9
            self.compound = 9
            self._sentiment = 9

    def get_sentiment(self):
        if self.positive == self.negative:
            return self.NEUTRAL    

        if self.positive > self.negative:
            return self.POSITIVE

        return self.NEGATIVE

    def print_results(self):
        print(f"\ntext: {self.text}")
        print(f"result positive sentiment = {self.positive}")
        print(f"result negative sentiment = {self.negative}")
        print(f"result neutral sentiment = {self.neutral}")
        print(f"result compound sentiment = {self.compound}")
        print(f"result sentiment = {self._sentiment}")
