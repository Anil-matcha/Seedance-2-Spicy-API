---
name: seedance-2-spicy
description: Generate AI videos with reduced content-safety filtering using Seedance 2 Spicy, Seedance 2 Spicy Fast, and Seedance 2 Mini Spicy (by ByteDance).
version: 1.0.0
metadata:
  openclaw:
    requires:
      env:
        - MUAPI_API_KEY
      bins:
        - python3.11
    emoji: 🌶️
    homepage: https://muapi.ai
    os: ["macos", "linux"]
---

# Seedance 2 Spicy

Seedance 2 Spicy is the relaxed-moderation VIP tier of ByteDance's Seedance 2.0 video model, delivered via MuAPI. It keeps Seedance 2 VIP's priority routing, native audio-visual sync, and up to 2K resolution, but with reduced content-safety filtering for broader creative freedom. Seedance 2 Mini Spicy applies the same relaxed filtering to the faster, lower-cost Mini tier.

## Prerequisites

- **MUAPI_API_KEY**: You must have an API key from [muapi.ai](https://muapi.ai). Set it as an environment variable.

## Usage Guide

### Text-to-Video (Spicy)
```bash
python3.11 skills/seedance-2-spicy/seedance_2_spicy_cli.py t2v --prompt "A cinematic shot of a futuristic city at night with neon lights reflecting on wet streets" --wait
```

### Text-to-Video (Spicy Fast)
```bash
python3.11 skills/seedance-2-spicy/seedance_2_spicy_cli.py t2v-fast --prompt "A dramatic chase scene through a neon city" --wait
```

### Image-to-Video (Spicy)
```bash
python3.11 skills/seedance-2-spicy/seedance_2_spicy_cli.py i2v --images "https://example.com/image.jpg" --prompt "The person walks forward with a smile" --wait
```

### Image-to-Video (Spicy Fast)
```bash
python3.11 skills/seedance-2-spicy/seedance_2_spicy_cli.py i2v-fast --images "https://example.com/image.jpg" --prompt "Make the clouds move slowly" --wait
```

### Omni-Reference (Spicy)
Condition a video on up to 9 images, 3 video clips, and 3 audio references.
```bash
python3.11 skills/seedance-2-spicy/seedance_2_spicy_cli.py omni --prompt "@image1 walks along a city street at sunset, cinematic lighting" --images "https://example.com/bg.jpg" --resolution 1080p --wait
```

### Omni-Reference (Spicy Fast)
```bash
python3.11 skills/seedance-2-spicy/seedance_2_spicy_cli.py omni-fast --prompt "@image1 and @video1 blend into a chase scene" --images "https://example.com/subject.jpg" --videos "https://example.com/motion.mp4" --wait
```

### Seedance 2 Mini Spicy Text-to-Video
```bash
python3.11 skills/seedance-2-spicy/seedance_2_spicy_cli.py mini-t2v --prompt "A golden retriever running through a sunlit meadow, slow motion" --wait
```

### Seedance 2 Mini Spicy Image-to-Video
```bash
python3.11 skills/seedance-2-spicy/seedance_2_spicy_cli.py mini-i2v --images "https://example.com/rooftop.jpg" --prompt "A slow cinematic push toward the subject, gentle breeze" --wait
```

### Seedance 2 Mini Spicy Omni Reference
```bash
python3.11 skills/seedance-2-spicy/seedance_2_spicy_cli.py mini-omni --prompt "The character walks forward confidently in a sunny meadow" --images "https://example.com/character.jpg" --wait
```

## Tips for Best Results

- **Be Descriptive**: Detailed prompts result in better video quality and more accurate motion.
- **Wait for Completion**: Use `--wait` to receive the final video URL directly. Without it, you get a `request_id` to check later with the `status` command.
- **Character References**: Use `@character:<id>` or `@omni-character:<id>` inline in the prompt to anchor a generation to a Seedance 2 character sheet.
- **Omni Reference Resolution**: `omni`/`omni-fast` price scales with `--resolution` (720p cheapest, 4k most expensive).
- **Fast vs. Standard**: The `-fast` variants trade a small amount of quality for the quickest queue at a lower price.
- **Mini for Volume**: Use the `mini-*` commands for high-volume or latency-sensitive pipelines where lowest cost matters most.

## Commands Reference

| Command | Arguments | Description |
| :--- | :--- | :--- |
| `t2v` | `--prompt`, `--aspect_ratio`, `--duration`, `--high_bitrate`, `--wait` | Spicy Text to Video |
| `t2v-fast` | `--prompt`, `--aspect_ratio`, `--duration`, `--high_bitrate`, `--wait` | Spicy Text to Video Fast |
| `i2v` | `--prompt`, `--images`, `--aspect_ratio`, `--duration`, `--high_bitrate`, `--wait` | Spicy Image to Video |
| `i2v-fast` | `--prompt`, `--images`, `--aspect_ratio`, `--duration`, `--high_bitrate`, `--wait` | Spicy Image to Video Fast |
| `omni` | `--prompt`, `--resolution`, `--images`, `--videos`, `--audios`, `--aspect_ratio`, `--duration`, `--high_bitrate`, `--wait` | Spicy Omni Reference |
| `omni-fast` | same as `omni` | Spicy Omni Reference Fast |
| `mini-t2v` | `--prompt`, `--aspect_ratio`, `--duration`, `--resolution`, `--no_audio`, `--high_bitrate`, `--wait` | Mini Spicy Text to Video |
| `mini-i2v` | `--prompt`, `--images`, `--aspect_ratio`, `--duration`, `--resolution`, `--no_audio`, `--high_bitrate`, `--wait` | Mini Spicy Image to Video |
| `mini-omni` | `--prompt`, `--images`, `--videos`, `--audios`, `--aspect_ratio`, `--duration`, `--resolution`, `--no_audio`, `--high_bitrate`, `--wait` | Mini Spicy Omni Reference |
| `status` | `--request_id` | Check Task Status |
