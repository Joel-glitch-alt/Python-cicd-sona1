pipeline {
    agent any

    stages {
        stage('Run Python in Docker') {
            steps {
                script {
                    // Run python:3.11-slim container and mount workspace
                    sh """
                    docker run --rm -v "$PWD":/app -w /app python:3.11-slim /bin/bash -c "
                        pip install -r requirements.txt &&
                        python index.py
                    "
                    """
                }
            }
        }
    }
}
