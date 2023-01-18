import datetime
import enum
import json
import logging
import random
import re
import string
import pandas as pd
from websocket import create_connection
import requests
from bs4 import BeautifulSoup
import json

logger = logging.getLogger(__name__)


class Interval(enum.Enum):
    in_1_minute = "1"
    in_3_minute = "3"
    in_5_minute = "5"
    in_15_minute = "15"
    in_30_minute = "30"
    in_45_minute = "45"
    in_1_hour = "1H"
    in_2_hour = "2H"
    in_3_hour = "3H"
    in_4_hour = "4H"
    in_daily = "1D"
    in_weekly = "1W"
    in_monthly = "1M"

def News_data_Gether():
    # Make a request to the Moneycontrol website and parse the HTML content
    url = "https://www.moneycontrol.com/indian-indices/bank-nifty-23.html"
    Main_page = requests.get(url)
    Main_page_soup = BeautifulSoup(Main_page.content, "html.parser")

    try:
        # Find the "See More" link and extract the href attribute
        link_for_see_more = Main_page_soup.find_all(
            "a", onclick="javascript:GAtabevent('See More','Market Live');", href=True)
        link_for_see_more = str(link_for_see_more[0])
        link_for_see_more_split = link_for_see_more.split('"')
    except:
        print("Not Found see more")
    # Find the index of the 'href=' string in the list
    Incre_ = 0
    for c in link_for_see_more_split:
        Incre_ += 1
        if " href=" == c:
            break

    # Construct the full URL of the page containing the data
    main_url = "https://www.moneycontrol.com"
    News_url = main_url + link_for_see_more_split[Incre_]

    # Make a request to the page and parse the HTML content
    News_page = requests.get(News_url)
    News_page_soup = BeautifulSoup(News_page.content, "html.parser")

    # Find the value of the 'tag_uri' input element and store it in a variable
    Data_for_date_id = News_page_soup.find("input", {"id": "tag_uri"}).get("value")

    # Construct the URL of the API endpoint that provides the data
    date_url = "https://liveblogapi.nw18.com/follow/web/getLiveBlogJson.php?tag=" + \
        Data_for_date_id + "&p=mc"

    # Make a request to the API endpoint and store the response
    Final_page = requests.get(date_url)
    Final_page_data = Final_page.text

    # Strip the parentheses from the response and load the JSON data
    Final_page_data = Final_page_data.lstrip("(")
    Final_page_data = Final_page_data.rstrip(")")
    Final_page_data_in_json = json.loads(Final_page_data)

    # Construct the URL of the API endpoint that provides the data for a specific time period
    front_URL = "https://liveblogapi.nw18.com/follow/web/getLiveBlogJson.php?tag=" + Data_for_date_id + \
        "&d=&classic=classic&p=mc&page=1&time=" + \
        Final_page_data_in_json["data"][0]["time"] + \
        "&d=pre&count=300&crossdomain=true"

    # print(front_URL)
    # Make a request to the API endpoint and store the response
    front_page = requests.get(front_URL)
    front_page_data = front_page.text

    # Strip the parentheses from the response and load the JSON data
    front_page_data = front_page_data.lstrip("(")
    front_page_data = front_page_data.rstrip(")")
    front_page_data_in_json = json.loads(front_page_data)

    # Initialize lists to store data
    time = []
    content = []
    data_path = []
    data_type = []
    image_path = []
    source = []
    title = []
    author_image = []
    author_name = []
    sticky = []
    type = []
    url = []

    # Loop through each data entry in front_page_data_in_json
    for i in range(front_page_data_in_json["count"]["count"]):
        # Check if the "source" field is present and append the value or "null" if not
        try:
            if not front_page_data_in_json["data"][i]["post"]["source"]:
                source.append("null")
            else:
                source.append(front_page_data_in_json["data"][i]["post"]["source"])
        except:
            source.append("null")

        try:    
            # Check if the "content" field is present and append the value or "null" if not
            if not front_page_data_in_json["data"][i]["post"]["content"]:
                content.append("null")
            else:
                content.append(front_page_data_in_json["data"][i]["post"]["content"])
        except:
            content.append("null")

        try:    
            # Check if the "data_path" field is present and append the value or "null" if not
            if not front_page_data_in_json["data"][i]["post"]["data_path"]:
                data_path.append("null")
            else:
                data_path.append(front_page_data_in_json["data"][i]["post"]["data_path"])
        except:
            data_path.append("null")

        try:
            # Check if the "data_type" field is present and append the value or "null" if not
            if not front_page_data_in_json["data"][i]["post"]["data_type"]:
                data_type.append("null")
            else:
                data_type.append(
                    front_page_data_in_json["data"][i]["post"]["data_type"])
        except:
            data_type.append("null")

        try:    
            # Check if the "image_path" field is present and append the value or "null" if not
            if not front_page_data_in_json["data"][i]["post"]["image_path"]:
                image_path.append("null")
            else:
                image_path.append(
                    front_page_data_in_json["data"][i]["post"]["image_path"])
        except:
            image_path.append("null")

        try:
            # Check if the "title" field is present and append the value or "null" if not
            if not front_page_data_in_json["data"][i]["post"]["title"]:
                title.append("null")
            else:
                title.append(front_page_data_in_json["data"][i]["post"]["title"])
        except:
            title.append("null")

        try:
            # Check if the "url" field is present and append the value or "null" if not
            if not front_page_data_in_json["data"][i]["post"]["url"]:
                url.append("null")
            else:
                url.append(front_page_data_in_json["data"][i]["post"]["url"])
        except:
            url.append("null")

        try:    
            # Check if the "author_image" field is present and append the value or "null" if not
            if not front_page_data_in_json["data"][i]["author_image"]:
                author_image.append("null")
            else:
                author_image.append(front_page_data_in_json["data"][i]["author_image"])
        except:
            author_image.append("null")

        try:    
            # Check if the "author_name" field is present and append the value or "null" if not
            if not front_page_data_in_json["data"][i]["author_name"]:
                author_name.append("null")
            else:
                author_name.append(front_page_data_in_json["data"][i]["author_name"])
        except:
            author_name.append("null")

        try:    
            # Check if the "sticky" field is present and append the value or "null" if not
            if not front_page_data_in_json["data"][i]["sticky"]:
                sticky.append("null")
            else:
                sticky.append(front_page_data_in_json["data"][i]["sticky"])
        except:
            sticky.append("null")

        try:    
            # Check if the "type" field is present and append the value or "null" if not
            if not front_page_data_in_json["data"][i]["type"]:
                type.append("null")
            else:
                type.append(front_page_data_in_json["data"][i]["type"])
        except:
            type.append("null")

        try:    
            # Check if the "time" field is present and append the value or "null" if not
            if not front_page_data_in_json["data"][i]["time"]:
                time.append("null")
            else:
                dt = datetime.datetime.strptime(
                    front_page_data_in_json["data"][i]["time"], "%Y%m%d%H%M%S")
                time.append(dt)
        except:
            time.append("null")

    Final_data_for_excel = {'time': time, 'content': content, 'data_path': data_path, 'data_type': data_type, 'image_path': image_path,
                            'source': source, 'title': title, 'author_image': author_image, 'author_name': author_name, 'sticky': sticky, 'type': type, 'url': url}

    df = pd.DataFrame(Final_data_for_excel)

    return df

    # df.to_excel('CarsData1.xlsx', index=False)

    # https://www.moneycontrol.com/news/business/markets/share-market-live-updates-stock-market-today-january-6-latest-news-bse-nse-sensex-nifty-covid-coronavirus-market-live-updates-sgx-nifty-negative-start-fomc-minutes-fed-powell-coal-godrej-consumer-rvnl-9819391.html

    # https://liveblogapi.nw18.com/follow/web/getLiveBlogJson.php?tag=marketlive_jan_06012023_63b77fe6f027c&d=&classic=classic&p=mc&page=1&time=20230106150141&d=pre&count=30&jsonp_callback=callbackjson_normal&crossdomain=true

    # https://liveblogapi.nw18.com/follow/web/getLiveBlogJson.php?tag=marketlive_jan_06012023_63b77fe6f027c&d=&classic=classic&p=mc&page=1&time=20230106161312&count=30&jsonp_callback=callbackjson_normal&crossdomain=true

    # https://liveblogapi.nw18.com/follow/web/getLiveBlogJson.php?timeframe=&tag=marketlive_jan_06012023_63b77fe6f027c&d=&classic=classic&p=mc&page=1&time=20230106161312&count=30&jsonp_callback=callbackjson_normal&crossdomain=true

    # https://liveblogapi.nw18.com/follow/web/getLiveBlogJson.php?tag=marketlive_jan_06012023_63b77fe6f027c&p=mc

