class BaseModel:

    def filter_state(self):
        del self.__dict__['_sa_instance_state']
        return self.__dict__