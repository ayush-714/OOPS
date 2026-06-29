"""
build_pdfs.py — Generate professional PDF notes for all OOPS topics using reportlab
"""
import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, HRFlowable, KeepTogether, Preformatted
)
from reportlab.lib.colors import HexColor

BASE = "/Users/ayussh-blrm24/Desktop/Code/Dev-Tools/New/OOPS"

# ─── COLOUR PALETTE ──────────────────────────────────────────────────────────
PRIMARY   = HexColor("#1a1a2e")
SECONDARY = HexColor("#16213e")
ACCENT    = HexColor("#0f3460")
HIGHLIGHT = HexColor("#e94560")
LIGHT_BG  = HexColor("#f0f4f8")
CODE_BG   = HexColor("#1e1e2e")
CODE_FG   = HexColor("#cdd6f4")
SUCCESS   = HexColor("#4ade80")
WARNING   = HexColor("#fbbf24")

# ─── STYLE SHEET ─────────────────────────────────────────────────────────────
def make_styles():
    styles = getSampleStyleSheet()

    styles.add(ParagraphStyle(
        "TopicTitle",
        fontName="Helvetica-Bold", fontSize=28, textColor=colors.white,
        alignment=TA_CENTER, spaceAfter=6, leading=34
    ))
    styles.add(ParagraphStyle(
        "SubTitle",
        fontName="Helvetica", fontSize=14, textColor=HexColor("#a0aec0"),
        alignment=TA_CENTER, spaceAfter=4
    ))
    styles.add(ParagraphStyle(
        "SectionHead",
        fontName="Helvetica-Bold", fontSize=16, textColor=HIGHLIGHT,
        spaceBefore=18, spaceAfter=6, borderPadding=(0,0,4,0)
    ))
    styles.add(ParagraphStyle(
        "Body",
        fontName="Helvetica", fontSize=10.5, textColor=HexColor("#2d3748"),
        leading=16, spaceAfter=8, alignment=TA_JUSTIFY
    ))
    styles.add(ParagraphStyle(
        "BulletItem",
        fontName="Helvetica", fontSize=10, textColor=HexColor("#2d3748"),
        leftIndent=16, leading=15, spaceAfter=4, bulletIndent=4
    ))
    styles.add(ParagraphStyle(
        "CodeBlock",
        fontName="Courier", fontSize=9, textColor=CODE_FG,
        backColor=CODE_BG, leading=13, leftIndent=8, rightIndent=8,
        spaceAfter=6, borderPadding=8
    ))
    styles.add(ParagraphStyle(
        "Note",
        fontName="Helvetica-Oblique", fontSize=10, textColor=HexColor("#4a5568"),
        backColor=HexColor("#ebf8ff"), borderColor=HexColor("#4299e1"),
        borderPadding=6, spaceAfter=8, leading=14
    ))
    styles.add(ParagraphStyle(
        "TableHeader",
        fontName="Helvetica-Bold", fontSize=10, textColor=colors.white,
        alignment=TA_CENTER
    ))
    styles.add(ParagraphStyle(
        "TableCell",
        fontName="Helvetica", fontSize=9.5, textColor=HexColor("#2d3748"),
        alignment=TA_CENTER, leading=13
    ))
    styles.add(ParagraphStyle(
        "SmallCode",
        fontName="Courier-Bold", fontSize=9.5, textColor=ACCENT,
    ))
    styles.add(ParagraphStyle(
        "InterviewQ",
        fontName="Helvetica-Bold", fontSize=10, textColor=SECONDARY,
        leftIndent=12, spaceAfter=4, spaceBefore=4
    ))
    return styles

S = make_styles()

# ─── HELPERS ─────────────────────────────────────────────────────────────────

def cover_page(topic_num: str, topic_title: str, subtitle: str = "") -> list:
    """Generate a styled cover page."""
    elements = []
    # Top colour bar
    elements.append(Table(
        [[Paragraph(f"{topic_num}", ParagraphStyle("N", fontName="Helvetica-Bold",
           fontSize=48, textColor=HexColor("#e2e8f0"), alignment=TA_CENTER))]],
        colWidths=[16*cm], rowHeights=[3*cm],
        style=TableStyle([("BACKGROUND",(0,0),(-1,-1), PRIMARY),
                          ("ALIGN",(0,0),(-1,-1),"CENTER"),
                          ("VALIGN",(0,0),(-1,-1),"MIDDLE")])
    ))
    elements.append(Spacer(1, 0.5*cm))
    elements.append(Paragraph(topic_title, S["TopicTitle"]))
    if subtitle:
        elements.append(Paragraph(subtitle, S["SubTitle"]))
    elements.append(HRFlowable(width="100%", thickness=2, color=HIGHLIGHT, spaceAfter=12))
    elements.append(Paragraph(
        "Python OOP Learning Series · Complete Study Notes",
        ParagraphStyle("Tag", fontName="Helvetica", fontSize=10,
                       textColor=HexColor("#718096"), alignment=TA_CENTER)
    ))
    elements.append(Spacer(1, 0.3*cm))
    return elements

def section(title: str) -> list:
    return [
        HRFlowable(width="100%", thickness=1, color=HexColor("#e2e8f0"), spaceAfter=4),
        Paragraph(title, S["SectionHead"]),
    ]

def body(text: str) -> Paragraph:
    return Paragraph(text, S["Body"])

def bullet(text: str) -> Paragraph:
    return Paragraph(f"&#9658;  {text}", S["BulletItem"])

def note(text: str) -> Paragraph:
    return Paragraph(f"<i>&#128161; {text}</i>", S["Note"])

def code(text: str) -> Preformatted:
    return Preformatted(text, S["CodeBlock"])

def q_and_a(question: str, answer: str) -> list:
    return [
        Paragraph(f"Q: {question}", S["InterviewQ"]),
        Paragraph(f"A: {answer}", S["Body"]),
        Spacer(1, 4),
    ]

def comparison_table(headers: list, rows: list, col_widths=None) -> Table:
    data = [[Paragraph(h, S["TableHeader"]) for h in headers]]
    for row in rows:
        data.append([Paragraph(str(c), S["TableCell"]) for c in row])

    if col_widths is None:
        w = 15.5 * cm
        col_widths = [w / len(headers)] * len(headers)

    t = Table(data, colWidths=col_widths)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), ACCENT),
        ("ROWBACKGROUNDS", (0,1), (-1,-1), [colors.white, LIGHT_BG]),
        ("GRID",       (0,0), (-1,-1), 0.5, HexColor("#cbd5e0")),
        ("VALIGN",     (0,0), (-1,-1), "MIDDLE"),
        ("TOPPADDING", (0,0), (-1,-1), 6),
        ("BOTTOMPADDING", (0,0), (-1,-1), 6),
        ("LEFTPADDING",   (0,0), (-1,-1), 8),
        ("RIGHTPADDING",  (0,0), (-1,-1), 8),
    ]))
    return t

def save_pdf(elements: list, filepath: str) -> None:
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    doc = SimpleDocTemplate(
        filepath, pagesize=A4,
        rightMargin=2*cm, leftMargin=2*cm,
        topMargin=2*cm, bottomMargin=2*cm
    )
    doc.build(elements)
    print(f"  ✅ {os.path.relpath(filepath, BASE)}")

# ═══════════════════════════════════════════════════════════════════════════════
#  PDF CONTENT BUILDERS
# ═══════════════════════════════════════════════════════════════════════════════

