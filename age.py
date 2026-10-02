from datetime import date, datetime

def get_zodiac_sign(month, day):
    signs = [
        ((1, 20), "Capricorn ♑"), ((2, 19), "Aquarius ♒"),
        ((3, 20), "Pisces ♓"),   ((4, 20), "Aries ♈"),
        ((5, 21), "Taurus ♉"),   ((6, 21), "Gemini ♊"),
        ((7, 22), "Cancer ♋"),   ((8, 23), "Leo ♌"),
        ((9, 23), "Virgo ♍"),    ((10, 23), "Libra ♎"),
        ((11, 22), "Scorpio ♏"), ((12, 22), "Sagittarius ♐"),
    ]
    for (m, d), sign in signs:
        if (month, day) < (m, d):
            return sign
    return "Capricorn ♑"

def get_life_stats(birth_date):
    birth_dt = datetime.combine(birth_date, datetime.min.time())
    delta = datetime.now() - birth_dt

    return {
        "Total hours": delta.days * 24 + delta.seconds // 3600,
        "Total minutes": delta.days * 1440 + delta.seconds // 60,
        "Total seconds": int(delta.total_seconds()),
        "Heartbeats": int(delta.total_seconds() * 1.2),   # ~72 bpm
        "Hours slept": delta.days * 8,                    # میانگین ۸ ساعت
    }


import json, os

PROFILE_FILE = "user_profile.json"

def save_profile(birth_date):
    with open(PROFILE_FILE, "w") as f:
        json.dump({"birth_date": birth_date.isoformat()}, f)

def load_profile():
    if os.path.exists(PROFILE_FILE):
        with open(PROFILE_FILE) as f:
            data = json.load(f)
        return date.fromisoformat(data["birth_date"])
    return None


def get_extra_calendar_info(birth_date):
    day_of_year = birth_date.timetuple().tm_yday
    week_of_year = birth_date.isocalendar()[1]
    seasons = {1:"Winter ❄️", 2:"Winter ❄️", 3:"Spring 🌸",
               4:"Spring 🌸", 5:"Spring 🌸", 6:"Summer ☀️",
               7:"Summer ☀️", 8:"Summer ☀️", 9:"Autumn 🍂",
               10:"Autumn 🍂", 11:"Autumn 🍂", 12:"Winter ❄️"}
    return day_of_year, week_of_year, seasons[birth_date.month]


def get_planet_ages(birth_date):
    days = (date.today() - birth_date).days
    orbital_periods = {
        "Mercury": 87.97, "Venus": 224.7, "Mars": 686.98,
        "Jupiter": 4332.59, "Saturn": 10759.22,
        "Uranus": 30688.5, "Neptune": 60182.0
    }
    return {p: round(days / per, 2) for p, per in orbital_periods.items()}



def get_milestone_dates(birth_date):
    milestones = [18, 30, 50, 65, 80, 100]
    result = {}
    for age in milestones:
        try:
            target = birth_date.replace(year=birth_date.year + age)
        except ValueError:  # 29 فوریه
            target = date(birth_date.year + age, 3, 1)
        if target >= date.today():
            result[f"Age {age}"] = target
    return result



def print_table(data: dict):
    width = max(len(k) for k in data) + 2
    print("┌" + "─" * (width + 20) + "┐")
    for k, v in data.items():
        print(f"│ {k:<{width}} : {str(v):<15} │")
    print("└" + "─" * (width + 20) + "┘")


import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Advanced Age Calculator")
    parser.add_argument("-d", "--date", help="Birth date (YYYY-MM-DD)")
    parser.add_argument("--no-save", action="store_true", help="Don't save profile")
    return parser.parse_args()
def main():
    args = parse_args()

    # گرفتن تاریخ تولد
    if args.date:
        birth_date = date.fromisoformat(args.date)
    else:
        birth_date = load_profile()
        if not birth_date:
            date_str = input("Enter your birth date (YYYY-MM-DD): ")
            birth_date = date.fromisoformat(date_str)
            if not args.no_save:
                save_profile(birth_date)

    # محاسبات
    age = date.today().year - birth_date.year
    life_stats = get_life_stats(birth_date)
    zodiac = get_rodic_sign(birth_date.month, birth_date.day)
    day_of_year, week_of_year, season = get_extra_calendar_info(birth_date)
    planet_ages = get_planet_ages(birth_date)
    milestones = get_milestone_dates(birth_date)

    # نمایش
    print(f"\n🎂 You are {age} years old.")
    print(f"♈ Zodiac sign: {zodiac}")
    print(f"📅 Day of year: {day_of_year}, Week: {week_of_year}, Season: {season}")

    print("\n⏱️  Life Stats:")
    print_table(life_stats)

    print("\n🪐 Planet Ages:")
    print_table(planet_ages)

    print("\n🏆 Upcoming Milestones:")
    print_table(milestones)


if __name__ == "__main__":
    main()






