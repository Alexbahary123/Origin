def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    if month == 2:
        return 29 if is_leap_year(year) else 28
    return [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][month - 1]
def get_planet_ages(birth_date):
    days = (date.today() - birth_date).days
    orbital_periods = {
        "Mercury": 87.97, "Venus": 224.7, "Mars": 686.98,
        "Jupiter": 4332.59, "Saturn": 10759.22,
        "Uranus": 30688.5, "Neptune": 60182.0
    }
    return {p: round(days / per, 2) for p, per in orbital_periods.items()}
