import boto3
import json
import uuid
import time
from datetime import datetime

class AgentCoreSession:
    """Interactive chat session with Bedrock AgentCore Runtime"""

    def __init__(self, agent_runtime_arn, region="us-east-1", profile=None, max_retries=3):
        self.agent_runtime_arn = agent_runtime_arn
        self.region = region
        self.max_retries = max_retries
        self.runtime_session_id = str(uuid.uuid4())  # Consistent session ID

        # Initialize boto3 client
        if profile:
            session = boto3.Session(profile_name=profile)
        else:
            session = boto3.Session()

        self.client = session.client('bedrock-agentcore', region_name=region)

        print(f"\n{'='*60}")
        print("Bedrock AgentCore - Interactive Chat")
        print(f"{'='*60}")
        print(f"Session ID: {self.runtime_session_id}")
        print(f"ARN: {agent_runtime_arn}")
        print(f"{'='*60}")
        print("Type '/exit' to quit\n")

    def send_message(self, prompt):
        """Send a message and get response"""

        for attempt in range(1, self.max_retries + 1):
            try:
                if attempt > 1:
                    print(f"  Retrying... (attempt {attempt}/{self.max_retries})")
                    time.sleep(2)

                # Simple payload
                payload = json.dumps({
                    "input": {"prompt": prompt}
                })

                # Use consistent runtimeSessionId for conversation continuity
                response = self.client.invoke_agent_runtime(
                    agentRuntimeArn=self.agent_runtime_arn,
                    runtimeSessionId=self.runtime_session_id,
                    payload=payload,
                    qualifier="DEFAULT"
                )

                # Parse response
                response_body = response['response'].read()
                response_data = json.loads(response_body)

                # Extract and display message
                assistant_message = self._extract_message(response_data)
                print(f"Assistant: {assistant_message}\n")

                return response_data

            except Exception as e:
                error_str = str(e)

                if "500" in error_str or "RuntimeClientError" in error_str:
                    if attempt < self.max_retries:
                        continue
                    else:
                        print(f"✗ All {self.max_retries} attempts failed: {error_str}\n")
                        raise
                else:
                    print(f"✗ Error: {error_str}\n")
                    raise

    def _extract_message(self, response_data):
        """Extract text message from response"""
        try:
            output = response_data.get("output", {})
            message = output.get("message", {})
            content = message.get("content", [])

            if content and len(content) > 0:
                return content[0].get("text", "")

            return str(response_data)
        except:
            return str(response_data)

    def run(self):
        """Run interactive chat loop"""

        while True:
            try:
                user_input = input("You: ").strip()

                if not user_input:
                    continue

                if user_input.lower() == '/exit':
                    print("\nGoodbye!")
                    break

                self.send_message(user_input)

            except KeyboardInterrupt:
                print("\n\nSession interrupted. Goodbye!")
                break
            except Exception as e:
                print(f"Error: {str(e)}\n")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description='Bedrock AgentCore Runtime - Interactive Chat',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Example:
  python agent-core-chat.py "arn:aws:bedrock-agentcore:us-east-1:123456789012:runtime/my_agent-xyz"
  python agent-core-chat.py "arn:aws:..." --region us-west-2 --profile myprofile
        '''
    )

    parser.add_argument('arn', help='AgentCore Runtime ARN')
    parser.add_argument('--region', '-r', default='us-east-1', help='AWS region (default: us-east-1)')
    parser.add_argument('--profile', '-p', help='AWS profile name')
    parser.add_argument('--retries', '-n', type=int, default=3, help='Max retry attempts (default: 3)')

    args = parser.parse_args()

    # Start interactive session
    session = AgentCoreSession(
        agent_runtime_arn=args.arn,
        region=args.region,
        profile=args.profile,
        max_retries=args.retries
    )

    session.run()