import configparser
import os

root_dir = 'D:/study/qim/app/config'


# get project cofnig data
def get_value(section, key):
    cf = configparser.ConfigParser()
    cf.read(root_dir + "/config.ini")
    value = cf.get(section, key)
    return value


if __name__ == '__main__':
    a = get_value('signature', 'signature')
    print(a)
