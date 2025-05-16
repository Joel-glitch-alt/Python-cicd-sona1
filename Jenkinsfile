pipeline {
    agent any

    stages {
        stage('Run Python in Docker') {
            steps {
                script {
                    sh """
                      echo "Welcome to Python in Docker!"
                      echo "This is a simple Jenkins pipeline that runs a Python script inside a Docker container."
                      echo "The script will print 'Hello, World!' to the console."
                    """
                }
            }
        }
    }
}
