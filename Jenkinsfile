pipeline {
    agent { label 'master' }
    stages {
        stage('build') {
            steps {
                sh 'echo building...'
            }
        }
        stage('test'){
            steps {
                sh 'pytest'
            }
        }
    }
}
