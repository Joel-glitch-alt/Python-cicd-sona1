pipeline {
    agent any

    environment {
       // SCANNER_HOME = tool 'sonar-scanner' // Jenkins > Global Tool Configuration > SonarScanner name
        SONARQUBE = 'sonar-server'         // Jenkins > Configure System > SonarQube server name
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
                        ${SCANNER_HOME}/bin/sonar-scanner \
                          -Dsonar.projectKey=python_cicd_sona1 \
                          -Dsonar.projectName="Python Sonar Project" \
                          -Dsonar.sources=. \
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
