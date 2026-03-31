context = {}

def chatbot_response(user_input):
    global context
    user_input = user_input.lower().strip()

    # -------- HELLO -------- #
    if any(word in user_input for word in ["hello", "hi", "hey"]):
        return """Hi 👋 Welcome to Indo Global College Bot!<br><br>

You can ask me about:<br>
👉 College Information<br>
👉 Engineering Courses<br>
👉 Fee Structure<br>
👉 Principal / Dean<br>
👉 Hostel & Transport<br>
👉 Placements<br>
👉 Admission Details<br><br>

Try asking:<br>
- fees for btech<br>
- who is principal<br>
- courses available<br>
- admission details
"""

    # -------- PRINCIPAL FLOW -------- #
    if context.get("ask_principal"):
        if "engineering" in user_input:
            context["ask_principal"] = False
            return "👩‍🏫 Engineering Principal: Dr. Promila Kaushal"

        elif "management" in user_input:
            context["ask_principal"] = False
            return "👨‍🏫 Management Principal: Dr. S P Ahuja"

        else:
            return "❓ Please choose: Engineering or Management"

    if "principal" in user_input or "principle" in user_input:
        context["ask_principal"] = True
        return "Which principal do you want?<br>👉 Engineering<br>👉 Management"

    # -------- COLLEGE INFO -------- #
    if "college information" in user_input or "about college" in user_input:
        return """Indo Global Group of Colleges, Mohali is a leading institution established in 2003.<br>
Located in Abhipur near Chandigarh.<br>
Affiliated with IKGPTU and approved by AICTE.<br>
Offers Engineering, Management and other programs."""

    if "name" in user_input:
        return "Indo Global Group of Colleges, Abhipur, Mohali."

    if "location" in user_input or "where" in user_input:
        return "📍 Located in Abhipur, Mohali, Punjab."

    if "chairman" in user_input:
        return "👑 Chairman: Mr. Sukhdev Singh"

    if "dean" in user_input:
        return "🎓 Dean: Dr. Hardeep Singh Saini"

    # -------- COURSES -------- #
    if "course" in user_input:
        return """💻 Engineering Courses:<br>
- Computer Science<br>
- Mechanical<br>
- Civil<br>
- Electrical<br>
- Electronics<br><br>
Duration: 4 Years"""

    # -------- FEES -------- #
    if "fee" in user_input:
        return """💰 Fee Structure:<br><br>
B.Tech: ₹70,000 – ₹90,000/year<br>
Hostel: ₹60,000 – ₹80,000/year<br>
Transport: ₹20,000 – ₹30,000/year"""

    # -------- HOSTEL -------- #
    if "hostel fee" in user_input:
        return "🏠 Hostel Fee: ₹60,000 – ₹80,000/year"

    if "hostel" in user_input:
        return "🏠 Hostel available for boys and girls."

    # -------- TRANSPORT -------- #
    if "transport" in user_input or "bus" in user_input:
        return "🚌 Transport facility available."

    # -------- PLACEMENT -------- #
    if "placement" in user_input:
        return """💼 Companies:<br>
Infosys, Wipro, TCS, IBM, Capgemini"""

    # -------- PACKAGE -------- #
    if "package" in user_input or "salary" in user_input:
        return "💰 Average: 3–5 LPA<br>Highest: 8–12 LPA"

    # -------- ADMISSION TABLE -------- #
    if any(word in user_input for word in ["admission", "apply"]):
        return """📋 <b>Admission Details</b><br><br>

<table class="table">
<tr>
<th>S.No</th>
<th>Course</th>
<th>Duration</th>
<th>Eligibility</th>
<th>Type</th>
</tr>

<tr><td>1</td><td>B.Tech CSE</td><td>4 Years</td><td>10+2</td><td>B.Tech</td></tr>
<tr><td>2</td><td>B.Tech ECE</td><td>4 Years</td><td>10+2</td><td>B.Tech</td></tr>
<tr><td>3</td><td>B.Tech Mechanical</td><td>4 Years</td><td>10+2</td><td>B.Tech</td></tr>
<tr><td>4</td><td>B.Tech Civil</td><td>4 Years</td><td>10+2</td><td>B.Tech</td></tr>
<tr><td>5</td><td>Direct 2nd Year</td><td>3 Years</td><td>Diploma</td><td>B.Tech</td></tr>
<tr><td>6</td><td>B.Arch</td><td>5 Years</td><td>10+2</td><td>Architecture</td></tr>
<tr><td>7</td><td>BBA</td><td>3 Years</td><td>10+2</td><td>Business</td></tr>
<tr><td>8</td><td>BCA</td><td>3 Years</td><td>10+2</td><td>Computer</td></tr>
<tr><td>9</td><td>B.Sc MLS</td><td>3 Years</td><td>10+2</td><td>Medical</td></tr>
<tr><td>10</td><td>Radiology</td><td>3 Years</td><td>10+2</td><td>Medical</td></tr>
<tr><td>11</td><td>Operation Theatre</td><td>3 Years</td><td>10+2</td><td>Medical</td></tr>

</table>
"""

    # -------- DEFAULT -------- #
    return "❗ Ask about fees, courses, placements, or admission."