pipeline {
    agent any
    environment {
        token = 'DZnyy741L7T6j9IWbrldx6Mur6LgZAtF7jNaQlodfjg '
        //token = 'TESTTESTTESTTESTTESTTESTTESTTEST '
        jobName = "${JOB_NAME} ${BRANCH_NAME != null ? BRANCH_NAME : ''}"
        buildNo = "${BUILD_NUMBER}"
        Job_url = "${BUILD_URL}"
        url = 'https://notify-api.line.me/api/notify'
        url_monitor = 'http://192.168.41.66:7902/?password=secret'
        url_website = 'https://www.irplus.in.th/Listed/KWM/home.asp'
        allureReportPath = 'reports'
    }

    stages {
        stage('AllureSetup') {
            steps {
                script {
                    allureReportPaths = []  // List to store Allure report paths
                }
            }
        }
        stage('Run KWM_news_clipping') {
            steps {
                script {
                    sleep 5
                    def retryCount = 1
                    def maxRetryCount = 3
                    def pytestCommand = 'pytest 3KWM_EN_PUBLIC.py --alluredir=Reports'
                    def pytestCommand1 = 'pytest 3KWM_EN_PUBLIC1.py --alluredir=Reports'

                    // Variable to track the overall result of the pipeline
                    def pipelineResult = 'FAILURE'

                    // First pytest attempt without catchError
                    script {
                        try {
                            // Run the pytest command
                            sh pytestCommand
                            // If the command succeeds, set the pipeline result to 'SUCCESS'
                            pipelineResult = 'SUCCESS'
                        } catch (Exception e) {
                            // Handle the exception (e.g., print an error message)
                            echo "First pytest attempt failed: ${e}"
                            // Keep the pipeline result as 'FAILURE'
                        }
                    }
                    echo "First pytest attempt result: ${pipelineResult}"

                    // Retry logic
                    def retryAttempt = 0
                    while (pipelineResult == 'FAILURE' && retryAttempt < retryCount && retryAttempt < maxRetryCount) {
                        retryAttempt++
                        echo "Retrying the pytest command, attempt ${retryAttempt}"
                        script {
                            try {
                                // Run the pytest command in the retry loop
                                sh pytestCommand1
                                // If the command succeeds, set the pipeline result to 'SUCCESS' and break the loop
                                pipelineResult = 'SUCCESS'
                                break
                            } catch (Exception e) {
                                // Handle the exception (e.g., print an error message)
                                echo "Retry attempt failed: ${e}"
                                // Keep the pipeline result as 'FAILURE'
                            }
                        }
                    }
                    // Append Allure report path to the list
                    allureReportPaths.add("${allureReportPath}/")
                }
            }
        }
    }


    post {
        always {
            // Publish accumulated Allure reports
            allure([
                includeProperties: false,
                jdk: '',
                results: allureReportPaths.collect { path -> [path: path] }
            ])
            
            // Send Line Notify message based on build result
            script {
                if (currentBuild.result == 'FAILURE') {
                    def message = """KWM
[🔴 การทดสอบสำเร็จ พบข้อผิดพลาด]
${jobName}
${url_website}  
${Job_url}"""
                    sh "curl $url -H \"Authorization: Bearer $token \" -F \"message= ${message}\""
                } else if (currentBuild.result == 'SUCCESS') {
                    def message = """KWM
[🟢 การทดสอบสำเร็จ ไม่พบข้อผิดพลาด] 
${jobName}
${url_website}  
${Job_url}"""
                    sh "curl $url -H \"Authorization: Bearer $token \" -F \"message= ${message}\""
                }
            }
        }
    }
}
