import os

def rename_files(folder_path):
    # Get list of files in the folder
    files = os.listdir(folder_path)

    # Sort the files to ensure consistent numbering
    files.sort()

    # Counter for numbering files
    count = 1
    label = "bread"

    # Iterate over each file and rename it
    for file_name in files:
        # Construct the new file name with the sequential number
        new_name = f"{label}_{count:03d}"  # Corrected formatting for sequential number
        new_name += os.path.splitext(file_name)[1]  # Preserve file extension

        # Construct the full paths for old and new names
        old_path = os.path.join(folder_path, file_name)
        new_path = os.path.join(folder_path, new_name)

        # Rename the file
        os.rename(old_path, new_path)

        # Increment the counter for the next file
        count += 1
        

if __name__ == "__main__":
    # Specify the folder path where you want to rename files
    folder_path = "D:\TITO\Documents\Deep-learning\edible-classification\dataset\\bread-edible-remove"

    # Call the function to rename files in the specified folder
    rename_files(folder_path)