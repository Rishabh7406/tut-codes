for filename in os.listdir(input_folder):
    if filename.endswith('.json'):
        file_path = os.path.join(input_folder, filename)
        with open(file_path, 'r') as f:
            notebook_json = json.load(f)
        # Convert the JSON dict to a NotebookNode object
        nb = nbformat.from_dict(notebook_json)
        output_file = os.path.join(output_folder, filename.replace('.json', '.ipynb'))
        with open(output_file, 'w') as f:
            nbformat.write(nb, f)
        print(f"Converted {filename} to {output_file}")
