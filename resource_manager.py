import csv

class ResourceManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.resources = []

    def create_resource(self, name, description):
        resource = {'id': len(self.resources) + 1, 'name': name, 'description': description}
        self.resources.append(resource)
        self.save_data()

    def get_resource(self, id):
        for resource in self.resources:
            if resource['id'] == id:
                return resource
        return None

    def update_resource(self, id, name, description):
        for resource in self.resources:
            if resource['id'] == id:
                resource['name'] = name
                resource['description'] = description
                self.save_data()
                return
        print("No matching resource found")

    def delete_resource(self, id):
        for i, resource in enumerate(self.resources):
            if resource['id'] == id:
                del self.resources[i]
                self.save_data()
                return
        print("No matching resource found")

    def save_data(self):
        with open(self.file_path, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=['id', 'name', 'description'])
            writer.writeheader()
            for resource in self.resources:
                writer.writerow(resource)

    def load_data(self):
        with open(self.file_path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.create_resource(row['name'], row['description'])
