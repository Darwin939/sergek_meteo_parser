from configparser import NoOptionError
from datetime import datetime
from models.models import Data, engine, Sensor
from sqlalchemy.orm import Session
import requests


class SergekParser:

    URL = 'http://opendata.kz/api/sensor/getListWithLastHistory?cityId=1'


    def request(self):
        r = requests.get(self.URL)
        sensors = r.json()['sensors']
        return sensors

    def parse(self):
        print('begin', datetime.now())
        sensors = self.request()
        for sensor in sensors:
            self.save_in_db(sensor)

    def save_in_db(self, sensor_data):
        if self.is_sensor_exist(sensor_data['sensor_id']):

            sensor = self.get_sensor(sensor_data['sensor_id'])
            d = sensor_data['history'][0]['data']
            data = Data(
                sensor_id = sensor.id,
                field1 = d['field1'],
                field2 = d['field2'],
                field3 = d['field3'],
                # field4 = d['field4'],
                field5 = d['field5'],
                created_on_their_data = d['field1_created_at']
            )
            session = self.get_db_session()
            session.add(data)
            session.commit()

        else:
            self.create_sensor(sensor_data)
            self.save_in_db(sensor_data)
            

    def create_sensor(self, sensor_data):
        s = Sensor(
            sensor_id_num = sensor_data['id'],
            sensor_id_string = sensor_data['sensor_id'],
            name = sensor_data['name'],
            longtitude = sensor_data['longitude'],
            latitude = sensor_data['latitude'],
            sensor_height = sensor_data['sensor_height'],
        )
        session = self.get_db_session()
        session.add(s)
        session.commit()

    def is_sensor_exist(self, sensor_id_string):
        sensors = self.get_db_session().query(Sensor).filter(Sensor.sensor_id_string == sensor_id_string).all()

        if sensors:
            return True
        return False

    def get_sensor(self, sensor_id_string):
        sensor = self.get_db_session().query(Sensor).filter(Sensor.sensor_id_string == sensor_id_string).first()
        return sensor

    def get_db_session(self):
        session = Session(bind=engine)
        return session
