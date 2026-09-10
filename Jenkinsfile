pipeline{
    agent any
        stages{
            stage('Build'){
                steps{
                echo 'Building docker image'
                bat 'docker build -t myflaskapp'
            }
            }
            stage('Run'){
                steps{
                    echo 'running the docker image'
                    bat 'docker rm -f mycontainer||exit(0)'
                    bat 'docker run -d -p 5000:5000 --name mycontainer myflaskapp'
                }
            }
        }
        post{
           success{
                    echo 'pipeline completed successfully'
                }
            
          failure{
                    echo 'pipeline failed, check the logs'
                }
        }
}
