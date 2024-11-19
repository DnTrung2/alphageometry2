import problem as pr

def inspect_definition():
    # Load definitions from the file
    defs = pr.Definition.from_txt_file('defs.txt', to_dict=True)
    
    # Access the 'semicircle' definition
    semicircle_def = defs.get('semicircle')
    
    if semicircle_def:
        # Print out the details of the 'semicircle' definition
        print("Semicircle Definition:")
        print(semicircle_def)
        
        # Print specific attributes of the 'semicircle' definition
        # Replace 'attribute_name' with the actual attribute names you want to print
        if hasattr(semicircle_def, 'name'):
            print(f"Name: {semicircle_def.name}")
        if hasattr(semicircle_def, 'description'):
            print(f"Description: {semicircle_def.description}")
        if hasattr(semicircle_def, 'some_other_attribute'):
            print(f"Some Other Attribute: {semicircle_def.some_other_attribute}")
    else:
        print("No definition found for 'semicircle'")

if __name__ == "__main__":
    inspect_definition()