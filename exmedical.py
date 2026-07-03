#Write a program to developing expert system for specific domain (ex- medical)

class Rule:
    def __init__(self, symptoms, disease):
        self.symptoms = symptoms
        self.disease = disease 

class ExpertSystem:
    def __init__(self):
        self.rules = []

    def add_rule(self, rule):
        self.rules.append(rule)

    def diagnose(self, symptoms):
        for rule in self.rules:
            if all(symptom in symptoms for symptom in rule.symptoms):
                return rule.disease
        return "Unknown disease"


rule1 = Rule(["fever", "cough", "headache"], "Flu")
rule2 = Rule(["fever", "rash", "itching"], "Chickenpox")
rule3 = Rule(["headache", "nausea", "vomiting"], "Migraine")


es = ExpertSystem()
es.add_rule(rule1)
es.add_rule(rule2)
es.add_rule(rule3)

symptoms = ["fever", "cough", "headache"]
print(es.diagnose(symptoms))  # Output: Flu


symptoms = ["fever", "rash", "itching"]
print(es.diagnose(symptoms))