def pdf_01_introduction():
    el = cover_page("01", "Introduction to OOP",
                    "What, Why, and How of Object-Oriented Programming")
    el += section("1. What is Object-Oriented Programming?")
    el += [body(
        "Object-Oriented Programming (OOP) is a programming paradigm that organises "
        "software around <b>objects</b> — self-contained units that combine <b>data (attributes)</b> "
        "and <b>behaviour (methods)</b>. Instead of writing a series of instructions that operate "
        "on separate data, OOP models the real world by grouping related data and the operations "
        "on that data into a single entity called an <b>object</b>."
    ), note("OOP is a design philosophy, not just a syntax feature. Python supports OOP "
            "alongside procedural and functional styles.")]

    el += section("2. Procedural vs Object-Oriented")
    el.append(comparison_table(
        ["Aspect", "Procedural", "Object-Oriented"],
        [
            ["Focus",        "Functions & procedures",     "Objects & classes"],
            ["Data",         "Shared / global state",      "Encapsulated in objects"],
            ["Reusability",  "Function reuse",             "Inheritance + composition"],
            ["Scalability",  "Harder at scale",            "Easier to extend"],
            ["Examples",     "C, Pascal, BASIC",           "Python, Java, C++"],
        ]
    ))
    el.append(Spacer(1, 8))

    el += section("3. Four Pillars of OOP")
    pillars = [
        ("Encapsulation",  "Bundling data and methods together; hiding internal state behind a public interface."),
        ("Abstraction",    "Exposing only what is necessary; hiding implementation complexity."),
        ("Inheritance",    "A child class acquires attributes and methods from a parent class — enabling code reuse."),
        ("Polymorphism",   "The same interface works on different types — one function, many behaviours."),
    ]
    for p, d in pillars:
        el.append(bullet(f"<b>{p}:</b> {d}"))
    el.append(Spacer(1, 8))

    el += section("4. Key Terminology")
    el.append(comparison_table(
        ["Term", "Definition", "Example"],
        [
            ["Class",       "Blueprint / template for objects",       "class Dog:"],
            ["Object",      "Instance of a class",                    "rex = Dog('Rex')"],
            ["Attribute",   "Data stored in an object",               "rex.name = 'Rex'"],
            ["Method",      "Function belonging to a class",          "rex.bark()"],
            ["Constructor", "Special method to initialise object",    "__init__"],
            ["self",        "Reference to the current instance",      "self.name"],
        ]
    ))
    el.append(Spacer(1, 8))

    el += section("5. Basic Syntax")
    el.append(code(
        "class Dog:\n"
        "    species = 'Canis lupus'   # class variable\n\n"
        "    def __init__(self, name, breed):  # constructor\n"
        "        self.name  = name     # instance variable\n"
        "        self.breed = breed\n\n"
        "    def bark(self):           # instance method\n"
        "        return f'{self.name} says Woof!'\n\n"
        "# Creating objects\n"
        "rex   = Dog('Rex',   'Labrador')\n"
        "buddy = Dog('Buddy', 'Poodle')\n"
        "print(rex.bark())   # Rex says Woof!"
    ))

    el += section("6. Real-World Analogy")
    el += [body(
        "Think of a <b>Class</b> as a <b>cookie cutter</b> and <b>Objects</b> as the cookies. "
        "The cutter defines the shape (blueprint). Each cookie is a separate instance — "
        "you can decorate each one differently (different attribute values), but they all "
        "share the same basic shape (class structure)."
    )]

    el += section("7. When to Use OOP")
    for txt in [
        "Modelling real-world entities: User, Product, Order, Employee",
        "Large codebases requiring clear structure and maintainability",
        "Code that will be extended or modified frequently (inheritance)",
        "When data and behaviour naturally belong together",
        "Frameworks, libraries, and APIs",
    ]:
        el.append(bullet(txt))

    el += section("8. Interview Questions")
    el += q_and_a("What is the difference between a class and an object?",
                  "A class is a blueprint or template. An object is a concrete instance of that blueprint with its own state.")
    el += q_and_a("What is 'self' in Python?",
                  "self is a reference to the current instance of the class. It must be the first parameter of every instance method. Python passes it automatically when you call a method on an object.")
    el += q_and_a("Is everything an object in Python?",
                  "Yes. Integers, strings, functions, classes — everything is an object in Python, derived from the base 'object' class.")
    el += q_and_a("What are the four pillars of OOP?",
                  "Encapsulation, Abstraction, Inheritance, and Polymorphism.")

    el += section("9. Summary")
    el += [body(
        "OOP organises code around objects rather than procedures. A <b>class</b> defines "
        "the structure; an <b>object</b> is a running instance of that structure. The four "
        "pillars — Encapsulation, Abstraction, Inheritance, and Polymorphism — provide "
        "tools for building scalable, maintainable, and reusable code."
    )]
    save_pdf(el, f"{BASE}/01_Introduction/OOP_Introduction.pdf")


def pdf_02_classes():
    el = cover_page("02", "Classes and Objects",
                    "Blueprints, Instances, Attributes, and Methods")
    el += section("1. Anatomy of a Class")
    el.append(code(
        "class ClassName:               # class keyword + PascalCase name\n"
        "    class_var = 'shared'       # class variable\n\n"
        "    def __init__(self, arg1, arg2):  # constructor\n"
        "        self.attr1 = arg1      # instance variable\n"
        "        self.attr2 = arg2\n\n"
        "    def method(self):          # instance method\n"
        "        return self.attr1\n\n"
        "# Instantiation\n"
        "obj = ClassName('val1', 'val2')\n"
        "print(obj.method())            # val1"
    ))

    el += section("2. Memory Model")
    el += [body(
        "When you create an object, Python allocates a block of memory for it. Each object "
        "has a unique identity (memory address) accessible via <b>id(obj)</b>. Instance "
        "variables are stored in the object's <b>__dict__</b>. Class variables are stored "
        "in the class's own <b>__dict__</b> and are looked up through the MRO."
    )]
    el.append(comparison_table(
        ["Where stored", "Class variable", "Instance variable"],
        [
            ["Storage",    "Class __dict__",    "Object __dict__"],
            ["Shared?",    "Yes (all instances)","No (per object)"],
            ["Access",     "cls.var or self.var","self.var only"],
            ["Modify via", "ClassName.var = x", "self.var = x"],
        ]
    ))
    el.append(Spacer(1, 8))

    el += section("3. Built-in Class Attributes")
    for attr, desc in [
        ("__name__",     "Class name as string"),
        ("__module__",   "Module where the class is defined"),
        ("__dict__",     "Dictionary of the class namespace"),
        ("__bases__",    "Tuple of immediate parent classes"),
        ("__doc__",      "Docstring of the class"),
        ("__mro__",      "Method Resolution Order tuple"),
    ]:
        el.append(bullet(f"<b>{attr}</b> — {desc}"))

    el += section("4. The __init__ Method")
    el += [body(
        "<b>__init__</b> is the <i>initialiser</i> (commonly called constructor). It is called "
        "automatically right after a new object is created by <b>__new__</b>. Its job is to set "
        "up the initial state of the object by assigning instance variables."
    )]

    el += section("5. Common Mistakes")
    for m in [
        "Forgetting 'self' as the first parameter of instance methods",
        "Using mutable default values in class variables (use None + instance init instead)",
        "Modifying class variables through self (creates instance shadow instead)",
        "Not calling super().__init__() in derived class constructors",
    ]:
        el.append(bullet(m))

    el += section("6. Interview Questions")
    el += q_and_a("What is __dict__?",
                  "__dict__ is a dictionary that stores the namespace of an object or class. "
                  "For an instance, it contains instance variables. For a class, it contains class variables and method definitions.")
    el += q_and_a("Can you add attributes to an object outside the class?",
                  "Yes: obj.new_attr = value. Python allows dynamic attribute addition. "
                  "Use __slots__ to prevent this.")
    el += q_and_a("What happens if a class and instance have the same attribute name?",
                  "The instance attribute shadows (hides) the class attribute for that specific instance. "
                  "The class attribute is still accessible via ClassName.attr.")
    save_pdf(el, f"{BASE}/02_Classes_and_Objects/Classes_and_Objects.pdf")


