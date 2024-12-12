import sys

class UI:
    def __init__(self, resource_manager):
        self.resource_manager = resource_manager

    def run(self):
        while True:
            print("1. Create")
            print("2. Read")
            print("3. Edit")
            print("4. Delete")
            print("5. Exit")
            choice = input("Enter your choice: ")
            if choice == '1':
                self.create_resource()
            elif choice == '2':
                self.read_resources()
            elif choice == '3':
                self.edit_resource()
            elif choice == '4':
                self.delete_resource()
            elif choice == '5':
                sys.exit(0)
            else:
                print("Invalid choice")

    def create_resource(self):
        name = input("Enter resource name: ")
        description = input("Enter resource description: ")
        self.resource_manager.create_resource(name, description)
        print("Resource created successfully")

    def read_resources(self):
        attribute = input("Enter attribute to search: ")
        matching_resources = [resource for resource in self.resource_manager.resources if attribute in str(resource)]
        if matching_resources:
            for resource in matching_resources:
                print(f"ID: {resource['id']}, Name: {resource['name']}, Description: {resource['description']}")
        else:
            print("No matching resources found")

    def edit_resource(self):
        id = int(input("Enter ID of the resource to edit: "))
        resource = self.resource_manager.get_resource(id)
        if resource:
            name = input("Enter new name: ")
            description = input("Enter new description: ")
            self.resource_manager.update_resource(id, name, description)
            print("Resource updated successfully")
        else:
            print("No matching resource found")

    def delete_resource(self):
        id = int(input("Enter ID of the resource to delete: "))
        self.resource_manager.delete_resource(id)
        print("Resource deleted successfully")
