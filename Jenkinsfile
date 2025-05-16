pipeline {
    agent any

    stages {
        stage('Install and Build') {
            agent {
                docker {
                    image 'python:3.8'
                    reuseNode true 
                }
            }
            steps {
                sh '''
                    echo "Installing Dependencies..."
                    pip install -r requirements.txt || echo "No requirements.txt file found"
                '''
            }
        }

        stage('Test') {
            agent {
                docker {
                    image 'python:3.8'
                    reuseNode true
                }
            }
            steps {
                sh '''
                    echo "Running Tests..."
                    python index.py
                '''
            }
        }
    }
}
