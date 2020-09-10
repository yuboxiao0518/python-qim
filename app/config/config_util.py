import configparser
import os

root_dir = os.path.dirname(os.path.abspath('.'))

# get project cofnig data
def get_value(section, key):
    cf = configparser.ConfigParser()
    cf.read(root_dir + "/config.ini")
    value = cf.get(section, key)
    print(value)
    return value


if __name__ == '__main__':
    a = get_value('token', 'token')
    print(a)
