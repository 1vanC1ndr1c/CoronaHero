import pygame


def split_animated_gif(gif):
    """
    This function splits a gif into a list of images that were the individual frames of the gif.
    :param gif: Gif to be split.
    :return: list: List of images that represent individual frames.
    """
    images = []
    for frame_index in range(gif.n_frames):
        gif.seek(frame_index)
        frame_rgba = gif.convert("RGBA")
        pygame_image = pygame.image.fromstring(frame_rgba.tobytes(), frame_rgba.size, frame_rgba.mode)
        images.append(pygame_image)
    return images
