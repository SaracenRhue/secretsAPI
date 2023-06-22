# secretsAPI

This application provides a RESTful interface for managing project data stored in YAML files.

## Application Setup

This is a FastAPI application and thus requires a Python environment with FastAPI installed. Also, ensure that you have installed PyYAML for working with YAML files.

## API Endpoints

The application provides the following endpoints:

1. **GET /{project}**

   This endpoint returns the data of the specified project. The data is read from a YAML file named `{project}.yaml` inside the `projects` directory.

   **Parameters:**

   - `project`: The name of the project to fetch. This corresponds to a `{project}.yaml` file inside the `projects` directory.

   **Responses:**

   - `200 OK`: The project data was found and is returned in the response body.
   - `404 Not Found`: There is no YAML file corresponding to the provided project name.

2. **POST /{project}**

   This endpoint updates the data of the specified project. The data is written to a YAML file named `{project}.yaml` inside the `projects` directory. If the file does not already exist, it will be created.

   **Parameters:**

   - `project`: The name of the project to update. This corresponds to a `{project}.yaml` file inside the `projects` directory.

   **Request Body:**

   - JSON object to be written to the project's YAML file.

   **Responses:**

   - `200 OK`: The project data was successfully updated. Returns a success message.
   - `500 Internal Server Error`: An error occurred while trying to update the project data.

3. **DELETE /{project}**

   This endpoint deletes the specified project by removing the corresponding `{project}.yaml` file from the `projects` directory.

   **Parameters:**

   - `project`: The name of the project to delete. This corresponds to a `{project}.yaml` file inside the `projects` directory.

   **Responses:**

   - `200 OK`: The project was successfully deleted. Returns a success message.
   - `404 Not Found`: There is no YAML file corresponding to the provided project name.
   - `500 Internal Server Error`: An error occurred while trying to delete the project.
