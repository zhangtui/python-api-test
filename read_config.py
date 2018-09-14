import configparser
class read_config:
    def read_config(self,dir,option,value):
        config = configparser.ConfigParser()
        config.read(dir)
        data= config.get(option,value)
        return data




if __name__=='__main__':

    app_key = read_config().read_config("common.conf", "http", "app_key")
    ip = read_config().read_config("common.conf", "http", "server_ip")
    print(app_key,ip)
