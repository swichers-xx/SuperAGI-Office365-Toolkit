
from superagi.tools.base_tool import BaseTool
from pydantic import BaseModel, Field
from typing import Type


class SendEmailInput(BaseModel):
    subject: str = Field(..., description="Subject of the email")
    body: str = Field(..., description="Body content of the email")
    to_recipients: str = Field(..., description="Recipient email addresses")

class SendEmailTool(BaseTool):
    name: str = "Send Email Tool"
    args_schema: Type[BaseModel] = SendEmailInput
    description: str = "Tool to send emails via Office 365"

    def _execute(self, subject: str, body: str, to_recipients: str):
        from superagi.config import get_tool_config
        import requests
        
        access_token = get_tool_config('ACCESS_TOKEN')
        endpoint = 'https://graph.microsoft.com/v1.0/me/sendMail'
        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json'
        }
        email_data = {
            'message': {
                'subject': subject,
                'body': {
                    'contentType': 'HTML',
                    'content': body
                },
                'toRecipients': [{'emailAddress': {'address': to_recipients}}]
            },
            'saveToSentItems': 'true'
        }
        response = requests.post(endpoint, headers=headers, json=email_data)
        return response.json()
                