import threading
import rclpy

def main(args=None):
    rclpy.init(args=args)
    node = rclpy.create_node("dummy_node")

    thread = threading.Thread(target=rclpy.spin, args=(node,), daemon=True)
    thread.start()

    rate = node.create_rate(2)
    try:
        while rclpy.ok():
            node.get_logger().info("rate loop")
            rate.sleep()
    except KeyboardInterrupt:
        pass
    thread.join()

if __name__ == "__main__":
    main()

