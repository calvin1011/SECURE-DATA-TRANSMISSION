import pyshark
import logging
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Logging configuration
logging.basicConfig(filename='packet_analysis.log', level=logging.INFO)

def monitor_packets(interface: str, capture_limit: int = 100):
    print(f"Starting packet capture on {interface}...")
    capture = pyshark.LiveCapture(interface=interface)
    start_time = time.time()
    packet_count = 0

    for packet in capture.sniff_continuously(packet_count=capture_limit):
        packet_count += 1
        print(f"Packet {packet_count}: {packet}")
        
        # Count packets per minute
        elapsed_time = time.time() - start_time
        if elapsed_time > 60:
            logging.info(f"Packets per minute: {packet_count}")
            print(f"Packets per minute: {packet_count}")
            packet_count = 0
            start_time = time.time()

        # Analyze for encrypted content
        if 'TLS' in packet:
            logging.info(f"Encrypted packet detected: {packet}")

    capture.save_to_file("output.pcap")  # Save to a file
    print("Packet capture complete. Saved to output.pcap.")

class FileMonitorHandler(FileSystemEventHandler):
    def on_deleted(self, event):
        logging.warning(f"File deleted: {event.src_path}")
        print(f"File deleted: {event.src_path}")

if __name__ == '__main__':
    # Monitor packets
    monitor_packets(interface="Wi-Fi", capture_limit=100)

    # Monitor file system changes
    observer = Observer()
    observer.schedule(FileMonitorHandler(), path="path_to_monitor", recursive=True)
    observer.start()
