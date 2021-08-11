import time, os

class Helper:
    def printline(text):
        _date_time = time.strftime('%Y/%m/%d %H:%M:%S')
        print(f"{_date_time}   {text}")

    # This helper method is useful to get a list of the folders only and ignore any files
    def list_folders():
        return [x for x in os.listdir() if os.path.isdir(x)]

    def list_country_folders():
        country_folders = Helper.list_folders()
        country_folders.remove("no_country")
        return country_folders

    def get_perc(count, total):
        if total == 0:
            return 0
            
        return round((float(count) / float(total)) * 100, 2)