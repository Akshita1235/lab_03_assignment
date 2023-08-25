class FlightTable:
    def __init__(self):
        self.entries = []
    
    def add_entry(self, entry):
        self.entries.append(entry)
    
    def print_table(self):
        print("P_ID\nProcess\n\tStart Time\nPriority")
        print("-" * 40)
        for entry in self.entries:
            print(f"{entry['P_ID']}\t{entry['Process']}\t\t{entry['Start Time (ms)']}\t\t{entry['Priority']}")
    
    def sort_table(self, sort_param):
        sort_keys = ['P_ID', 'Start Time (ms)', 'Priority']
        if sort_param in [1, 2, 3]:
            self.entries.sort(key=lambda x: x[sort_keys[sort_param - 1]])
        else:
            print("Invalid sorting parameter")
    
    def get_sorting_param(self):
        return int(input("\nChoose a sorting parameter: [1. P_ID, 2. Start Time, 3. Priority]: "))

flight_table = FlightTable()

data = [
    {"P_ID": "P1", "Process": "VSCode", "Start Time (ms)": 100, "Priority": "MID"},
    {"P_ID": "P23", "Process": "Eclipse", "Start Time (ms)": 234, "Priority": "MID"},
    {"P_ID": "P93", "Process": "Chrome", "Start Time (ms)": 189, "Priority": "High"},
    {"P_ID": "P42", "Process": "JDK", "Start Time (ms)": 9, "Priority": "High"},
    {"P_ID": "P9", "Process": "CMD", "Start Time (ms)": 7, "Priority": "High"},
    {"P_ID": "P87", "Process": "NotePad", "Start Time (ms)": 23, "Priority": "Low"}
]

for entry in data:
    flight_table.add_entry(entry)

print("Flight Table:")
flight_table.print_table()

sorting_param = flight_table.get_sorting_param()
flight_table.sort_table(sorting_param)

print("\nSorted Flight Table:")
flight_table.print_table()


