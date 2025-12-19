pipeline {
    agent any
    
    stages {
        stage('Setup Environment') {
            steps {
                echo 'Installing Python venv...'
                // התקנת חבילת ה-venv של פייתון
                sh 'apt-get update && apt-get install -y python3-venv'
            }
        }
        
        stage('Install Dependencies') {
            steps {
                echo 'Creating venv and installing requirements...'
                sh '''
                    python3 -m venv venv
                    ./venv/bin/pip install -r requirements.txt
                '''
            }
        }
        
        stage('Run Tests') {
            steps {
                echo 'Running pytest from venv...'
                // הרצת pytest מתוך ה-venv שיצרנו
                sh './venv/bin/python3 -m pytest test_calc.py'
            }
        }
    }
}