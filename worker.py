from typing import List, Dict, Set, Tuple, Optional
import random

class Worker:
    """A member of staff who can supervise N dogs
    """

    def __init__(self, name: str, days: List[str], sites: List[str]):
        self.name = name
        self.driver = True
        self.assistant = False
        self.sites = sites
        self.days = days


class Assistant(Worker):

    def __init__(self, *args):
        super().__init__(*args)
        self.driver = False
        self.assistant = True


class Site:
    """A field location that can hold N dogs"""

    def __init__(self, name: str, max_dogs: int):
        self.name = name
        self.max_dogs = max_dogs


class Dog:
    def __init__(self, name: str, sites: Site):
        self.name = name
        self.sites = sites

    @property
    def possible_sites(self):
        return self.sites


class Day:
    """A scheduled day. Provides the staff schedule based on required dogs and available staff and sites"""

    def __init__(self, name: str, staff: List[Worker], dogs: List[Dog] = None, sites: List[Site] = None):
        self.name = name
        self.sites = sites
        self.dogs = dogs
        self.available_staff = staff
        self.sites = sites

    def schedule_day(self):
        day_staff = []
        num_staff = 0
        site_to_fill = self.sites[random.randint(0, len(self.sites))]  # Select one of the sites randomly to fill (not necessary but helps with fairness?
        while num_staff < site_to_fill.max_dogs:
            for s in random.shuffle(self.available_staff):
                if site_to_fill.name in s.sites:
                    day_staff.append(s)






class Week:
    def __init__(self):
        self.days = list()

    def add_day(self, day: Day):
        self.days.append(day)


class Rota:

    def __init__(self, staff: List[Worker], dog_booking: dict):
        self.staff = staff
        self.dog_booking = dog_booking
        self.week = Week()
        self.sites = [
            Site("Ockham", 30),
            Site("Ripley", 50)
        ]

    def build_week(self):
        for day_name, num_dogs in self.dog_booking.items():
            self.week.add_day(Day(name=day_name, staff=self.staff, dogs=self.num_dogs, sites=self.sites))



if __name__ == "__main__":

    full_week = ["mon", "tue", "wed", "thu", "fri"]
    all_sites = ["Ockham", "Ripley"]
    all_staff = {
        "Owen": {
            "days": full_week,
            "sites": all_sites
        },
        "Heidi": {
            "days": full_week,
            "sites": all_sites
        },
        "Christine": {
            "days": full_week,
            "sites": all_sites
        },
        "Ian": {
            "days": full_week,
            "sites": all_sites
        },
        "Farley": {
            "days": full_week,
            "sites": all_sites
        },
        "Tom": {
            "days": full_week,
            "sites": all_sites
        },
        "Dick": {
            "days": full_week,
            "sites": all_sites
        },
        "Harry": {
            "days": full_week,
            "sites": all_sites
        }
    }
    workers = list()
    for name, details in all_staff.items():
        workers.append(Worker(name=name, days=details.days(), sites=details.sites))
    bookings = {
        "mon": 50,
        "tue": 55,
        "wed": 60,
        "thu": 35,
        "fri": 40
    }

    week_rota = Rota(workers, bookings)
    week_rota.build_week()
