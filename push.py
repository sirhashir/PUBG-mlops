from github import Github
import os

# Create a Github instance using the Personal Access Token
g = Github(os.environ['FULL_ACCESS'])

# Get the repository that you want to work with
repo = g.get_repo("Yuvraj-Sharma-2000/ec2")

# Create a folder inside the repository
folder_name = "I did it"
repo.create_file(f"{folder_name}/Katze.txt", "Initial commit", "")

# # Push a file inside the folder
# file_name = "example.txt"
# file_path = os.path.join(folder_name, file_name)
# with open(file_path, "w") as f:
#     f.write("This is an example file.")
# repo.create_file(file_path, "Add example file", "")
