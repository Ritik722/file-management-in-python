import os

def soldier(directory, enter_txt_fname, enter_lname):
    """
    This function organizes files in the given directory. 
    It renames all files with the specified extension and capitalizes the content of a specified text file.

    Parameters:
    directory (str): The directory path where files are located.
    enter_txt_fname (str): The name of the text file whose content should be capitalized.
    enter_lname (str): The file extension (e.g., '.txt') to filter files for renaming.
    """
    try:
        i = 0
        # Renaming files with the specified extension
        for file in os.listdir(directory):
            if file.endswith(enter_lname):
                i += 1
                old_content = os.path.join(directory, file)
                new_content = os.path.join(directory, f"{i}{enter_lname}")
                os.rename(old_content, new_content)

        # Capitalizing the content of the specified text file
        txt_filepath = os.path.join(directory, enter_txt_fname)
        if os.path.exists(txt_filepath):
            with open(txt_filepath, 'r') as f:
                content = f.read()
            with open(txt_filepath, 'w') as f:
                f.write(content.title())
        else:
            print(f"File '{enter_txt_fname}' not found in the directory '{directory}'.")

    except Exception as e:
        print(f"An error occurred: {e}")

if _name_ == "_main_":
    # Input from the user
    directory = input("Enter the working directory: ")
    enter_txt_fname = input("Enter the txt filename: ")
    enter_lname = input("Enter the file extension (e.g., .txt): ")

    # Calling the function
    soldier(directory, enter_txt_fname, enter_lname)
