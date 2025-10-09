import numpy as np
from datetime import datetime

def generate_matric(college, department, num):
    """
    This is a method that help generate maticulation number 
    for Crescent University Student in Abeokuta, Nigeria
    """
    codes = {'COHES': 60,
             'CPL': 50,
             'CASMAS': 30, 
             'depts': {
                'nursing': 10,
                'anatomy': 20,
                'masscom': 30,
                'law': 10
            }}
    college_upper = college.upper()
    current_year = datetime.today().year
    year_last_digits = current_year % 100
    base_matric = 'S1'
    dept = department.lower()
    gen_matrics = []
    if college_upper in codes.keys():
        c_code = codes[college_upper]
        if dept in codes['depts'].keys():
            d_code = codes['depts'][dept]
            counter = 1  

            for _ in range(num):  
                if counter > 99:
                    counter = 0
                    d_code += 1
                
                gen_matric = (
                    base_matric
                    + str(year_last_digits)
                    + str(c_code)
                    + str(d_code)
                    + f"{counter:02d}"
                )
                gen_matrics.append(gen_matric)
                counter += 1
    return gen_matrics

print(generate_matric('casmas', 'masscom', 15))


