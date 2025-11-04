from pyscript import document

def calculate_gwa(event=None):
    # Get student name
    fname = document.getElementById("fname").value
    lname = document.getElementById("lname").value

    # Get grades
    math = int(document.getElementById("math").value or 0)
    science = int(document.getElementById("science").value or 0)
    english = int(document.getElementById("english").value or 0)
    ict = int(document.getElementById("ict").value or 0)
    filipino = int(document.getElementById("filipino").value or 0)
    pe = int(document.getElementById("pe").value or 0)

    # Compute average
    average = round((math + science + english + ict + filipino + pe) / 6, 2)

    # Display results
    output = document.getElementById("output")
    output.innerHTML = f"""
        <h5>Student Name: {fname} {lname}</h5>
        <p>Math: {math}</p>
        <p>Science: {science}</p>
        <p>English: {english}</p>
        <p>ICT: {ict}</p>
        <p>Filipino: {filipino}</p>
        <p>PE: {pe}</p>
        <hr>
        <h5>Your General Weighted Average: {average}</h5>
    """
