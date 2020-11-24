pipeline {
  agent any
  stages {
    stage('build') {
      steps {
        echo 'Nothing to Build'
        sh 'pip3 install -r requirements.txt'
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
         sh 'mv flaskapi.tar.gz /home/deploy'
      } 
    }
  }
}
