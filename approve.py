import boto3

pipeline_name = "DemoApplication-pipeline"

client = boto3.client('codepipeline')
response = client.get_pipeline_state(name=pipeline_name)

stage_name = response['stageStates'][2]['stageName']
action_name = response['stageStates'][2]['actionStates'][0]['actionName']
token = response['stageStates'][2]['actionStates'][0]['latestExecution']['token']
status = response['stageStates'][2]['actionStates'][0]['latestExecution']['status']


if status == "InProgress":
  client.put_approval_result(
    pipelineName=pipeline_name,
    stageName=stage_name,
    actionName=action_name,
    result={
        'summary': 'Automatically approved by Python',
        'status': 'Approved'
    },
    token=token
  )
