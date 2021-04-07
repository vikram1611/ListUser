pipeline {
    agent any

    stages {
        stage('Get User') {
            steps {
                sh 'pwd'
                sh 'ls'
                sh 'chmod +777 get_user.sh'
                sh './get_user.sh'
            }
        }
    }
}