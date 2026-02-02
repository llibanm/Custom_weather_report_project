import os
from dotenv import load_dotenv
import requests
import sqlite3

class weather_report():

    def __init__(self) -> None:

        load_dotenv(".env")
        
        base_url = os.getenv("base_url") # base url which we will build the complete url upon
        api_key =  os.getenv("API_KEY")

        if base_url is not None and api_key is not None:

            self.base_url = base_url
            self.api_key = api_key


        else :
            raise ValueError('Error : base url and api key not found')

        #API METHOD
        # we will use just 2 for now
        self.current_weather = "/current.json"
        self.forecast = "/forecast.json"


 

         

    def build_request(self,city:str,days:int = 1,current_weather : bool = False,forecast : bool = True,aqi : bool = False):
        complete_url = ""

        if current_weather is True:

            if aqi is False:

                complete_url = self.base_url + self.current_weather+'?'+'key='+self.api_key+'&'+'q='+city+'&aqi=no'

            else :
                complete_url = self.base_url + self.current_weather+'?'+'key='+self.api_key+'&'+'q='+city+'&aqi=yes'

        elif forecast is True:

            if aqi is False:

                complete_url = self.base_url + self.forecast+'?'+'key='+self.api_key+'&'+'q='+city+"&days="+str(days)+'&aqi=no'

            else :

                complete_url = self.base_url + self.forecast+'?'+'key='+self.api_key+'&'+'q='+city+"&days="+str(days)+'&aqi=yes'

        return complete_url



    def weather_report_today(self,city:str):
        
        response = requests.get(self.build_request("Poitiers")
)
        data = response.json()

        region =  data["location"]["region"]

        forecast = data["forecast"]

        sunrise = forecast["forecastday"][0]["astro"]["sunrise"]

        sunset = forecast["forecastday"][0]["astro"]["sunset"]

        forecast_hour = forecast["forecastday"][0]["hour"]

        degree_per_hour = [] # in Celsuis

        feels_like_temp = [] # in Celsuis

        for e in forecast_hour:
            tmp = e["temp_c"]
            tmp_2 = e["feelslike_c"]

            degree_per_hour.append(tmp)
            feels_like_temp.append(tmp_2)

        points = '*' * 20

        print(points,'\n')

        print("Ville :", city)

        print('\n',points,'\n')

        print("levé du soleil :",sunrise," coucher du soleil :",sunset)

        print('\n',points,'\n')

        for i in range(len(degree_per_hour)):  # normally, degree_per_hour and feels_like_temp have the exact size
            print(f"\n Heure :",float(i)," Température :",degree_per_hour[i]," Ressenti :",feels_like_temp[i])


        pass



if __name__=='__main__':

    weather = weather_report()
    weather.weather_report_today("Nantes")

    pass       
