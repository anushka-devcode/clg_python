t_slots = ["9-10 AM", "10-11 AM", "11-12 PM", "1-2 PM", "2-3 PM", "3-4 PM"]

tt = []
ocp_slots = {}  
def is_available(tch, stds, clsr, t):
    if ocp_slots.get(tch)==t:
        return False
    if any(ocp_slots.get(std)==t for std in stds):
        return False
    if ocp_slots.get(clsr)==t:
        return False
    return True

def schedule_class(c, tch, stds, clsr):
    for t in t_slots:
        if is_available(tch, stds, clsr, t):
            tt.append({"Course": c, "Teacher": tch, "Students": stds, "Classroom": clsr, "Time": t})
            ocp_slots[tch]=t
            for std in stds:
                ocp_slots[std]=t
            ocp_slots[clsr]=t
            print("Scheduled ",c," at ",t)
            return
    print("Could not schedule ",c," due to clashes")
    
schedule_class("Math", "M", ["S1", "S2"], "6205")
schedule_class("DSA", "D", ["S2", "S3"], "9205")
schedule_class("DE", "A", ["S1", "S3"], "9206")  
schedule_class("Python", "P", ["S1", "S2", "S3"], "10101")  
print("\nFinal Timetable:")
for entry in tt:
    print(f"{entry['Course']} | {entry['Teacher']} | {entry['Classroom']} | {entry['Time']}")
