#!/usr/bin/env python3
"""
GIF Combine - A utility to combine two GIF images side by side while maintaining the frame rate of the first GIF.
"""

import sys
from typing import Tuple
from PIL import Image
import imageio
import numpy

def get_gif_info(gif_path: str) -> Tuple[int, Tuple[int, int]]:
    """
    Get the frame count and dimensions of a GIF file.
    
    Args:
        gif_path (str): Path to the GIF file
        
    Returns:
        Tuple[int, Tuple[int, int]]: (frame_count, (width, height))
    """
    gif = Image.open(gif_path)
    frames = 0
    try:
        while True:
            frames += 1
            gif.seek(gif.tell() + 1)
    except EOFError:
        pass
    return frames, gif.size

def combine_gifs(gif1_path: str, gif2_path: str, output_path: str) -> None:
    """
    Combine two GIF images side by side while maintaining the frame rate of the first GIF.
    The output GIF will loop forever.
    
    Args:
        gif1_path (str): Path to the first GIF file (frame rate will be maintained)
        gif2_path (str): Path to the second GIF file
        output_path (str): Path where the combined GIF will be saved
    """
    # Get information about both GIFs
    gif1_frames, (gif1_width, gif1_height) = get_gif_info(gif1_path)
    gif2_frames, (gif2_width, gif2_height) = get_gif_info(gif2_path)
    
    # Read both GIFs
    gif1 = imageio.get_reader(gif1_path)
    gif2 = imageio.get_reader(gif2_path)
    
    # Get the frame rate from the first GIF
    frame_duration = gif1.get_meta_data()['duration'] / 1000  # Convert to seconds
    
    # Calculate dimensions for the combined GIF
    max_height = max(gif1_height, gif2_height)
    total_width = gif1_width + gif2_width
    
    # Create writer for the output GIF with loop=0 for infinite looping
    writer = imageio.get_writer(
        output_path,
        mode='I',
        duration=frame_duration,
        loop=0  # 0 means loop forever in GIF format
    )
    
    # Process frames
    for i in range(max(gif1_frames, gif2_frames)):
        # Get frames from both GIFs (loop if necessary)
        frame1 = Image.fromarray(gif1.get_data(i % gif1_frames))
        frame2 = Image.fromarray(gif2.get_data(i % gif2_frames))
        
        # Create a new blank frame
        combined = Image.new('RGBA', (total_width, max_height))
        
        # Calculate vertical positions to center the images
        pos1_y = (max_height - gif1_height) // 2
        pos2_y = (max_height - gif2_height) // 2
        
        # Paste both frames
        combined.paste(frame1, (0, pos1_y))
        combined.paste(frame2, (gif1_width, pos2_y))
        
        # Add the combined frame to the output GIF
        writer.append_data(numpy.array(combined))
    
    writer.close()

def main():
    """Main function to handle command line arguments."""
    if len(sys.argv) != 4:
        print("Usage: python gifcombine.py input1.gif input2.gif output.gif")
        sys.exit(1)
        
    gif1_path = sys.argv[1]
    gif2_path = sys.argv[2]
    output_path = sys.argv[3]
    
    try:
        combine_gifs(gif1_path, gif2_path, output_path)
        print(f"Successfully combined GIFs into {output_path}")
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main() 