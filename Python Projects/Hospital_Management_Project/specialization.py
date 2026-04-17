class Specialization:
    def __init__(self, name):
        self.name = name
        self.queue = []

    def add_patient(self, patient):
        self.queue.append(patient)
        print(f"{patient.name} added to {self.name}")

    def get_next_patient(self):
        if self.queue:
            return self.queue.pop(0)
        return None

    def list_patients(self):
        if not self.queue:
            print("No patients.")
            return

        for p in self.queue:
            print(p)