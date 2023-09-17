import inspect
import datetime


def get_current_function_name():
    current_frame = inspect.currentframe()

    caller_frame = current_frame.f_back

    function_name = caller_frame.f_code.co_name

    return function_name


def get_current_time():
    return datetime.datetime.now()