def pdf_03_constructors():
    el = cover_page("03", "Constructors",
                    "__init__, __new__, Factory Methods, Validation")
    el += section("1. What is a Constructor?")
    el += [body(
        "A constructor is a special method that runs automatically when an object is "
        "created. In Python, this is <b>__init__</b>. It sets up the initial state of "
        "the object. Unlike __new__ (which allocates memory), __init__ initialises the "
        "already-created object."
    )]
    el.append(comparison_table(
        ["Method", "Role", "Return value", "Called by"],
        [
            ["__new__",  "Allocate memory, create instance", "New instance", "Python runtime"],
            ["__init__", "Initialise instance attributes",   "None",         "After __new__"],
            ["__del__",  "Clean up before garbage collection","None",        "Garbage collector"],
        ]
    ))
    el.append(Spacer(1, 8))

    el += section("2. Types of Constructors")
    el.append(bullet("<b>Default:</b> No parameters except self. Python provides one if none is defined."))
    el.append(bullet("<b>Parameterised:</b> Takes arguments to customise each instance."))
    el.append(bullet("<b>Factory methods (@classmethod):</b> Alternative constructors for different input types."))

    el += section("3. Constructor Overloading in Python")
    el += [body(
        "Python doesn't support traditional constructor overloading (like Java). Instead, use:"
    ), bullet("Default parameter values: def __init__(self, name, age=18)"),
       bullet("*args / **kwargs for flexible signatures"),
       bullet("@classmethod factory methods: Person.from_json(), Person.from_dict()"),
       bullet("if/isinstance checks inside __init__")]

    el += section("4. Code Example")
    el.append(code(
        "class Person:\n"
        "    def __init__(self, name: str, age: int = 0) -> None:\n"
        "        self.name = name\n"
        "        self.age  = age\n\n"
        "    @classmethod\n"
        "    def from_dict(cls, data: dict) -> 'Person':\n"
        "        return cls(data['name'], data.get('age', 0))\n\n"
        "    @classmethod\n"
        "    def from_string(cls, s: str) -> 'Person':\n"
        "        name, age = s.split(',')\n"
        "        return cls(name.strip(), int(age))\n\n"
        "p1 = Person('Alice', 30)\n"
        "p2 = Person.from_dict({'name': 'Bob', 'age': 25})\n"
        "p3 = Person.from_string('Carol, 22')"
    ))

    el += section("5. Validation in __init__")
    el += [body("Always validate arguments in __init__ to prevent objects from entering an invalid state.")]
    el.append(code(
        "class Temperature:\n"
        "    ABSOLUTE_ZERO = -273.15\n\n"
        "    def __init__(self, celsius: float) -> None:\n"
        "        if celsius < self.ABSOLUTE_ZERO:\n"
        "            raise ValueError(f'Invalid: {celsius}C below absolute zero')\n"
        "        self._celsius = celsius"
    ))

    el += section("6. Interview Questions")
    el += q_and_a("What is the difference between __new__ and __init__?",
                  "__new__ is called first and creates the object (returns a new instance). "
                  "__init__ is called second to initialise it (returns None). You rarely override __new__ — "
                  "it's used for immutable types or singletons.")
    el += q_and_a("Can __init__ return a value?",
                  "No. If __init__ returns anything other than None, Python raises a TypeError.")
    el += q_and_a("What is a factory method in Python?",
                  "A @classmethod that creates and returns an instance of the class. "
                  "It provides alternative constructors (e.g., from_json, from_string) without overloading __init__.")
    save_pdf(el, f"{BASE}/03_Constructors/Constructors.pdf")


def pdf_04_variables():
    el = cover_page("04", "Instance & Class Variables",
                    "Variable Scope, Shared State, and Class Constants")
    el += section("1. Instance Variables")
    el += [body(
        "Instance variables are <b>unique to each object</b>. They are defined inside "
        "<b>__init__</b> using <b>self.var_name</b> and stored in the object's __dict__. "
        "Modifying one object's instance variable does not affect any other object."
    )]

    el += section("2. Class Variables")
    el += [body(
        "Class variables are <b>shared across all instances</b> of a class. They are "
        "defined directly in the class body (outside any method). Changing a class variable "
        "through the class name affects all instances. However, assigning through an instance "
        "creates a new instance variable that <i>shadows</i> the class variable."
    )]
    el.append(comparison_table(
        ["Property",      "Instance Variable",       "Class Variable"],
        [
            ["Defined in",   "__init__",                  "Class body"],
            ["Scope",        "Per object",                "Shared across all instances"],
            ["Storage",      "obj.__dict__",              "ClassName.__dict__"],
            ["Access",       "self.x",                    "cls.x or ClassName.x"],
            ["Use case",     "Object-specific data",      "Counters, constants, registries"],
        ]
    ))
    el.append(Spacer(1, 8))

    el += section("3. The Shadowing Trap")
    el.append(code(
        "class Employee:\n"
        "    company = 'TechCorp'   # class variable\n\n"
        "e1 = Employee()\n"
        "e2 = Employee()\n\n"
        "Employee.company = 'MegaCorp'  # changes for all instances\n"
        "print(e1.company)  # 'MegaCorp'\n"
        "print(e2.company)  # 'MegaCorp'\n\n"
        "e1.company = 'Freelancer'  # creates instance var in e1 ONLY\n"
        "print(e1.company)  # 'Freelancer'  (instance shadow)\n"
        "print(e2.company)  # 'MegaCorp'   (still class var)"
    ))

    el += section("4. Class Constants")
    el += [body(
        "Convention: UPPER_CASE class variables are treated as constants. Python doesn't "
        "enforce immutability (use frozen dataclass or property for that), but UPPER_CASE "
        "signals 'do not modify'."
    )]

    el += section("5. Interview Questions")
    el += q_and_a("How do you access a class variable inside a method?",
                  "Via self.var_name (reads class var if no instance var shadows it) or "
                  "ClassName.var_name (explicit — always accesses the class variable).")
    el += q_and_a("What happens when you do self.class_var = value?",
                  "A new instance variable is created in the object's __dict__, shadowing the "
                  "class variable. The class variable itself is unchanged.")
    save_pdf(el, f"{BASE}/04_Instance_and_Class_Variables/Variables.pdf")


