def zip_files():
    # Replace with the path to the directory containing your files
    directory_path = '/path/to/your/files'

    # List of files to include in the ZIP archive
    file_list = ['file1.txt', 'file2.txt', 'file3.txt']

    # Create a temporary ZIP archive file
    zip_filename = 'archive.zip'
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for filename in file_list:
            file_path = os.path.join(directory_path, filename)
            if os.path.exists(file_path):
                zipf.write(file_path, os.path.basename(file_path))

    # Send the ZIP archive as a response to the client
    return send_file(zip_filename, as_attachment=True)
