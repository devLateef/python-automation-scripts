import gradio as gr
from datetime import datetime

def generate_matric(college, department, num):
    """
    Generate matriculation numbers for Crescent University students.
    """
    codes = {
        'COHES': 60,
        'CPL': 50,
        'CASMAS': 30,
        'depts': {
            'nursing': 10,
            'anatomy': 20,
            'masscom': 30,
            'law': 10
        }
    }

    college_upper = college.upper().strip()
    dept = department.lower().strip()
    current_year = datetime.today().year
    year_last_digits = current_year % 100
    base_matric = 'S1'
    gen_matrics = []

    if college_upper in codes and dept in codes['depts']:
        c_code = codes[college_upper]
        d_code = codes['depts'][dept]
        counter = 1

        for _ in range(int(num)):
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

        # Return only matric numbers as text
        return "\n".join(gen_matrics)

    else:
        return "Invalid college or department. Please check your input."


# Gradio Interface
interface = gr.Interface(
    fn=generate_matric,
    inputs=[
        gr.Textbox(label="College (e.g., COHES, CPL, CASMAS)"),
        gr.Textbox(label="Department (e.g., Nursing, Law, Masscom)"),
        gr.Number(label="Number of Matric Numbers to Generate")
    ],
    outputs=gr.Textbox(label="Generated Matric Numbers", lines=15),
    title="Crescent University Matric Number Generator",
    description="Enter college, department, and the number of matric numbers to generate."
)

interface.launch()