def pdf_05_methods():
    el = cover_page("05", "Methods",
                    "Instance, Class, and Static Methods — Definitive Guide")
    el += section("1. Three Types of Methods")
    el.append(comparison_table(
        ["Type",             "Decorator",     "First param", "Access",                 "Use case"],
        [
            ["Instance method", "None",          "self",        "Instance + class",       "Most methods; modify object state"],
            ["Class method",    "@classmethod",  "cls",         "Class only",             "Factories, class-level operations"],
            ["Static method",   "@staticmethod", "None",        "Neither",                "Utilities; pure functions in class namespace"],
        ]
    ))
    el.append(Spacer(1, 8))

    el += section("2. Instance Methods")
    el += [body("Instance methods have access to the instance (self) and its class. They can read and modify instance and class attributes.")]
    el.append(code(
        "class Circle:\n"
        "    def __init__(self, radius):\n"
        "        self.radius = radius\n\n"
        "    def area(self):           # instance method\n"
        "        import math\n"
        "        return math.pi * self.radius ** 2"
    ))

    el += section("3. Class Methods")
    el += [body("Class methods receive the class (cls) as the first argument, not the instance. "
                "Use them for factory constructors and operations on the class itself.")]
    el.append(code(
        "class Date:\n"
        "    def __init__(self, year, month, day):\n"
        "        self.year, self.month, self.day = year, month, day\n\n"
        "    @classmethod\n"
        "    def today(cls):           # factory method\n"
        "        from datetime import date\n"
        "        d = date.today()\n"
        "        return cls(d.year, d.month, d.day)\n\n"
        "    @classmethod\n"
        "    def from_string(cls, s):  # 'YYYY-MM-DD'\n"
        "        y, m, d = map(int, s.split('-'))\n"
        "        return cls(y, m, d)\n\n"
        "d = Date.today()\n"
        "d2 = Date.from_string('2024-07-04')"
    ))

    el += section("4. Static Methods")
    el += [body("Static methods are plain functions inside a class namespace. They don't receive "
                "self or cls. Use them for utility functions that logically belong to the class "
                "but don't need access to class or instance state.")]
    el.append(code(
        "class MathUtils:\n"
        "    @staticmethod\n"
        "    def is_prime(n: int) -> bool:\n"
        "        if n < 2: return False\n"
        "        for i in range(2, int(n**0.5)+1):\n"
        "            if n % i == 0: return False\n"
        "        return True\n\n"
        "print(MathUtils.is_prime(17))  # True\n"
        "m = MathUtils()\n"
        "print(m.is_prime(17))         # also works"
    ))

    el += section("5. When to Use Each")
    for row in [
        ("✅ Instance method",  "Reading/modifying object state, most class behaviour"),
        ("✅ Class method",     "Alternative constructors (from_x), class counters, registry"),
        ("✅ Static method",    "Pure utilities that logically belong to the class namespace"),
        ("❌ Instance as static","Don't pass unnecessary self if you don't use it"),
    ]:
        el.append(bullet(f"{row[0]}: {row[1]}"))

    el += section("6. Interview Questions")
    el += q_and_a("Can a static method access the class? Can it call instance methods?",
                  "No to both. A static method has no reference to cls or self. It is a "
                  "regular function that lives in the class namespace.")
    el += q_and_a("What is the difference between @classmethod and @staticmethod?",
                  "@classmethod receives cls (the class) as first arg, enabling it to "
                  "create instances and access class attributes. @staticmethod receives "
                  "nothing — it's a plain function. Use @classmethod for factories; "
                  "@staticmethod for utilities.")
    save_pdf(el, f"{BASE}/05_Methods/Methods.pdf")


def pdf_06_encapsulation():
    el = cover_page("06", "Encapsulation",
                    "Data Hiding, Access Modifiers, @property, Validation")
    el += section("1. What is Encapsulation?")
    el += [body(
        "Encapsulation means bundling data (attributes) and the methods that operate on that "
        "data into a single unit (class), and restricting direct access to some of the object's "
        "components. It protects the internal state of an object from unintended modification."
    ), note("Real-world analogy: A car's engine. You use pedals and steering wheel (public interface) "
            "without needing to know the internal combustion details (private implementation).")]

    el += section("2. Access Modifiers in Python")
    el.append(comparison_table(
        ["Convention",    "Syntax",     "Access",                    "Name mangling"],
        [
            ["Public",    "name",       "Anywhere",                  "No"],
            ["Protected", "_name",      "Class + subclasses (convention)","No"],
            ["Private",   "__name",     "Class only (enforced via mangling)","Yes: _Class__name"],
        ]
    ))
    el.append(Spacer(1, 8))
    el += [note("Python has no true private variables. __name is just name-mangled to _ClassName__name. "
                "It is a strong convention, not a security measure.")]

    el += section("3. The @property Decorator")
    el += [body(
        "@property transforms a method into a computed attribute. It gives you getter/setter/deleter "
        "syntax (obj.attr = value) while running validation or computation underneath."
    )]
    el.append(code(
        "class Circle:\n"
        "    def __init__(self, radius):\n"
        "        self.radius = radius   # calls setter\n\n"
        "    @property\n"
        "    def radius(self):\n"
        "        return self._radius\n\n"
        "    @radius.setter\n"
        "    def radius(self, value):\n"
        "        if value < 0:\n"
        "            raise ValueError('Radius must be >= 0')\n"
        "        self._radius = value\n\n"
        "    @property\n"
        "    def area(self):        # read-only computed property\n"
        "        import math\n"
        "        return math.pi * self._radius ** 2\n\n"
        "c = Circle(5)\n"
        "print(c.area)      # 78.54\n"
        "c.radius = -1      # raises ValueError"
    ))

    el += section("4. Advantages of Encapsulation")
    for a in [
        "Protects object integrity — invalid state is prevented at the setter",
        "Internal representation can change without affecting external code",
        "Makes debugging easier — only one place to look for state changes",
        "Reduces coupling between components",
    ]:
        el.append(bullet(a))

    el += section("5. Interview Questions")
    el += q_and_a("What is the difference between _name and __name?",
                  "_name is a convention meaning 'protected — use with care'. __name is "
                  "name-mangled to _ClassName__name, making it harder to access accidentally "
                  "(but still possible). Neither is truly private in Python.")
    el += q_and_a("Why use @property instead of direct attributes?",
                  "Properties allow you to add validation, transformation, or computation "
                  "without changing the public API. You can start with a plain attribute and "
                  "later convert it to a property without breaking client code.")
    save_pdf(el, f"{BASE}/06_Encapsulation/Encapsulation.pdf")


def pdf_07_abstraction():
    el = cover_page("07", "Abstraction",
                    "ABC Module, Abstract Methods, Protocols")
    el += section("1. What is Abstraction?")
    el += [body(
        "Abstraction means hiding complex implementation details and exposing only a "
        "clean, simple interface. Users interact with the interface without needing to "
        "understand the underlying mechanics."
    ), note("Analogy: A TV remote. You press 'Volume Up' without knowing how IR signals, "
            "electronics, and audio circuits work together.")]

    el += section("2. Abstract Base Classes (ABC)")
    el += [body(
        "Python's <b>abc</b> module lets you define abstract classes — classes that "
        "cannot be instantiated and require subclasses to implement specific methods."
    )]
    el.append(code(
        "from abc import ABC, abstractmethod\n\n"
        "class Shape(ABC):\n"
        "    @abstractmethod\n"
        "    def area(self) -> float: ...\n\n"
        "    @abstractmethod\n"
        "    def perimeter(self) -> float: ...\n\n"
        "    def describe(self):    # concrete method\n"
        "        return f'area={self.area():.2f}'\n\n"
        "class Circle(Shape):\n"
        "    def __init__(self, r): self.r = r\n"
        "    def area(self): return 3.14 * self.r ** 2\n"
        "    def perimeter(self): return 2 * 3.14 * self.r\n\n"
        "# Shape()  → TypeError: cannot instantiate abstract class\n"
        "c = Circle(5)\n"
        "print(c.describe())   # area=78.54"
    ))

    el += section("3. Abstract Properties and Class/Static Methods")
    el.append(code(
        "from abc import ABC, abstractmethod\n\n"
        "class Vehicle(ABC):\n"
        "    @property\n"
        "    @abstractmethod\n"
        "    def speed(self) -> float: ...\n\n"
        "    @classmethod\n"
        "    @abstractmethod\n"
        "    def create(cls, *args): ...\n\n"
        "    @staticmethod\n"
        "    @abstractmethod\n"
        "    def validate_id(id_str: str) -> bool: ..."
    ))

    el += section("4. Protocols (Structural Subtyping)")
    el += [body(
        "Python 3.8+ introduced <b>Protocol</b> for duck-typing with type-checker support. "
        "A class satisfies a Protocol if it has the required attributes/methods — "
        "no explicit inheritance needed."
    )]
    el.append(code(
        "from typing import Protocol, runtime_checkable\n\n"
        "@runtime_checkable\n"
        "class Drawable(Protocol):\n"
        "    def draw(self) -> str: ...\n\n"
        "class Circle:\n"
        "    def draw(self) -> str: return 'Drawing circle'\n\n"
        "print(isinstance(Circle(), Drawable))  # True — no inheritance!"
    ))

    el += section("5. Interview Questions")
    el += q_and_a("What is the difference between Abstraction and Encapsulation?",
                  "Encapsulation bundles data + methods and hides internal state. "
                  "Abstraction hides implementation complexity and exposes only a clean interface. "
                  "Encapsulation is about HOW data is stored; Abstraction is about WHAT interface you expose.")
    el += q_and_a("Can an ABC have concrete methods?",
                  "Yes. An ABC can have both abstract methods (must be overridden) and concrete methods "
                  "(inherited as-is). Abstract methods define the contract; concrete methods provide shared behaviour.")
    save_pdf(el, f"{BASE}/07_Abstraction/Abstraction.pdf")


