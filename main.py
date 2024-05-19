import leap
import pygame, sys

FPS = 60
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 300
BACK_GROUND = (0, 0, 0)

pygame.init()

WIN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Drawing")


class MyListener(leap.Listener):

    def __init__(self) -> None:
        super().__init__()
        self.palm_right_x = 0
        self.palm_right_y = 0
        self.palm_right_z = 0

        self.palm_left_x = 0
        self.palm_left_y = 0
        self.palm_left_z = 0

        self.should_draw = False
        self.should_erase = False
        self.radius = 1 

    def on_connection_event(self, event):
        print("Connected")

    def on_device_event(self, event):
        try:
            with event.device.open():
                info = event.device.get_info()
        except leap.LeapCannotOpenDeviceError:
            info = event.device.get_info()

        print(f"Found device {info.serial}")

    def on_tracking_event(self, event):
        for hand in event.hands:
            hand_type = "left" if str(hand.type) == "HandType.Left" else "right"
            if hand_type ==  "right":
                self.palm_right_x = hand.palm.position.x
                self.palm_right_y = hand.palm.position.y
                self.palm_right_z = hand.palm.position.z

                self.radius = int(hand.pinch_distance//5)
                print(self.radius)

            else:
                self.palm_left_x = hand.palm.position.x
                self.palm_left_y = hand.palm.position.y
                self.palm_left_z = hand.palm.position.z


                if hand.thumb.distal.prev_joint.z - hand.middle.distal.prev_joint.z <= 48:
                    self.should_erase = True
                else:
                    self.should_erase = False

                # print(hand.thumb.distal.prev_joint.z - hand.middle.distal.prev_joint.z)

                if hand.thumb.distal.prev_joint.z - hand.index.distal.prev_joint.z <= 20:
                    self.should_draw = True
                else:
                    self.should_draw = False

    def return_right_hand_position(self):
        return (self.palm_right_x, self.palm_right_y, self.palm_right_z)
    def return_left_hand_position(self):
        return (self.palm_left_x, self.palm_left_y, self.palm_left_z)

def main():
    my_listener = MyListener()

    connection = leap.Connection()
    connection.add_listener(my_listener)

    running = True

    WIN.fill(BACK_GROUND)
    with connection.open():
        connection.set_tracking_mode(leap.TrackingMode.Desktop)
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            rx, ry, rz = my_listener.return_right_hand_position()

            if rx + WINDOW_WIDTH//2 >= WINDOW_WIDTH:
                rx = WINDOW_WIDTH//2 

            if rx + WINDOW_WIDTH//2 <= 0:
                rx = -WINDOW_WIDTH//2

            if rz + WINDOW_HEIGHT//2 >= WINDOW_HEIGHT:
                rz = WINDOW_HEIGHT//2 

            if rz + WINDOW_HEIGHT//2 <= 0:
                rz = -WINDOW_HEIGHT//2

            if my_listener.should_draw:
                if my_listener.should_erase:
                    pygame.draw.circle(WIN, (255, 255, 255), [WINDOW_WIDTH//2 + rx, WINDOW_HEIGHT//2 + rz], my_listener.radius * 1.6, 1)
                else:
                    pygame.draw.circle(WIN, (255, 255, 255), [WINDOW_WIDTH//2 + rx, WINDOW_HEIGHT//2 + rz], my_listener.radius)

            pygame.display.update()
            fpsClock.tick(FPS)

            if my_listener.should_erase:
                pygame.draw.circle(WIN, (BACK_GROUND), [WINDOW_WIDTH//2 + rx, WINDOW_HEIGHT//2 + rz], my_listener.radius * 1.7)

if __name__ == "__main__":
    main()
