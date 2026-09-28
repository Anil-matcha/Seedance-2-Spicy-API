import os
import requests
import time
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Seedance2SpicyAPI:
    def __init__(self, api_key=None):
        """
        Initialize the Seedance 2 Spicy API client.
        :param api_key: Your MuAPI.ai API key. Defaults to MUAPI_API_KEY environment variable.
        """
        self.api_key = api_key or os.getenv("MUAPI_API_KEY")
        if not self.api_key:
            raise ValueError("API Key is required. Set MUAPI_API_KEY in .env or pass it to the constructor.")

        self.base_url = "https://api.muapi.ai/api/v1"
        self.headers = {
            "x-api-key": self.api_key,
            "Content-Type": "application/json"
        }

    def text_to_video(self, prompt, aspect_ratio="16:9", duration=5, high_bitrate=False):
        """
        Submits a Seedance 2 Spicy Text-to-Video task. Same VIP-tier priority routing,
        native audio-visual sync, and up to 2K resolution as Seedance 2 VIP, with
        reduced content-safety filtering.

        :param prompt: Text description of the video to generate. Use @character:<id> to
                       anchor to a Seedance 2 character (switches to image-to-video mode).
                       Use @omni-character:<char_id> for a trained omni-character.
        :param aspect_ratio: '21:9', '16:9', '4:3', '1:1', '3:4', or '9:16'.
        :param duration: Video duration in seconds (4-15).
        :param high_bitrate: Enable high bitrate mode for better visual fidelity.
        :return: JSON response with request_id.
        """
        endpoint = f"{self.base_url}/seedance-2-spicy-text-to-video"
        payload = {
            "prompt": prompt,
            "aspect_ratio": aspect_ratio,
            "duration": duration,
            "high_bitrate": high_bitrate,
        }
        return self._post_request(endpoint, payload)

    def text_to_video_fast(self, prompt, aspect_ratio="16:9", duration=5, high_bitrate=False):
        """
        Submits a Seedance 2 Spicy Text-to-Video Fast task — the quickest Spicy-tier
        text-to-video generation, same fast queue as Seedance 2 VIP Fast.

        :param prompt: Text description of the video to generate.
        :param aspect_ratio: '21:9', '16:9', '4:3', '1:1', '3:4', or '9:16'.
        :param duration: Video duration in seconds (4-15).
        :param high_bitrate: Enable high bitrate mode for better visual fidelity.
        :return: JSON response with request_id.
        """
        endpoint = f"{self.base_url}/seedance-2-spicy-text-to-video-fast"
        payload = {
            "prompt": prompt,
            "aspect_ratio": aspect_ratio,
            "duration": duration,
            "high_bitrate": high_bitrate,
        }
        return self._post_request(endpoint, payload)

    def image_to_video(self, prompt, images_list, aspect_ratio="16:9", duration=5, high_bitrate=False):
        """
        Submits a Seedance 2 Spicy Image-to-Video task. Animates a start frame (and
        optional end frame) into cinematic video with VIP-tier priority routing and
        up to 2K resolution, reduced content-safety filtering.

        :param prompt: Text description guiding the animation. Use @character:<id> or
                       @omni-character:<char_id> to reference a trained character.
        :param images_list: 1 or 2 image URLs — 1 for a start frame, 2 for a start-to-end transition.
        :param aspect_ratio: '21:9', '16:9', '4:3', '1:1', '3:4', or '9:16'.
        :param duration: Video duration in seconds (4-15).
        :param high_bitrate: Enable high bitrate mode for better visual fidelity.
        :return: JSON response with request_id.
        """
        endpoint = f"{self.base_url}/seedance-2-spicy-image-to-video"
        payload = {
            "prompt": prompt,
            "images_list": images_list,
            "aspect_ratio": aspect_ratio,
            "duration": duration,
            "high_bitrate": high_bitrate,
        }
        return self._post_request(endpoint, payload)

    def image_to_video_fast(self, prompt, images_list, aspect_ratio="16:9", duration=5, high_bitrate=False):
        """
        Submits a Seedance 2 Spicy Image-to-Video Fast task — the quickest Spicy-tier
        image animation, same fast queue as Seedance 2 VIP Fast.

        :param prompt: Text description guiding the animation.
        :param images_list: 1 or 2 image URLs.
        :param aspect_ratio: '21:9', '16:9', '4:3', '1:1', '3:4', or '9:16'.
        :param duration: Video duration in seconds (4-15).
        :param high_bitrate: Enable high bitrate mode for better visual fidelity.
        :return: JSON response with request_id.
        """
        endpoint = f"{self.base_url}/seedance-2-spicy-image-to-video-fast"
        payload = {
            "prompt": prompt,
            "images_list": images_list,
            "aspect_ratio": aspect_ratio,
            "duration": duration,
            "high_bitrate": high_bitrate,
        }
        return self._post_request(endpoint, payload)

    def omni_reference(self, prompt, resolution="720p", images_list=None, video_files=None,
                        audio_files=None, aspect_ratio="16:9", duration=5, high_bitrate=False):
        """
        Submits a Seedance 2 Spicy Omni Reference task. Generates video from up to 9
        image references, 3 video clips, and 3 audio references, with reduced
        content-safety filtering. Reference materials in the prompt with
        @image1...@image9, @video1...@video3, @audio1...@audio3.

        :param prompt: Video description referencing @imageN/@videoN/@audioN and/or
                       @character:<id> / @omni-character:<id>.
        :param resolution: '720p', '1080p', or '4k'. Price scales with resolution.
        :param images_list: Up to 9 reference image URLs.
        :param video_files: Up to 3 reference video URLs (max 15s each).
        :param audio_files: Up to 3 reference audio URLs (total max 15s).
        :param aspect_ratio: '21:9', '16:9', '4:3', '1:1', '3:4', or '9:16'.
        :param duration: Video duration in seconds (4-15).
        :param high_bitrate: Enable high bitrate mode for better visual fidelity.
        :return: JSON response with request_id.
        """
        endpoint = f"{self.base_url}/seedance-2-spicy-omni-reference"
        payload = {
            "prompt": prompt,
            "resolution": resolution,
            "aspect_ratio": aspect_ratio,
            "duration": duration,
            "high_bitrate": high_bitrate,
        }
        if images_list:
            payload["images_list"] = images_list
        if video_files:
            payload["video_files"] = video_files
        if audio_files:
            payload["audio_files"] = audio_files
        return self._post_request(endpoint, payload)

    def omni_reference_fast(self, prompt, resolution="720p", images_list=None, video_files=None,
                             audio_files=None, aspect_ratio="16:9", duration=5, high_bitrate=False):
        """
        Submits a Seedance 2 Spicy Omni Reference Fast task — faster generation with
        priority routing, up to 9 image references, 3 video clips, and 3 audio
        references, reduced content-safety filtering.

        :param prompt: Video description referencing @imageN/@videoN/@audioN.
        :param resolution: '720p', '1080p', or '4k'. Price scales with resolution.
        :param images_list: Up to 9 reference image URLs.
        :param video_files: Up to 3 reference video URLs (max 15s each).
        :param audio_files: Up to 3 reference audio URLs (total max 15s).
        :param aspect_ratio: '21:9', '16:9', '4:3', '1:1', '3:4', or '9:16'.
        :param duration: Video duration in seconds (4-15).
        :param high_bitrate: Enable high bitrate mode for better visual fidelity.
        :return: JSON response with request_id.
        """
        endpoint = f"{self.base_url}/seedance-2-spicy-omni-reference-fast"
        payload = {
            "prompt": prompt,
            "resolution": resolution,
            "aspect_ratio": aspect_ratio,
            "duration": duration,
            "high_bitrate": high_bitrate,
        }
        if images_list:
            payload["images_list"] = images_list
        if video_files:
            payload["video_files"] = video_files
        if audio_files:
            payload["audio_files"] = audio_files
        return self._post_request(endpoint, payload)

    def mini_text_to_video(self, prompt, aspect_ratio="16:9", duration=5, resolution="720p",
                            generate_audio=True, high_bitrate=False):
        """
        Submits a Seedance 2 Mini Spicy Text-to-Video task — the fastest, lowest-cost
        Spicy-tier text-to-video, with reduced content-safety filtering on top of
        Seedance 2 Mini's speed and pricing.

        :param prompt: Text prompt describing the video scene and motion.
        :param aspect_ratio: '16:9', '9:16', '1:1', '3:4', '4:3', or '21:9'.
        :param duration: Video duration in seconds (4-15).
        :param resolution: '480p' or '720p'.
        :param generate_audio: Whether to generate AI audio synchronized with the video.
        :param high_bitrate: Enable high bitrate mode for better visual fidelity.
        :return: JSON response with request_id.
        """
        endpoint = f"{self.base_url}/seedance-2-mini-spicy-text-to-video"
        payload = {
            "prompt": prompt,
            "aspect_ratio": aspect_ratio,
            "duration": duration,
            "resolution": resolution,
            "generate_audio": generate_audio,
            "high_bitrate": high_bitrate,
        }
        return self._post_request(endpoint, payload)

    def mini_image_to_video(self, images_list, prompt=None, aspect_ratio="16:9", duration=5,
                             resolution="720p", generate_audio=True, high_bitrate=False):
        """
        Submits a Seedance 2 Mini Spicy Image-to-Video task — the fastest, lowest-cost
        Spicy-tier image animation, with reduced content-safety filtering.

        :param images_list: 1 image = start frame. 2-9 images = reference images
                            (reference them in the prompt with @image1, @image2, etc.).
        :param prompt: Text prompt guiding the video animation.
        :param aspect_ratio: '16:9', '9:16', '1:1', '3:4', '4:3', or '21:9'.
        :param duration: Video duration in seconds (4-15).
        :param resolution: '480p' or '720p'.
        :param generate_audio: Whether to generate AI audio synchronized with the video.
        :param high_bitrate: Enable high bitrate mode for better visual fidelity.
        :return: JSON response with request_id.
        """
        endpoint = f"{self.base_url}/seedance-2-mini-spicy-image-to-video"
        payload = {
            "images_list": images_list,
            "aspect_ratio": aspect_ratio,
            "duration": duration,
            "resolution": resolution,
            "generate_audio": generate_audio,
            "high_bitrate": high_bitrate,
        }
        if prompt:
            payload["prompt"] = prompt
        return self._post_request(endpoint, payload)

    def mini_omni_reference(self, prompt, images_list=None, video_files=None, audio_files=None,
                             aspect_ratio="16:9", duration=5, resolution="720p",
                             generate_audio=True, high_bitrate=False):
        """
        Submits a Seedance 2 Mini Spicy Omni Reference task — cost-efficient mini-tier
        model for reference-driven workflows, with reduced content-safety filtering.

        :param prompt: Text prompt. Reference images with @image1..@image9, videos with
                       @video1..@video3, audio with @audio1..@audio3.
        :param images_list: Up to 9 reference images (JPEG/PNG/WebP).
        :param video_files: Up to 3 reference video clips (MP4, total max 15s).
        :param audio_files: Up to 3 reference audio files (MP3/WAV, total max 15s).
        :param aspect_ratio: '16:9', '9:16', '1:1', '3:4', '4:3', or '21:9'.
        :param duration: Video duration in seconds (4-15).
        :param resolution: '480p' or '720p'.
        :param generate_audio: Whether to generate AI audio synchronized with the video.
        :param high_bitrate: Enable high bitrate mode for better visual fidelity.
        :return: JSON response with request_id.
        """
        endpoint = f"{self.base_url}/seedance-2-mini-spicy-omni-reference"
        payload = {
            "prompt": prompt,
            "aspect_ratio": aspect_ratio,
            "duration": duration,
            "resolution": resolution,
            "generate_audio": generate_audio,
            "high_bitrate": high_bitrate,
        }
        if images_list:
            payload["images_list"] = images_list
        if video_files:
            payload["video_files"] = video_files
        if audio_files:
            payload["audio_files"] = audio_files
        return self._post_request(endpoint, payload)

    def _post_request(self, endpoint, payload):
        response = requests.post(endpoint, json=payload, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def upload_file(self, file_path):
        """
        Uploads a file (image or video) to MuAPI for use in generation tasks.

        :param file_path: Path to the local file to upload.
        :return: JSON response from the MuAPI containing the URL of the uploaded file.
        """
        endpoint = f"{self.base_url}/upload_file"

        # Omit Content-Type to let requests set the multipart boundary automatically
        headers = {
            "x-api-key": self.api_key
        }

        with open(file_path, "rb") as file_data:
            files = {"file": file_data}
            response = requests.post(endpoint, headers=headers, files=files)

        response.raise_for_status()
        return response.json()

    def get_result(self, request_id):
        """
        Polls for the result of a generation task.
        """
        endpoint = f"{self.base_url}/predictions/{request_id}/result"
        response = requests.get(endpoint, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def wait_for_completion(self, request_id, poll_interval=5, timeout=600):
        """
        Waits for the video generation to complete and returns the result.
        """
        start_time = time.time()
        while time.time() - start_time < timeout:
            result = self.get_result(request_id)
            status = result.get("status")

            if status == "completed":
                return result
            elif status == "failed":
                raise Exception(f"Video generation failed: {result.get('error')}")

            print(f"Status: {status}. Waiting {poll_interval} seconds...")
            time.sleep(poll_interval)

        raise TimeoutError("Timed out waiting for video generation to complete.")


if __name__ == "__main__":
    try:
        api = Seedance2SpicyAPI()
        prompt = "A cinematic shot of a futuristic city at night with neon lights reflecting on wet streets"

        print(f"Submitting Seedance 2 Spicy T2V task with prompt: {prompt}")
        submission = api.text_to_video(prompt=prompt, duration=5)
        request_id = submission.get("request_id")
        print(f"Task submitted. Request ID: {request_id}")

        print("Waiting for completion...")
        result = api.wait_for_completion(request_id)
        print(f"Generation completed! Video URL: {result.get('outputs', [result.get('url')])[0]}")

    except Exception as e:
        print(f"Error: {e}")
