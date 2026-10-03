# Python-Object-Oriented-Programming-Mastery
# 👑 Lecture 01: Classes and Objects (The Basics)

In this first lecture, I successfully transitioned from **Procedural Programming** to **Object-Oriented Programming (OOP)** in Python. I built a dynamic blueprint and generated physical objects using industrial standards.

---

### What I Learned & Implemented:

1. **`class` Blueprint:** Created the `Student` class as a reusable structural template.
2. **`pass` Statement:** Learned how `pass` acts as a placeholder to prevent syntax indentation errors in empty blocks.
3. **The Constructor (`__init__`):** Mastered how data is automatically packaged inside an object at the moment of creation without manually mapping attributes outside the class.
4. **The `self` Keyword:** Understood the invisible link that connects class methods back to the calling object (`s1` vs `s2`).
5. **Methods over Print Statements:** Implemented the `introduce(self)` method to prevent code duplication (following the **DRY Principle: Don't Repeat Yourself**).

---

### 💻 Code Snippet Overview:
- Instantiated two distinct student profiles (`s1` for Kinza, `s2` for Sana).
- Dynamically executed internal class functions to output unique object states via a single automated line of call.
-


---

## 🏛️ Lecture 02: Instance vs Class Variables & Parametric Methods

In this second lecture, I mastered memory optimization using shared static properties and engineered data flows to turn temporary runtime arguments into permanent object states.

### 🧠 What I Learned & Implemented:

1. **Class Variables vs Instance Variables:** Implemented `university_name = "IUB"` as a static class-level property to optimize memory across all objects, while keeping `name` and `roll_no` unique to each instance state.
2. **Temporary vs Permanent Attributes:** Learned how external parameters passed inside a method remain temporary, and how to permanently map them using `self.marks = marks` to make them globally accessible across other class structures.
3. **Multi-Functional State Sharing:** Engineered the `print_report_card(self)` method to successfully read and output instance attributes modified by completely independent method cycles, eliminating the need to pass redundant parameters.

### 💻 Code Snippet Overview:
- Verified unique student profile evaluations (`sana` and `hina`) mapping back to a single shared enterprise property (`IUB`).
- Successfully tracked global state variables across multi-layered method executions.
-