class TvDatafeed:
    __sign_in_url = 'https://www.tradingview.com/accounts/signin/'
    __search_url = 'https://symbol-search.tradingview.com/symbol_search/?text={}&hl=1&exchange={}&lang=en&type=&domain=production'
    __ws_headers = json.dumps({"Origin": "https://data.tradingview.com"})
    __signin_headers = {'Referer': 'https://www.tradingview.com'}
    __ws_timeout = 5

    def __init__(
        self,
        username: str = None,
        password: str = None,
    ) -> None:
        """Create TvDatafeed object

        Args:
            username (str, optional): tradingview username. Defaults to None.
            password (str, optional): tradingview password. Defaults to None.
        """

        self.ws_debug = False

        self.token = self.__auth(username, password)

        if self.token is None:
            self.token = "unauthorized_user_token"
            logger.warning(
                "you are using nologin method, data you access may be limited"
            )

        self.ws = None
        self.session = self.__generate_session()
        self.chart_session = self.__generate_chart_session()

    def __auth(self, username, password):

        if (username is None or password is None):
            token = None

        else:
            data = {"username": username,
                    "password": password,
                    "remember": "on"}
            try:
                response = requests.post(
                    url=self.__sign_in_url, data=data, headers=self.__signin_headers)
                    # print(url)
                token = response.json()['user']['auth_token']
            except Exception as e:
                logger.error('error while signin')
                token = None

        return token

    def __create_connection(self):
        logging.debug("creating websocket connection")
        self.ws = create_connection(
            "wss://data.tradingview.com/socket.io/websocket", headers=self.__ws_headers, timeout=self.__ws_timeout
        )
        # print(self.ws)

    @staticmethod
    def __filter_raw_message(text):
        try:
            found = re.search('"m":"(.+?)",', text).group(1)
            found2 = re.search('"p":(.+?"}"])}', text).group(1)

            return found, found2
        except AttributeError:
            logger.error("error in filter_raw_message")

    @staticmethod
    def __generate_session():
        stringLength = 12
        letters = string.ascii_lowercase
        random_string = "".join(random.choice(letters)
                                for i in range(stringLength))
        # print(random_string)
        return "qs_" + random_string

    @staticmethod
    def __generate_chart_session():
        stringLength = 12
        letters = string.ascii_lowercase
        random_string = "".join(random.choice(letters)
                                for i in range(stringLength))
        # print(random_string)    
        return "cs_" + random_string

    @staticmethod
    def __prepend_header(st):
        return "~m~" + str(len(st)) + "~m~" + st

    @staticmethod
    def __construct_message(func, param_list):
        return json.dumps({"m": func, "p": param_list}, separators=(",", ":"))

    def __create_message(self, func, paramList):
        return self.__prepend_header(self.__construct_message(func, paramList))

    def __send_message(self, func, args):
        m = self.__create_message(func, args)
        if self.ws_debug:
            print(m)
            # print(m)
        self.ws.send(m)

    @staticmethod
    def __create_df(raw_data, symbol):
        try:
            out = re.search('"s":\[(.+?)\}\]', raw_data).group(1)
            x = out.split(',{"')
            # print(x)
            data = list()
            volume_data = True

            for xi in x:
                xi = re.split("\[|:|,|\]", xi)
                ts = datetime.datetime.fromtimestamp(float(xi[4]))

                row = [ts]

                for i in range(5, 10):

                    # skip converting volume data if does not exists
                    if not volume_data and i == 9:
                        row.append(0.0)
                        continue
                    try:
                        row.append(float(xi[i]))

                    except ValueError:
                        volume_data = False
                        row.append(0.0)
                        logger.debug('no volume data')

                data.append(row)

            data = pd.DataFrame(
                data, columns=["datetime", "open",
                               "high", "low", "close", "volume"]
            ).set_index("datetime")
            data.insert(0, "symbol", value=symbol)
            return data
        except AttributeError:
            logger.error("no data, please check the exchange and symbol")

    @staticmethod
    def __format_symbol(symbol, exchange, contract: int = None):

        if ":" in symbol:
            pass
        elif contract is None:
            symbol = f"{exchange}:{symbol}"

        elif isinstance(contract, int):
            symbol = f"{exchange}:{symbol}{contract}!"

        else:
            raise ValueError("not a valid contract")

        return symbol

    def get_hist(
        self,
        symbol: str,
        exchange: str = "NSE",
        interval: Interval = Interval.in_daily,
        n_bars: int = 10,
        fut_contract: int = None,
        extended_session: bool = False,
    ) -> pd.DataFrame:
        """get historical data

        Args:
            symbol (str): symbol name
            exchange (str, optional): exchange, not required if symbol is in format EXCHANGE:SYMBOL. Defaults to None.
            interval (str, optional): chart interval. Defaults to 'D'.
            n_bars (int, optional): no of bars to download, max 5000. Defaults to 10.
            fut_contract (int, optional): None for cash, 1 for continuous current contract in front, 2 for continuous next contract in front . Defaults to None.
            extended_session (bool, optional): regular session if False, extended session if True, Defaults to False.

        Returns:
            pd.Dataframe: dataframe with sohlcv as columns
        """
        symbol = self.__format_symbol(
            symbol=symbol, exchange=exchange, contract=fut_contract
        )

        interval = interval.value

        self.__create_connection()

        self.__send_message("set_auth_token", [self.token])
        self.__send_message("chart_create_session", [self.chart_session, ""])
        self.__send_message("quote_create_session", [self.session])
        self.__send_message(
            "quote_set_fields",
            [
                self.session,
                "ch",
                "chp",
                "current_session",
                "description",
                "local_description",
                "language",
                "exchange",
                "fractional",
                "is_tradable",
                "lp",
                "lp_time",
                "minmov",
                "minmove2",
                "original_name",
                "pricescale",
                "pro_name",
                "short_name",
                "type",
                "update_mode",
                "volume",
                "currency_code",
                "rchp",
                "rtc",
            ],
        )

        self.__send_message(
            "quote_add_symbols", [self.session, symbol,
                                  {"flags": ["force_permission"]}]
        )
        self.__send_message("quote_fast_symbols", [self.session, symbol])

        self.__send_message(
            "resolve_symbol",
            [
                self.chart_session,
                "symbol_1",
                '={"symbol":"'
                + symbol
                + '","adjustment":"splits","session":'
                + ('"regular"' if not extended_session else '"extended"')
                + "}",
            ],
        )
        self.__send_message(
            "create_series",
            [self.chart_session, "s1", "s1", "symbol_1", interval, n_bars],
        )
        self.__send_message("switch_timezone", [
                            self.chart_session, "exchange"])

        raw_data = ""

        logger.debug(f"getting data for {symbol}...")
        while True:
            try:
                result = self.ws.recv()
                # f = open("MyFile1.txt","a")
                # f.write(result)
                # f.close()
                raw_data = raw_data + result + "\n"
            except Exception as e:
                logger.error(e)
                break

            if "series_completed" in result:
                break

        return self.__create_df(raw_data, symbol)

    def search_symbol(self, text: str, exchange: str = ''):
        url = self.__search_url.format(text, exchange)

        symbols_list = []
        try:
            resp = requests.get(url)

            symbols_list = json.loads(resp.text.replace(
                '</em>', '').replace('<em>', ''))
        except Exception as e:
            logger.error(e)

        return symbols_list


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    tv = TvDatafeed()
    print(tv.get_hist("CRUDEOIL", "MCX", fut_contract=1))
    print(tv.get_hist("NIFTY", "NSE", fut_contract=1))
    print(
        tv.get_hist(
            "EICHERMOT",
            "NSE",
            interval=Interval.in_1_hour,
            n_bars=500,
            extended_session=False,
        )
    )
