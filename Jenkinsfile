pipeline {
    agent none
    options { timestamps() }
    stages {
        stage('Check scm') {
            agent any
            steps {
                checkout scm
            }
        }
        stage('Build') {
            agent any
            steps {
                echo "Building ...${BUILD_NUMBER}"
                echo "Build completed"
            }
        }
        stage('Test') {
            agent { 
                docker { 
                    image 'python:3.9-alpine' 
                    args '-u root'
                } 
            }
            steps {
                sh 'pip install Flask xmlrunner'
                sh 'python3 app_tests.py'
            }
            post {
                always {
                    junit 'test-reports/*.xml'
                }
                success {
                    echo "Application testing successfully completed"
                }
                failure {
                    echo "Tests failed!"
                }
            }
        }
    }
}
