from datetime import date

# گرفتن سال تولد از کاربر
birth_year = int(input("Please enter your birth year: "))

# گرفتن سال فعلی
current_year = date.today().year

# محاسبه سن
age = current_year - birth_year

# نمایش نتیجه
print(f"You are {age} years old.")
