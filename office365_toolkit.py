
from abc import ABC
from superagi.tools.base_tool import BaseToolkit, BaseTool
from typing import Type, List
from send_email_tool import SendEmailTool
from read_email_tool import ReadEmailTool

class Office365Toolkit(BaseToolkit, ABC):
    name: str = "Office 365 Toolkit"
    description: str = "Toolkit to manage Office 365 emails"

    def get_tools(self) -> List[BaseTool]:
        return [SendEmailTool(), ReadEmailTool()]

    def get_env_keys(self) -> List[str]:
        return ["ACCESS_TOKEN"]
                