import requests
import os
import concurrent.futures

'Utility class to use for multi-thread downloads of multiple webpages for scraping scripts '


class MutliDownloader:
    """__init__ takes a url as an input"""

    def __init__(self):
        self.url = None
        self.MAX_THREADS = 30
        self.path = os.getcwd()  # set path to current but can be set to whatever is needed

    def save_url_as_file(self, url):
        # print(url)
        resp = requests.get(url)

        # test to see the url returns a valid page and not a 404
        if resp.status_code == 200:
            # in the original script this .isnumeric tested for numbers as the page urls were contructed from retail items ids but
            # this can be tweaked to create whatever dynamic naming requirment is needed
            title = ''.join(x for x in url if x.isnumeric()) + ".html"

            with open(title, "wb") as fh:
                fh.write(resp.content)
        return


if __name__ == "__main__":
    downloader = MutliDownloader()

    urlList = []

    # Some kind of loop to create a list of urls to be downloaded
    # for something in something:
    #   urlist.append(url)

    threads = min(downloader.MAX_THREADS, len(urlList))

    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        executor.map(downloader.save_url_as_file, urlList)
