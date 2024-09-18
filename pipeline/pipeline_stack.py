from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
    pipelines
)
from constructs import Construct

class PipelineStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "PipelineQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )

        pipeline = pipelines.CodePipeline(self, "Pipeline",
            pipeline_name="TestPipeline",
            synth=pipelines.ShellStep("Synth",
                input=pipelines.CodePipelineSource.git_hub("LelouchCcCC/pipeline-lambda", "main"),
                commands=[
                    "npm ci",
                    "npm run build",
                    "npx cdk synth"
                ]
            )
        )
