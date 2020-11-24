pipeline {
  agent any
  stages {
    stage('build') {
      steps {
        echo 'Nothing to Build'
        sh 'pip3 install flask_pymongo'
      }
    }
    stage('test') {
      steps {
        sh 'export FLASK_APP=test.py'
        sh 'python3 -m flask run'
      }   
    }
    stage('deploy') {
      steps {
         echo 'zipping files'
         sh 'pwd'
         sh 'ls -las'
         sh 'tar -czvf flaskapi.tar.gz *'
         sh 'mv flaskapi.tar.gz /home/deploy'
      } 
    }
  }
}
