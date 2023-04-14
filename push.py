from github import Github
import os

# Create a Github instance using the Personal Access Token
g = Github(os.environ['FULL_ACCESS'])

# Get the repository that you want to work with
repo = g.get_repo("Yuvraj-Sharma-2000/ec2")

# Define the folder and file names
folder_name = "I did it"
file_name = "Katze sensi.txt"
file_path = f"{folder_name}/{file_name}"

# Delete the folder and its contents if it already exists
try:
    folder = repo.get_contents(folder_name)
    repo.delete_file(folder.path, "Deleting folder", folder.sha)
    print(f"Deleted folder {folder_name}")
except Exception as e:
    pass

# Create the new folder
repo.create_file(folder_name, "Creating folder", "")

# Create the file
file_contents = "This is the new content of the file"
repo.create_file(file_path, "Creating file", file_contents)
print(f"Created file {file_path}")