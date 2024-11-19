import unittest

from absl.testing import absltest
import graph as gh
import numericals as nm
import problem as pr



defs = pr.Definition.from_txt_file('defs.txt', to_dict=True)
rules = pr.Theorem.from_txt_file('rules.txt', to_dict=True)

# Specify the attributes you want to check for in each definition
# Specify the attributes you want to check for in each definition
attributes_to_check = ['construction', 'rely', 'deps', 'basics', 'numerics', 'points', 'args']

# Initialize a dictionary to track missing attributes across all definitions
missing_attributes = {attr: [] for attr in attributes_to_check}

# Function to check missing attributes across all definitions
def check_missing_attributes(defs):
    for key, obj in defs.items():
        for attr in attributes_to_check:
            if not hasattr(obj, attr):
                missing_attributes[attr].append(key)

# Call the function
check_missing_attributes(defs)

# Print the results
for attr, missing_keys in missing_attributes.items():
    if missing_keys:
        print(f"Attribute '{attr}' is missing in keys: {', '.join(missing_keys)}")
    else:
        print(f"Attribute '{attr}' is present in all definitions.")

def print_defs_info(defs):
    for key, obj in defs.items():
        print(f"Key: {key}")
        # Accessing the object's internal attributes
        obj_attrs = vars(obj)

        # Printing the relevant attributes
        for attr, value in obj_attrs.items():
            if isinstance(value, list):
                print(f"  {attr} (count: {len(value)}): {value}")
            elif hasattr(value, '__dict__'):
                print(f"  {attr}: {value} (with internal data: {vars(value)})")
            else:
                print(f"  {attr}: {value}")

        print()  # New line for better separation between entries

# Call the function
print_defs_info(defs)
