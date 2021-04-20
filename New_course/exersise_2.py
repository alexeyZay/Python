import random
import time
import pdb

def is_status_success():
    """
    Check the status of a process and return True if status is success and False if not.
    :return:
    """
    print("Checking the status of the process.")
    list_to_chose_from = [True, True, False, False, False, False, False]

    bool_to_return = random.choice(list_to_chose_from)

    return bool_to_return


def wait_and_retry_until_status_is_success():
    current_time = time.time()
    max_time=time.time()+1
    while current_time < max_time:
        current_time = time.time()
        if is_status_success():
            print('hi')
            break
        else:
            time.sleep(3)
    else:
        raise Exception('some error')

wait_and_retry_until_status_is_success()
