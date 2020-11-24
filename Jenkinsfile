pipeline {
  agent any
  stages {
    stage('build') {
      steps {
        echo 'Nothing to Build'
        sh 'export FLASK_APP=test.py'
      }
    }
    stage('test') {
      steps {
        sh 'python3 -m flask run'
      }   
    }
    stage('deploy') {
      steps {
         echo 'zipping files'
         sh 'pwd'
         sh 'ls -las'
         sh 'tar -czvf flaskapi.tar.gz *'
      } 
    }
  }
}
