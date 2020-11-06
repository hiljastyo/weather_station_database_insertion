import pymysql.cursors
import pymongo
import time
import datetime


def Database_mysql(Temperature, Pressure, Humidity, AirQuality, RainFall, WindSpeed, WindGust, WindDirection, LightningDistance, UV): #Function for mysql database insertion
        connection = pymysql.connect(host = '', 
                                     user = '',
                                     password = '',
                                     db = '',
                                     charset = 'utf8mb4',
                                     cursorclass = pymysql.cursors.DictCursor)
        print("Connection to mysql database established")

        try:
                with connection.cursor() as cursor:

                        sql = "INSERT INTO Sensors (temperature,humidity,rainfall) VALUES (%s,%s,%s)"
                        
                        cursor.execute(sql)

                        connection.commit() # commit changes to the database
        finally:
                connection.close() # Close connection to the remote database
                       
def Database_mongodb(Temperature, Pressure, Humidity, AirQuality, RainFall, WindSpeed, WindGust, WindDirection, LightningDistance, UV): #Function for mongodb database insertion
        humidity = HTU21D.HTU21D()
        air_qual = tgs2600.TGS2600()
        sensor = BMP085.BMP085()
        interrupts = interrupt_client.interrupt_client(port =)
        pressure = sensor.read_pressure()/1000.00
        
        myclient = pymongo.MongoClient("")
        mydb = myclient[""]
        mycol = mydb[""]
        mylist=[
                {"Temperature": humidity.read_temperature(), "date": datetime.datetime.utcnow() },
                {"Pressure": sensor.read_pressure()/1000.00,"date": datetime.datetime.utcnow()},
                {"Humidity": humidity.read_humidity(), "date": datetime.datetime.utcnow()},
                {"Air quality": air_qual.get_value(), "date": datetime.datetime.utcnow()},
                {"Rainfall": interrupts.get_rain(), "date": datetime.datetime.utcnow()},
                {"Windspeed": interrupts.get_wind(), "date": datetime.datetime.utcnow()},
                {"Wind gust": interrupts.get_wind_gust(), "date": datetime.datetime.utcnow()},
                #{"Wind Direction": WindDirection, "date": datetime.datetime.utcnow()},
                #{"Lightning Distance": LightningDistance, "date": datetime.datetime.utcnow()},
                #{"UV": UV, "date": datetime.datetime.utcnow()}
                ] 
        mycol.insert_many(mylist)    
        mylist = mycol.find().sort("date", -1) #sort results by date and time
        
        myclient.close()