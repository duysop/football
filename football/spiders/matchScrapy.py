import scrapy
import json
import re
import csv
import pandas


class ExampleSpider(scrapy.Spider):
    name = 'match'
    def start_requests(self):
        for year in range(2013,2023):
            for month in range(1,10):
                for day in range(1,10):
                    url=f"https://www.espn.in/football/scoreboard/_/league/eng.1/date/{year}0{month}0{day}"
                    yield scrapy.Request(url,self.parse)
                for day in range(10,32):
                    url=f"https://www.espn.in/football/scoreboard/_/league/eng.1/date/{year}0{month}{day}"
                    yield scrapy.Request(url,self.parse)
            for month in range(10,13):
                for day in range(1,10):
                    url=f"https://www.espn.in/football/scoreboard/_/league/eng.1/date/{year}{month}0{day}"
                    yield scrapy.Request(url,self.parse)
                for day in range(10,32):
                    url=f"https://www.espn.in/football/scoreboard/_/league/eng.1/date/{year}{month}{day}"
                    yield scrapy.Request(url,self.parse)
    # start_urls = ['https://www.espn.in/football/scoreboard/_/league/eng.1/date/20140101']

    parse_url = 'https://www.espn.in/football/match/'
    def parse(self, response):
        json_string = response.xpath('//script[contains(.,"window.espn.scoreboardData")]/text()').get()
        match_ids = re.findall("_/gameId/[\d]+", json_string)
        for id in match_ids:
            yield scrapy.Request(self.parse_url+id,callback=self.parseAMatch)

    def parseAMatch(self,response):
        # from scrapy.shell import inspect_response
        # inspect_response(response, self)
        data = dict()
        data['team']=response.xpath('//span[@class="long-name"]/text()').getall()[0]
        data['opponent']=response.xpath('//span[@class="long-name"]/text()').getall()[1]
        data['homePct(%)'] =int(response.xpath('//span[@data-stat="possessionPct"][@data-home-away="home"]/text()').getall()[0][0:-1])
        data['awayPct(%)']=int(response.xpath('//span[@data-stat="possessionPct"][@data-home-away="away"]/text()').getall()[0][0:-1])
        shot_data_away=response.xpath('//span[@data-home-away="away"][@data-stat="shotsSummary"]/text()').getall()
        data['awayShot']=int(shot_data_away[0].split(" ")[0])
        data['awayShotOnGoal']=int(shot_data_away[0].split(" ")[1][1:-1] )
        shot_data_home=response.xpath('//span[@data-home-away="home"][@data-stat="shotsSummary"]/text()').getall()
        data['homeShot']=int(shot_data_home[0].split(" ")[0])
        data['homeShotOnGoal']=int(shot_data_home[0].split(" ")[1][1:-1])
        data['goal']=int(response.xpath('//span[@data-home-away="home"][@data-stat="score"]/text()').getall()[0].strip('\n\t'))
        data['opGoal']=int(response.xpath('//span[@data-home-away="away"][@data-stat="score"]/text()').getall()[0].strip('\n\t'))
        data['session']=response.xpath('//div[@class="game-details header"]/text()').getall()[0].strip('\n\t ')
        data['corner']=int(response.xpath('//td[@data-home-away="home"][@data-stat="wonCorners"]/text()').getall()[0])
        data['opcorner']=int(response.xpath('//td[@data-home-away="away"][@data-stat="wonCorners"]/text()').getall()[0])
        yield data

        




    