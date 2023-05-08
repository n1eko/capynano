# Capynano

This project was created as a learning exercise for deploying a machine learning model. The goal was to create a simple web application that would allow users to input data and receive a prediction from the trained model.

## [Website](capynano.n1eko.com)

## Prerequisites

Before running this project, you will need to have the following software installed on your machine:

- Python 3.6 or higher
- FastAI 2.7.12
- Gradio 3.28.3

## Docker

### Build image

```bash
docker build . -t capynano:latest
```

### Run

```bash
docker run --rm -it -p 8080:8080 capynano:latest
```