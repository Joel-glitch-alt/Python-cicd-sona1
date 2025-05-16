pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    dockerImage = docker.build("my-python-app:${env.BUILD_ID}")
                }
            }
        }

        stage('Run Python Script') {
            steps {
                script {
                    dockerImage.inside {
                        sh 'python index.py'
                    }
                }
            }
        }
    }
}
