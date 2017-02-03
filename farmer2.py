import os
from sqlalchemy import schema, types, Table, column, String
class CsvParser():
    def __init__(self, *args, **kwargs):
        import csv
        with open('data.csv', 'rU') as infile:
            reader = csv.DictReader(infile)
            data = {}
            for row in reader:
                for header, value in row.items():
                    try:
                        data[header].append(value)
                    except KeyError:
                        data[header] = [value]
        self.ascending_order(data)
        self.get_average(data)
        self.dump_csv_to_postgres()
        self.get_min_sql()
        self.get_max_sql()
        self.ascending_order_sql()
        self.get_average_sql()
  
    def ascending_order(self,data):
        import time
        dates = data['Harvesting date']
        #print [a.strip('/') for a in dates]
        #dates= [a.replace('/','') for a in dates]
        #print sorted(dates)
        #todo match dates with names
    def get_average(self,data):
        plants_harvested = data['No of plants harvest']
        plants_harvested=[int(i) for i in plants_harvested]
        #print reduce(lambda x, y: x + y, plants_harvested) / len(plants_harvested)
    def dump_csv_to_postgres(self):
        a= postgres_connection.connect_to_db()
        (engine, metadata, connection) = a
        from numpy import genfromtxt
        from time import time
        from datetime import datetime
        from sqlalchemy import Column, Integer, Float, Date
        from sqlalchemy.ext.declarative import declarative_base
        from sqlalchemy import create_engine
        from sqlalchemy.orm import sessionmaker
        data = genfromtxt('farmers.csv', delimiter=',', skiprows=1, converters={0: lambda s: str(s)})
        data=data.tolist()
        session = sessionmaker()
        session.configure(bind=engine)
        s = session()
        # for i in data:
        #     save="farmers_records"(**{
        #         "column_name":i[1] #increament this
        #         "column_name":i[2]
        #     })
        #     s.add(save)
        # s.commit()
        
    def get_sql_data():
        (engine, metadata, connection) = a
        data=Table('farmers_records',metadata, autoload=True)
        arr=[]
        def run(stmt):
            rs=stmt.execute()
            for row in rs:
                arr.append({
                    #i removed slashes 
                    row.total_biomass.encode('utf-8')
                })
        query=data.select()
        run(query)
        return arr
    def get_min_sql(self):
        data=get_sql_data()
        print min(data)
    def get_max_sql(self):
        data=get_sql_data()
        print max(data)
    def ascending_order_sql(self):
        data=get_sql_data()
        print sorted(data)
    def get_average_sql(self):
        data=get_sql_data()
        data=[int(i) for i in data]
        print reduce(lambda x, y: x + y, data) / len(data)               
                
           
                
app=CsvParser()
