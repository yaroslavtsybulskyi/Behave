# README

## Prerequisites
Before running the code, ensure that you have the following installed:

- Behave
- Selenium
- WebDriver for your preferred browser (Chrome in this example)
- Gherkin

## Running Tests
To execute the tests, follow these steps:

1. Open Terminal.
2. Navigate to the project directory.
3. Run the following command to execute all tests located in the feature folders:

```
behave features
```

If you want to run a specific feature, use the following command syntax, replacing `login.feature` with the name of your desired feature file:

```
behave features/login.feature
```

For example, to run the Login feature, execute:

```
behave features/login.feature
```

To run a specific group of tests within a feature, you can specify tags. For instance, if you have positive and negative tests for `pom_login.feature`, you can run only the negative tests using:

```
behave features/pom_login.feature --tags=negative
```

(Note: POM stands for Page Object Model)
