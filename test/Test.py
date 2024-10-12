import inspect
import os
import re

class Test:
    _passed_tests_counter = 0
    _failed_tests_counter = 0
    _total_tests_counter = 0

    GREEN = "\033[92m"
    RED = "\033[91m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    RESET = "\033[0m"
    @classmethod
    def assert_equals(cls, espected, result, description=""):
        if espected == result:
            cls._passed_tests_counter += 1
            cls._total_tests_counter += 1 
            print(f"{cls.GREEN}✓ {description} -> Passed!{cls.RESET}")
        else:
            #frame = inspect.stack()[1]

            cls._failed_tests_counter += 1
            cls._total_tests_counter += 1 
            #current_test = cls._passed_tests_counter + cls._failed_tests_counter
            print(f"{cls.RED}\n--------------------------------------------------")
            #print(f"{cls.YELLOW}Method 'assert_equals' was called {cls.RED}on line {frame.lineno}{cls.YELLOW} in file {cls.RED}'{frame.filename}'.")
            print(Reporter.error_location())
            print(f"{cls.RED}Test {cls._total_tests_counter} failed: {description}")
            print(f"{cls.YELLOW}Expected: {espected}")
            print(f"{cls.RED   }Result:   {result}")
            print(f"--------------------------------------------------{cls.RESET}\n")

    @classmethod
    def print_summary(cls):
        Reporter.print_summary()


class Reporter:
    #def __init__(self):


    @classmethod
    def print_summary(cls):
        print(f"{Test.RESET}\n\n--------------------------------------------------")
        print(f"{Test.BLUE}SUMMARY OF TESTS")
        print(f"{Test.YELLOW} Total: {Test._total_tests_counter}")
        print(f"{Test.GREEN }Passed: {Test._passed_tests_counter}")
        print(f"{Test.RED   }Failed: {Test._failed_tests_counter}")
        print(f"{Test.RESET}--------------------------------------------------\n\n")
        
    @classmethod
    def error_location(cls):
        frame = inspect.stack()[1]
        path = re.split(r"[\\/]", frame.filename)
        file = path.pop()
        if os.name == 'nt':
            path = "\\".join(path) + "\\"
        elif os.name == 'posix':
            path = "/".join(path) + "/"

        return f"{Test.YELLOW}Method 'assert_equals' was called {Test.RED}on line {frame.lineno}{Test.YELLOW} in file '{path}{Test.RED}{file}'."
    