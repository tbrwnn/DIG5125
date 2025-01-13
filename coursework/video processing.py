import cv2

def webcam_contrast_brightness(output_video_path):
    """
    Adjusts the brightness and contrast of webcam video in real-time using keyboard controls,
    and saves the output to another video file.

    Parameters:
    output_video_path (str): Path to the output video file.
    """

    cap = cv2.VideoCapture(0)

    # Check if the webcam is opened successfully
    if not cap.isOpened():
        print('Error: Could not access the camera') 
        return

    # Get video properties
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS)) or 30  # Use default FPS if not provided
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')

    # Create VideoWriter object
    out = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))
    
    print(f"Processing video with resolution {width}x{height} and {fps} FPS.")
    print("Controls:")
    print("'a' to increase brightness")
    print("'d' to decrease brightness")
    print("'w' to increase contrast")
    print("'s' to decrease contrast")
    print("'q' to exit")
    
    # Initial brightness and contrast
    brightness = 1.0  # No change
    contrast = 0      # Default contrast

    while True:
        # Read frame
        ret, frame = cap.read()
        if not ret:
            print('Unable to read frame')
            break

        # Adjust brightness and contrast
        adjusted_frame = cv2.convertScaleAbs(frame, alpha=brightness, beta=contrast)

        # Write frame to output file
        out.write(adjusted_frame)

        # Display frame
        cv2.imshow('Webcam Brightness and Contrast Adjustment', adjusted_frame)
        
        # Keyboard controls for brightness and contrast adjustment
        key = cv2.waitKey(10) & 0xFF
        if key == ord('q'):  # Quit
            print("Processing stopped by user.")
            break
        elif key == ord('a'):  # Increase brightness
            brightness += 0.1
            print(f"Brightness increased to {brightness:.1f}")
        elif key == ord('d'):  # Decrease brightness
            brightness = max(0.1, brightness - 0.1)  # Ensure brightness is not negative
            print(f"Brightness decreased to {brightness:.1f}")
        elif key == ord('w'):  # Increase contrast
            contrast += 10
            print(f"Contrast increased to {contrast}")
        elif key == ord('s'):  # Decrease contrast
            contrast -= 10
            print(f"Contrast decreased to {contrast}")

    # Release resources
    cap.release()
    out.release()
    cv2.destroyAllWindows()
    print(f"Output video saved to {output_video_path}")

# Example usage
output_video = 'output_with_brightness_contrast.mp4'  # Output video file
webcam_contrast_brightness(output_video)

