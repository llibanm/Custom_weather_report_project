from datetime import datetime






if __name__=='__main__':


    maintenant = datetime.now()

    #heure = maintenant.strftime("%H %M %S")

    timestamp = int(maintenant.timestamp())

    print(timestamp)


    pass