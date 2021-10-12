import random
import csv


class Week:
    def __init__(self):
        self.all_staff = dict()
        self.days = list()
        self.day_names = ["mon", "tue", "wed", "thu", "fri"]
        self.load_staff()
        for day_name in self.day_names:
            cur_day = Day(day_name, self.all_staff)
            cur_day.schedule()
            self.days.append(cur_day)

    def load_staff(self, filename="staff.csv"):
        with open(filename, "r") as f:
            file_reader = csv.reader(f, delimiter=",")
            next(file_reader)  # skip header
            for row in file_reader:
                name, ockham, ripley, *days = row
                sites = []
                if ockham.lower() in ["y", "yes", "1"]:
                    sites.append("Ockham")
                if ripley.lower() in ["y", "yes", "1"]:
                    sites.append("Ripley")
                working_days = [
                    day_name
                    for day_name, val in zip(self.day_names, days)
                    if val.lower() in ["y", "yes", 1]
                ]
                self.all_staff[name] = {"sites": sites, "days": working_days}
        print(f"Loaded staff information from {filename}")
        print(self.all_staff)
        print()


class Day:
    def __init__(self, day_name: str, staff: dict, site_name: str = "Ockham"):
        self.day_name = day_name
        self.staff = staff
        self.site_name = site_name
        self.site_staff = list()

    def schedule(self):
        print(f"Scheduling {self.day_name}...\n")
        staff_copy = self.staff.copy()
        while len(self.site_staff) < 3:
            print(f"Staff to choose from: {[n for n in staff_copy.keys()]}")
            staff_name, details = random.choice(list(staff_copy.items()))
            print(f"Randomly chose for {self.site_name}: {staff_name}")
            if (
                self.day_name in details["days"]
                and self.site_name in details["sites"]
                and staff_name not in self.site_staff
            ):
                print(
                    f"Selected {staff_name} to work at {self.site_name} on {self.day_name}"
                )
                self.site_staff.append(staff_name)
            else:
                print(
                    f"{staff_name} is NOT able to work at {self.site_name} on {self.day_name}. Removing them from the list"
                )
                print("Trying again...")
            del staff_copy[staff_name]
        print("----------------")
        print(f"{self.day_name.upper()}: {self.site_staff}")
        print("----------------")


if __name__ == "__main__":
    new_week = Week()
