from superagi.tools.base_tool import BaseTool
from pydantic import BaseModel, Field
from typing import Type
import os
import requests
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

class ReadEmailInput(BaseModel):
    filter: str = Field(None, description="Filter criteria for emails")
    orderby: str = Field(None, description="Order criteria for emails")

class ReadEmailTool(BaseTool):
    name: str = "Read Email Tool"
    args_schema: Type[BaseModel] = ReadEmailInput
    description: str = "Tool to read emails from Office 365"

    def _execute(self, filter: str = None, orderby: str = None):
        access_token = os.getenv('ACCESS_TOKEN')
        if not access_token:
            return "Error: ACCESS_TOKEN environment variable not set."
        
        endpoint = 'https://graph.microsoft.com/v1.0/me/messages'
        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json'
        }
        params = {}
        if filter:
            params['$filter'] = filter
        if orderby:
            params['$orderby'] = orderby
        response = requests.get(endpoint, headers=headers, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            return f"Error: {response.status_code}, {response.text}"

