loopVariable = True
from collections import defaultdict

# Creating a function that will open a text file and create a dictionary of patients
def readPatientsFromFile():
    patients = defaultdict(list)
    with open('patients.txt', 'r') as f:
        # In f, go line by line, if there are 8 things in an index (patient id, check up date, body temp, etc)
        # Add the patient visit to a new dictionary
        for line in f:
            patientInfo = line.strip().split(',')
            if len(patientInfo) == 8:
                patient_id, checkup_date, bodyTemp, heartRate, respRate, sysBP, diaBP, oSat = patientInfo
                patients[patient_id].append({
                    "patientId": patient_id,
                    "date": checkup_date,
                    "temp": bodyTemp,
                    "hr": heartRate,
                    "rr": respRate,
                    "sbp": sysBP,
                    "dbp": diaBP,
                    "spo2": oSat
                })
    return patients

# This function will take the new dictionary created and display it in an organized manner
def displayPatientData(patients, patientID=None):
    # If the user inputs a specific patient ID, print the patients visits in an organized manner
    if patientID:
        if patientID in patients:
            for patient in patients[patientID]:
                print(f'Patient ID: {patient["patientId"]}')
                print(f' Visit Date: {patient["date"]}')
                print(f'  Body Temperature: {patient["temp"]}')
                print(f'  Heart Rate: {patient["hr"]}')
                print(f'  Respiratory Rate: {patient["rr"]}')
                print(f'  Systolic Blood Pressure: {patient["sbp"]}')
                print(f'  Diastolic Blood Pressure: {patient["dbp"]}')
                print(f'  Oxygen Saturation: {patient["spo2"]}\n')
        # If the patient ID is not in the dicitonary, output this message
        else:
            print(f"No data found for patient with ID {patientID}.")
    # If the previous if statement is not true, print every visit
    else:
        for patient_id, patient_data in patients.items():
            for patient in patient_data:
                print(f'Patient ID: {patient["patientId"]}')
                print(f' Visit Date: {patient["date"]}')
                print(f'  Body Temperature: {patient["temp"]}')
                print(f'  Heart Rate: {patient["hr"]}')
                print(f'  Respiratory Rate: {patient["rr"]}')
                print(f'  Systolic Blood Pressure: {patient["sbp"]}')
                print(f'  Diastolic Blood Pressure: {patient["dbp"]}')
                print(f'  Oxygen Saturation: {patient["spo2"]}\n')

# This function will display vitals for a specified patient (body temp, heart rate, etc.)
def displayStats(patients, patientId=0):
    # If the patient ID is a specific number,
    # check if that patient ID is in the dictionary
    # and display the average stats of that patients visits
    if patientId != '0':
        if patientId in patients:
            patient_data = patients[patientId]
            if patient_data:
                temp_sum = hr_sum = rr_sum = sbp_sum = dbp_sum = spo2_sum = 0
                for patient in patient_data:
                    temp_sum += float(patient['temp'])
                    hr_sum += int(patient['hr'])
                    rr_sum += int(patient['rr'])
                    sbp_sum += int(patient['sbp'])
                    dbp_sum += int(patient['dbp'])
                    spo2_sum += int(patient['spo2'])
                num_patients = len(patient_data)
                avg_temp = temp_sum / num_patients
                avg_hr = hr_sum / num_patients
                avg_rr = rr_sum / num_patients
                avg_sbp = sbp_sum / num_patients
                avg_dbp = dbp_sum / num_patients
                avg_spo2 = spo2_sum / num_patients
                print(f"Average temperature: {avg_temp:.2f} °C")
                print(f"Average heart rate: {avg_hr:.2f} bpm")
                print(f"Average respiratory rate: {avg_rr:.2f} bpm")
                print(f"Average systolic blood pressure: {avg_sbp:.2f} mmHg")
                print(f"Average diastolic blood pressure: {avg_dbp:.2f} mmHg")
                print(f"Average oxygen saturation: {avg_spo2:.2f} %\n")
            else:
                print(f"No data found for patient with ID {patientId}.")
        # If the patient ID is not in the dictionary, print this message
        else:
            print(f"No data found for patient with ID {patientId}.\n")
    # If the user does not enter a specific patient ID, print the average stats for all visits
    else:
        all_data = []
        for patient_data in patients.values():
            all_data.extend(patient_data)
        if all_data:
            temp_sum = hr_sum = rr_sum = sbp_sum = dbp_sum = spo2_sum = 0
            for patient in all_data:
                temp_sum += float(patient['temp'])
                hr_sum += int(patient['hr'])
                rr_sum += int(patient['rr'])
                sbp_sum += int(patient['sbp'])
                dbp_sum += int(patient['dbp'])
                spo2_sum += int(patient['spo2'])
            num_patients = len(all_data)
            avg_temp =temp_sum / num_patients
            avg_hr = hr_sum / num_patients
            avg_rr = rr_sum / num_patients
            avg_sbp = sbp_sum / num_patients
            avg_dbp = dbp_sum / num_patients
            avg_spo2 = spo2_sum / num_patients
            print(f"Average temperature: {avg_temp:.2f} °C")
            print(f"Average heart rate: {avg_hr:.2f} bpm")
            print(f"Average respiratory rate: {avg_rr:.2f} bpm")
            print(f"Average systolic blood pressure: {avg_sbp:.2f} mmHg")
            print(f"Average diastolic blood pressure: {avg_dbp:.2f} mmHg")
            print(f"Average oxygen saturation: {avg_spo2:.2f} %\n")
        else:
            print("No data found for any patients.\n")
