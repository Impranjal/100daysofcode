res = [
    {"rc": 244, "stderr": ["s", "error msg"]},
    {"env": None, "rc": 0, "stdout": None, "stderr": None}
]
result_list = []
app_stop = False
error_message = None

for item in res:
    # Check if "rc" equals 0
    if "rc" in item and item["rc"] == 0:
        app_stop = True
        result_list.append({
        "app_stop": app_stop})
    # Check for "stderr" and create error_message
    if "stderr" in item and item["stderr"]:
        error_message = item["stderr"][-1]
          # Taking the last element from stderr list

if error_message != None:
    result_list = error_message  # Append individual dictionary to result_list
    
# Print the result_list
print(result_list)