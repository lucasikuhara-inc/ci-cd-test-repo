pipeline{
    agent any;

    stages{
        stage("Repository ls"){
            steps{
                echo "Build Id: ${BUILD_ID}"
                ls
            }
            post{
                always{
                    echo "========always========"
                }
                success{
                    echo "========A executed successfully========"
                }
                failure{
                    echo "========A execution failed========"
                }
            }
        }
    }

}