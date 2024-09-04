pipeline{
    agent any;

    stages{
        stage("Repository ls"){
            steps{
                echo "Build Id: ${BUILD_ID}"
                ls
            }
            post{
                success{
                    echo "The build was successful."
                }
                failure{
                    echo "The build has failed."
                }
            }
        }
    }

}