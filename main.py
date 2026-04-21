from pyscript import document

# defining class with lesson earlier
class Classmate:
    def __init__(self, name, section, favorite_subject): #underscore initialize and self usage :>
        self.name = name
        self.section = section
        self.favorite_subject = favorite_subject

    def introduce(self):
        return f"Hi! I am {self.name} from Section {self.section}. My favorite subject is {self.favorite_subject}."


# 9 unique classmates because yes. Also made it so that they have unique favorites.
classmates = [
    Classmate("David", "Emerald", "ICT"),
    Classmate("Samuel", "Emerald", "Filipino"),
    Classmate("Opdesh", "Emerald", "PE"),
    Classmate("Sky", "Emerald", "Math"),
    Classmate("Cenmar", "Emerald", "Science"),
    Classmate("Sahil", "Ruby", "English"),
    Classmate("Alex", "Ruby", "Social Studies"),
    Classmate("Dylan", "Ruby", "VE"),
    Classmate("Tristan", "Ruby", "Music and Arts")
]

# little bit of help to make the show list become possible to unshow
error_shown = False
list_visible = False


# The add classmate feature wherein you can put info and press add so it shows in the list
def add_classmate(e):
    global error_shown

    name = document.getElementById("classmate1").value.strip()
    section = document.getElementById("section").value.strip()
    subject = document.getElementById("subject").value.strip()
    output = document.getElementById("output")

    if not name or not section or not subject:
        if not error_shown:
            output.innerHTML = "<p style='color:red;'>⚠️ Please fill in all input fields.</p>"
            error_shown = True
        return

    error_shown = False

    classmates.append(Classmate(name, section, subject))

    document.getElementById("classmate1").value = ""
    document.getElementById("section").value = ""
    document.getElementById("subject").value = ""

    if list_visible:
        show_classmates(None)


# This is the actual toggle show/unshow list that I got help with for aethetics
def show_classmates(e):
    global list_visible

    output = document.getElementById("output")
    button = document.getElementById("toggleBtn")
    search_value = document.getElementById("search").value.lower()

    if list_visible:
        output.innerHTML = ""
        button.value = "Show List"
        list_visible = False
        return

    #This shows the list
    output.innerHTML = ""
    list_visible = True
    button.value = "Unshow List"

    for student in classmates:
        if search_value not in student.name.lower():
            continue

        if student.section.lower() == "emerald":
            glow = "0 0 10px lime"
        else:
            glow = "0 0 10px red"

        card = f"""
        <div style="
            border: 1px solid cyan;
            border-radius: 12px;
            padding: 8px;
            margin-bottom: 8px;
            font-size: 14px;
            box-shadow: {glow};
            transition: 0.25s;
        "
        onmouseover="this.style.transform='scale(1.02)'"
        onmouseout="this.style.transform='scale(1)'"
        >
            {student.introduce()}
        </div>
        """

        output.innerHTML += card