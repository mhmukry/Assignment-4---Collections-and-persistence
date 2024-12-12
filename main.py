import os

if __name__ == '__main__':
    file_path = 'resources.csv'
    if not os.path.exists(file_path):
        open(file_path, 'w').close()

    resource_manager = ResourceManager(file_path)
    ui = UI(resource_manager)

    # Load existing data from file
    resource_manager.load_data()

    # Start UI
    ui.run()

    # Save data to file on exit
    resource_manager.save_data()
