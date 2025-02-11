import os, shutil, sys
from datetime import datetime

def backupfile(source_dir, dest_dir):
    if not os.path.exists(source_dir):
        print("Error: The source directory '{source_dir}' does not exi")
    if not os.path.exists(dest_dir):
        print("Error: The destination directory '{dest_dir}' does not exist")
        return
    for filename in os.listdir(source_dir):
        sororce_file = os.path.join(source_dir, filename)
        if os.path.isfile(source_file):
            source_file = os.path.join(source_dir, filename)

 def main():
    if len(sys.argv) != 3:
        print("Usage: python backup.py <source_directory> <destination_directory>")
        sys.exit(1)

    source_dir = sys.argv[1]
    dest_dir = sys.argv[2]

    backup_files(source_dir, dest_dir)

if __name__ == "__main__":
    main()

# def backup_files(source_dir, dest_dir):
#     if not os.path_exists(source_dir):
#         print(f"Error: The source directory '{source_dir}' does not exist.")
#         return
#     if not os.path.exists(dest_dir):
#         print(f"Error: The destination directory '{dest_dir}' does not exist.")
#         return

#     # Iterate through files in the source directory
#     for filename in os.listdir(source_dir):
#         source_file = os.path.join(source_dir, filename)
        
#         if os.path.isfile(source_file):
#             dest_file = os.path.join(dest_dir, filename)

#             # If file already exists in the destination, append timestamp
#             if os.path.exists(dest_file):
#                 base, ext = os.path.splitext(dest_file)
#                 dest_file = f"{base}_{datetime.now().strftime('%Y%m%d%H%M%S')}{ext}"

#             shutil.copy(source_file, dest_file)
#             print(f"Backed up: {filename} -> {dest_file}")

# # def main():
# #     if len(sys.argv) != 3:
# #         print("Usage: python backup.py <source_directory> <destination_directory>")
# #         sys.exit(1)

# #     source_dir = sys.argv[1]
# #     dest_dir = sys.argv[2]

# #     backup_files(source_dir, dest_dir)

# # if __name__ == "__main__":
# #     main()