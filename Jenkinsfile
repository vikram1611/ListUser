pipeline {
    agent any

    stages {
        stage('Get User') {
            steps {
                sh 'apt-get install python3-jenkins-job-builder'
                sh 'pwd'
                sh 'ls'
                sh 'chmod +777 get_user.sh'
                sh './get_user.sh'
            }
        }
    }
}