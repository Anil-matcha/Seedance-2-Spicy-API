import sys
import os
import argparse
import json

# Add the parent directory to the path so we can import the existing Seedance2SpicyAPI
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from seedance_2_spicy_api import Seedance2SpicyAPI


def main():
    parser = argparse.ArgumentParser(description="Seedance 2 Spicy CLI Wrapper for OpenClaw Skill")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    t2v = subparsers.add_parser("t2v", help="Generate video from text (Spicy)")
    t2v.add_argument("--prompt", required=True, help="Text prompt")
    t2v.add_argument("--aspect_ratio", default="16:9", help="Aspect ratio")
    t2v.add_argument("--duration", type=int, default=5, help="Duration in seconds (4-15)")
    t2v.add_argument("--high_bitrate", action="store_true", help="Enable high bitrate mode")
    t2v.add_argument("--wait", action="store_true", help="Wait for completion")

    t2v_fast = subparsers.add_parser("t2v-fast", help="Generate video from text (Spicy Fast)")
    t2v_fast.add_argument("--prompt", required=True, help="Text prompt")
    t2v_fast.add_argument("--aspect_ratio", default="16:9", help="Aspect ratio")
    t2v_fast.add_argument("--duration", type=int, default=5, help="Duration in seconds (4-15)")
    t2v_fast.add_argument("--high_bitrate", action="store_true", help="Enable high bitrate mode")
    t2v_fast.add_argument("--wait", action="store_true", help="Wait for completion")

    i2v = subparsers.add_parser("i2v", help="Generate video from image (Spicy)")
    i2v.add_argument("--prompt", required=True, help="Text prompt")
    i2v.add_argument("--images", required=True, nargs="+", help="1-2 image URLs")
    i2v.add_argument("--aspect_ratio", default="16:9", help="Aspect ratio")
    i2v.add_argument("--duration", type=int, default=5, help="Duration in seconds (4-15)")
    i2v.add_argument("--high_bitrate", action="store_true", help="Enable high bitrate mode")
    i2v.add_argument("--wait", action="store_true", help="Wait for completion")

    i2v_fast = subparsers.add_parser("i2v-fast", help="Generate video from image (Spicy Fast)")
    i2v_fast.add_argument("--prompt", required=True, help="Text prompt")
    i2v_fast.add_argument("--images", required=True, nargs="+", help="1-2 image URLs")
    i2v_fast.add_argument("--aspect_ratio", default="16:9", help="Aspect ratio")
    i2v_fast.add_argument("--duration", type=int, default=5, help="Duration in seconds (4-15)")
    i2v_fast.add_argument("--high_bitrate", action="store_true", help="Enable high bitrate mode")
    i2v_fast.add_argument("--wait", action="store_true", help="Wait for completion")

    omni = subparsers.add_parser("omni", help="Generate video with image/video/audio references (Spicy)")
    omni.add_argument("--prompt", required=True, help="Text prompt")
    omni.add_argument("--resolution", default="720p", choices=["720p", "1080p", "4k"], help="Output resolution")
    omni.add_argument("--images", nargs="*", help="Up to 9 image URLs")
    omni.add_argument("--videos", nargs="*", help="Up to 3 video URLs")
    omni.add_argument("--audios", nargs="*", help="Up to 3 audio URLs")
    omni.add_argument("--aspect_ratio", default="16:9", help="Aspect ratio")
    omni.add_argument("--duration", type=int, default=5, help="Duration in seconds (4-15)")
    omni.add_argument("--high_bitrate", action="store_true", help="Enable high bitrate mode")
    omni.add_argument("--wait", action="store_true", help="Wait for completion")

    omni_fast = subparsers.add_parser("omni-fast", help="Generate video with references (Spicy Fast)")
    omni_fast.add_argument("--prompt", required=True, help="Text prompt")
    omni_fast.add_argument("--resolution", default="720p", choices=["720p", "1080p", "4k"], help="Output resolution")
    omni_fast.add_argument("--images", nargs="*", help="Up to 9 image URLs")
    omni_fast.add_argument("--videos", nargs="*", help="Up to 3 video URLs")
    omni_fast.add_argument("--audios", nargs="*", help="Up to 3 audio URLs")
    omni_fast.add_argument("--aspect_ratio", default="16:9", help="Aspect ratio")
    omni_fast.add_argument("--duration", type=int, default=5, help="Duration in seconds (4-15)")
    omni_fast.add_argument("--high_bitrate", action="store_true", help="Enable high bitrate mode")
    omni_fast.add_argument("--wait", action="store_true", help="Wait for completion")

    mini_t2v = subparsers.add_parser("mini-t2v", help="Generate video from text (Mini Spicy)")
    mini_t2v.add_argument("--prompt", required=True, help="Text prompt")
    mini_t2v.add_argument("--aspect_ratio", default="16:9", help="Aspect ratio")
    mini_t2v.add_argument("--duration", type=int, default=5, help="Duration in seconds (4-15)")
    mini_t2v.add_argument("--resolution", default="720p", choices=["480p", "720p"], help="Output resolution")
    mini_t2v.add_argument("--no_audio", action="store_true", help="Disable AI audio generation")
    mini_t2v.add_argument("--high_bitrate", action="store_true", help="Enable high bitrate mode")
    mini_t2v.add_argument("--wait", action="store_true", help="Wait for completion")

    mini_i2v = subparsers.add_parser("mini-i2v", help="Generate video from image (Mini Spicy)")
    mini_i2v.add_argument("--prompt", help="Optional text prompt")
    mini_i2v.add_argument("--images", required=True, nargs="+", help="1-9 image URLs")
    mini_i2v.add_argument("--aspect_ratio", default="16:9", help="Aspect ratio")
    mini_i2v.add_argument("--duration", type=int, default=5, help="Duration in seconds (4-15)")
    mini_i2v.add_argument("--resolution", default="720p", choices=["480p", "720p"], help="Output resolution")
    mini_i2v.add_argument("--no_audio", action="store_true", help="Disable AI audio generation")
    mini_i2v.add_argument("--high_bitrate", action="store_true", help="Enable high bitrate mode")
    mini_i2v.add_argument("--wait", action="store_true", help="Wait for completion")

    mini_omni = subparsers.add_parser("mini-omni", help="Reference-driven generation (Mini Spicy Omni)")
    mini_omni.add_argument("--prompt", required=True, help="Text prompt")
    mini_omni.add_argument("--images", nargs="*", help="Up to 9 image URLs")
    mini_omni.add_argument("--videos", nargs="*", help="Up to 3 video URLs")
    mini_omni.add_argument("--audios", nargs="*", help="Up to 3 audio URLs")
    mini_omni.add_argument("--aspect_ratio", default="16:9", help="Aspect ratio")
    mini_omni.add_argument("--duration", type=int, default=5, help="Duration in seconds (4-15)")
    mini_omni.add_argument("--resolution", default="720p", choices=["480p", "720p"], help="Output resolution")
    mini_omni.add_argument("--no_audio", action="store_true", help="Disable AI audio generation")
    mini_omni.add_argument("--high_bitrate", action="store_true", help="Enable high bitrate mode")
    mini_omni.add_argument("--wait", action="store_true", help="Wait for completion")

    status = subparsers.add_parser("status", help="Get task status")
    status.add_argument("--request_id", required=True, help="Request ID")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    try:
        api = Seedance2SpicyAPI()

        if args.command == "t2v":
            res = api.text_to_video(args.prompt, args.aspect_ratio, args.duration, args.high_bitrate)
        elif args.command == "t2v-fast":
            res = api.text_to_video_fast(args.prompt, args.aspect_ratio, args.duration, args.high_bitrate)
        elif args.command == "i2v":
            res = api.image_to_video(args.prompt, args.images, args.aspect_ratio, args.duration, args.high_bitrate)
        elif args.command == "i2v-fast":
            res = api.image_to_video_fast(args.prompt, args.images, args.aspect_ratio, args.duration, args.high_bitrate)
        elif args.command == "omni":
            res = api.omni_reference(args.prompt, args.resolution, args.images, args.videos, args.audios, args.aspect_ratio, args.duration, args.high_bitrate)
        elif args.command == "omni-fast":
            res = api.omni_reference_fast(args.prompt, args.resolution, args.images, args.videos, args.audios, args.aspect_ratio, args.duration, args.high_bitrate)
        elif args.command == "mini-t2v":
            res = api.mini_text_to_video(args.prompt, args.aspect_ratio, args.duration, args.resolution, not args.no_audio, args.high_bitrate)
        elif args.command == "mini-i2v":
            res = api.mini_image_to_video(args.images, args.prompt, args.aspect_ratio, args.duration, args.resolution, not args.no_audio, args.high_bitrate)
        elif args.command == "mini-omni":
            res = api.mini_omni_reference(args.prompt, args.images, args.videos, args.audios, args.aspect_ratio, args.duration, args.resolution, not args.no_audio, args.high_bitrate)
        elif args.command == "status":
            res = api.get_result(args.request_id)
            print(json.dumps(res, indent=2))
            return

        request_id = res.get("request_id")

        if args.wait and request_id:
            print(f"Task submitted: {request_id}. Waiting for completion...")
            result = api.wait_for_completion(request_id)
            print(json.dumps(result, indent=2))
        else:
            print(json.dumps(res, indent=2))

    except Exception as e:
        print(json.dumps({"error": str(e)}, indent=2))
        sys.exit(1)


if __name__ == "__main__":
    main()