def pdf_08_inheritance():
    el = cover_page("08", "Inheritance",
                    "Single, Multiple, Multilevel, Hierarchical, Hybrid")
    el += section("1. What is Inheritance?")
    el += [body(
        "Inheritance allows a class (child/derived) to acquire attributes and methods from "
        "another class (parent/base). It promotes <b>code reuse</b> and establishes an "
        "<b>IS-A relationship</b>. A Dog IS-A Animal."
    )]
    el += section("2. Types of Inheritance")
    el.append(comparison_table(
        ["Type",          "Description",                              "Python syntax"],
        [
            ["Single",       "Child inherits from one parent",          "class B(A)"],
            ["Multiple",     "Child inherits from multiple parents",    "class C(A, B)"],
            ["Multilevel",   "A → B → C chain",                        "class C(B), class B(A)"],
            ["Hierarchical", "Multiple children from one parent",       "class B(A), class C(A)"],
            ["Hybrid",       "Combination of above types",              "Various"],
        ]
    ))
    el.append(Spacer(1, 8))

    el += section("3. super() Function")
    el += [body("super() returns a proxy object that delegates method calls to the parent class. "
                "Always use super().__init__() to ensure parent is initialised correctly.")]
    el.append(code(
        "class Animal:\n"
        "    def __init__(self, name):\n"
        "        self.name = name\n\n"
        "class Dog(Animal):\n"
        "    def __init__(self, name, breed):\n"
        "        super().__init__(name)  # calls Animal.__init__\n"
        "        self.breed = breed\n\n"
        "    def speak(self):\n"
        "        return f'{self.name} says Woof!'"
    ))

    el += section("4. Method Overriding")
    el += [body(
        "A child class can provide its own implementation of a parent method. The child's "
        "version takes precedence. Use super().method() to also call the parent version."
    )]

    el += section("5. The Diamond Problem")
    el += [body(
        "When multiple parent classes define the same method, Python resolves the conflict "
        "using the C3 Linearization algorithm (MRO). super() cooperates with the MRO, "
        "ensuring each class in the chain is called exactly once."
    )]
    el.append(code(
        "class A:\n"
        "    def greet(self): print('A')\n\n"
        "class B(A):\n"
        "    def greet(self): super().greet(); print('B')\n\n"
        "class C(A):\n"
        "    def greet(self): super().greet(); print('C')\n\n"
        "class D(B, C):         # Diamond\n"
        "    def greet(self): super().greet(); print('D')\n\n"
        "D().greet()  # Output: A, C, B, D  (MRO order)\n"
        "print(D.__mro__)  # D, B, C, A, object"
    ))

    el += section("6. Best Practices")
    for bp in [
        "Prefer composition over inheritance for code reuse",
        "Keep inheritance hierarchies shallow (max 2-3 levels)",
        "Always call super().__init__() in derived __init__",
        "Use ABC for well-defined contracts, not just for code sharing",
        "The IS-A test: only inherit if child IS-A parent (Dog IS-A Animal ✅, Stack IS-A List ❌)",
    ]:
        el.append(bullet(bp))

    el += section("7. Interview Questions")
    el += q_and_a("What is the difference between overriding and overloading?",
                  "Overriding: child class provides a new implementation of a method defined in the parent. "
                  "Overloading: multiple methods with the same name but different signatures. Python "
                  "doesn't support traditional overloading — use default args or *args instead.")
    el += q_and_a("What does issubclass() do?",
                  "issubclass(Child, Parent) returns True if Child is a subclass of Parent (direct or indirect).")
    save_pdf(el, f"{BASE}/08_Inheritance/Inheritance.pdf")


def pdf_09_polymorphism():
    el = cover_page("09", "Polymorphism",
                    "Method Overriding, Duck Typing, Operator Overloading")
    el += section("1. What is Polymorphism?")
    el += [body(
        "'Poly' = many, 'morphism' = forms. Polymorphism allows the same interface to work "
        "on different types. The same method call produces different behaviour depending on "
        "the object it is called on."
    ), note("Analogy: The '+' operator in Python. 1+2=3 (int addition), 'a'+'b'='ab' (string concat). "
            "Same operator, different behaviour based on type.")]

    el += section("2. Types in Python")
    el.append(comparison_table(
        ["Type",               "How it works",                              "Python mechanism"],
        [
            ["Method Overriding",  "Child class redefines parent method",     "def method() in child"],
            ["Duck Typing",        "If it walks/quacks like a duck, it is one","No isinstance check needed"],
            ["Operator Overload",  "Custom behaviour for +,-,*,==,<,etc.",    "__add__, __eq__, __lt__..."],
            ["Function Poly.",     "Same function works on multiple types",   "isinstance / duck typing"],
        ]
    ))
    el.append(Spacer(1, 8))

    el += section("3. Duck Typing")
    el += [body(
        "Python doesn't require explicit type declarations. Any object that has the required "
        "methods will work — regardless of its actual class. This is more flexible than "
        "traditional OOP polymorphism."
    )]
    el.append(code(
        "def make_sound(animal):\n"
        "    print(animal.speak())  # works for ANY object with speak()\n\n"
        "class Dog:\n"
        "    def speak(self): return 'Woof!'\n\n"
        "class Cat:\n"
        "    def speak(self): return 'Meow!'\n\n"
        "class Robot:\n"
        "    def speak(self): return 'Beep boop!'\n\n"
        "for thing in [Dog(), Cat(), Robot()]:\n"
        "    make_sound(thing)  # all work!"
    ))

    el += section("4. Operator Overloading — Key Dunder Methods")
    el.append(comparison_table(
        ["Operator", "Dunder method", "Example"],
        [
            ["+",    "__add__",      "v1 + v2"],
            ["-",    "__sub__",      "v1 - v2"],
            ["*",    "__mul__",      "v1 * 3"],
            ["==",   "__eq__",       "v1 == v2"],
            ["<",    "__lt__",       "v1 < v2"],
            ["len()", "__len__",     "len(collection)"],
            ["str()", "__str__",     "str(obj)"],
            ["repr()","__repr__",    "repr(obj)"],
        ]
    ))

    el += section("5. Interview Questions")
    el += q_and_a("What is duck typing?",
                  "'If it walks like a duck and quacks like a duck, it's a duck.' "
                  "Python checks for the presence of methods/attributes at runtime rather than "
                  "requiring explicit type declarations. Any object with the right methods will work.")
    el += q_and_a("What is __rmul__ for?",
                  "__rmul__ handles the case where your object is on the RIGHT side of *. "
                  "If 3 * v fails (int doesn't know how to handle Vector), Python tries v.__rmul__(3).")
    save_pdf(el, f"{BASE}/09_Polymorphism/Polymorphism.pdf")


