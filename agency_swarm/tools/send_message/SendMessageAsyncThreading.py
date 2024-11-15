from typing import ClassVar, Type
from agency_swarm.threads.thread_async import ThreadAsync
from .SendMessage import SendMessage

class SendMessageAsyncThreading(SendMessage):
    """Use this tool for asynchronous communication with other agents within your agency. Initiate tasks by messaging, and check status and responses later with the 'GetResponse' tool. Relay responses to the user, who instructs on status checks. Continue until task completion."""
    class ToolConfig:
        async_mode = "threading"

    def run(self):
        thread = self._get_thread()

        message = thread.get_completion_async(message=self.message,
                                                message_files=self.message_files,
                                                additional_instructions=self.additional_instructions)

        return message or ""