# This function will add new patient visit information with prompts given to the user
def addPatientData(patients, fileName):
    # Asking the user to input patient ID, visit date, body temp, etc.
    patientId = input("Enter patient ID: ")
    date = input("Enter visit date (YYYY-MM-DD): ")
    temp = float(input("Enter body temperature (Celsius): "))
    hr = int(input("Enter heart rate (bpm): "))
    rr = int(input("Enter respiratory rate (breaths per minute): "))
    sbp = int(input("Enter systolic blood pressure (mmHg): "))
    dbp = int(input("Enter diastolic blood pressure (mmHg): "))
    spo2 = int(input("Enter oxygen saturation (%): "))
    # The following are checks to see if the information the user is entering is valid
    if temp <= 35.0 or temp >= 42.0:
        print('Invalid temperature. Please enter a temperature between 35.0 and 42.0 Celsius.')
        return
    if hr <= 30 or hr >= 180:
        print('Invalid heart rate. Please enter a heart rate between 30 and 180 bpm.')
        return
    if rr <= 5 or rr >= 40:
        print('Invalid heart rate. Please enter a heart rate between 5 and 40 bpm.')
        return
    if sbp <= 70 or sbp >= 200:
        print('Invalid systolic blood pressure. Please enter a systolic blood pressure between 30 and 180 mmHg.')
        return
    if dbp <= 40 or dbp >= 120:
        print('Invalid diastolic blood pressure. Please enter a diastolic blood pressure between 30 and 120 mmHg.')
        return
    if spo2 <= 70 or spo2 >= 100:
        print('Invalid oxygen saturation. Please enter an oxygen saturation between 70 and 100 %.')
        return
    # Once the checks are passed, add the new patieint to the dictionary and update the text file/dictionary
    newPatient = {
        "patientId": patientId,
        "date": date,
        "temp": temp,
        "hr": hr,
        "rr": rr,
        "sbp": sbp,
        "dbp": dbp,
        "spo2": spo2
    }

    if patientId in patients:
        patients[patientId].append(newPatient)
    else:
        patients[patientId] = newPatient

    with open(fileName, 'a') as f:
        f.write(','.join([str(value) for value in newPatient.values()]) + '\n')

    print(f"Visit added for patient # {patientId}.\n")
# This function will find visits based on certain dates
# If the year prompt is 0, display all years
# If the month prompt is 0, display all months for the specified year
def findVisitsByDate(patients, year=None, month=None):
    results = []
    for patient_id, visits in patients.items():
        for visit in visits:
            # Check if visit has a complete date
            if len(visit['date']) == 10:
                visit_year = int(visit['date'][0:4])
                visit_month = int(visit['date'][5:7])
                # Check if year matches
                if year is None or year == 0 or visit_year == year:
                    # Check if month matches
                    if month is None or month == 0 or visit_month == month:
                        results.append((patient_id, visit))
    # If the year and month do not exist in the dictionary, print this message
    if not results:
        print('No visits found for the specified year/month.\n')
    # If the year and month are valid, print all of the visits
    else:
        for result in results:
            patient_id, visit = result
            print(f"Patient ID: {patient_id}")
            print(f"Visit Date: {visit['date']}")
            print(f" Body Temperature: {visit['temp']}")
            print(f" Heart Rate: {visit['hr']}")
            print(f" Respiratory Rate: {visit['rr']}")
            print(f" Systolic Blood Pressure: {visit['sbp']}")
            print(f" Diastolic Blood Pressure: {visit['dbp']}")
            print(f" Oxygen Saturation: {visit['spo2']}\n")
