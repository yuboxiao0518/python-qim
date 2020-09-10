import baostock as bs


def auth(baostock_function):
    def run(*args, **kwargs):
        lg = bs.login()
        datas = baostock_function(*args, **kwargs)
        return datas
        bs.logout()
    return run
