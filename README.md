# codepipeline_approval

## Setup CodeCommit
1. Create a repo called myrepo
2. Upload buildspec.yaml and buildspec2.yaml

## Create the CloudFormation stack
1. aws cloudformation create-stack --stack-name MyRepo-Pipeline --template-body file://pipeline.yaml --capabilities CAPABILITY_NAMED_IAM

## Make a change to the repo
1. Create and commit README.md
2. Update the README.md to trigger the pipeline

## Check the pipeline 
1. The pipeline should be Pending Approval
2. Run ```python3 approve.py```
3. CodePipeline should execute the next stage 

## Cleanup 
1. Delete the MyRepo-Pipeline stack
2. Remove the CodeCommit repo myrepo




