import requests
import os
from datetime import date
#from dotenv import load_dotenv

if __name__=='__main__':
    """
    load_dotenv(".env")

    api_key =  os.getenv("API_KEY")
    base_url = os.getenv("base_url")
    

    print('My key is',api_key)

    print('\n*****************************************\n')

    ville = 'Nantes'
    api_method_current_weather = "/current.json"

    
    if base_url is not None and api_key is not None:
        complete_url = base_url+api_method_current_weather+'?'+'key='+api_key+'&'+'q='+ville+'&aqi=yes'

        response = requests.get(complete_url)

        print(response.json())"""
    
    date = date.today()

    formatted_date = date.strftime("%d-%m-%Y")

    print('today\'s date is :',formatted_date)

    pass