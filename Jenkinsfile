pipeline {
    agent any

    tools {
        // This should match the name in Jenkins > Global Tool Configuration
        sonarQubeScanner 'SonarScanner'
    }

    environment {
        // This should match the name defined in Jenkins > Configure System > SonarQube servers
        SONARQUBE = 'sonar-server'
    }

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

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv("${SONARQUBE}") {
                    sh '''
                        sonar-scanner \
                          -Dsonar.projectKey=my_project \
                          -Dsonar.projectName="Python-Sona-Project" \
                          -Dsonar.sources=./src \
                          -Dsonar.language=py \
                          -Dsonar.sourceEncoding=UTF-8
                    '''
                }
            }
        }

        stage('Quality Gate') {
            steps {
                timeout(time: 5, unit: 'MINUTES') {
                    waitForQualityGate abortPipeline: true
                }
            }
        }
    }
}
