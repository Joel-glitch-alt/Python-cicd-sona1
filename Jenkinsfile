pipeline {
    agent any

    stages {
        stage('Run Python in Docker') {
            steps {
                script {
                    sh """
                    docker run --rm -v "${WORKSPACE}:/app" -w /app python:3.11-slim /bin/bash -c "
                        pip install -r requirements.txt &&
                        python index.py
                    "
                    """
                }
            }
        }
    }
}
