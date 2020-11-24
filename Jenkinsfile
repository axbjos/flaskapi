pipeline {
  agent any
  stages {
    stage('build') {
      steps {
        echo 'Nothing to Build'
      }
    }
    stage('test') {
      steps {
        sh 'python3 -m flask run test.py'
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
