from patient import Patient
from specialization import Specialization


class OperationsManager:
    def __init__(self):
        self.specializations = {
            "cardiology": Specialization("Cardiology"),
            "neurology": Specialization("Neurology")
        }

    def run(self):
        while True:
            print("\n1. Add Patient")
            print("2. List Patients")
            print("3. Exit")

            choice = input("Enter choice: ")

            if choice == "1":
                name = input("Enter name: ")
                status = int(input("Enter status: "))
                spec = input("Enter specialization: ")

                patient = Patient(name, status)

                if spec in self.specializations:
                    self.specializations[spec].add_patient(patient)
                else:
                    print("Invalid specialization")

            elif choice == "2":
                spec = input("Enter specialization: ")

                if spec in self.specializations:
                    self.specializations[spec].list_patients()

            elif choice == "3":
                print("Exiting...")
                break