#!/usr/bin/env python3
"""
Test suite for the GIF combine utility.
"""

import os
import pytest
from PIL import Image
from gifcombine import get_gif_info, combine_gifs

@pytest.fixture
def sample_gif1(tmp_path):
    """Create a sample GIF file for testing."""
    gif_path = tmp_path / "test1.gif"
    frames = []
    for i in range(3):
        img = Image.new('RGB', (100, 100), color=f'rgb({i*50}, {i*50}, {i*50})')
        frames.append(img)
    
    frames[0].save(
        gif_path,
        save_all=True,
        append_images=frames[1:],
        duration=100,
        loop=0
    )
    return str(gif_path)

@pytest.fixture
def sample_gif2(tmp_path):
    """Create another sample GIF file for testing."""
    gif_path = tmp_path / "test2.gif"
    frames = []
    for i in range(2):
        img = Image.new('RGB', (50, 50), color=f'rgb({i*100}, {i*100}, {i*100})')
        frames.append(img)
    
    frames[0].save(
        gif_path,
        save_all=True,
        append_images=frames[1:],
        duration=200,
        loop=0
    )
    return str(gif_path)

def test_get_gif_info(sample_gif1, sample_gif2):
    """Test getting GIF information."""
    frames1, size1 = get_gif_info(sample_gif1)
    frames2, size2 = get_gif_info(sample_gif2)
    
    assert frames1 == 3
    assert size1 == (100, 100)
    assert frames2 == 2
    assert size2 == (50, 50)

def test_combine_gifs(sample_gif1, sample_gif2, tmp_path):
    """Test combining two GIFs."""
    output_path = str(tmp_path / "output.gif")
    combine_gifs(sample_gif1, sample_gif2, output_path)
    
    assert os.path.exists(output_path)
    frames, (width, height) = get_gif_info(output_path)
    
    # Check that the output has the correct dimensions
    assert width == 150  # 100 + 50
    assert height == 100  # max(100, 50)
    
    # Check that we have the correct number of frames
    assert frames == 3  # max(3, 2) 