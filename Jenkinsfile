pipeline {
  agent any
  stages {
    stage('build') {
      steps {
        echo 'Install Flask'
        sh 'pip3 install flask'
        sh 'which flask'
        sh 'flask'
      }
    }
    stage('test') {
      steps {
        sh 'python3 test.py'
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