# This program will check if there is a patient that has critical vitals and print the patient that needs a follow-up
def findPatientsWhoNeedFollowUp(patients):
    patients_need_follow_up = []
    for patient_id, visits in patients.items():
        for visit in visits:
            if (int(visit["hr"]) > 100 or int(visit["hr"]) < 60 or
                int(visit["sbp"]) > 140 or int(visit["dbp"]) > 90 or
                int(visit["spo2"]) < 90):
                print(f"Patient ID {patient_id} needs a follow-up visit.")
                patients_need_follow_up.append(patient_id)
                break
    if not patients_need_follow_up:
        print("No patients need follow-up visits.")

# This function will delete all visits of a specified patient (if the patient exists in the dictionary)
def deleteAllVisitsOfPatient(patients, patientID, fileName):
    if patientID not in patients:
        print(f"No data found for patient with ID {patientID}.")
        return

    # Remove all visits of the specified patient from the dictionary
    del patients[patientID]

    # Write the remaining patient data to the file
    with open(fileName, 'w') as f:
        for patient_id, visits in patients.items():
            for visit in visits:
                f.write(
                    f"{visit['patientId']},{visit['date']},{visit['temp']},{visit['hr']},{visit['rr']},{visit['sbp']},{visit['dbp']},{visit['spo2']}\n")

    print(f"All visits for patient with ID {patientID} have been deleted.")

# While the loopVariable is true, keep running the program
while loopVariable == True:
    # Prints the different options for the Health Information System
    print('\nWelcome to the Health Information System\n\n'
          '1. Display all patient data\n'
          '2. Display patient data by ID\n'
          '3. Add patient data\n'
          '4. Display patient statistics\n'
          '5. Find visits by year, month, or both\n'
          '6. Find patients who need follow-up\n'
          '7. Delete all visits of a particular patient\n'
          '8. Quit\n\n')
    # This will check if the user is inputting a number between 1 and 8 (inclusive)
    # If they are not, 'Invalid choice. Please try again.' will be printed and the user will be prompted to enter a valid number
    while True:
        try:
            choice = int(input('Enter your choice (1-8): '))
            if choice > 8 or choice < 1:
                raise ValueError

        except ValueError:
            print('Invalid choice. Please try again.\n')
            continue

        except:
            print('Invalid choice. Please try again.\n')
            continue
        else:
            break
    # If the user inputs 1, display all patient data
    if choice == 1:
        patients = readPatientsFromFile()
        displayPatientData(patients)
    # If the user inputs 2, display patient data by ID
    elif choice == 2:
        patients = readPatientsFromFile()
        patientChoice = input('Which patient ID?: ')
        displayPatientData(patients, patientChoice)
    # If the user inputs 3, Add patient data
    elif choice == 3:
        patients = readPatientsFromFile()
        addPatientData(patients, 'patients.txt')
    # If the user inputs 4, Display patient statistics
    elif choice == 4:
        patients = readPatientsFromFile()
        patientChoice = input('Enter patient ID (or \'0\' for all patients): ')
        displayStats(patients,patientChoice)
    # If the user inputs 5, Find visits by year, month, or both
    elif choice == 5:
        patientYear = int(input('Enter year (YYYY) (or 0 for all years): '))
        patientMonth = int(input('Enter month (MM) or (0 for all months): '))
        patients = readPatientsFromFile()
        findVisitsByDate(patients, patientYear, patientMonth)
    # If the user inputs 6, Find patients who need follow-up
    elif choice == 6:
        patients = readPatientsFromFile()
        follow_up = findPatientsWhoNeedFollowUp(patients)
        print(follow_up)
    # If the user inputs 7, Delete all visits of a particular patient
    elif choice == 7:
        patients = readPatientsFromFile()
        patientChoice = input('Enter patient ID?: ')
        deletion = deleteAllVisitsOfPatient(patients, patientChoice,'patients.txt')
        print(deletion)
    # If the user inputs 8, quit the program
    elif choice == 8:
        break
    # If the loopVariable is true, keep running the program
    if loopVariable == True:
        continue