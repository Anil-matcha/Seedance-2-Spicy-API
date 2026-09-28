# Seedance 2 Spicy API: Python Wrapper for ByteDance's Relaxed-Moderation AI Video Generator

[![Powered by MuAPI](https://img.shields.io/badge/Powered%20by-MuAPI-6366f1?style=flat-square&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0id2hpdGUiIGQ9Ik0xMiAyQzYuNDggMiAyIDYuNDggMiAxMnM0LjQ4IDEwIDEwIDEwIDEwLTQuNDggMTAtMTBTMTcuNTIgMiAxMiAyem0tMSAxNHYtNGgtMnYtMmg0djZoLTJ6bTAtOFY2aDJ2MmgtMnoiLz48L3N2Zz4=)](https://muapi.ai?utm_source=github&utm_medium=badge&utm_campaign=seedance-2-spicy-api)

[![PyPI version](https://img.shields.io/pypi/v/seedance-2-spicy-api.svg)](https://pypi.org/project/seedance-2-spicy-api/)
[![GitHub stars](https://img.shields.io/github/stars/Anil-matcha/Seedance-2-Spicy-API.svg)](https://github.com/Anil-matcha/Seedance-2-Spicy-API/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)

The most comprehensive Python wrapper for the **Seedance 2 Spicy API** (developed by ByteDance), delivered via [muapi.ai](https://muapi.ai?utm_source=github&utm_medium=readme&utm_campaign=seedance-2-spicy-api). Seedance 2 Spicy is the relaxed-moderation VIP tier of Seedance 2.0 — same priority routing, native audio-visual sync, and up to 2K resolution as [Seedance 2 VIP](https://github.com/Anil-matcha/Seedance-2-API), with **reduced content-safety filtering** for broader creative freedom. **Seedance 2 Mini Spicy** applies the same relaxed filtering to the faster, lower-cost Mini tier.

> ⚠️ **Content policy notice**: "Spicy" means reduced automated content-safety filtering, not an anything-goes endpoint. Generated content still must comply with MuAPI's and the underlying provider's terms of service and applicable law. Do not use this API to generate content involving minors, non-consensual imagery, or other prohibited material.

## Related Projects

- [Seedance-2-API](https://github.com/Anil-matcha/Seedance-2-API) — Python wrapper for the standard-moderation Seedance 2.0, 2.5, and 2 Mini API.
- [Seedance-2.5-Spicy-API](https://github.com/Anil-matcha/Seedance-2.5-Spicy-API) — Python SDK and MCP server for the Seedance 2.5 Spicy tier (native 4K, 30s clips).
- [Wan-3.0-Spicy-API](https://github.com/Anil-matcha/Wan-3.0-Spicy-API) — Python SDK and MCP server for the Wan 3.0 Spicy tier.
- [Seedance-3-API](https://github.com/Anil-matcha/Seedance-3-API) — companion project for the next Seedance API generation on MuAPI.
- [seedance-2-mcp](https://github.com/Anil-matcha/seedance-2-mcp) — Focused MCP server for Seedance 2 from Claude, Cursor, and other AI assistants.
- [seedance2-comfyui](https://github.com/Anil-matcha/seedance2-comfyui) — Run Seedance 2 inside ComfyUI.
- [n8n-nodes-seedance2](https://github.com/Anil-matcha/n8n-nodes-seedance2) — Automate Seedance 2 in n8n workflows.
- [awesome-seedance-2.5-api-prompts](https://github.com/Anil-matcha/awesome-seedance-2.5-api-prompts) — Curated Seedance 2.5 API guide, prompts, camera controls, and video generation examples.
- [awesome-seedance-motion-control-api](https://github.com/Anil-matcha/awesome-seedance-motion-control-api) — Seedance 2 & 2.5 Motion Control API guide.

## 🚀 Why Use Seedance 2 Spicy API?

- **Relaxed Content Filtering**: Broader creative range than the standard Seedance 2.0 tier, while keeping the same underlying model quality.
- **VIP Priority Routing**: Same fast, priority-queue infrastructure as Seedance 2 VIP.
- **Native Audio-Visual Sync**: Synchronized audio generated alongside the video.
- **Up to 2K Resolution**: Sharp, cinematic output.
- **Character Consistency**: Reference an existing [Seedance 2 character sheet](https://github.com/Anil-matcha/Seedance-2-API/blob/main/CHARACTER_CONSISTENCY.md) inline with `@character:<id>` in any prompt.
- **Omni-Reference**: Condition a single generation on up to 9 images, 3 video clips, and 3 audio references — selectable 720p/1080p/4K output.
- **Seedance 2 Mini Spicy**: The relaxed-moderation Mini tier — outperforms Seedance 2.0 Fast at a fraction of the cost, ideal for prototyping and high-volume pipelines.

## 🌟 Key Features

- ✅ **Text-to-Video (Spicy / Spicy Fast)**: Transform prompts into cinematic video clips, with a `-fast` tier for the quickest queue.
- ✅ **Image-to-Video (Spicy / Spicy Fast)**: Animate a start frame (and optional end frame) into video.
- ✅ **Omni-Reference (Spicy / Spicy Fast)**: Multi-modal generation from image, video, and audio references in a single request.
- ✅ **Seedance 2 Mini Spicy Text-to-Video / Image-to-Video / Omni-Reference**: Fast, affordable generation at Mini-tier pricing.
- ✅ **Optional AI Audio**: Mini-tier endpoints let you toggle synchronized AI-generated audio.
- ✅ **High Bitrate Mode**: Trade file size for better visual fidelity on any endpoint.
- ✅ **File Upload**: Upload local images/videos directly via `upload_file()`.

---

## 🛠 Installation

### Via Pip (Recommended)
```bash
pip install seedance-2-spicy-api
```

### From Source
```bash
git clone https://github.com/Anil-matcha/Seedance-2-Spicy-API.git
cd Seedance-2-Spicy-API
pip install -r requirements.txt
```

### Configuration
Create a `.env` file in the root directory and add your [MuAPI](https://muapi.ai?utm_source=github&utm_medium=readme&utm_campaign=seedance-2-spicy-api) API key:
```env
MUAPI_API_KEY=your_muapi_api_key_here
```

---

## 🤖 Seedance 2 Spicy MCP Server

Use Seedance 2 Spicy as an **MCP (Model Context Protocol)** server so AI assistants (Claude Desktop, Cursor, etc.) can invoke the tools directly.

```bash
python3 mcp_server.py
```

Test with the MCP Inspector:
```bash
npx -y @modelcontextprotocol/inspector python3 mcp_server.py
```

---

## 💻 Quick Start (Python)

```python
from seedance_2_spicy_api import Seedance2SpicyAPI

api = Seedance2SpicyAPI()

# Text-to-Video (Spicy)
submission = api.text_to_video(
    prompt="A cinematic shot of a futuristic city at night with neon lights reflecting on wet streets",
    aspect_ratio="16:9",
    duration=5,
)
result = api.wait_for_completion(submission["request_id"])
print(f"Video: {result['outputs'][0]}")
```

---

## 📡 API Endpoints & Reference

### 1. Seedance 2 Spicy Text-to-Video
**Endpoint**: `POST https://api.muapi.ai/api/v1/seedance-2-spicy-text-to-video`

Same VIP-tier priority routing, native audio-visual sync, and up to 2K resolution as Seedance 2 VIP, with reduced content-safety filtering.

| Field | Type | Required | Default | Description |
|---|---|---|---|---|
| `prompt` | string | Yes | — | Text description. Use `@character:<id>` or `@omni-character:<char_id>` for a trained character. |
| `aspect_ratio` | enum | No | `16:9` | `21:9`, `16:9`, `4:3`, `1:1`, `3:4`, `9:16` |
| `duration` | int | No | `5` | Seconds (4-15) |
| `high_bitrate` | boolean | No | `false` | Higher visual fidelity, larger files |

```bash
curl --location --request POST "https://api.muapi.ai/api/v1/seedance-2-spicy-text-to-video" \
  --header "Content-Type: application/json" \
  --header "x-api-key: YOUR_API_KEY" \
  --data-raw '{
      "prompt": "A cinematic shot of a futuristic city at night with neon lights reflecting on wet streets",
      "aspect_ratio": "16:9",
      "duration": 5
  }'
```

### 2. Seedance 2 Spicy Text-to-Video Fast
**Endpoint**: `POST https://api.muapi.ai/api/v1/seedance-2-spicy-text-to-video-fast`

Same fields as above. The quickest Spicy-tier text-to-video generation, same fast queue as Seedance 2 VIP Fast.

### 3. Seedance 2 Spicy Image-to-Video
**Endpoint**: `POST https://api.muapi.ai/api/v1/seedance-2-spicy-image-to-video`

| Field | Type | Required | Default | Description |
|---|---|---|---|---|
| `prompt` | string | Yes | — | Guides the animation. Supports `@character:<id>` / `@omni-character:<char_id>`. |
| `images_list` | array[string] | Yes | — | 1 image = start frame, 2 images = start-to-end transition (max 2). |
| `aspect_ratio` | enum | No | `16:9` | `21:9`, `16:9`, `4:3`, `1:1`, `3:4`, `9:16` |
| `duration` | int | No | `5` | Seconds (4-15) |
| `high_bitrate` | boolean | No | `false` | Higher visual fidelity, larger files |

```bash
curl --location --request POST "https://api.muapi.ai/api/v1/seedance-2-spicy-image-to-video" \
  --header "Content-Type: application/json" \
  --header "x-api-key: YOUR_API_KEY" \
  --data-raw '{
      "prompt": "The person walks forward with a smile",
      "images_list": ["https://example.com/person.jpg"],
      "aspect_ratio": "16:9",
      "duration": 5
  }'
```

### 4. Seedance 2 Spicy Image-to-Video Fast
**Endpoint**: `POST https://api.muapi.ai/api/v1/seedance-2-spicy-image-to-video-fast`

Same fields as above. The quickest Spicy-tier image animation.

### 5. Seedance 2 Spicy Omni Reference
**Endpoint**: `POST https://api.muapi.ai/api/v1/seedance-2-spicy-omni-reference`

Generates video from up to 9 image references, 3 video clips, and 3 audio references. Reference materials in the prompt with `@image1`…`@image9`, `@video1`…`@video3`, `@audio1`…`@audio3`.

| Field | Type | Required | Default | Description |
|---|---|---|---|---|
| `prompt` | string | Yes | — | Description referencing `@imageN`/`@videoN`/`@audioN` and/or `@character:<id>`. |
| `resolution` | enum | No | `720p` | `720p`, `1080p`, `4k` — price scales with resolution. |
| `images_list` | array[string] | No | — | Up to 9 reference image URLs. |
| `video_files` | array[string] | No | — | Up to 3 reference video URLs (max 15s each). |
| `audio_files` | array[string] | No | — | Up to 3 reference audio URLs (total max 15s). |
| `aspect_ratio` | enum | No | `16:9` | `21:9`, `16:9`, `4:3`, `1:1`, `3:4`, `9:16` |
| `duration` | int | No | `5` | Seconds (4-15) |
| `high_bitrate` | boolean | No | `false` | Higher visual fidelity, larger files |

```bash
curl --location --request POST "https://api.muapi.ai/api/v1/seedance-2-spicy-omni-reference" \
  --header "Content-Type: application/json" \
  --header "x-api-key: YOUR_API_KEY" \
  --data-raw '{
      "prompt": "@image1 is the main character. The person walks along a city street at sunset, cinematic lighting.",
      "resolution": "1080p",
      "images_list": ["https://example.com/scene_ref.jpg"]
  }'
```

### 6. Seedance 2 Spicy Omni Reference Fast
**Endpoint**: `POST https://api.muapi.ai/api/v1/seedance-2-spicy-omni-reference-fast`

Same fields as above. Faster generation with priority routing.

### 7. Seedance 2 Mini Spicy Text-to-Video
**Endpoint**: `POST https://api.muapi.ai/api/v1/seedance-2-mini-spicy-text-to-video`

The fastest, lowest-cost Spicy-tier text-to-video generation.

| Field | Type | Required | Default | Description |
|---|---|---|---|---|
| `prompt` | string | Yes | — | Text prompt describing the video scene and motion. |
| `aspect_ratio` | enum | No | `16:9` | `16:9`, `9:16`, `1:1`, `3:4`, `4:3`, `21:9` |
| `resolution` | enum | No | `720p` | `480p`, `720p` |
| `duration` | int | No | `5` | Seconds (4-15) |
| `generate_audio` | boolean | No | `true` | Generate AI audio synchronized with the video. |
| `high_bitrate` | boolean | No | `false` | Higher visual fidelity, larger files |

```bash
curl --location --request POST "https://api.muapi.ai/api/v1/seedance-2-mini-spicy-text-to-video" \
  --header "Content-Type: application/json" \
  --header "x-api-key: YOUR_API_KEY" \
  --data-raw '{
      "prompt": "A golden retriever running through a sunlit meadow, slow motion, vibrant summer colors, wide angle shot",
      "aspect_ratio": "16:9",
      "duration": 5
  }'
```

### 8. Seedance 2 Mini Spicy Image-to-Video
**Endpoint**: `POST https://api.muapi.ai/api/v1/seedance-2-mini-spicy-image-to-video`

| Field | Type | Required | Default | Description |
|---|---|---|---|---|
| `images_list` | array[string] | Yes | — | 1 image = start frame. 2-9 images = reference images (`@image1`, `@image2`, ...) (max 9). |
| `prompt` | string | No | — | Text prompt guiding the animation. |
| `aspect_ratio` | enum | No | `16:9` | `16:9`, `9:16`, `1:1`, `3:4`, `4:3`, `21:9` |
| `resolution` | enum | No | `720p` | `480p`, `720p` |
| `duration` | int | No | `5` | Seconds (4-15) |
| `generate_audio` | boolean | No | `true` | Generate AI audio synchronized with the video. |
| `high_bitrate` | boolean | No | `false` | Higher visual fidelity, larger files |

### 9. Seedance 2 Mini Spicy Omni Reference
**Endpoint**: `POST https://api.muapi.ai/api/v1/seedance-2-mini-spicy-omni-reference`

Cost-efficient mini-tier reference-driven generation. Reference images with `@image1..@image9`, videos with `@video1..@video3`, audio with `@audio1..@audio3`.

| Field | Type | Required | Default | Description |
|---|---|---|---|---|
| `prompt` | string | Yes | — | Text prompt referencing `@imageN`/`@videoN`/`@audioN`. |
| `images_list` | array[string] | No | — | Up to 9 reference images. |
| `video_files` | array[string] | No | — | Up to 3 reference video clips (total max 15s). |
| `audio_files` | array[string] | No | — | Up to 3 reference audio files (total max 15s). |
| `aspect_ratio` | enum | No | `16:9` | `16:9`, `9:16`, `1:1`, `3:4`, `4:3`, `21:9` |
| `resolution` | enum | No | `720p` | `480p`, `720p` |
| `duration` | int | No | `5` | Seconds (4-15) |
| `generate_audio` | boolean | No | `true` | Generate AI audio synchronized with the video. |
| `high_bitrate` | boolean | No | `false` | Higher visual fidelity, larger files |

---

## 💰 Pricing

| Endpoint | Cost |
|---|---|
| Seedance 2 Spicy Text-to-Video | $1.65 / generation |
| Seedance 2 Spicy Text-to-Video Fast | $1.155 / generation |
| Seedance 2 Spicy Image-to-Video | $1.65 / generation |
| Seedance 2 Spicy Image-to-Video Fast | $1.155 / generation |
| Seedance 2 Spicy Omni Reference | $1.50 / generation (scales with resolution) |
| Seedance 2 Spicy Omni Reference Fast | $1.05 / generation (scales with resolution) |
| Seedance 2 Mini Spicy Text-to-Video | $0.22 / generation |
| Seedance 2 Mini Spicy Image-to-Video | $0.22 / generation |
| Seedance 2 Mini Spicy Omni Reference | $0.75 / generation |

Pricing is illustrative and subject to change — check [muapi.ai/seedance-2](https://muapi.ai/seedance-2?utm_source=github&utm_medium=readme&utm_campaign=seedance-2-spicy-api) for current rates.

---

## 📖 Method Reference

| Method | Parameters | Description |
| :--- | :--- | :--- |
| `text_to_video` | `prompt`, `aspect_ratio`, `duration`, `high_bitrate` | Spicy Text-to-Video. |
| `text_to_video_fast` | same | Spicy Text-to-Video Fast. |
| `image_to_video` | `prompt`, `images_list`, `aspect_ratio`, `duration`, `high_bitrate` | Spicy Image-to-Video. |
| `image_to_video_fast` | same | Spicy Image-to-Video Fast. |
| `omni_reference` | `prompt`, `resolution`, `images_list`, `video_files`, `audio_files`, `aspect_ratio`, `duration`, `high_bitrate` | Spicy Omni-Reference. |
| `omni_reference_fast` | same | Spicy Omni-Reference Fast. |
| `mini_text_to_video` | `prompt`, `aspect_ratio`, `duration`, `resolution`, `generate_audio`, `high_bitrate` | Mini Spicy Text-to-Video. |
| `mini_image_to_video` | `images_list`, `prompt`, `aspect_ratio`, `duration`, `resolution`, `generate_audio`, `high_bitrate` | Mini Spicy Image-to-Video. |
| `mini_omni_reference` | `prompt`, `images_list`, `video_files`, `audio_files`, `aspect_ratio`, `duration`, `resolution`, `generate_audio`, `high_bitrate` | Mini Spicy Omni-Reference. |
| `upload_file` | `file_path` | Upload a local file (image or video) to MuAPI. |
| `get_result` | `request_id` | Check task status. |
| `wait_for_completion` | `request_id`, `poll_interval`, `timeout` | Blocking helper for generation tasks. |

---

## 🔗 Official Resources
- **Landing page**: [Seedance 2 on MuAPI](https://muapi.ai/seedance-2?utm_source=github&utm_medium=readme&utm_campaign=seedance-2-spicy-api)
- **Playground**: [Text-to-Video](https://muapi.ai/playground/seedance-2-spicy-text-to-video?utm_source=github&utm_medium=readme&utm_campaign=seedance-2-spicy-api) · [Image-to-Video](https://muapi.ai/playground/seedance-2-spicy-image-to-video?utm_source=github&utm_medium=readme&utm_campaign=seedance-2-spicy-api)
- **Access Keys**: [muapi.ai/access-keys](https://muapi.ai/access-keys?utm_source=github&utm_medium=readme&utm_campaign=seedance-2-spicy-api)
- **API Reference**: [muapi.ai/docs/api-reference](https://muapi.ai/docs/api-reference?utm_source=github&utm_medium=readme&utm_campaign=seedance-2-spicy-api)
- **API Provider**: [MuAPI.ai](https://muapi.ai?utm_source=github&utm_medium=readme&utm_campaign=seedance-2-spicy-api)

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Keywords**: Seedance 2 Spicy API, Seedance 2 Spicy Fast, Seedance 2 Mini Spicy, ByteDance Seedance Spicy, uncensored AI video generator, relaxed content moderation video API, Text-to-Video AI, Image-to-Video API, Omni Reference video generation, Seedance Python SDK, Sora Alternative, MuAPI, Video Generation API, Cinematic AI Video, Python Video API.
