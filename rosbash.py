import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import os
import subprocess

class BashCommandSubscriber(Node):
    
    def __init__(self):
        namespace = subprocess.check_output('echo $USER', shell=True, text=True).strip()
        super().__init__("bash_listener",namespace=namespace)
        # Create a subscription to the '/bash_command' topic
        self.subscription = self.create_subscription(
            String,
            "bash_command",
            self.listener_callback,
            1  # QoS history depth
        )
        self.subscription = self.create_subscription(
            String,
            "/bash_command",
            self.listener_callback,
            1  # QoS history depth
        )
    def listener_callback(self, msg):
        # Get the message data
        command = msg.data
        self.get_logger().info(f'Received command: {command}')
        
        # Use os.system to execute the command
        response = os.system(command)
        
        # Log the response
        if response == 0:
            self.get_logger().info(f'Command "{command}" executed successfully.')
        else:
            self.get_logger().error(f'Command "{command}" failed with response code {response}.')

def main(args=None):
    rclpy.init(args=args)

    # Create the node
    bash_command_subscriber = BashCommandSubscriber()

    # Spin the node to keep it alive and processing callbacks
    rclpy.spin(bash_command_subscriber)

    # Clean up after shutdown
    bash_command_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