def pdf_10_dunder():
    el = cover_page("10", "Special (Dunder) Methods",
                    "__str__, __repr__, __len__, __add__, Context Managers, and more")
    el += section("1. What are Dunder Methods?")
    el += [body(
        "Dunder (double underscore) methods are special methods that Python calls automatically "
        "in response to certain operations. They let your objects integrate with Python's "
        "built-in syntax and functions."
    )]
    el.append(comparison_table(
        ["Category",          "Methods"],
        [
            ["String repr",    "__str__, __repr__, __format__"],
            ["Arithmetic",     "__add__, __sub__, __mul__, __truediv__, __pow__"],
            ["Comparison",     "__eq__, __ne__, __lt__, __le__, __gt__, __ge__"],
            ["Container",      "__len__, __getitem__, __setitem__, __delitem__, __contains__"],
            ["Iteration",      "__iter__, __next__"],
            ["Context mgr",    "__enter__, __exit__"],
            ["Callable",       "__call__"],
            ["Lifecycle",      "__new__, __init__, __del__"],
            ["Hashing",        "__hash__"],
            ["Truth value",    "__bool__"],
        ]
    ))
    el.append(Spacer(1, 8))

    el += section("2. __repr__ vs __str__")
    el += [body("<b>__repr__:</b> For developers. Should be unambiguous, ideally valid Python code to recreate the object. Called by repr() and in the REPL."
                "<br/><b>__str__:</b> For end users. Human-readable. Called by str() and print().")]
    el.append(code(
        "class Point:\n"
        "    def __init__(self, x, y): self.x, self.y = x, y\n"
        "    def __repr__(self): return f'Point(x={self.x}, y={self.y})'\n"
        "    def __str__(self):  return f'({self.x}, {self.y})'\n\n"
        "p = Point(3, 4)\n"
        "print(repr(p))  # Point(x=3, y=4)  — unambiguous\n"
        "print(str(p))   # (3, 4)            — user-friendly\n"
        "print(p)        # (3, 4)            — str() used by print()"
    ))

    el += section("3. Context Manager Protocol")
    el.append(code(
        "class ManagedFile:\n"
        "    def __init__(self, path, mode='r'):\n"
        "        self.path = path\n"
        "        self.mode = mode\n\n"
        "    def __enter__(self):\n"
        "        self._file = open(self.path, self.mode)\n"
        "        return self._file\n\n"
        "    def __exit__(self, exc_type, exc_val, exc_tb):\n"
        "        self._file.close()\n"
        "        return False  # don't suppress exceptions\n\n"
        "with ManagedFile('test.txt', 'w') as f:\n"
        "    f.write('Hello!')"
    ))

    el += section("4. Making Objects Callable")
    el.append(code(
        "class Adder:\n"
        "    def __init__(self, n): self.n = n\n"
        "    def __call__(self, x): return x + self.n\n\n"
        "add5 = Adder(5)\n"
        "print(add5(10))    # 15\n"
        "print(callable(add5))  # True"
    ))

    el += section("5. Interview Questions")
    el += q_and_a("When is __repr__ called vs __str__?",
                  "__repr__ is called by repr(), in the REPL, and as fallback if __str__ is not defined. "
                  "__str__ is called by print() and str(). If both are defined, print() uses __str__; "
                  "repr() always uses __repr__.")
    el += q_and_a("What does __exit__ returning True do?",
                  "Returning True from __exit__ suppresses any exception that occurred inside the with block. "
                  "Returning False (or None) lets the exception propagate normally.")
    save_pdf(el, f"{BASE}/10_Special_Methods/Dunder_Methods.pdf")


def pdf_solid():
    el = cover_page("19", "Design Principles — SOLID",
                    "Five Principles for Clean, Maintainable Object-Oriented Code")
    el += section("Overview")
    el += [body(
        "SOLID is an acronym for five design principles that make software designs more "
        "understandable, flexible, and maintainable. Introduced by Robert C. Martin."
    )]
    principles = [
        ("S — Single Responsibility Principle",
         "A class should have only one reason to change.",
         "Separate User, UserRepository, and EmailService instead of one God class."),
        ("O — Open/Closed Principle",
         "Open for extension, closed for modification.",
         "Add new Discount subclasses without modifying Order class."),
        ("L — Liskov Substitution Principle",
         "Subclasses must be substitutable for their base class.",
         "Any code using Shape should work with Circle or Rectangle without modification."),
        ("I — Interface Segregation Principle",
         "No class should be forced to implement methods it doesn't use.",
         "Split large interfaces: Workable, Eatable instead of one fat Worker interface."),
        ("D — Dependency Inversion Principle",
         "Depend on abstractions, not concretions.",
         "Notification depends on MessageSender (ABC), not EmailSender directly."),
    ]
    for name, defn, example in principles:
        el += section(name)
        el += [body(f"<b>Definition:</b> {defn}"), body(f"<b>Example:</b> {example}")]

    el += section("Interview Questions")
    el += q_and_a("What is the Open/Closed Principle?",
                  "Classes should be open for extension (you can add new behaviour) but closed for modification "
                  "(you shouldn't need to change existing code). Achieve this via inheritance, strategy pattern, or plugins.")
    el += q_and_a("Give a real Python example of DIP.",
                  "Use ABC as MessageSender interface. EmailSender and SMSSender both implement it. "
                  "Notification class accepts MessageSender, not EmailSender. "
                  "You can swap senders without changing Notification.")
    save_pdf(el, f"{BASE}/19_Design_Principles/SOLID.pdf")


def pdf_design_patterns():
    el = cover_page("20", "Design Patterns",
                    "Creational, Structural, Behavioural — Python Implementations")
    el += section("1. What are Design Patterns?")
    el += [body(
        "Design patterns are reusable solutions to commonly occurring problems in software design. "
        "They are not code — they are blueprints describing how to structure your code. "
        "Popularised by the 'Gang of Four' book (GoF, 1994)."
    )]
    el.append(comparison_table(
        ["Category",     "Purpose",                             "Examples"],
        [
            ["Creational", "Object creation mechanisms",         "Singleton, Factory, Builder, Prototype"],
            ["Structural", "Object composition / structure",     "Adapter, Decorator, Facade, Proxy"],
            ["Behavioural","Object interaction / responsibility","Observer, Strategy, State, Command"],
        ]
    ))
    el.append(Spacer(1, 8))

    el += section("2. Singleton Pattern")
    el += [body("Ensures only one instance of a class exists. Useful for: configuration, logging, connection pools.")]
    el.append(code(
        "class Config:\n"
        "    _instance = None\n"
        "    def __new__(cls):\n"
        "        if cls._instance is None:\n"
        "            cls._instance = super().__new__(cls)\n"
        "        return cls._instance\n\n"
        "c1 = Config(); c2 = Config()\n"
        "print(c1 is c2)  # True"
    ))

    el += section("3. Factory Pattern")
    el += [body("Creates objects without specifying the exact class. The factory decides which class to instantiate.")]
    el.append(code(
        "class NotificationFactory:\n"
        "    _registry = {'email': EmailNotif, 'sms': SMSNotif}\n\n"
        "    @classmethod\n"
        "    def create(cls, kind: str):\n"
        "        return cls._registry[kind]()"
    ))

    el += section("4. Observer Pattern")
    el += [body("One-to-many dependency: when one object changes state, all dependents are notified automatically.")]
    el.append(code(
        "class EventBus:\n"
        "    def __init__(self): self._listeners = {}\n\n"
        "    def on(self, event, fn): self._listeners.setdefault(event,[]).append(fn)\n\n"
        "    def emit(self, event, **data):\n"
        "        for fn in self._listeners.get(event, []): fn(**data)"
    ))

    el += section("5. Strategy Pattern")
    el += [body("Defines a family of algorithms, encapsulates each one, and makes them interchangeable.")]

    el += section("6. Interview Questions")
    el += q_and_a("What is the difference between Factory and Builder?",
                  "Factory creates objects in one step, hiding which class is instantiated. "
                  "Builder constructs complex objects step-by-step with a fluent interface, "
                  "giving fine-grained control over the construction process.")
    el += q_and_a("When should you NOT use design patterns?",
                  "When they add complexity without benefit. Over-engineering simple code with "
                  "patterns is an anti-pattern itself (YAGNI — You Aren't Gonna Need It). "
                  "Apply patterns only when a recurring problem clearly matches the pattern.")
    save_pdf(el, f"{BASE}/20_Design_Patterns/Design_Patterns.pdf")


