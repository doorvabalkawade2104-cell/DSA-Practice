class Hospital:
    def __init__(self):
        self.patient_list = []

    def add_patient(self):
        p_id = input("Enter Patient ID: ")
        p_name = input("Enter Patient Name: ")

        print("\nPriority:")
        print("1. Critical")
        print("2. Serious")
        print("3. Normal")

        priority = int(input("Enter Priority (1-3): "))

        if priority not in [1, 2, 3]:
            print("Invalid Priority!")
            return

        patient = {
            "id": p_id,
            "name": p_name,
            "priority": priority
        }

        self.patient_list.append(patient)

        
        self.patient_list.sort(key=lambda p: p["priority"])

        print("Patient added successfully!")

    # display
    def display_next(self):
        if not self.patient_list:
            print("No patients waiting!")
        else:
            patient = self.patient_list[0]
            print("\nNext Patient to be Treated:")
            print("Patient ID:", patient["id"])
            print("Patient Name:", patient["name"])
            print("Priority:", patient["priority"])

    #remove 
    def remove_patient(self):
        if not self.patient_list:
            print("No patients to treat!")
        else:
            patient = self.patient_list.pop(0)
            print("\nPatient Treated Successfully!")
            print("Patient ID:", patient["id"])
            print("Patient Name:", patient["name"])

    # 4. display
    def display_all(self):
        if not self.patient_list:
            print("No waiting patients!")
        else:
            print("\nWaiting Patients in Priority Order:")
            print("------------------------------------")

            for patient in self.patient_list:
                if patient["priority"] == 1:
                    status = "Critical"
                elif patient["priority"] == 2:
                    status = "Serious"
                else:
                    status = "Normal"

                print("Patient ID:", patient["id"])
                print("Patient Name:", patient["name"])
                print("Priority:", status)
                print("------------------------------------")


hospital = Hospital()

while True:
    print("\n----- HOSPITAL EMERGENCY -----")
    print("1. Add Patient")
    print("2. Display Next Patient")
    print("3. Remove Patient (Dequeue)")
    print("4. Display All Patients")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        hospital.add_patient()

    elif choice == 2:
        hospital.display_next()

    elif choice == 3:
        hospital.remove_patient()

    elif choice == 4:
        hospital.display_all()

    elif choice == 5:
        print("Exiting ...")
        break

    else:
        print("Invalid Choice!")