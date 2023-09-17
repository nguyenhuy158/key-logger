import inspect
import datetime
import socket


def get_current_function_name():
    current_frame = inspect.currentframe()

    caller_frame = current_frame.f_back

    function_name = caller_frame.f_code.co_name

    return function_name


def get_current_time():
    return datetime.datetime.now()


def get_hostname():
    hostname = socket.gethostname()
    return hostname