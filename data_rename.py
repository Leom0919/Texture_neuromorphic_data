import os
import shutil

def process_directory(source_base, output_directory, rename_mappings):
    source_directory = os.path.join(source_base, 'events')
    if not os.path.exists(source_directory):
        print(f"Source directory does not exist: {source_directory}")
        return

    print(f"Processing files in directory: {source_directory}")
    files_found = False
    for filename in os.listdir(source_directory):
        for old_part, new_part in rename_mappings.items():
            if old_part in filename:
                files_found = True
                new_filename = filename.replace(old_part, new_part)
                source_file = os.path.join(source_directory, filename)
                target_file = os.path.join(output_directory, new_filename)

                print(f"Copying {source_file} to {target_file}...")
                shutil.copy(source_file, target_file)
                print(f"Copied and renamed {filename} to {new_filename}")
                break

    if not files_found:
        print("No relevant files found for renaming.")

# Directory mappings, according to the real name
directory_mappings = {
    "ABB_0419_acrylic_fashionfabric": {'pose_0': 'acrylic', 'pose_1': 'fashionfabric'},
    "ABB_0419_fur_wood": {'pose_0': 'fur', 'pose_1': 'wood'},
    "ABB_0419_wool_canvas": {'pose_0': 'wool', 'pose_1': 'canvas'},
    "ABB_0419_cotton_nylon": {'pose_0': 'cotton', 'pose_1': 'nylon'},
    "ABB_0419_mesh_felt": {'pose_0': 'mesh', 'pose_1': 'felt'}
}

# Output directory
output_directory = r'D:\five layer convolution'

# Ensure the output directory exists
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Process each specified directory with its specific renaming rules
base_source_directory = r'D:\ABB_neuro_texture\ABB_0419_DEPTH2'
for directory, mappings in directory_mappings.items():
    full_source_directory = os.path.join(base_source_directory, directory)
    process_directory(full_source_directory, output_directory, mappings)
