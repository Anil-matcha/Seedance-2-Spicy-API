import json
from mcp.server.fastmcp import FastMCP
from seedance_2_spicy_api import Seedance2SpicyAPI

# Initialize FastMCP server
mcp = FastMCP("Seedance 2 Spicy API Server")


def get_api():
    return Seedance2SpicyAPI()


@mcp.tool()
def text_to_video(prompt: str, aspect_ratio: str = "16:9", duration: int = 5, high_bitrate: bool = False) -> str:
    """
    Generate a video from a text prompt using Seedance 2 Spicy (relaxed content moderation, VIP tier).

    :param prompt: Text description. Supports @character:<id> / @omni-character:<id>.
    :param aspect_ratio: '21:9', '16:9', '4:3', '1:1', '3:4', or '9:16'.
    :param duration: Duration in seconds (4-15).
    :param high_bitrate: Enable high bitrate mode.
    """
    api = get_api()
    result = api.text_to_video(prompt, aspect_ratio, duration, high_bitrate)
    return json.dumps(result, indent=2)


@mcp.tool()
def text_to_video_fast(prompt: str, aspect_ratio: str = "16:9", duration: int = 5, high_bitrate: bool = False) -> str:
    """
    Generate a video from text using Seedance 2 Spicy Fast (quickest Spicy-tier text-to-video).
    """
    api = get_api()
    result = api.text_to_video_fast(prompt, aspect_ratio, duration, high_bitrate)
    return json.dumps(result, indent=2)


@mcp.tool()
def image_to_video(prompt: str, images_list: list[str], aspect_ratio: str = "16:9", duration: int = 5, high_bitrate: bool = False) -> str:
    """
    Animate 1-2 images into a video using Seedance 2 Spicy.

    :param images_list: 1 image for a start frame, 2 for a start-to-end transition.
    """
    api = get_api()
    result = api.image_to_video(prompt, images_list, aspect_ratio, duration, high_bitrate)
    return json.dumps(result, indent=2)


@mcp.tool()
def image_to_video_fast(prompt: str, images_list: list[str], aspect_ratio: str = "16:9", duration: int = 5, high_bitrate: bool = False) -> str:
    """
    Animate 1-2 images into a video using Seedance 2 Spicy Fast.
    """
    api = get_api()
    result = api.image_to_video_fast(prompt, images_list, aspect_ratio, duration, high_bitrate)
    return json.dumps(result, indent=2)


@mcp.tool()
def omni_reference(prompt: str, resolution: str = "720p", images_list: list[str] = None,
                    video_files: list[str] = None, audio_files: list[str] = None,
                    aspect_ratio: str = "16:9", duration: int = 5, high_bitrate: bool = False) -> str:
    """
    Generate a video conditioned on up to 9 images, 3 videos, and 3 audio references using Seedance 2 Spicy Omni Reference.

    :param resolution: '720p', '1080p', or '4k'. Price scales with resolution.
    """
    api = get_api()
    result = api.omni_reference(prompt, resolution, images_list, video_files, audio_files, aspect_ratio, duration, high_bitrate)
    return json.dumps(result, indent=2)


@mcp.tool()
def omni_reference_fast(prompt: str, resolution: str = "720p", images_list: list[str] = None,
                         video_files: list[str] = None, audio_files: list[str] = None,
                         aspect_ratio: str = "16:9", duration: int = 5, high_bitrate: bool = False) -> str:
    """
    Faster Seedance 2 Spicy Omni Reference generation with priority routing.
    """
    api = get_api()
    result = api.omni_reference_fast(prompt, resolution, images_list, video_files, audio_files, aspect_ratio, duration, high_bitrate)
    return json.dumps(result, indent=2)


@mcp.tool()
def mini_text_to_video(prompt: str, aspect_ratio: str = "16:9", duration: int = 5, resolution: str = "720p",
                        generate_audio: bool = True, high_bitrate: bool = False) -> str:
    """
    Generate a video from text using Seedance 2 Mini Spicy — fastest, lowest-cost Spicy-tier T2V.
    """
    api = get_api()
    result = api.mini_text_to_video(prompt, aspect_ratio, duration, resolution, generate_audio, high_bitrate)
    return json.dumps(result, indent=2)


@mcp.tool()
def mini_image_to_video(images_list: list[str], prompt: str = None, aspect_ratio: str = "16:9", duration: int = 5,
                         resolution: str = "720p", generate_audio: bool = True, high_bitrate: bool = False) -> str:
    """
    Animate an image using Seedance 2 Mini Spicy — fastest, lowest-cost Spicy-tier image animation.
    """
    api = get_api()
    result = api.mini_image_to_video(images_list, prompt, aspect_ratio, duration, resolution, generate_audio, high_bitrate)
    return json.dumps(result, indent=2)


@mcp.tool()
def mini_omni_reference(prompt: str, images_list: list[str] = None, video_files: list[str] = None,
                         audio_files: list[str] = None, aspect_ratio: str = "16:9", duration: int = 5,
                         resolution: str = "720p", generate_audio: bool = True, high_bitrate: bool = False) -> str:
    """
    Reference-driven video generation using Seedance 2 Mini Spicy Omni Reference.
    """
    api = get_api()
    result = api.mini_omni_reference(prompt, images_list, video_files, audio_files, aspect_ratio, duration, resolution, generate_audio, high_bitrate)
    return json.dumps(result, indent=2)


@mcp.tool()
def upload_file(file_path: str) -> str:
    """
    Upload a local file (image or video) to MuAPI for use in generation tasks.
    """
    api = get_api()
    result = api.upload_file(file_path)
    return json.dumps(result, indent=2)


@mcp.tool()
def get_task_status(request_id: str) -> str:
    """
    Check the status and get results of a generation task.
    """
    api = get_api()
    result = api.get_result(request_id)
    return json.dumps(result, indent=2)


if __name__ == "__main__":
    mcp.run()
