from pyscript import document

def compute_grade(event=None):
    first_name = document.getElementById("first").value
    last_name = document.getElementById("last").value
    result_box = document.getElementById("result-box")

    try:
        grades = [
            float(document.getElementById("science").value),
            float(document.getElementById("english").value),
            float(document.getElementById("ict").value),
            float(document.getElementById("math").value),
            float(document.getElementById("filipino").value),
            float(document.getElementById("pe").value)
        ]

        gwa = sum(grades) / len(grades)
        document.getElementById("show1").innerText = f"Name: {first_name} {last_name}"
        document.getElementById("show2").innerText = f"Your General Weighted Average is {gwa:.2f}"

        result_box.style.display = "block"

    except ValueError:
        document.getElementById("show1").innerText = "⚠️ Please enter valid numeric grades!"
        document.getElementById("show2").innerText = ""
        result_box.style.display = "block"