def pdf_interview():
    el = cover_page("22", "Interview Preparation",
                    "100+ Python OOP Questions, Tricky Problems & MCQs")
    el += section("1. Core Concept Questions")
    qas = [
        ("What is OOP? Name its four pillars.",
         "OOP organises code around objects (data + behaviour). Four pillars: Encapsulation, Abstraction, Inheritance, Polymorphism."),
        ("Difference between class and object?",
         "Class is a blueprint/template. Object is a concrete instance of that class with its own state."),
        ("What is 'self' in Python?",
         "self is a reference to the current instance. Must be first parameter in instance methods. Python passes it automatically."),
        ("What is __init__? Is it a constructor?",
         "__init__ is the initialiser. Python's actual constructor is __new__ (allocates memory). __init__ sets up the object's initial state."),
        ("Can a class exist without __init__?",
         "Yes. Python provides a default __init__ from object. Attributes can be added dynamically."),
        ("What is method overriding?",
         "A child class provides a new implementation of a method defined in the parent class."),
        ("What is duck typing?",
         "Python checks for method/attribute presence at runtime, not class type. If it has the right methods, it works."),
        ("What is the MRO?",
         "Method Resolution Order — the order Python searches for methods in an inheritance chain. Uses C3 linearization."),
        ("What is name mangling?",
         "__name becomes _ClassName__name. Makes accidental access harder but doesn't truly hide the attribute."),
        ("Difference between @classmethod and @staticmethod?",
         "@classmethod receives cls (class reference). @staticmethod receives nothing. Use @classmethod for factories."),
        ("What is an abstract class?",
         "A class with @abstractmethod decorators. Cannot be instantiated. Forces subclasses to implement specific methods."),
        ("What are dunder/magic methods?",
         "Special methods with double underscores: __init__, __str__, __add__, etc. Called automatically by Python built-ins."),
        ("What is a descriptor?",
         "An object implementing __get__, __set__, or __delete__. Used to customise attribute access (e.g., @property uses descriptors)."),
        ("What is a mixin?",
         "A class designed to be inherited alongside other classes to add specific functionality without a full IS-A relationship."),
        ("What is a metaclass?",
         "A class whose instances are classes. type is Python's default metaclass. Used to customise class creation."),
    ]
    for q, a in qas:
        el += q_and_a(q, a)

    el += [PageBreak()]
    el += section("2. Tricky Questions")
    tricky = [
        ("What is the output of: A.x=1; class B(A): pass; class C(A): pass; A.x=2; print(B.x, C.x)?",
         "2 2. B and C inherit x from A. When A.x changes to 2, both inherit the new value (no shadowing yet)."),
        ("Why should you not use mutable default arguments in __init__?",
         "class Bad:\\n  def __init__(self, items=[]):  # items shared across ALL instances!\\n      self.items=items\\n"
         "Use: def __init__(self, items=None): self.items = items or []"),
        ("What happens if you set a class variable through an instance?",
         "An instance variable with the same name is created, shadowing the class variable for that instance only."),
        ("Can you have __init__ without __new__?",
         "Yes — this is the normal case. __new__ is inherited from object and creates the instance. __init__ just initialises it."),
        ("What does super() return?",
         "A proxy object that delegates method calls to the parent class in the MRO order. super().__init__() calls the next class in MRO."),
    ]
    for q, a in tricky:
        el += q_and_a(q, a)

    el += section("3. Coding Questions")
    for cq in [
        "Implement a Singleton class in Python",
        "Write a Stack class with __len__, __iter__, __repr__",
        "Implement a custom iterator (Countdown from N to 0)",
        "Write a context manager class for timing code",
        "Create a generic Stack[T] with type annotations",
        "Implement __add__ for a Matrix class",
        "Write a descriptor that validates positive integers",
        "Implement the Observer pattern for a stock ticker",
        "Create a mixin that adds JSON serialization to any class",
        "Write a Factory method that creates different database connections",
    ]:
        el.append(bullet(cq))

    save_pdf(el, f"{BASE}/22_Interview_Preparation/Interview_Questions.pdf")


def pdf_dataclasses():
    el = cover_page("17", "Data Classes",
                    "@dataclass — Modern Python Data Modeling")
    el += section("1. What is @dataclass?")
    el += [body(
        "@dataclass (Python 3.7+) automatically generates __init__, __repr__, and __eq__ "
        "from class annotations. It reduces boilerplate for data-holding classes."
    )]
    el.append(code(
        "from dataclasses import dataclass, field\n\n"
        "@dataclass\n"
        "class Point:\n"
        "    x: float\n"
        "    y: float\n\n"
        "p1 = Point(3, 4)\n"
        "p2 = Point(3, 4)\n"
        "print(p1)         # Point(x=3, y=4)  — auto __repr__\n"
        "print(p1 == p2)   # True              — auto __eq__"
    ))

    el += section("2. Common Parameters")
    el.append(comparison_table(
        ["Parameter", "Default", "Effect"],
        [
            ["init",   "True",  "Generate __init__"],
            ["repr",   "True",  "Generate __repr__"],
            ["eq",     "True",  "Generate __eq__"],
            ["order",  "False", "Generate __lt__, __le__, __gt__, __ge__"],
            ["frozen", "False", "Make instance immutable (generates __hash__)"],
            ["slots",  "False", "Use __slots__ for memory efficiency (3.10+)"],
        ]
    ))
    el.append(Spacer(1, 8))

    el += section("3. field() for Advanced Control")
    el.append(code(
        "from dataclasses import dataclass, field\n\n"
        "@dataclass\n"
        "class Student:\n"
        "    name: str\n"
        "    gpa: float = 0.0\n"
        "    courses: list = field(default_factory=list)  # mutable default!\n"
        "    _internal: str = field(default='x', init=False, repr=False)\n\n"
        "s = Student('Alice', 3.9)\n"
        "s.courses.append('Math')\n"
        "print(s)  # Student(name='Alice', gpa=3.9, courses=['Math'])"
    ))

    el += section("4. Frozen Dataclasses")
    el += [body("frozen=True makes the dataclass immutable. Attempts to modify raise a FrozenInstanceError. "
                "Frozen dataclasses are hashable and can be used as dict keys or in sets.")]
    el.append(code(
        "@dataclass(frozen=True)\n"
        "class Color:\n"
        "    r: int; g: int; b: int\n\n"
        "red = Color(255, 0, 0)\n"
        "# red.r = 100  → FrozenInstanceError\n\n"
        "palette = {red, Color(0, 255, 0)}  # hashable!"
    ))

    el += section("5. Interview Questions")
    el += q_and_a("What is the difference between @dataclass and namedtuple?",
                  "dataclass: mutable by default, supports methods, inheritance, validators. "
                  "namedtuple: always immutable, less boilerplate, tuple-based (indexable). "
                  "Use dataclass for most cases; namedtuple for lightweight immutable records.")
    el += q_and_a("How do you add post-init logic to a dataclass?",
                  "Define __post_init__(self). It's called after __init__ finishes. "
                  "Use it for validation or computing derived attributes.")
    save_pdf(el, f"{BASE}/17_Data_Classes/Dataclasses.pdf")


