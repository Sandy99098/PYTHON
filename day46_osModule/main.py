# os module in python
import os
# os.mkdir("day46_osModule/python practice")

# for i in range(2):
#     os.mkdir(f"day46_osModule/python practice/day{i+1}")

# #rename 
# for i in range(2):
#     os.rename(f"day46_osModule/python practice/day{i+1}",f"day46_osModule/python practice/Tutorial day{i+1}")

# folders=os.listdir("day46_osModule")
# # print(folders)

# for folder in folders:
#     print(folder)
#     print(os.listdir(f"python practice\{folder}"))


#  for making multiple folder and files in it 

# import os
# def create_project_folder(folder_name):
#     # Create directory for the project
#     project_path = os.path.join(os.getcwd(), folder_name)
#     os.makedirs(project_path, exist_ok=True)

#     # Create main.py file
#     main_py_path = os.path.join(project_path, "main.py")
#     with open(main_py_path, "w") as main_py_file:
#         main_py_file.write("# Your Python code goes here\n")

#     # Create README.md file
#     readme_md_path = os.path.join(project_path, "README.md")
#     with open(readme_md_path, "w") as readme_md_file:
#         readme_md_file.write(f"# {folder_name}\n\n")

#     print(f"Project folder '{folder_name}' created successfully.")

# # Example usage to create folders from day60 to day100
# for day in range(60, 101):
#     create_project_folder(f"day{day}")
