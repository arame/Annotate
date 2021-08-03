import time, os

class Helper:
    def printline(text):
        _date_time = time.strftime('%Y/%m/%d %H:%M:%S')
        print(f"{_date_time}   {text}")

    # This helper method is useful to get a list of the folders only and ignore any files
    def listfolders():
        return [x for x in os.listdir() if os.path.isdir(x)]

    def listcountryfolders():
        all_folders = Helper.listfolders()
        country_folders = all_folders.remove("no_country")
        return country_folders