def pdf_type_hints():
    el = cover_page("18", "Type Hints",
                    "Annotations, Generics, Protocols — Python's Type System")
    el += section("1. Why Type Hints?")
    el += [body(
        "Type hints (PEP 484, 526) make code more readable and enable static analysis tools "
        "(mypy, pyright) to catch bugs before runtime. They don't affect runtime behaviour "
        "— Python remains dynamically typed."
    )]
    el.append(code(
        "def greet(name: str, times: int = 1) -> str:\n"
        "    return ('Hello, ' + name + '! ') * times\n\n"
        "result: str = greet('Alice', 3)"
    ))

    el += section("2. Common Types")
    el.append(comparison_table(
        ["Type",         "Example",                 "Note"],
        [
            ["int, float, str, bool", "def f(x: int) -> str",  "Built-ins"],
            ["list[int]",   "items: list[int]",      "Python 3.9+ (use List[int] before)"],
            ["dict[str, int]", "d: dict[str, int]",  "Key-value mapping"],
            ["Optional[T]", "val: Optional[str]",    "T | None (3.10+: str | None)"],
            ["Union[A, B]", "Union[int, str]",       "3.10+: int | str"],
            ["Callable",    "Callable[[int], str]",  "Function types"],
            ["TypeVar",     "T = TypeVar('T')",      "Generic type variable"],
        ]
    ))
    el.append(Spacer(1, 8))

    el += section("3. Generics")
    el.append(code(
        "from typing import TypeVar, Generic\n\n"
        "T = TypeVar('T')\n\n"
        "class Stack(Generic[T]):\n"
        "    def __init__(self) -> None:\n"
        "        self._items: list[T] = []\n\n"
        "    def push(self, item: T) -> None:\n"
        "        self._items.append(item)\n\n"
        "    def pop(self) -> T:\n"
        "        return self._items.pop()\n\n"
        "s: Stack[int] = Stack()\n"
        "s.push(42)   # type-safe!"
    ))

    el += section("4. Interview Questions")
    el += q_and_a("Does Python enforce type hints at runtime?",
                  "No. Type hints are purely for static analysis tools and documentation. "
                  "You can pass wrong types at runtime and Python won't raise an error (unless "
                  "you use runtime checking like pydantic or beartype).")
    el += q_and_a("What is the difference between Optional[T] and T | None?",
                  "They are equivalent. Optional[X] = Union[X, None] = X | None (Python 3.10+). "
                  "Use X | None in new code (3.10+); Optional[X] for older codebases.")
    save_pdf(el, f"{BASE}/18_Type_Hints/Type_Hints.pdf")


# ─── REMAINING STUBS ─────────────────────────────────────────────────────────

def stub_pdf(num: str, title: str, folder: str, filename: str, topics: list):
    el = cover_page(num, title, f"Complete Guide to {title}")
    for i, (head, body_text) in enumerate(topics, 1):
        el += section(f"{i}. {head}")
        el += [body(body_text)]
    save_pdf(el, f"{BASE}/{folder}/{filename}")


STUBS = [
    ("11", "Property & Descriptors",
     "11_Property_and_Descriptors", "Properties.pdf",
     [("The @property Decorator", "Provides computed attributes with validation. Getter, setter, and deleter."),
      ("Descriptor Protocol", "__get__, __set__, __delete__, __set_name__. Reusable attribute logic."),
      ("Data vs Non-data Descriptors", "Data descriptors define __set__. Non-data define only __get__."),
      ("Use cases", "Validators, lazy properties, type-checked fields, ORM columns."),
      ("Interview Q", "Q: What is a descriptor? A: Any object that defines __get__, __set__, or __delete__. @property is a descriptor.")]),

    ("12", "Static and Class Methods",
     "12_Static_and_Class_Methods", "Static_Class_Methods.pdf",
     [("Recap", "@staticmethod — no self/cls. @classmethod — receives cls."),
      ("Factory Pattern with @classmethod", "Employee.from_dict(), Date.today(), Config.load_from_env()"),
      ("When to use @staticmethod", "Utility functions that logically belong to the class but don't need its state."),
      ("Anti-patterns", "Don't make everything static. If you need self/cls, use instance/class method."),
      ("Interview Q", "Q: Can a child class override a @classmethod? A: Yes. cls will be the child class.")]),

    ("13", "Composition and Aggregation",
     "13_Composition_and_Aggregation", "Composition.pdf",
     [("Relationships", "Association (uses), Aggregation (has-a, independent), Composition (has-a, owned)."),
      ("Composition vs Inheritance", "Prefer composition for flexibility. Inherit only for IS-A relationships."),
      ("Diagrams", "Association: A ----> B. Aggregation: A <>---> B. Composition: A <*>---> B."),
      ("Code", "Car owns Engine (composition). Book references Author (aggregation)."),
      ("Interview Q", "Q: When to prefer composition over inheritance? A: When the relationship is HAS-A, not IS-A.")]),

    ("14", "Multiple Inheritance",
     "14_Multiple_Inheritance", "Multiple_Inheritance.pdf",
     [("Syntax", "class Child(Parent1, Parent2): ..."),
      ("Mixin Pattern", "Small classes with focused functionality mixed into other classes."),
      ("Common Mixins", "JSONMixin, LogMixin, ValidateMixin, SerializeMixin."),
      ("Pitfalls", "Complexity, diamond problem, attribute conflicts. Keep mixins small and focused."),
      ("Interview Q", "Q: What is a mixin? A: A class providing specific functionality to be inherited but not meant as a standalone base class.")]),

    ("15", "Method Resolution Order",
     "15_Method_Resolution_Order", "MRO.pdf",
     [("C3 Linearization", "Algorithm that defines method lookup order in multiple inheritance."),
      ("Viewing MRO", "ClassName.__mro__ or ClassName.mro(). Lists classes in lookup order."),
      ("Cooperative super()", "super() follows MRO, calling each class in order exactly once."),
      ("Diamond Problem", "Base.__init__ is called once despite two paths thanks to cooperative super()."),
      ("Interview Q", "Q: What is MRO? A: Method Resolution Order — the sequence Python searches for attributes/methods in an inheritance hierarchy, computed using C3 Linearization.")]),

    ("16", "Abstract Base Classes",
     "16_Abstract_Base_Classes", "ABC.pdf",
     [("abc module", "from abc import ABC, abstractmethod"),
      ("Purpose", "Define contracts. Prevent instantiation. Force subclass implementation."),
      ("@abstractmethod", "Methods that must be overridden. Also: @property + @abstractmethod."),
      ("register()", "ABC.register(SomeClass) — virtual subclass without inheritance."),
      ("Interview Q", "Q: Difference between ABC and interface? A: Python has no interface keyword. ABC with all abstract methods acts as an interface.")]),

    ("21", "Real-World Projects",
     "21_Real_World_Projects", "Projects_Overview.pdf",
     [("Project 1: Library Management", "Classes: Book, Member, Loan, Library. Features: issue/return, fines, search."),
      ("Project 2: Bank System", "Classes: Account, Transaction, Customer, Bank. Features: deposit/withdraw, interest, statements."),
      ("Project 3: Hospital System", "Classes: Patient, Doctor, Appointment, Ward. Features: scheduling, records, billing."),
      ("How to approach projects", "1. Identify nouns (classes). 2. Identify verbs (methods). 3. Draw class diagram. 4. Code bottom-up."),
      ("UML Class Diagram", "Rectangle with class name, attributes, and methods. Arrows for relationships.")]),

    ("23", "Practice Exercises",
     "23_Practice", "Practice_Guide.pdf",
     [("Beginner (30 Qs)", "Classes, objects, constructors, encapsulation, basic inheritance."),
      ("Intermediate (30 Qs)", "Dunder methods, descriptors, design patterns, ABC, mixins."),
      ("Advanced (30 Qs)", "Metaclasses, descriptors, type system, protocol, composition patterns."),
      ("How to use", "Attempt without looking at solution. Time yourself. Review, refactor, improve."),
      ("Recommended schedule", "2 questions per day = complete all 90 questions in 45 days.")]),
]


def build_all_pdfs():
    print("Generating PDFs...")
    pdf_01_introduction()
    pdf_02_classes()
    pdf_03_constructors()
    pdf_04_variables()
    pdf_05_methods()
    pdf_06_encapsulation()
    pdf_07_abstraction()
    pdf_08_inheritance()
    pdf_09_polymorphism()
    pdf_10_dunder()
    pdf_solid()
    pdf_design_patterns()
    pdf_interview()
    pdf_dataclasses()
    pdf_type_hints()

    for num, title, folder, filename, topics in STUBS:
        stub_pdf(num, title, folder, filename, topics)

    print(f"✅ All PDFs generated!")


if __name__ == "__main__":
    build_all_pdfs()
