# Diabetes Prediction using Flask API

This project is a simple classification machine learning project aimed at predicting whether a person suffers from diabetes based on parameters such as blood sugar level, BMI, and blood pressure. However, the primary goal of this project is to create a Flask REST API, allowing access to the machine learning algorithm from any backend system.

## Table of Contents
- [Use Case](#use-case)
- [Usage](#usage)
  - [Setup](#setup)
  - [Running the Program](#running-the-program)
  - [Accessing the API](#accessing-the-api)
- [Note](#note)
- [API Link](#api-link)
- [License](#license)
- [Author](#author)

## Use Case
This project's use case includes:
- Integration with other backend systems: The Flask API allows seamless integration with various backend systems, enabling the prediction of diabetes status.
- Healthcare applications: Healthcare providers can use the API to incorporate diabetes prediction into their systems, aiding in early diagnosis and treatment.
- Research purposes: Researchers can access the API to study diabetes prediction algorithms and develop new insights into the disease.

## Usage
### Setup
1. Clone the repository to your local machine.
2. Install the necessary dependencies by running:
```bash
   pip install -r requirements.txt
```
### Run the program using Gunicorn:
```bash
  gunicorn app:app
```

### Accessing the API
To access the API:
- Use Postman or any other API testing tool.
- Send data in the correct format as specified in the `app.py` file.
- Refer to the API link provided to interact with the deployed project directly.

## Note
- This is an API project with no graphical user interface (UI).
- The program can be run locally or accessed via the deployed API link.
- Ensure data is sent in the correct format for accurate predictions.

## API Link
The deployed project is accessible via the following API link: [API Link](link-to-api)

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
