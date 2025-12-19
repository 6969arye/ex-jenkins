pipeline {
    agent any
    
    stages {
        stage('Install Dependencies') {
            steps {
                sh 'apt-get update && apt-get install -y python3-pip'
                sh 'pip3 install -r requirements.txt'
            }
        }
        
        stage('Run Tests') {
            steps {
                // הרצת ה-pytest על הקובץ שלך
                sh 'python3 -m pytest test_calc.py'
            }
        }
    }
    
    post {
        always {
            echo 'CI process finished.'
        }
    }
}