from slack_sdk import WebClient
from datetime import datetime

class MessageFormatter:
    @staticmethod
    def format_success_msg(msg):
        return f"""
            date: {datetime.today().strftime('%Y-%m-%d %H:%M:%S')}
            dag id: "{msg.get('task_instance').dag_id}" All clear.
            log url: {msg.get('task_instance').log_url}
        """

    @staticmethod
    def format_fail_msg(msg):
        return f"""
            date: {datetime.today().strftime('%Y-%m-%d %H:%M:%S')}
            
            ╔═╗┬─┐┬─┐┌─┐┬─┐
            ║╣ ├┬┘├┬┘│ │├┬┘
            ╚═╝┴└─┴└─└─┘┴└─

            Error task id: {msg.get('task_instance').task_id},
            Error dag id: {msg.get('task_instance').dag_id},
            log url: {msg.get('task_instance').log_url}
        """

    @staticmethod
    def format_alert_msg(msg):
        return f"""
            date: {datetime.today().strftime('%Y-%m-%d %H:%M:%S')}
            OVER 10 min
            LONG dag id: {msg.get('task_instance').dag_id},
            log url: {msg.get('task_instance').log_url}
        """

class SlackCommunicator:
    def __init__(self, channel, token):
        self.channel = channel
        self.client = WebClient(token=token)

    def send_message(self, text):
        self.client.chat_postMessage(channel=self.channel, text=text)

class AlertManager:
    def __init__(self, channel, token):
        self.message_formatter = MessageFormatter()
        self.slack_communicator = SlackCommunicator(channel, token)

    def send_success_alert(self, msg):
        success_msg = self.message_formatter.format_success_msg(msg)
        self.slack_communicator.send_message(success_msg)

    def send_fail_alert(self, msg):
        fail_msg = self.message_formatter.format_fail_msg(msg)
        self.slack_communicator.send_message(fail_msg)

    def send_alert(self, msg):
        alert_msg = self.message_formatter.format_alert_msg(msg)
        self.slack_communicator.send_message(alert_msg)
