 Simple Expert System (Medical Domain)

This project demonstrates a 'basic expert system' implemented in Python.  
It uses a rule-based approach to diagnose diseases based on given symptoms.

---

~ Features
- Define rules that map "symptoms → disease".
- Add multiple rules dynamically.
- Diagnose based on user-provided symptoms.
- Returns `"Unknown disease"` if no matching rule is found.

---

~ How It Works
1. Each **Rule** consists of:
   - A list of symptoms
   - A disease name
2. The "ExpertSystem" stores rules and checks if all symptoms in a rule match the input.
3. If a match is found, the corresponding disease is returned.


~ Test diagnoses
print(es.diagnose(["fever", "cough", "headache"]))  # Output: Flu
print(es.diagnose(["fever", "rash", "itching"]))    # Output: Chickenpox
